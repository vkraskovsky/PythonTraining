# Ввести три числа А,В,С. Удвоить каждое из них, если А>=В>=С, иначе поменять значения А и В

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
if a >= b >= c:
    print('Condition:A>=B>=C')
    a = a * 2
    b = b * 2
    c = c * 2
else:
    x = a
    a = b
    b = x
print(a, b, c)
