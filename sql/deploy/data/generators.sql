-- Deploy nyiso:data/generators to pg
-- requires: data/create_data_schema

BEGIN;
SET ROLE nyiso_admin;
CREATE TABLE data.generators (
    id          varchar primary key,
    ptid        int NOT NULL UNIQUE,
    name        varchar,
    location    point,
    owner       text,
    address     jsonb,
    fields      jsonb
);

RESET ROLE;
COMMIT;
