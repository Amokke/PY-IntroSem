bushes = int(input("Введите колличество кустов: "))

berrybush = {}

for i in range(bushes):
	berrybush[i+1] = int(input(f"Введите колличество ягод на {i+1} кусте: "))

max = 0
optimal = 0

for bush, berry in berrybush:
	if max < (berrybush[bush] + berrybush[bush - 1] + berrybush[bush + 1]):
		max = (berrybush[bush] + berrybush[bush - 1] + berrybush[bush + 1])
		optimal = bush

print(f"Оптимальные куста для сбора {optimal - 1}{optimal}{optimal + 1}{max}")
