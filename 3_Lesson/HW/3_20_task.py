word = input("Введите слово: ").upper()

score = {1:"AEIOULNSTRАВЕИНОРСТ",
         2:"DGДКЛМПУ",
         3:"BCMPБГЁЬЯ",
         4:"FHVWYЙЫ",
         5:"KЖЗХЦЧ",
         8:"JXШЭЮ",
         10:"QZФЩЪ"}

summscore = 0

for i in word:
    for point, letter in score.items():
        if i in letter:
            summscore += point

print(f"Вы заработали {summscore} очков")