-- Revert nyiso:data/generators from pg

BEGIN;

DROP TABLE data.generators;
COMMIT;
