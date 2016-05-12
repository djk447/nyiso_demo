-- Revert nyiso:api_v001/create from pg

BEGIN;

DROP SCHEMA api_v001;
COMMIT;
