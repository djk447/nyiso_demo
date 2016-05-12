-- Revert nyiso:data/create_data_schema from pg

BEGIN;
DROP SCHEMA data;
COMMIT;
