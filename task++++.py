# На вход программе подаются две строки текста, содержащие по одному слову из перечня  
# "камень", "ножницы", "бумага", "ящерица" или "Спок". На первой строке записан выбор Тимура, на второй – выбор Руслана. 
 
# Формат выходных данных 
# Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью. 
 
# Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень.
# Камень давит ящерицу, а ящерица травит Спока, в то время как Спок ломает ножницы,
# которые, в свою очередь, отрезают голову ящерице, которая ест бумагу,
# на которой улики против Спока. Спок испаряет камень, а камень, разумеется, затупляет ножницы. 

a=input() 
b=input() 
m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан', 
        'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья', 
        'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур', 
        'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур', 
        'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан', 
        'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан', 
        'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья', 
        'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур', 
        'Спок-ящерица': 'Руслан'} 

res = f'{a}-{b}' 
if res in m: 
    print(f'{m[res]}') 
else: 
    print('Not in list')