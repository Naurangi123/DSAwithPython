
def stack(s):
    if s==0:
        return True
    else:
        return False

# def push(s,x):
#     s=[]
#     while(s!=x):
#         s=+1
#         s=x
#     return s

# def push1(s,x):
#     s.append(x)
#     return x

def push(s, x, index):
    l = []
    for i in range(len(s)):
        if i == index:
            l.append(x)
        l.append(s[i])
    if index == len(s): 
        l.append(x)
    return l

s=[]
x=89
index=3
result=push(s,x,index)
print(result)



