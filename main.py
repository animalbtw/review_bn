from urllib.request import urlretrieve
import time
import zipfile
import os


def main(url):
# Скачиваем zip файл с данными.
	try:
		zipdata = 'dataset.zip'
		urlretrieve(url, zipdata)
		print('\nZip файл успешно загружен\n')
	except:
		print('Ошибка загрузки\n')

# Извлечение txt.
	try:
		print('Извлечение...\n')
		f = zipfile.ZipFile('dataset.zip', 'r')
		f.extractall()
		print('Извлечение успешно\n')
	except:
		print('Извлечение не выполнено\n')

# Распределение файлов по спискам для дальнейшего сравнения.
	dataSet1 = []
	dataSet2 = []
# первый файл.
	with open('time series 1.txt', 'r') as q:
		dataSet1 = q.read().split()
		q.close()
# второй файл.
	with open('time series 2.txt', 'r') as w:
		dataSet2 = w.read().split()
		w.close()

# Сравнение списков
	resultIntersection = [] # Пересечение.
	resultDifferences = [] # Отличия.

	for x in dataSet1:
		if x in dataSet2:
			resultIntersection.append(x)
	print(str(resultIntersection), '- Пересечение списков\n')

	for y in dataSet1:
		if y not in dataSet2:
			resultDifferences.append(y)
	print(str(resultDifferences), '- Значения, не пересекающиеся в списках\n')
	return resultDifferences, resultIntersection


url = 'https://drive.google.com/uc?authuser=0&id=1MJecQrW-LEnutKl93DxiI-GYmg49MWES&export=download'

while True:
	main(url)
# Пауза 10 минут, после этого цикл повторится.
	time.sleep(600)
# Для наглядности продемонстрировано удаление zip файла, после чего функция скачает его вновь.
	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dataset.zip')
	os.remove(path)
