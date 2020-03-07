--Instruction 1
SELECT title
FROM films
WHERE release_year IN (2000, 2012)
ORDER BY release_year;

--Instruction 2	
SELECT *
FROM films
WHERE release_year <> 2015
ORDER BY duration;

--Instruction 3	
SELECT title, gross
FROM films
WHERE title LIKE 'M%'
ORDER BY title;

