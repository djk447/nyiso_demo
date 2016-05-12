-- Revert nyiso:auth/create_administrator from pg

BEGIN;
REVOKE ALL ON DATABASE nyiso FROM nyiso_admin;
DROP ROLE nyiso_admin;

COMMIT;
