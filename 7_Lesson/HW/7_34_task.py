text = input("Введите фразу: ").split()
dictionary = 'уеыаоэяию'
result = [sum([True for j in word.lower() if j in dictionary]) for word in text]

print(result)
if all(result) and len(set(result)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')