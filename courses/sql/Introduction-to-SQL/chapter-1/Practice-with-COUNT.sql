-- Instruction 1
SELECT COUNT(*)
FROM people;

-- Instruction 2
SELECT COUNT(birthdate)
FROM people;

-- Instruction 3
SELECT COUNT(DISTINCT birthdate)
FROM people;

-- Instruction 4
SELECT COUNT(DISTINCT language)
FROM films;

-- Instruction 5
SELECT COUNT(DISTINCT country)
FROM films;
