-- select count(JOB_ID)  from employees;

-- select avg(SALARY), count(EMPLOYEE_ID) from employees where DEPARTMENT_ID = "90";

-- SELECT COUNT(*) FROM employees group by JOB_ID;

-- SELECT   concat(FIRST_NAME," ",LAST_NAME) AS Name, departments.DEPARTMENT_ID
-- FROM employees
-- LEFT JOIN departments ON departments.DEPARTMENT_ID = employees.DEPARTMENT_ID  ;

-- SELECT  concat(FIRST_NAME," ",LAST_NAME) AS Name,  jobs.JOB_TITLE, employees.DEPARTMENT_ID
-- FROM employees
-- INNER JOIN jobs ON employees.JOB_ID = jobs.JOB_ID
-- INNER JOIN departments ON employees.DEPARTMENT_ID = departments.DEPARTMENT_ID
-- INNER JOIN locations ON  departments.LOCATION_ID = locations.LOCATION_ID 
-- WHERE CITY = "London";
