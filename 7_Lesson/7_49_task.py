orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
    pi = 3.14
    orbits_new = [(0, 0)]
    max = 0
    for i in orbits:
        if i[0] != i[1]:
            if max < pi * i[0] * i[1]:
                max = pi * i[0] * i[1]
                orbits_new.pop() # если выполняется условие, то удаляем предыдущее значение кортежа
                orbits_new.append(i) # и добавляем новое, чтобы в списке оставалась только одно, max
    return orbits_new[0] # добавили [0], чтобы распаковывался список

print(*find_farthest_orbit(orbits))