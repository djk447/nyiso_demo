-- Revert nyiso:api_v001/generators.view from pg

BEGIN;
DROP VIEW api_v001.generators;
COMMIT;
