--Instrution 1
SELECT SUM(gross)
FROM films
WHERE release_year >= 2000;

--Instrution 2
SELECT AVG(gross)
FROM films
WHERE title LIKE 'A%'

--Instrution 3
SELECT MIN(gross)
FROM films
WHERE release_year = 1994;

--Instrution 4
SELECT MAX(gross)
FROM films
WHERE release_year BETWEEN 2000 AND 2012;
