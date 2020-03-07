--Instruction 1
SELECT country, AVG(budget) as avg_budget, AVG(gross) as avg_gross
FROM films
GROUP BY country
HAVING COUNT(title) > 10
ORDER BY country LIMIT 5
