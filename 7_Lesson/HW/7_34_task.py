text = str(input("Введите фразу: "))

def ritm(str):
    str = str.split()
    list_w = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_w.append(sum_w)
    return len(list_w) == list_w.count(list_w[0])

if ritm(text):
    print('Парам пам-пам')
else:
    print('Пам парам')