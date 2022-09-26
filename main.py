num_1 = int(input('Перше число '))
num_2 = int(input('Друге число '))
num_3 = int(input('Третє число '))
ver = int(input(' 1 додавання \n 2 множення \n'))
if ver == 1:
    r = num_1+num_2+num_3
    p = 'додавання'
    y = p
    print(r)
else:
    r = num_1*num_2*num_3
    m = 'множення'
    y = m
    print(r)

