days = int(input("Введите колличество дней: "))

count = 0
result = 0

for i in range(days):
    temp = int(input(f"{i + 1} день: "))
    if temp > 0:
        count += 1
        if count > result:
            result = count
    else:
        count = 0
print(result)