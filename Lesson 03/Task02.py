# Задача 1
# Исключить из списка А1..AN максимальный элемент.

itr = int(input('Number of iterations:'))
my_list = []
list_new = []
# Getting the list and printing the item to exclude
for i in range(itr):
    my_list.append(input('Type item' + str(i + 1) + ' :'))
print('Max item to exclude:', max(my_list))
# Variant1 using append method
for x in range(len(my_list)):
    if my_list[x] != max(my_list):
        list_new.append(my_list[x])
print(list_new)
# Variant2 using slices
y = 0
while (y <= len(my_list)) and (my_list[y] != max(my_list)):
    y = y + 1
list_final = my_list[:y] + my_list[y + 1:]
print(list_final)
