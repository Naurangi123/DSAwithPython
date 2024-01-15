# Create an Array and Traverse
from array import *

my_Array=[1,4,6,8,0,3,5,4,8,7,5,2,4,6]
for i in my_Array:
    print(i)

#Access indivisual element through indexes

print("Step 2")

My_array=[1,4,6,8,0,3,5,4,8,7,5,2,4,6]
print(My_array[5])

#Append any value to the array using append method

print("Step 3")
mY_Array=[1,4,6,8,0,3,5,4,8,7,5,2,4,6]
mY_Array.append(4567)
print(mY_Array)

#Insert value in Array using insert method
print("Step 4")

myArr=[1,4,6,8,0,3,5,4,8,7,5,2,4,6]
myArr.insert(5,23)
print(myArr)

#Extend the Array using extend method

print("step 5")
Ex_Arr=[1,4,6,8,0,3,5,4,8,7,5,2,4,6]
Ex_Arr.extend(Ex_Arr)
print(Ex_Arr)

#Add items from list into array using fromlist() method
# print("step 6")
# Ex_arr1=[1,4,6,8,0,3,5,4,8,7,5,2,4,6]
# templist=[1,4,8,0,3]
# Ex_arr1.fromlist(templist)
# print(Ex_Arr)

# Remove an element in array using remove() method
print("Step 7")
Ex_Arr.remove(7)
print(Ex_Arr)

#Remove last element in the array using pop() method
print("Step 8")
ex_Arr=[1,4,6,8,0,3,5,4,8,7,5,2,4,6]
ex_Arr.pop(5)
print(ex_Arr)

#Fetch any element through its index using index() method
print("step 9")
ex_Arr=[1,4,6,8,0,3,5,4,8,7,5,2,4,6]
print(ex_Arr.index(3))

#Reverse array
print("Step 10")
ex_Arr2=[1,4,6,8,0,3,5,4,8,7,5,2,4,6]
ex_Arr2.reverse()
print(ex_Arr2)

# Buffer information of an array using buffer_info() method
# print('Step 11')
# ex_Arr2=[1,4,6,8,0,3,5,4,8,7,5,2,4,6]
# ex_Arr2.buffer_info()
# print(ex_Arr2)

#Check number of occurence of an element using count() method

print("step 12")
ex_Arr=[1,4,6,8,0,3,5,4,8,7,5,2,4,6]
print(ex_Arr.count(4))

#Convert array to string using tostring() method
# print('Step 13')
# strTemp=mY_Array.tostring()
# print(strTemp)
# ints=mY_Array('i')
# ints.fromstring(strTemp)
# print(ints)

#
