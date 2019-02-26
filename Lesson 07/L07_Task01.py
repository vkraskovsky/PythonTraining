# Test task 01.
from collections import Counter

my_string = input('Enter string:')
my_list = sorted(my_string.split(), key=len, reverse=True)
print(my_list)
count = Counter(my_list)
final_list = (list(count.items()))
for i in final_list:
    if (lambda x: x[1])(i) == 1:
        print((lambda x: x[0])(i))
        break
    else:
        print((lambda x: x[0])(final_list[1]))
        break
