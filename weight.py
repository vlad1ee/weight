a = int(input('Введите ваш вес: '))
def func(weight):
    moonw = 165/10/100
    print(weight * moonw)
    for i in range(1, 16):
        weight += 1
        weightmoon = round(weight * moonw, 2)
        print(weightmoon)

func(a)
