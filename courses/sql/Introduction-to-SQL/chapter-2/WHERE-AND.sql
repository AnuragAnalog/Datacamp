-- Instruction 1
SELECT title, release_year
FROM films
WHERE language = 'Spanish' and release_year < 2000;

-- Instruction 2
SELECT *
FROM films
WHERE language = 'Spanish' and release_year > 2000;

-- Instruction 3
SELECT *
FROM films
WHERE language = 'Spanish' and release_year > 2000 and release_year < 2010;
