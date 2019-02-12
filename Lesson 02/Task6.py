a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
x = a
y = a
e = int(a % 2)
print(e)
f = int(b % 2)
print(f)
g = int(c % 2)
print(g)
if a%2==0 or b%2==0 or c%2==0:
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

