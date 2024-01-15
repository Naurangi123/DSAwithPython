import numpy as np

twoDArray=np.array([[11,13,15,18],[12,17,16,19],[2,45,9,8],[78,6,4,2]])
print(twoDArray)

# #Insertion in two dimension Array

newTwoDArray=np.insert(twoDArray,0,[[1,2,3,4]],axis=0)
print(newTwoDArray)

print('others')
newTwoDArray=np.insert(twoDArray,1,[[1,2,3,4]],axis=0)
print(newTwoDArray)


print('others')
newTwoDArray=np.append(twoDArray, [[1,2,3,4]],  axis=0)
print(newTwoDArray)
# #
def accessElement(array,rowIndex,colIndex):
    if rowIndex>=len(array) and colIndex>=len(array[0]):
        print("incorrect index")
    else:
        print(array[rowIndex][colIndex])

accessElement(twoDArray,3,2)

# #Traverse in Two Dimensional Array

def traversTDArr(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traversTDArr(twoDArray)


# # Search element nin Two Dimensional Array

def searchElemTDArr(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return 'The valuer in index at'+str(i)+" "+str(j)
            return 'The element is not found'
print(searchElemTDArr(twoDArray,15))

# #Deleting eelement in the 2D array

twoDArray=np.array([[11,13,15,18],[12,17,16,19],[2,45,9,8],[78,6,4,2]])

newTDArr=np.delete(twoDArray,1,axis=1)
print(newTDArr)