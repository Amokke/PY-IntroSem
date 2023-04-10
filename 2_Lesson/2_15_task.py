watermelons = int(input("Введите колличество арбузов: "))

count = 1

weight = int(input(f"Вес {count} арбуза: "))

min = weight
max = weight

for i in range(watermelons - 1):
    count += 1
    weight = int(input(f"Вес {count} арбуза: "))
    if min > weight:
        min = weight
    if max < weight:
        max = weight
print(f"Самый легкий арбуз: {min}, самый тяжелый арбуз: {max}")