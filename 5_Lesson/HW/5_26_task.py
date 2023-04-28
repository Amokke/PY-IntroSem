A = int(input("Введите число А: "))
B = int(input("Введите число B: "))

def pow_num(x, y):
    if y == 1:
        return x
    return x * pow_num(x, y - 1)

print(f"A в степени B: {pow_num(A,B)}")

