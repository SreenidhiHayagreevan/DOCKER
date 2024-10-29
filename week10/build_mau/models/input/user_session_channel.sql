SELECT
userId,
sessionId,
channel
FROM {{ source('analytics', 'user_session_channel') }}
WHERE sessionId IS NOT NULL