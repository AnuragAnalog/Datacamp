--Instruction 1
SELECT release_year, MIN(gross)
FROM films
GROUP BY release_year

--Instruction 2
SELECT language, SUM(gross)
FROM films
GROUP BY language

--Instruction 3
SELECT country, SUM(budget)
FROM films
GROUP BY country

--Instruction 4
SELECT release_year, country, MAX(budget)
FROM films
GROUP BY release_year, country
ORDER BY release_year, country

--Instruction 5
SELECT country, release_year, MIN(gross)
FROM films
GROUP BY release_year, country
ORDER BY country, release_year

