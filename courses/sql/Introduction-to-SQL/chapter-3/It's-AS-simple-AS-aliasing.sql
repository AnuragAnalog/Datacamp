--Instructon 1
SELECT title, (gross - budget) AS net_profit
FROM films;

--Instructon 2
SELECT title,duration/60.0 AS duration_hours
FROM films;

--Instructon 3
SELECT AVG(duration)  / 60.0 AS avg_duration_hours
FROM films;
