import sqlite3
from sqlite3 import Error
from pprint import pprint


def create_connection(path: str):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f'Sqlite connection error {e}')

    return connection


def execute_query(connection, query: str):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f'Sqlite connection error {e}')


connection = create_connection('hr.db')


def select_query(connection, query: str):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'Sqlite connection error {e}')

# 1. Write a query in SQL to display the first name,
# last name, department number, and department name
# for each employee

employee_info = """
SELECT employees.first_name, employees.last_name, 
employees.department_id,  departments.depart_name
FROM employees
JOIN departments using (department_id)
"""

for item in select_query(connection, employee_info):
    print(item)

# 2. Write a query in SQL to display the first and last name,
# department, city, and state province for each employee

employee_info_address = """
SELECT employees.first_name, employees.last_name, 
departments.depart_name, locations.city, locations.state_province
FROM employees
JOIN departments using (department_id)
JOIN locations using (location_id)
"""

for item in select_query(connection, employee_info_address):
    print(item)

# 3. Write a query in SQL to display the first name, last name,
# department number, and department name,
# for all employees for departments 80 or 40

employee_departments_40_80 = """
SELECT employees.first_name, employees.last_name, 
employees.department_id,  departments.depart_name
FROM employees
JOIN departments using (department_id)
WHERE employees.department_id in (40, 80)
"""

for item in select_query(connection, employee_departments_40_80):
    print(item)

# 4. Write a query in SQL to display all departments including those
# where does not have any employee

all_departments = """
SELECT department_id, depart_name  FROM departments
"""
for item in select_query(connection, all_departments):
    print(item)

# 5.Write a query in SQL to display the first name of all employees
# including the first name of their manager

employee_manager = """
SELECT E.first_name AS 'Employee Name',
M.first_name AS 'Manager Name' 
FROM employees E
    JOIN employees M
        ON E.manager_id = M.employee_id
"""

for item in select_query(connection, employee_manager):
    print(item)

# 6. Write a query in SQL to display the job title, full name
# (first and last name ) of the employee,
# and the difference between the maximum salary
# for the job and the salary of the employee

employee_salary_difference = """
SELECT jobs.job_title, 
employees.first_name || employees.last_name AS 'Full name',
jobs.max_salary - employees.salary AS 'Salary difference'
FROM employees
JOIN jobs using (job_id)
"""

for item in select_query(connection, employee_salary_difference):
    print(item)

# 7. Write a query in SQL to display the job title and
# the average salary of employees

employee_avg_salary = """
SELECT jobs.job_title, AVG(employees.salary)
FROM employees
LEFT JOIN jobs using (job_id)
GROUP BY jobs.job_title
"""

for item in select_query(connection, employee_avg_salary):
    print(item)

# 8. Write a query in SQL to display the full name (first and last name),
# and salary of those employees who work in any department located in London

employee_salary_london = """
SELECT employees.first_name || employees.last_name AS 'Full name',
employees.salary, locations.city
FROM employees
JOIN departments using (department_id)
JOIN locations using (location_id)
WHERE locations.city = 'London'
"""

for item in select_query(connection, employee_salary_london):
    print(item)

# 9. Write a query in SQL to display the department name and the number
# of employees in each department

employees_in_department = """
SELECT departments.depart_name, count(*) 
FROM employees
JOIN departments using (department_id)
GROUP BY departments.depart_name
"""

for item in select_query(connection, employees_in_department):
    print(item)