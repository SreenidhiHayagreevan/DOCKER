# Movie Search and Recommendation System

This repository contains scripts and data for a movie search and recommendation system using the TMDB API and Vespa search engine.

## Files

- **`process_tmdb_csv_2_jsonl.py`**: Fetches movie data from the TMDB API, processes it, and converts it to CSV and JSONL formats.
- **`pyvespa_search.py`**: Interacts with Vespa to perform keyword-based (BM25) and semantic-based (embedding) searches, as well as document embedding-based recommendations.
- **`clean_themoviedb.jsonl`**: Processed movie data in JSONL format, ready for Vespa.
- **`themoviedb_movies.csv`**: Raw movie data fetched from the TMDB API.

## What the Code Does

1. **Fetches movie data** from TMDB, including title, overview, and genre information.
2. **Processes and stores the data** in CSV and JSONL formats.
3. **Uses Vespa search** to perform:
   - **Keyword search** based on BM25 ranking.
   - **Semantic search** using document embeddings.
   - **Recommendation system** based on nearest-neighbor embeddings.

## How to Run

1. Install required dependencies:
   ```bash
   pip install requests pandas vespa
   ```

2. Run the scripts:
   - To fetch and process TMDB data:
     ```bash
     python process_tmdb_csv_2_jsonl.py
     ```
   - To perform searches and recommendations:
     ```bash
     python pyvespa_search.py
     ```
