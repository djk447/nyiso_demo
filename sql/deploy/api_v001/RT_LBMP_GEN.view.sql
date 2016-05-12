-- Deploy nyiso:api_v001/RT_LBMP_GEN.view to pg
-- requires: api_v001/create

BEGIN;
SET ROLE nyiso_admin;
CREATE VIEW api_v001."RT_LBMP_GEN" AS SELECT
    r.generator AS "Gen Name",
    g.ptid AS "Gen PTID",
    r.record_time AS "RTD End Time Stamp",
    r.lbmp AS "RTD Gen LBMP",
    r.losses AS "RTD Gen Losses",
    r.congestion AS "RTD Gen Congestion",
    r.price_version AS "RTD Gen Price Version"
    FROM data.rt_lbmp_generators r INNER JOIN data.generators g ON r.generator = g.id;

    CREATE OR REPLACE FUNCTION api_v001.rt_lbmp_gen_insert_trigger()
    RETURNS TRIGGER AS $body$

    BEGIN
    /* This will run instead of the insert on the view.
    Need to check to make sure of ownership of the device and then go from there.*/

        IF NEW."Gen Name" NOT IN (SELECT id FROM api_v001.generator WHERE id=NEW."Gen Name") THEN
            INSERT INTO api_v001.generators(id,ptid) VALUES(NEW."Gen Name",NEW."Gen PTID");
        END IF;
        INSERT INTO data.rt_lbmp_generators(generator,record_time, lbmp,losses,congestion,price_version)
                VALUES(NEW."Gen Name",NEW."RTD End Time Stamp",NEW."RTD Gen LBMP",NEW. "RTD Gen Losses",NEW."RTD Gen Congestion",NEW."RTD Gen Price Version")
                ON CONFLICT DO NOTHING;
        RETURN NEW;
    END;
    $body$ LANGUAGE plpgsql;

    CREATE TRIGGER rt_lbmp_gen_insert
    INSTEAD OF INSERT ON api_v001."RT_LBMP_GEN"
    FOR EACH ROW EXECUTE PROCEDURE  api_v001.rt_lbmp_gen_insert_trigger();
RESET ROLE;
COMMIT;
