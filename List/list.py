# # # A List is a data structure that holds an ordered collection of items.
# A list is containing d/f type of data
list=[1,4,7,9,'naurangi','rajesh',1.5,6.7]
print(list)

list1=[1,3,2,['ldfkjnv','gjkb',7,5]]
print(list1)

# #Search element present in the list
#
lis=[1,34,6,79,8,7,65,4,3,2]
if 6 in lis:
    print(lis.index(6))
else:
    print('Not exist')

# # Linear search in List
def searchElement(lis,value):
    for i in lis:
        if i==value:
            return lis.index(value)
    return 'not exist'
print(searchElement(lis,65))
#
# # operations on the list
#
a=[1,3,5,4,8,6,9]
b=[3,6,8]
c=[0,6,2,]
print(len(a))
print(max(b))
print(sum(a)/len(a))

myList=[]
while True:
    num=input("Enter the number")
    if num=='done':
        break
    print(myList)
    value=float(num)
    myList.append(value)
avarage=sum(myList)/len(myList)
print('Avarage',avarage)

a='naurangi-rajesh-rahul'
delimiter='a'
b=a.split(delimiter)
c=list(a)
print(a,b)
print(delimiter.join(b))

import numpy as np
myArray=np.array([1,2,3,4,5,7])
myList=[2,3,4,5,6]
print(myArray)
print(myList)