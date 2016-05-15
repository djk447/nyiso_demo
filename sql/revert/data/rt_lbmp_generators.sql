-- Revert nyiso:data/rt_lbmp_generators from pg

BEGIN;
DROP INDEX data.rt_lbmp_gen_generator_idx;
DROP INDEX data.rt_lbmp_gen_record_time_idx;
DROP TABLE data.rt_lbmp_generators;
COMMIT;
