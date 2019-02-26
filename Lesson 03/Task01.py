# Задача 0
# Дан список А1..AN.Вывести элементы списка в обратном порядке.

# Variant1 - using 'while'

print('Now with -while-')
num_itr = int(input('Type number of iterations:'))
my_list = []
i = 0
while i < num_itr:
    my_list.append(input('Type smth:' + str(i + 1) + ' '))
    i += 1
print(list[::-1])
# Variant2 - using 'for'

print('Now with -for-')
list1 = []
num_itr = int(input('Type number of iterations:'))
for x in range(num_itr):
    list1.append(input('Type smth:' + str(x + 1) + ' '))
print(list1[::-1])
