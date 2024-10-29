SELECT
sessionId,
ts
FROM {{ source('analytics', 'session_timestamp') }}
WHERE sessionId IS NOT NULL