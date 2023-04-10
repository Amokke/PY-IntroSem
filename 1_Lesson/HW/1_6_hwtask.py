number = int(input("Введите шестизначное число: "))

n1 = number // 1000
n2 = number % 1000

if number > 99999 and number < 1000000:
        e = n1 % 10
        n1 = n1 // 10
        d = n1 % 10
        s = n1 // 10
        sum1 = e + d + s
        e = n2 % 10
        n2 = n2 // 10
        d = n2 % 10
        s = n2 // 10
        sum2 = e + d + s
        if sum1 == sum2:
                print("yes")
        else:
                print("no")
else:
        print("Введено некорректное число")
