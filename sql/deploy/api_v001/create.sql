-- Deploy nyiso:api_v001/create to pg
-- requires: auth/create_administrator

BEGIN;
SET ROLE nyiso_admin;
CREATE SCHEMA api_v001;
RESET ROLE;
COMMIT;
