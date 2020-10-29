"1" SELECT employees.first_name, employees.last_name, departments.department_id, departments.depart_name 
FROM employees LEFT JOIN departments ON employees.department_id = departments.department_id

"2" SELECT e.first_name, e.last_name, d.department_id, d.depart_name, l.city, l.state_province
FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id 
LEFT JOIN locations l ON d.location_id=l.location_id

"3" SELECT e.first_name, e.last_name, d.department_id, d.depart_name
FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id = 40 OR e.department_id = 80

"4" SELECT * FROM departments

"5" SELECT e.first_name, m.first_name AS "Manager first_name"
FROM employees e, employees m
WHERE e.manager_id = m.employee_id

"6" SELECT j.job_title, e.first_name + " " + e.last_name AS "Full Name", j.max_salary - e.salary AS "Max salary minus salary"
FROM employees e LEFT JOIN jobs j ON e.job_id = j.job_id

"7" SELECT j.job_title, avg(e.salary)
FROM jobs j LEFT JOIN employees e on e.job_id = j.job_id
GROUP BY e.job_id

"8" SELECT e.first_name + " " + e.last_name AS "Full Name", e.salary
FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id
LEFT JOIN locations l ON d.location_id=l.location_id
WHERE l.city = "Seattle"

"9" SELECT d.depart_name, count(e.employee_id) AS "Number of employees"
FROM departments d LEFT JOIN employees e ON d.department_id=e.department_id
GROUP BY e.department_id