--Instruction 1
SELECT COUNT(deathdate) * 100.0 / COUNT(*) AS percentage_dead
FROM people

--Instruction 2
SELECT MAX(release_year) - MIN(release_year) AS difference
FROM films
	 
--Instruction 3
SELECT (MAX(release_year) - MIN(release_year))/10 AS number_of_decades
FROM films
 
