--Instruction 1
SELECT release_year, count(*)
FROM films
GROUP BY release_year

--Instruction 2	
SELECT release_year, AVG(duration)
FROM films
GROUP BY release_year

--Instruction 3 
SELECT release_year, MAX(budget)
FROM films
GROUP BY release_year

--Instruction 4
SELECT imdb_score, COUNT(num_votes)
FROM reviews
GROUP BY imdb_score
