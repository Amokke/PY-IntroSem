n = int(input("Введите натуральное число: "))

count = 1
N = 1
if n > 0:
	while count <= n:
		N = N * count
		count += 1
	print(f"Факториал числа {n} равен: {N}")
else:
	print("Введены не корректные данные")
