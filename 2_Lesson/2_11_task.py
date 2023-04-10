A = int(input("Введите натуральное число больше 1: "))

a1 = 0
a2 = 1
count = 2

if A > 1:
	while a2 <= A:
		if a2 == A:
			print(count)
			break
		a1, a2 = a2, a1 + a2
		count += 1
		if a2 > A:
			print(-1)
			break
