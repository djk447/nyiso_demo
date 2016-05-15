-- Deploy nyiso:maint/create_pg_stat_statements to pg

BEGIN;

CREATE EXTENSION pg_stat_statements;

COMMIT;
