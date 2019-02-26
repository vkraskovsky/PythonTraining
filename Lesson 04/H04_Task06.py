# Задача 6
# Преобразовать массив так, чтобы сначала шли все отрицательные элементы,
# а потом положительные(0 считать положительным). Порядок следования должен быть сохранен.


my_list = [10, -1, -6, 15, -5, 100, 0, 20, 4, -7, 8]
negative_list = []
positive_list = []
for i in my_list:
    if i < 0:
        negative_list.append(i)
    else:
        positive_list.append(i)
negative_list.extend(positive_list)
print(negative_list)
