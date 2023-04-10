coins = int(input("Введите колличество монеток: "))

eagle = 0
tails = 0

for i in range(coins):
    coin = int(input("Орел: 1, Решка: 0 :"))
    if coin == 1:
        eagle += 1
    elif coin == 0:
        tails += 1
if eagle > tails:
    print(f"Монетку необходимо перевернуть {tails} раз")
else:
    print(f"Монетку необходимо перевернуть {eagle} раз")