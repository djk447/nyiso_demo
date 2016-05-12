-- Deploy nyiso:data/rt_lbmp_generators to pg
-- requires: data/generators

BEGIN;
SET ROLE nyiso_admin;
CREATE TABLE data.rt_lbmp_generators(
    generator          varchar references data.generators(id) ON UPDATE CASCADE ON DELETE SET NULL DEFERRABLE,
    record_time        timestamptz NOT NULL,
    lbmp               float,
    losses             float,
    congestion         float,
    price_version      int
);
CREATE UNIQUE INDEX rt_lbmp_gen_idx ON data.rt_lbmp_generators (generator,record_time);
RESET ROLE;
COMMIT;
