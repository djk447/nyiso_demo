-- Deploy nyiso:api_v001/generators.view to pg
-- requires: api_v001/create

BEGIN;
SET ROLE nyiso_admin;
CREATE VIEW api_v001.generators as SELECT id, name, ptid,location,owner, address, fields FROM data.generators;
RESET ROLE;
COMMIT;
