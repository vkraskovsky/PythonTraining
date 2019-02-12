itr=int(input('Number of inerations:'))
list=[]
list_new=[]
#Getting the list and printing the item to exclude
for i in range(itr):
    list.append(input('Type item'+ str(i+1) + ' :'))
print('Max item to exclude:',max(list))
#Variant1 using append method
for x in range(len(list)):
    if list[x]!=max(list):
        list_new.append(list[x])
print(list_new)
#Variant2 using slices
y=0
while (y<=len(list)) and (list[y]!=max(list)):
    y=y+1
list_final=list[:y] + list[y+1:]
print(list_final)


