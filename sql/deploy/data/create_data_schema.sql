-- Deploy nyiso:data/create_data_schema to pg
-- requires: auth/create_administrator

BEGIN;
SET ROLE nyiso_admin;
CREATE SCHEMA data;
RESET ROLE;
COMMIT;
