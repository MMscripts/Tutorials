import sqlite3

tridb_path = r'D:\type_example_3.TRIDB'
connection = sqlite3.connect(tridb_path)
cursor = connection.cursor()

# SQL-запрос для получения имен каркасов и их авторов
sql_request = "SELECT Name, CreateBy FROM GeneralInformation"
# Выполнение SQL-запроса
cursor.execute(sql_request)
# Вывод результатов на экран
print("Имена каркасов и их авторы: ", cursor.fetchall())

# SQL-запрос для изменения имени автора
sql_request = "UPDATE GeneralInformation set CreateBy = 'Andrey' where CreateBy = 'Max'"
# Выполнение SQL-запроса
cursor.execute(sql_request)
# Подтверждение внесенных изменений
connection.commit()

# Повторение первого SQL-запроса для того, чтобы увидеть внесенные изменения
sql_request = "SELECT Name, CreateBy FROM GeneralInformation"
cursor.execute(sql_request)
print("Имена каркасов и их авторы: ", cursor.fetchall())

connection.close()