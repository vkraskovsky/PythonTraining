# Для двух чисел Х,У определить, являются ли они корнями уравнения А*P4+D*P2+C=0

x = float(input('Enter x value:'))
y = float(input('Enter y value:'))

a = 1
b = 2
c = -24
if a * (x ** 4) + b * (x**2) + c == 0:
    print('{} is root'.format(x))
if a * (y ** 4) + b * (y**2) + c == 0:
    print('{} is root'.format(y))
if a * (x ** 4) + b * (x**2) + c != 0:
    print('{} is NOT root'.format(x))
if a * (y ** 4) + b * (y**2) + c != 0:
    print('{} is NOT root'.format(y))


