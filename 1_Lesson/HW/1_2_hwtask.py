number = int(input("Введите трехзначное число: "))

if number > 99 and number < 1000:
        e = number % 10
        number = number // 10
        d = number % 10
        s = number // 10
        sum = e + d + s
        print(f"{sum} ({s} + {d} + {e})" )
else:
        print("Введено некорректное число")
