DROP USER IF EXISTS app;

CREATE USER app WITH CREATEDB CREATEROLE SUPERUSER LOGIN PASSWORD 'app';

DROP DATABASE IF EXISTS be;

CREATE DATABASE be WITH OWNER postgres;
GRANT ALL PRIVILEGES ON DATABASE be TO app;