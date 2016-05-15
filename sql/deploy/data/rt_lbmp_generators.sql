-- Deploy nyiso:data/rt_lbmp_generators to pg
-- requires: data/generators

BEGIN;
SET ROLE nyiso_admin;
CREATE TABLE data.rt_lbmp_generators(
    generator          varchar references data.generators(id) ON UPDATE CASCADE ON DELETE RESTRICT,
    record_time        timestamptz NOT NULL,
    lbmp               float,
    losses             float,
    congestion         float,
    price_version      int,
    PRIMARY KEY(generator,record_time)
);
CREATE INDEX rt_lbmp_gen_record_time_idx ON data.rt_lbmp_generators (record_time);
CREATE INDEX rt_lbmp_gen_generator_idx ON data.rt_lbmp_generators (generator);
RESET ROLE;
COMMIT;
