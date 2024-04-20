"""Расписание случайных проверок."""

import sqlite3

con = sqlite3.connect('sber_tasks.db')

cur = con.cursor()

query = '''
WITH RECURSIVE Dates AS (
  SELECT DATE('now') AS RandomDate
  UNION ALL
  SELECT DATE(RandomDate, '+' || (ABS(RANDOM()) % 6 + 2) || ' days')
  FROM Dates
  LIMIT 100
)
SELECT *
FROM Dates;
'''

dates = con.execute(query)

for date in dates:
    print(date[0])
