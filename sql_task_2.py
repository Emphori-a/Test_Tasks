"""Оценка эффективности продавцов."""

import sqlite3

con = sqlite3.connect('sber_tasks.db')

cur = con.cursor()

create_emloyee_query = '''
CREATE TABLE IF NOT EXISTS employee(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50)
);
'''

create_sales_query = '''
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    price INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employee (id) ON DELETE CASCADE
);
'''
filling_employee_query = '''
INSERT INTO employee(name)
VALUES
('Vasya'),
('Petya'),
('Masha'),
('Katya');
'''
filling_sales_query = '''
INSERT INTO sales(employee_id, price)
VALUES
(1, 1555),
(1, 980),
(1, 5963),
(3, 8963),
(3, 88963),
(3, 48.50),
(2, 77423),
(2, 15500);
'''
cur.execute(create_emloyee_query)
cur.execute(create_sales_query)
cur.execute(filling_employee_query)
con.commit()
cur.execute(filling_sales_query)
con.commit()

task_query = '''
SELECT employee.id, employee.name, COUNT(sales.employee_id) as sales_c,
    DENSE_RANK() OVER (ORDER BY COUNT(sales.employee_id) DESC) AS sales_rank_c,
    CASE
        WHEN SUM(price) is NULL THEN  0
        WHEN SUM(price) is not NULL THEN SUM(price)
    END AS sales_s,
    RANK() OVER (ORDER BY SUM(price) DESC) AS sales_rank_s
FROM employee
    LEFT JOIN sales ON employee.id = sales.employee_id
GROUP BY employee.id, employee.name
ORDER BY sales_rank_c, sales_rank_s
'''

result = cur.execute(task_query)
for res in result:
    print(res)

con.close()
