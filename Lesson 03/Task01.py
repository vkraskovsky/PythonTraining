#Variant1 - using 'while'
print ('Now with -while-')
num_itr=int(input('Type number of iterations:'))
list=[]
i=0
while i < num_itr:
    list.append(input('Type smth:'+ str(i+1) + ' '))
    i+=1
print (list[::-1])
#Variant2 - using 'for'
print ('Now with -for-')
list1=[]
num_itr=int(input('Type number of iterations:'))
for x in range(num_itr):
    list1.append(input('Type smth:'+ str(x+1) + ' '))
print (list1[::-1])

