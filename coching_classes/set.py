li=[12,23,12,8,34,5,6,8,9]

s1=set()
s2=set()

for i in li:
    if i not in s1:
        s1.add(i)
    else:
        s2.add(i)

print("Set 1",s1)
print("set2",s2)

print("No of element",(len(s1)+len(s2)))

# frozenset is called "read only set" because it does not allow any modification
a2=frozenset({1,2,34,12,34,56,56,78,7,8,9,3,6})
print(a2)


#TUPLE

#tuple is read only data ,hetrogenious nature,ordered data collection ,may be nested,imutable data collection,and is created by () and tuple()

#it's main purpose to return data in tuple form which can't be modifiable

t=(1,3,4,5,6,7,2,4,6,2,3,6)

print(t.count(2))
print(t)


