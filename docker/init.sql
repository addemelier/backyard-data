-- Runs on first container startup via /docker-entrypoint-initdb.d/
-- The postgis/postgis image includes the extension but does not enable it automatically.

CREATE EXTENSION IF NOT EXISTS postgis;
