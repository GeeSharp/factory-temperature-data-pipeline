-- 1. How many readings do we have ?
SELECT COUNT(*) AS total_readings
FROM temperature_readings;

--2. Min, max, average temperature
SELECT
    MIN(temperature_c) AS min_temp,
    MAX(temperature_c) AS max_temp,
    AVG(temperature_c) AS avg_temp
FROM temperature_readings;

--3 Top 10 highest temperatures (overheating period )
SELECT timestamp, machine_id, temperature_c
FROM temperature_readings
ORDER BY temperature_c DESC
LIMIT 10;

--4. Average temperature by hour
SELECT
    substr(timestamp, 1, 13) AS hour_slot,
    AVG(temperature_c) AS avg_temp
FROM temperature_readings
GROUP BY hour_slot
ORDER BY hour_slot;
