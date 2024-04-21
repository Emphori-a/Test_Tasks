# Тестовые задания  

## Python  

1) Особенный номер – строка формата [2-4 цифры]\[2-5 цифр]. 
Хороший номер - строка формата [4 цифры]\[5 цифр]. 
Хороший номер можно получить из особенного дополнением нулей слева к обоим числам.

Пример:
17\234 => 0017\00234 

Напишите функцию, которая принимает на вход строку и для каждого особенного номера, встречающегося в строке, выводит соответствующий хороший номер.

------------------------------------------------------------------------------
- Получаем на вход строку.
- Передаем строку в функцию, выбирающие все необходимые нам номера с помощью регулярного выражения.
- Функция возвращает либо список номеров для дальнейшей обработки, либо сообщение об отсутствии таких номеров.
- Если полученный ответ является списком отдаем список во вторую функцию, обрабатывающую такие номера.
- Для обработки номера делим номер по слэшу, добавляем нужное количество нулей к строке с помощью метода zfill(), соедиянем номер обратно, возвращаем список обработанных номеров.
- Выводим список обратботанных номеров построчно на печать.
------------------------------------------------------------------------------

2) На прямой дороге расположено n банкоматов. Было решено построить ещё k банкоматов для того, чтобы уменьшить расстояние между соседними банкоматами. 
На вход подаются натуральные числа n и k, а также n-1 расстояний L, где – расстояние между банкоматами i и  i+1. Напишите функцию, которая добавляет k банкоматов таким образом, чтобы максимальное расстояние между соседними банкоматами являлось минимально возможным, и возвращает список новых расстояний между банкоматами.

------------------------------------------------------------------------------
- формируем словарь для сохранения количества делений каждой дистанции типа "индекс значения дистанции : количество делений (изначально = 1)"
- далее в цикле while (по количеству банкоматов, оторые нужно добавить) ищем максимальную дистанцию с учетом их делителя из словаря, для максимальной дистанции увеличиваем количество делений на 1
- с помощью list comprehension собираем новый список дистанций
------------------------------------------------------------------------------

3) Напишите функцию, которая принимает на вход список строк, состоящих из цифр, и возвращает максимальное возможное число, которое может получиться в результате конкатенации всех строк из этого списка.

------------------------------------------------------------------------------
- Получаем строку с числами, формируем из нее список строк, состоящий из цифр.
- Полученный список передаем в функцию для получения масимального числа при конкатенации строк.
- В функции сортируем список по убыванию, в качестве ключа сортировки используем лямбда-функцию для того, чтобы учесть различия в длинне строк.
- Полученный список соединяем в строку, возвращаем полученную строку и выводим ее на печать.
------------------------------------------------------------------------------

## SQL

1) Требуется составить расписание случайных проверок. Создайте оператор выбора, который выдаст 100 дат, начиная с текущей, при этом каждая дата отличается от предыдущей на 2-7 дней.

------------------------------------------------------------------------------
- С помощью оператора WITH создаем общее табличное выражение. Далее с помощью ключевого слова RECURSIVE указываем, что данное выражение может ссылаться на себя внутри выражения.
- Первый SELECT - выбирает первую дату для добавления в таблицу (текущая дата).
- UNION ALL - объединяем первую дату с последующими, которые сформируем (объединяем 2 SELECT).
- Второй SELECT - выбираем предыдущую дату и добавляем к ней случайное количество дней 
и формируем из нее новую дату.
- LIMIT - ограничивает рекурсию нужным нам количеством дат.
- SELECT * FROM Dates - выбирает все даты из общего табличного выражения.
------------------------------------------------------------------------------

2) Требуется оценить эффективность продавцов. Создайте запрос, который вернёт количество и сумму продаж для каждого продавца, а также ранжирует продавцов по количеству продаж и по сумме продаж.

Результат запроса должен содержать столбцы id, name из таблицы employee, а также столбцы:
sales_c - количество продаж, 
sales_rank_c - ранг по количеству продаж, 
sales_s - сумма продаж, 
sales_rank_s -  ранг по сумме продаж.

------------------------------------------------------------------------------
Основной запрос для выполнения задания хранится в переменной task_query.
- Соединяем таблицы employee и sales с помощью LEFT JOIN для того, чтобы по всем продавцам сформировалась данные, даже если у них нет продаж.
- В SELECT выбираем нужные нам столбцы, а также дополнительно формируем столбцы:
    - sales_c с помощью функции COUNT
    - sales_rank_c с помощью функции DENSE_RANK()
    - sales_s с помощью функции SUM, с помощью CASE обрабатываем случай, когда значение sales_s None
    - sales_rank_s - с помощью функции RANK()
- Группируем полученные результаты по id и name
- Сортируем полученные результаты по рассчитанным рангам
------------------------------------------------------------------------------

3) Имеется таблица денежных переводов transfers. Где:
from – номер аккаунта, с которого сделан перевод,
to – номер аккаунта, на который сделан перевод,
amount – сумма перевода,
tdate – дата перевода.
Требуется создать оператор выбора, который для каждого аккаунта выведет периоды постоянства остатков. Результат запроса должен содержать столбцы acc – номер аккаунта, dt_from - начало периода,
dt_to - конец периода, balance – остаток на счёте в данном периоде.
Дата конца последнего периода – 01.01.3000.

------------------------------------------------------------------------------
Решение задачи два запроса: create_temp_table и task_query.
1) В запросе create_temp_table:
- Создаем временную таблицу путем соединения двух запросов на выборку из нашей основной таблицы:
    - в первом SELECT выбираем транзакции "на списание" по полю from_acc и соответственно сумму баланса для таких транзакций делаем отрицательной.
    - во втором SELECT выбираем транзакции "на зачисление" по полю to_acc и соответственно для таких транзакций делаем баланс положительным.
    - Объединяем оба запроса с помощью UNION ALL в один набор данных.
2) В запросе task_query:
- выбираем необходимые нам значения из временной таблицы
- с помощью функции LEAD вычисляем дату окончания периода, если следующей строки с датой нет, берем значение по умолчанию для даты последнего периода
- с помощью функции SUM считаем сумму баланса
- с помощью конструкции OVER (PARTITION BY acc ORDER BY tdate) мы группируем данные по полю acc и сортируем их по дате, к этим группам применяются вышеуказанные функции LEAD и SUM
- полученные данные сортируем по номеру аккаунта и дате
------------------------------------------------------------------------------