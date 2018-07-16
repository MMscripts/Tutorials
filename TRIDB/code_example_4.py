import sqlite3

tridb_path = r'D:\type_example_4.TRIDB'
connection = sqlite3.connect(tridb_path)
cursor = connection.cursor()

# Получение ID и объемы каркасов
cursor.execute('SELECT ID, Volume FROM GeneralInformation')
ids_volumes = cursor.fetchall()
print("ID и объем каркасов: ", ids_volumes)

# Добавление нового пользовательского атрибута "Тоннаж" с ID = 1
cursor.execute("INSERT INTO UserAttributeDefinition (ID, Name, Type, Precision) VALUES (1, 'Тоннаж', 0, 0);")

# Для каждого каркаса расчитывается и добавляется значение нового атрибута
for id, volume in ids_volumes:
	fact_volume = volume * 2.7
	cursor.execute('INSERT INTO UserAttributeValue (TriangulationID, AttributeID, ValueText) VALUES (?, ?, ?)', (id, 1, fact_volume))

# Получение ID и тоннажа каркасов
cursor.execute('SELECT TriangulationID, ValueText FROM UserAttributeValue')
print("ID и тоннаж каркасов: ", cursor.fetchall())

connection.commit()
connection.close()