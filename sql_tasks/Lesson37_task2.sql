"1" SELECT first_name AS "First Name", last_name as "Last Name" FROM employees
"2" SELECT DISTINCT department_id FROM employees
"3" SELECT * from employees ORDER BY first_name DESC
"4" SELECT first_name, last_name, salary, salary*0.12 as "PF" FROM employees
"5" SELECT min(salary), max(salary) FROM employees
"6" SELECT first_name, last_name, ROUND(salary/12, 2) as "monthly salary" FROM employees