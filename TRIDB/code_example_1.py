# Импорт модуля sqlite3 для работы с файлами TRIDB
import sqlite3

# Путь к файлу TRIDB
tridb_path = r'D:\type_example_1.TRIDB'

# Создание подключения к указанному TRIDB файлу
connection = sqlite3.connect(tridb_path)
# Создание курсора
cursor = connection.cursor()