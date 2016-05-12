-- Revert nyiso:data/rt_lbmp_generators from pg

BEGIN;
DROP INDEX data.rt_lbmp_gen_idx;
DROP TABLE data.rt_lbmp_generators;
COMMIT;
