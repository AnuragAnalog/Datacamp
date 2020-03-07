--Instruction 1
SELECT title, release_year
FROM films
WHERE release_year IN(1990, 2000)
AND duration > 120;

--Instruction 2
SELECT title, language
FROM films
WHERE language IN('English', 'Spanish', 'French');

--Instruction 3
SELECT title, certification
FROM films
WHERE certification IN('NC-17', 'R');
