-- Active: 1703501931418@@127.0.0.1@3306@hrDB
select distinct YEAR(hire_date) from employees;
DESCRIBE employees;

SELECT *
FROM employees
LIMIT 5;

SELECT first_name, last_name, salary, SUM(salary) OVER() sum_salary
FROM employees;

-- **FIRST_VALUE**
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

-- *LAG()*
SELECT *
FROM employees
LIMIT 5;
DESCRIBE basic_pays;
-- CUrrent and previous year's salary of all employees
SELECT
    employee_id,
    fiscal_year,
    salary,
    LAG(salary) OVER(
        PARTITION BY employee_id
        ORDER BY fiscal_year) as previous_salary
FROM basic_pays;

-- Year on Year increment for each employee
SELECT 
    full_name,
    employee_id,
    fiscal_year,
    salary,
    previous_salary,
    CONCAT(ROUND((salary - previous_salary)*100/previous_salary,0),'%') as YoY
FROM 
    (SELECT 
        CONCAT(first_name, ' ', last_name) as full_name,
        bp.employee_id,
        fiscal_year,
        bp.salary,
        LAG(bp.salary,1,0) OVER(
            PARTITION BY employee_id
            ORDER BY fiscal_year
        ) as previous_salary
    FROM basic_pays as bp
    INNER JOIN employees as e
    ON e.employee_id = bp.employee_id
    ) as t;

select distinct CONCAT(first_name, ' ', last_name), e.employee_id
from employees as e
INNER JOIN basic_pays as bp
on e.employee_id = bp.employee_id;

--LAST_VALUE()
SELECT
    first_name,
    last_name,
    salary,
    LAST_VALUE(first_name) OVER (
        ORDER BY salary
        RANGE BETWEEN UNBOUNDED PRECEDING AND
        UNBOUNDED FOLLOWING
    ) AS highest_salary
FROM employees;

-- Highest salary in each department using LAST_VALUE
SELECT
    CONCAT(first_name, ' ', last_name) as full_name,
    department_name,
    salary,
    LAST_VALUE(CONCAT(first_name, ' ', last_name)) OVER (
        PARTITION BY department_name
        ORDER BY salary
        RANGE BETWEEN UNBOUNDED PRECEDING AND
        UNBOUNDED FOLLOWING
    ) as highest_salary
FROM employees as emp
INNER JOIN departments as dep
ON dep.department_id = emp.department_id;

-- LEAD()
-- Each employee in the company, the hire date of the employee hired just after
SELECT
    CONCAT(first_name, ' ', last_name) as full_name,
    hire_date,
    LEAD(hire_date, 1) OVER(
        ORDER BY hire_date
    ) AS next_hired
FROM employees;

-- For each employee, the hire date of the employee in the same department which was hired just after
SELECT
    CONCAT(first_name, ' ', last_name) as full_name,
    department_name,
    hire_date,
    LEAD(hire_date, 1, 'NA') OVER(
        PARTITION BY department_name
        ORDER BY hire_date
    ) as next_hired
FROM employees as emp
INNER JOIN departments as dep
ON dep.department_id = emp.department_id;

-- CUME_DIST()
-- Creating a view department_headcounts
CREATE OR REPLACE VIEW department_headcounts
AS
SELECT 
    department_name, 
    COUNT(employee_id) headcount
FROM employees as emp
INNER JOIN departments as dep
ON dep.department_id = emp.department_id
GROUP BY emp.department_id;

-- From the created view get the headcount for each department
SELECT
    department_name,
    headcount,
    ROUND(CUME_DIST() OVER (
        ORDER BY headcount
    ), 3) cume_dist_val
FROM department_headcounts;

--DENSE_RANK()
CREATE TABLE IF NOT EXISTS t (
    col CHAR
);
INSERT INTO t(col)
VALUES('A'),('B'),('B'),('C'),('D'),('D'),('E');
SELECT * FROM t;

SELECT
    col,
    DENSE_RANK() OVER (
        ORDER BY col
    ) my_dense_rank,
    RANK() OVER (
        ORDER BY col
    ) my_rank
FROM t;

-- Ranking employees by their salaries
SELECT
    CONCAT(first_name, ' ', last_name) full_name,
    department_name,
    salary,
    DENSE_RANK() OVER (
        ORDER BY salary DESC
    ) rank_by_salary
FROM employees as emp
INNER JOIN departments as dep
ON emp.department_id = dep.department_id;

-- Ranking employees in each department by their salaries
SELECT
    CONCAT(first_name, ' ', last_name) full_name,
    department_name,
    salary,
    DENSE_RANK() OVER (
        PARTITION BY department_name
        ORDER BY salary DESC
    ) rank_by_department
FROM employees as emp
INNER JOIN departments as dep
ON emp.department_id = dep.department_id;

-- Employees who have the highest salary in their deparment
-- Use the above query and add where rank_by_department = 1

SELECT * 
FROM (
    SELECT
        CONCAT(first_name, ' ', last_name) full_name,
        department_name,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department_name
            ORDER BY salary DESC
        ) rank_by_department
    FROM employees as emp
    INNER JOIN departments as dep
    ON emp.department_id = dep.department_id) as ranks
WHERE rank_by_department = 1;