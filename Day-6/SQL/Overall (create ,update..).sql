CREATE TABLE STUDENTS(
  STUDENT_NAME CHAR(10),
  STUDENT_ID INT,
  STUDENT_DEPARTMENT VARCHAR(50),
  STUDENT_AGE INT
  );

INSERT INTO STUDENTS

VALUES ('GOKUL',7010,'EEE',24);

SELECT * FROM STUDENTS;

/*

STUDENT_NAME | STUDENT_ID | STUDENT_DEPARTMENT | STUDENT_AGE
-------------|------------|--------------------|------------
GOKUL        | 7010       | EEE                | 24
*/

UPDATE STUDENTS
SET STUDENT_DEPARTMENT = 'CSE'
WHERE STUDENT_ID = 7010;

/*
STUDENT_NAME | STUDENT_ID | STUDENT_DEPARTMENT | STUDENT_AGE
-------------|------------|--------------------|------------
GOKUL        | 7010       | CSE                | 24*/


DELETE FROM STUDENTS 
WHERE STUDENT_DEPARTMENT = 'CSE';

/*STUDENT_NAME | STUDENT_ID | STUDENT_DEPARTMENT | STUDENT_AGE
-------------|------------|--------------------|------------
(empty)
*/

ALTER TABLE STUDENTS
ADD COLUMN STUDENTS_BG CHAR(10);


INSERT INTO STUDENTS
VALUES ('GOKUL', 7010, 'MECH', 24, 'B');

/*STUDENT_NAME | STUDENT_ID | STUDENT_DEPARTMENT | STUDENT_AGE | STUDENTS_BG
-------------|------------|--------------------|-------------|------------
GOKUL        | 7010       | MECH               | 24          | B*/

ALTER TABLE STUDENTS RENAME COLUMN STUDENTS_BG TO STUDENT_BLOOD_GROUP;

/*STUDENT_NAME | STUDENT_ID | STUDENT_DEPARTMENT | STUDENT_AGE | STUDENT_BLOOD_GROUP
-------------|------------|--------------------|-------------|--------------------
GOKUL        | 7010       | MECH               | 24          | B       */

ALTER TABLE STUDENTS DROP COLUMN STUDENT_BLOOD_GROUP;


/*
STUDENT_NAME | STUDENT_ID | STUDENT_DEPARTMENT | STUDENT_AGE
-------------|------------|--------------------|------------
GOKUL        | 7010       | MECH               | 24
*/

DROP TABLE STUDENTS;
--STUDENTS table no longer exists.

