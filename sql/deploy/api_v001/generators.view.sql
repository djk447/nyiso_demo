-- Deploy nyiso:api_v001/generators.view to pg
-- requires: api_v001/create

BEGIN;
SET ROLE nyiso_admin;
CREATE VIEW api_v001.generators as SELECT id, name, ptid,location,owner, address, fields FROM data.generators;


CREATE VIEW api_v001.generators_times AS SELECT g.id,g.name,g.ptid,ss.min_time,ss.max_time
  FROM data.generators g, LATERAL ( SELECT min(r.record_time) AS min_time, max(r.record_time) as max_time
                                    FROM data.rt_lbmp_generators r
                                    WHERE r.generator::text = g.id::text) ss;
RESET ROLE;
COMMIT;
