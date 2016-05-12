-- Revert nyiso:api_v001/RT_LBMP_GEN.view from pg

BEGIN;
DROP TRIGGER rt_lbmp_gen_insert ON api_v001."RT_LBMP_GEN";
DROP FUNCTION api_v001.rt_lbmp_gen_insert_trigger();
DROP VIEW api_v001."RT_LBMP_GEN";
COMMIT;
