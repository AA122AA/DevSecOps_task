#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER serv_2 PASSWORD 0000;
	CREATE DATABASE serv_2_db;
	GRANT ALL PRIVILEGES ON DATABASE serv_2_db TO serv_2;
EOSQL