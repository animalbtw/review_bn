from urllib.request import urlretrieve
import time
import zipfile
import os
import numpy as np


def main(url):
# Скачиваем zip файл с данными.
	try:
		zipdata = 'dataset.zip'
		urlretrieve(url, zipdata)
		print('\nZip файл успешно загружен\n')
	except:
		print('Ошибка загрузки, либо файл уже загружен\n')

# Извлечение txt.
	try:
		print('Извлечение...\n')
		f = zipfile.ZipFile('dataset.zip', 'r')
		f.extractall()
		print('Извлечение успешно\n')
	except:
		print('Извлечение не выполнено, либо извлечение уже было произведено\n')

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
	resultIntersection = []
	resultDifferences = []
# Пересечение(1)
	for x in dataSet1:
		if x in dataSet2:
			resultIntersection.append(x)
# Отличия(2)
	for y in dataSet1:
		if y not in dataSet2:
			resultDifferences.append(y)
# Медиана(3)
	a = np.array(dataSet1, float)
	b = np.array(dataSet2, float)
	aMed = np.median(a)
	bMed = np.median(b)
	medians = (aMed,bMed)
# Корреляция(4)
	d = np.array(dataSet1).astype(np.float)
	b = np.array(dataSet2).astype(np.float)
	corr = np.corrcoef(d,b)
	

# Создание файла с результатом
	try:
		strCorr = ('Значение корреляции\n' + str(corr))
		strMedian = ('Значения медиан\n' + str(medians))
		strResultIntersection = ('Пересечение списков\n' + str(resultIntersection) + '\n\n')
		strResultDifferences = ('\n\nЗначения, не пересекающиеся в списках\n' + str(resultDifferences) + '\n\n')
		with open('result.txt', 'w') as result:
			result.write(strResultIntersection)
			result.write(strResultDifferences)
			result.write(strCorr)
			result.write(strMedian)
			result.close()
		print('Результат сохранен в файл result.txt')
	except:
		print('Ошибка сохранения результата')

	return strResultDifferences, strResultIntersection, strMedian, strCorr


url = 'https://drive.google.com/uc?authuser=0&id=1MJecQrW-LEnutKl93DxiI-GYmg49MWES&export=download'
while True:
	main(url)
# Пауза 10 минут, после этого цикл повторится.
	time.sleep(600)
# Для наглядности продемонстрировано удаление zip файла, после чего функция скачает его вновь.
	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dataset.zip')
	os.remove(path)
