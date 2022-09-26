vari = int(input("number->"))
part_1= int(vari/1000)
part_2= int(vari/100%10)
part_3= int(vari%100/10)
part_4= int(vari%10)
summa = part_1*part_2*part_3*part_4
print(summa)