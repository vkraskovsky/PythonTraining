# Если среди трех чисел А,В,С имеется хотя бы одно четное вычислить максимальное, иначе - минимальное

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
x = a
y = a
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    if a < b:
        x = b
    if x < c:
        x = c
    print('The biggest number is', x)
else:
    if a > b:
        y = b
    if y > c:
        y = c
    print('The smallest number is', y)
