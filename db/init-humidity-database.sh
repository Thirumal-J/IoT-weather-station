#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER humidityadmin;
    CREATE DATABASE humidity;
    GRANT ALL PRIVILEGES ON DATABASE humidity TO humidityadmin;
	ALTER ROLE postgres WITH PASSWORD '1234';
EOSQL
