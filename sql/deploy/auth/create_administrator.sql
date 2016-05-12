-- Deploy nyiso:auth/create_administrator to pg

BEGIN;
CREATE ROLE nyiso_admin WITH BYPASSRLS;
GRANT ALL ON DATABASE nyiso TO nyiso_admin WITH GRANT OPTION;

COMMIT;
