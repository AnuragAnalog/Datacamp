--Instruction 1
SELECT release_year
FROM films
GROUP BY release_year
HAVING COUNT(release_year) > 200;

