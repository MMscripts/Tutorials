# Импорт библиотек для визуализации экспортированного каркаса
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

# Функция для вызова диалогового окна Файл - Экспорт - Каркасы
# Параметры функции: тип и имя каркаса, пути к новым файлам с точками и треугольниками
def wf_geo_to_mm_file(wf_type, wf_name, points_path, triangles_path):
	WireframesExport_FormSet1 = MMpy.FormSet("WIREFRAMES_EXPORT", "16.1.1251.2")
	WireframesExport_FormSet1.set_field("POINTSFILE_TYPE", "2")
	WireframesExport_FormSet1.set_field("POINTSFILE", points_path)
	WireframesExport_FormSet1.set_field("TRIANGLESFILE_TYPE", "2")
	WireframesExport_FormSet1.set_field("TRIANGLESFILE", triangles_path)
	WireframesExport_FormSet1.set_field("EXPORT_TYPE", "5")
	WireframesExport_FormSet1.set_field("FILENAME", "")
	WireframesExport_FormSet1.set_field("LAYER_BOOL", "0")
	WireframesExport_FormSet1.set_field("WF_NAME", wf_name)
	WireframesExport_FormSet1.set_field("WFTYPE", wf_type)
	WireframesExport_FormSet1.set_field("SET_BOOL", "0")
	WireframesExport_FormSet1.set_field("SINGLE_BOOL", "1")
	WireframesExport_FormSet1.run()

# Функция для чтения экспортированных файлов STR
# Данные записываются в список data
def mm_read(path):
	mm_file = MMpy.File()
	mm_file.open(path)
	data = []
	for i_record in range(mm_file.records_count):
		data.append([])
		for i_column in range(1, 4):
			data[i_record].append(mm_file.get_num_field_value(i_column, i_record + 1))
	mm_file.close()
	return data

# Путь к файлу TRIDB и имя каркаса
wf_type = r'D:\type_example_6.tridb'
wf_name = 'каркас_2'
# Пути для сохранения файлов точек и треугольников
points_path = r'D:\points.STR'
triangles_path = r'D:\tris.STR'

# Вызываем функцию для получения файлов с геометрией
wf_geo_to_mm_file(wf_type, wf_name, points_path, triangles_path)

# Записываем информацию из файлов точек и треугольников в переменные points и tri соответственно
points = mm_read(points_path)
tri = mm_read(triangles_path)

# Списки координат
x, y, z = list(zip(*points))
# Создание визуализации
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri, cmap=plt.cm.Purples)
plt.show()