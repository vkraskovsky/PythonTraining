# Test task 02.
from random import randint

my_list_rows = int(input('Enter number of rows:'))
my_list_columns = int(input('Enter number of columns:'))
my_matrix = []
for i in range(my_list_rows):
    my_row = []
    for j in range(my_list_columns):
        my_row.append(randint(10, 20))
    my_matrix.append(my_row)
    print(my_row)
column1 = int(input('1st to change:'))
column2 = int(input('2nd to change:'))
for i in range(my_list_rows):
    my_matrix[i][column1], my_matrix[i][column2] = my_matrix[i][column2], my_matrix[i][column1]
    print(my_matrix[i])


