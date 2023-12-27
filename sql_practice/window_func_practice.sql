-- Active: 1703501931418@@127.0.0.1@3306@hrDB
DESCRIBE employees;

SELECT first_name, last_name, salary, SUM(salary) OVER() sum_salary
FROM employees;

-- FIRST_VALUE
-- Using over first_name
SELECT first_name, last_name, salary, FIRST_VALUE(first_name) OVER (ORDER BY salary ASC) as lowest_salary
FROM employees;

-- Using PARTITION
SELECT first_name, last_name, salary, department_name, FIRST_VALUE(CONCAT(first_name,' ', last_name)) OVER(
    PARTITION BY department_name
    ORDER BY salary) as lowest_salary
FROM employees as e
INNER JOIN departments as d
on d.department_id = e.department_id;

-- Using partition over salary across various departments
SELECT 
    first_name,
    last_name,
    salary,
    department_name
FROM employees as e
INNER JOIN departments as d
on d.department_id = e.department_id
ORDER BY salary ASC;

