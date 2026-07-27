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
WHERE salary BETWEEN 50000 AND 70000;

/*employee_id | name  | department | salary
------------|-------|------------|-------
101         | Gokul | IT         | 50000
103         | Priya | Finance    | 55000
104         | Rahul | IT         | 60000
106         | Kumar | Finance    | 70000*/
