#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER pressureadmin;
    CREATE DATABASE pressure;
    GRANT ALL PRIVILEGES ON DATABASE pressure TO pressureadmin;
	ALTER ROLE postgres WITH PASSWORD '1234';
EOSQL
