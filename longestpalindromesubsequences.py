

def findLPS(s,stIndex,ndIndex):
    if stIndex>ndIndex:
        return 0
    elif stIndex==ndIndex:
        return 1
    elif s[stIndex]==s[ndIndex]:
        return 2+findLPS(s,stIndex+1,ndIndex-1)
    else:
        op1=findLPS(s,stIndex,ndIndex-1)
        op2=findLPS(s,stIndex+1,ndIndex)
        return max(op1,op2)
    
s=input("Enter String :")
print(findLPS(s,0,7))
