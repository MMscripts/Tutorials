import sqlite3

tridb_path = r'D:\Scripts\one-hit wonder script\tutorials\tridb_tutorials\type_example_2.TRIDB'
connection = sqlite3.connect(tridb_path)
cursor = connection.cursor()

# SQL-запрос для получения имен каркасов с объемом больше, чем 400
sql_request = "SELECT Name, Volume, CreateBy FROM GeneralInformation WHERE Volume > 400"
# Выполнение SQL-запроса
cursor.execute(sql_request)
# Вывод результатов на экран
print("Имя каркаса, объем и автор: ", cursor.fetchall())

# SQL-запрос для получения суммарного объема
sql_request = "SELECT SUM(Volume) FROM GeneralInformation WHERE Volume > 400"
# Выполнение SQL-запроса
cursor.execute(sql_request)
# Вывод результата на экран
print("Суммарный объем найденных каркасов: ", cursor.fetchone()[0])

# Закрыть соединение
connection.close()