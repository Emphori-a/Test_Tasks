"""Оператор выбора, для вывода периодов постоянства остатков."""

import sqlite3

con = sqlite3.connect('sber_tasks.db')

cur = con.cursor()

create_transfers_query = '''
CREATE TABLE IF NOT EXISTS transfers(
    from_acc INTEGER,
    to_acc INTEGER,
    amount INTEGER,
    tdate DATE
);
'''
cur.execute(create_transfers_query)
filling_transfers_query = '''
INSERT INTO transfers(from_acc, to_acc, amount, tdate)
VALUES
(1, 2, 500, '2023-02-23'),
(2, 3, 300, '2023-03-01'),
(3, 1, 200, '2023-03-05'),
(1, 3, 400, '2023-04-05');
'''
cur.execute(filling_transfers_query)
con.commit()

create_temp_table = '''
CREATE TEMPORARY TABLE IF NOT EXISTS Transaction_Balances AS
SELECT tdate, from_acc AS acc, -amount AS balance
FROM transfers

UNION ALL

SELECT tdate, to_acc AS acc, amount AS balance
FROM transfers;
'''
cur.execute(create_temp_table)

task_query = '''
SELECT acc, tdate AS dt_from,
    LEAD(tdate, 1, '3000-01-01')
        OVER (PARTITION BY acc ORDER BY tdate) AS dt_to,
    SUM(balance) OVER (PARTITION BY acc ORDER BY tdate) AS balance
FROM Transaction_Balances
ORDER BY acc, dt_from
'''

result = cur.execute(task_query)
for res in result:
    print(res)

con.close()
