metr = int(input('Кількість метрів '))
km = metr/1000
mili = km*0.621
duim = metr*39.3
yard = metr*1.09
ver = int(input(' 1 милі \n 2 дюйми \n 3 ярди \n'))
if ver == 1:
    print(mili)
elif ver == 2:
    print(duim)
elif ver == 3:
    print(yard)
