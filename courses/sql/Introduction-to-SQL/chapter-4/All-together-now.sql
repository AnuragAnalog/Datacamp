--Instruction 1
SELECT release_year, budget, gross
FROM films

--Instrucion 2 
SELECT release_year, budget, gross
FROM films
WHERE release_year > 1990

--Instruction 3
SELECT release_year
FROM films
GROUP BY release_year
HAVING release_year > 1990

--Instruction 4
SELECT release_year, AVG(budget) as avg_budget, AVG(gross) as avg_gross
FROM films
GROUP BY release_year
HAVING release_year > 1990

--Instruction 5
SELECT release_year, AVG(budget) as avg_budget, AVG(gross) as avg_gross
FROM films
GROUP BY release_year
HAVING AVG(budget) > 60000000

--Instruction 6
SELECT release_year, AVG(budget) as avg_budget, AVG(gross) as avg_gross
FROM films
GROUP BY release_year
HAVING AVG(budget) > 60000000
ORDER BY AVG(gross) DESC;

