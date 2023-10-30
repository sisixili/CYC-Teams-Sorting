ALTER TABLE f23_students DROP COLUMN Term;
UPDATE f23_students SET Theme='Theme1' WHERE FirstName='John' AND LastName='Smith';
SHOW INDEX FROM student_info;

SELECT * FROM student_info;
SELECT * FROM themes;
SELECT * FROM trankings;
SELECT * FROM teams;
SELECT * FROM members;

SELECT COUNT(*), min(ID), max(ID) FROM trankings;
INSERT INTO temp_student_info (firstname, lastname, grade, school, email, isIB) VALUES (1, 1, 1, 1, 1, 1);

-- Test queries --
-- SELECT * FROM members WHERE team_id = null AND 

SELECT * FROM members AS m, trankings AS t 
WHERE m.team_id IS NULL AND m.mem_id = t.s_id AND t.t_id = 6 AND t.ranking = 1;
