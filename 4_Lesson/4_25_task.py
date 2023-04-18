string = "a a a b c a a d c d d".split()

dict = {}.fromkeys(string, 0)

for i in string:
	print(f"{i}_{dict[i]}" if dict[i] else i, end = " ")
	dict[i] += 1

