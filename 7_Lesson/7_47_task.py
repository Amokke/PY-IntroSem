transformation = lambda x: x # вводим в код строку, lambda (анонимную) функцию которая ничего не делает х=х
values = [1, 23, 42, 'asdfg'] # чтобы не писать return
transformed_values = list(map(transformation, values)) #list функция, которая оборачивает в список работу map
 # если не поставить list, то выдаст объект map <map object at 0x000000B67783B070> 
 # map применяет функцию transformation, на 
 # каждый элемент списка values
if values == transformed_values:
 print('ok')
else:
 print('fail')

print(values)
print(transformed_values)