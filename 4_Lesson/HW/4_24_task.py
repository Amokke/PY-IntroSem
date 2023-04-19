bushes = int(input("Введите колличество кустов: "))

berrybush = list()

for i in range(bushes):
	berrybush.append(int(input(f"Введите колличество ягод на {i+1} кусте: ")))


count = list()

for i in range(bushes -1):
	count.append((berrybush[i - 1]) + (berrybush[i]) + (berrybush[i + 1]))
count.append((berrybush[-2]) + (berrybush[-1]) + (berrybush[0]))
print(max(count))