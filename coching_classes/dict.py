#Dict(dictionary)

#it is a collection of key and values whwre key never be duplicate,it is hetrogenious,mutable,nested,created by {} and dict()
# keys=it retuns only all keys
# values=it return only values
#dict have some method that are used for delete elements 1.pop-it takes keys as params,popitem-> it removes last element from dict


# to remove whole dict use universal method 'del' it delete dict completly

# Code 1
# di={1:'a',2:'B',4:'Y',9:'G'}
# for k,v in di.items():
#     print(k,":",v)



# Code 2
# stu = {}
# no = int(input("How many Students: "))
# for i in range(no):
#     sid = int(input("Student Id: "))
#     s_name = input("Student Name: ")
#     p = int(input("Physics Marks: "))
#     c = int(input("Chemistry Marks: "))
#     m = int(input("Maths Marks: "))
#     stu[sid] = {'Name': s_name, 'Phy': p, 'Chem': c, 'Maths': m}

# print('Roll no\tStudent name\tTotal Marks\tDivision')
# for roll, marks in stu.items():
#     print(roll, end='\t')
#     total = 0
#     for k, value in marks.items():
#         if type(value) == str:
#             print(value, end="\t")
#         else:
#             total += value
#     print(total, end='\t')
#     per=total//3
#     if per >= 60:  
#         print("First Division")
#     elif per >= 45 and per<60:  
#         print("Second Division")
#     elif per >= 33 and per<45:  
#         print("third Division")
#     else:
#         print("Third Division")

#Code 3

# Sample dictionary
my_dict = {'a': 5, 'b': 2, 'c': 7, 'd': 1}

# Sorting the dictionary based on values
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict)

def bubble_sort_dict(d):
    items = list(d.items())
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j][1] > items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    sorted_dict = dict(items)
    return sorted_dict


my_dict = {'a': 5, 'b': 2, 'c': 7, 'd': 1}

sorted_dict = bubble_sort_dict(my_dict)

print(sorted_dict)

import operator
di={101:'Naurangi',102:'Sakshi',100:'Pratham',20:'Amar'}

sdi=sorted(di.items(),key=operator.itemgetter(1))

print(sdi)


marks={'phy':25,'math':76}
internal_marks={'Practical':56}

marks.update(internal_marks)
print(marks)
    

# List Comprehensive

li = [1, 3, 5, 7, 2, 4, 6, 8]
result = ['even %d' % x if x % 2 == 0 else 'odd %d' % x for x in li]
print(result)
