/*employee_id | name  | department | salary
------------|-------|------------|-------
101         | Gokul | IT         | 50000
102         | Arun  | HR         | 45000
103         | Priya | Finance    | 55000
104         | Rahul | IT         | 60000
105         | Divya | HR         | 48000
106         | Kumar | Finance    | 70000 */

CREATE TABLE employees (
    employee_id INTEGER,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INTEGER
);

INSERT INTO employees VALUES (101, 'Gokul', 'IT', 50000);
INSERT INTO employees VALUES (102, 'Arun', 'HR', 45000);
INSERT INTO employees VALUES (103, 'Priya', 'Finance', 55000);
INSERT INTO employees VALUES (104, 'Rahul', 'IT', 60000);
INSERT INTO employees VALUES (105, 'Divya', 'HR', 48000);
INSERT INTO employees VALUES (106, 'Kumar', 'Finance', 70000);

SELECT *
FROM employees
WHERE department = 'IT'
  AND salary > 48000
  AND employee_id = 103
  AND salary <= 50000
  AND employee_id <> 60000
  AND employee_id <> 70000;

--OUTPUT
--No rows returned.
