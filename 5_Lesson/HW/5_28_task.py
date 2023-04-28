A = int(input("Введите число А: "))
B = int(input("Введите число B: "))

def sum(x, y):
    if x == 0:
        return y;
    return sum(x-1, y+1)

print(f"Сумма чисел A и B: {sum(A,B)}")
