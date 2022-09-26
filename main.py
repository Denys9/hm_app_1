numb1 = int(input("Число -> "))
numb2 = 0
while numb1 > 0:
    digit = numb1 % 10
    numb1 = numb1 // 10
    numb2 = numb2 * 10
    numb2 = numb2 + digit
print('Обратное число ->', numb2)