a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
x=a * b
print(x)
if a < b:
    a = (a + b)/2
 #   b = a * b * 2
    b = x * 2
else:
    b = (a + b) / 2
 #   a = (a * b) * 2
    a = x * 2
print('a -', a)
print('b -', b)