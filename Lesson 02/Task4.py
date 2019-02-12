a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
x = a
y = a
if a < b:
    x = b
if x < c:
    x = c
print('The biggest number is', x)
if a > b:
    y = b
if y > c:
    y = c
print('The smallest number is', y)




