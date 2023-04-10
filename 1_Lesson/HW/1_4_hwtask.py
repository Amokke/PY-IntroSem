sum = int(input("Введите число журавликов: "))

if sum % 6 == 0:
	x = int(sum / 6)
	y = x * 4
	print(f"{x}  {y}  {x}")
else:
	print("Введено некорректное число")
