N = int(input("Введите колличество элиментов в массиве: "))
A = []
count = 0

for i in range(N):
    A.append(int(input(f"Введите {i+1} целое число: ")))

X= int(input("Введите искомое число: "))

for i in range(N):
    if A[i] == X:
        count += 1

print(f"{X} найдено {count} раз ")