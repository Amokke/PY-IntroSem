n = int(input("Введите размер первого множества: "))
m = int(input("Введите размер второго множества: "))

onenumbers = []
twonumbers = []

for i in range(n):
	onenumbers.append(int(input(f"Введите {i+1} число множества: ")))
for i in range(m):
        twonumbers.append(int(input(f"Введите {i+1} число множества: ")))

one = set(onenumbers)
two = set(twonumbers)

summnumbers = []

for i in one:
	for j in two:
		if i == j:
			summnumbers.append(j)

numbers = sorted(summnumbers)
print("Общие числа множеств: ", end = " ")
for i in numbers:
	print(i, end = " ")
