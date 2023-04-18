N = int(input("Введите колличество элиментов в массиве: "))
A = []
count = 0
equally = []

for i in range(N):
    A.append(int(input(f"Введите {i+1} целое число: ")))

X= int(input("Введите искомое число: "))

min = abs(A[0] - X)
for i in range(N):
    Y = abs((A[i] - X))
    if min >= Y:
        min = Y
        equally.append(A[i])

print(f"Числа максимально близкие к {X} :", end = " ")
for i in range(len(equally)):
    if abs((A[i] - X)) == min:
        print(A[i], end = "  ")