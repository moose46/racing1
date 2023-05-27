-- Active: 1684262528760@@127.0.0.1@5432

SELECT t."name",c."race_date", finish_pos, nascar_driver.name
 FROM nascar_results a, nascar_driver, nascar_race c, nascar_track t
 where nascar_driver.id = a.driver_id and c."id" = a."race_id" and t."id" = c."track_id"
--  GROUP BY race_date
   ORDER BY "finish_pos",race_date asc LIMIT 30