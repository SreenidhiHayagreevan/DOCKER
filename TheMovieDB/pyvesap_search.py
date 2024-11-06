import pandas as pd
from vespa.application import Vespa
from vespa.io import VespaQueryResponse

# Function to display Vespa search results as a DataFrame
def display_hits_as_df(response: VespaQueryResponse, fields) -> pd.DataFrame:
    records = []
    for hit in response.hits:
        record = {}
        for field in fields:
            record[field] = hit["fields"].get(field, None)  # Use get to handle missing fields gracefully
        records.append(record)
    return pd.DataFrame(records)

# Function for keyword search using BM25 ranking
def keyword_search(app, search_query):
    query = {
        "yql": "select * from sources * where userQuery() limit 5",
        "query": search_query,
        "ranking": "bm25",
    }
    response = app.query(query)
    return display_hits_as_df(response, ["doc_id", "title", "text"])

# Function for semantic search using embedding nearest-neighbor ranking
def semantic_search(app, search_query):
    query = {
        "yql": "select * from sources * where ({targetHits:100}nearestNeighbor(embedding,e)) limit 5",
        "query": search_query,
        "ranking": "semantic",
        "input.query(e)": "embed(@query)"
    }
    response = app.query(query)
    return display_hits_as_df(response, ["doc_id", "title", "text"])

# Function to retrieve a document’s embedding by doc_id
def get_embedding(app, doc_id):
    query = {
        "yql" : f"select doc_id, title, text, embedding from content.doc where doc_id contains '{doc_id}'",
        "hits": 1
    }
    result = app.query(query)

    if result.hits:
        return result.hits[0]
    return None

# Function to query documents by their embedding vector
def query_movies_by_embedding(app, embedding_vector):
    query = {
        'hits': 5,
        'yql': 'select * from content.doc where ({targetHits:5}nearestNeighbor(embedding, user_embedding))',
        'ranking.features.query(user_embedding)': str(embedding_vector),
        'ranking.profile': 'recommendation'
    }
    response = app.query(query)
    return display_hits_as_df(response, ["doc_id", "title", "text"])

# Replace with the host and port of your local Vespa instance
app = Vespa(url="http://localhost", port=8082)  # Adjusted to use port 8082

# Test Queries
query = "How the Grinch Stole Christmas"

# Run keyword search and print results
df_keyword = keyword_search(app, query)
print("Keyword Search Results:")
print(df_keyword.head())

# Run semantic search and print results
df_semantic = semantic_search(app, query)
print("\nSemantic Search Results:")
print(df_semantic.head())

# Get embedding for a specific document and print recommendation results
emb_doc = get_embedding(app, "767")  # Adjust doc_id as needed for testing
if emb_doc:
    results_recommendation = query_movies_by_embedding(app, emb_doc["fields"]["embedding"])
    print("\nRecommendation Results Based on Embedding:")
    print(results_recommendation.head())
else:
    print("\nEmbedding not found for doc_id.")