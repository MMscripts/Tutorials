import sqlite3

tridb_path = r'D:\type_example_5.TRIDB'
connection = sqlite3.connect(tridb_path)
cursor = connection.cursor()

# Получение имен и ID всех каркасов
cursor.execute("SELECT Name, ID FROM GeneralInformation")
print("Имена и ID всех каркасов: ", cursor.fetchall())

# Получение имен и ID каркасов, которые создал пользователь по имени Andrey
cursor.execute("SELECT Name, ID FROM GeneralInformation WHERE CreateBy = 'Andrey'")
names_and_ids = cursor.fetchall()
print("Каркасы, которые создал Андрей: ", names_and_ids)
# Используя полученные ID каркасов, удаляем соответствующие записи в базе данных
for name, id in names_and_ids:
	cmd ="""
		 DELETE FROM UserAttributeValue WHERE TriangulationId = {0};
		 DELETE FROM TriangleAttributeValue WHERE TriangulationId = {0};
		 DELETE FROM PointAttributeValue WHERE TriangulationId = {0};
		 DELETE FROM Geometry WHERE ID = {0};
		 DELETE FROM GeneralInformation WHERE ID = {0};
		 """.format(id)
	cursor.executescript(cmd)
connection.commit()

# Повторение первого SQL-запроса для того, чтобы увидеть изменения
cursor.execute("SELECT Name, ID FROM GeneralInformation")
print("Имена и ID всех оставшихся каркасов: ", cursor.fetchall())

connection.close()