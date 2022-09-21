import array
#a = input('Введите целое число \n')
#b = input('Введите целое число \n')
#c = input('Введите целое число \n')
#if a<b:
#    if a<c:
#        y=a
#    else:
#        y=c
#else:
#    if b<c:
#        y=b
#    else:
#        y=c
#print('min число:', y)

#a = float(input("Vvedite chislo: "))
#rez = "bolshe nulya" if a > 0 else "menshe nulya"
#if(rez = 0):
#    rez = "ravno"
#print(rez)

a = int(input())
b = int(input())
c = int(input())
if a <= 3 and a >= 1:
    print(a, " vhodit")
else:
    print(a, "ne vhodit")
if b <= 3 and b >= 1:
    print(b, " vhodit")
else:
    print(b, "ne vhodit")
if c <= 3 and c >= 1:
    print(c, " vhodit")
else:
    print(c, "ne vhodit")

a = int(input())
b = int(input())
c = int(input())
if a > 10 or a < 1:
    print(a, " vhodit")
else:
    print(a, "ne vhodit")
if b > 10 or b < 1:
    print(b, " vhodit")
else:
    print(b, "ne vhodit")
if c > 10 or c < 1:
    print(c, " vhodit")
else:
    print(c, "ne vhodit")