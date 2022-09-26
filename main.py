num_1 = int(input('Перше число '))
num_2 = int(input('Друге число '))
num_3 = int(input('Третє число '))
ver = int(input(' 1 більше число \n 2 меньше число \n 3 середнє арифметичне \n'))
if ver == 1:
    if num_1<num_2<num_3:
        print(num_3)
    elif num_1<num_2>num_3:
        print(num_2)
    elif num_1>num_2>num_3:
        print(num_1)
if ver == 2:
    if num_1<num_2<num_3:
        print(num_1)
    elif num_1>num_2>num_3:
        print(num_3)
    elif num_2<num_3<num_1:
        print(num_2)
if ver == 3:
    r = (num_1+num_2+num_3)/3
    print(r)