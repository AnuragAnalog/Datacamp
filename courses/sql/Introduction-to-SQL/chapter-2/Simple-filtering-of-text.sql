-- Instruction 1
SELECT *
FROM films
WHERE language = 'French';

-- Instruction 2
SELECT *
FROM people
WHERE birthdate = '1974-11-11';

-- Instruction 3
SELECT COUNT(language)
FROM films
WHERE language = 'Hindi';

-- Instruction 4
SELECT *
FROM films
WHERE certification = 'R';
