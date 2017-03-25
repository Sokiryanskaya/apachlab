with open('myfile.txt', 'w', encoding='utf-8') as myfile:
	myfile.write('Привет, мир')
with open('myfile.txt', 'a', encoding='utf-8') as myfile:
	myfile.write('Пока, мир\n')
with open('myfile.txt', 'a', encoding='utf-8') as myfile:
	myfile.write('\tВсе дома\n')
with open('myfile.txt', 'r', encoding='utf-8') as myfile:
	text=myfile.read()
	print(text)
# этот вариант плох, лучше следующий, это медленно, лучше построчное чтение
with open('myfile.txt', 'r', encoding='utf-8') as myfile:
	for ln in myfile:
		ln=ln.upper()
		ln=ln.replace('\n', ' ')
		print(ln)

#ДЗ - Скачайте файл по ссылке
#Прочитайте его и подсчитайте количество слов в тексте

with open('referat.txt','r',encoding ='utf-8') as homefile:
	words=0
	for line in homefile:
		words_line=len(line.split())
		words+=words_line
		#quantity = len(homefile)
		print (words)
#решила задачу







#сработало
#Режимы открытия файлоы - r-чтение из файла
#w - для записи (содержимое перезаписывается
#a - для добавления (новое содержимое пишется в конец файла)
#\n- перенос строки
#\t - табуляция вначало

