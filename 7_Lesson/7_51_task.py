def same_by(charac, objects): # charac это lambda x: x % 2, objects это values
    list_characteristic = [charac(i) for i in objects] # list comprehension - генератор списка
    for i in range(len(list_characteristic) - 1):
        if list_characteristic[i] != list_characteristic[i+1]:
            return False
    return True
    
values = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values):
 print('same')
else:
 print('different')