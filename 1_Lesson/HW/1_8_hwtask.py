n = int(input("Введите колличество долек по горизонтали: "))
m = int(input("Введите колличество долек по вертикали: "))
k = int(input("Введите колличество долек которое необходимо отломить: "))

if k < n * m and k % n == 0 or k % m == 0:
	print("yes")
else:
	print("no")
