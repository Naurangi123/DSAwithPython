
def Count_Alphabet(Str):
    obj={}
    for x in Str:
        if x in obj:
            obj[x]+=1
        else:
            obj[x]=1
    return obj

Str="naurangi lal"
result=Count_Alphabet(Str)
print(result)


#Recursion

def Letter_Frequency(Str,obj=None):

    #First Base Case
    if not Str:
        return obj
    
    #Second Base Case
    if obj is None:
        obj={}

    #initialize variable X with Zero
    x=Str[0]

    #Main code for checking frequency of letter
    if x in obj:
            obj[x]+=1
    else:
        obj[x]=1
    return Letter_Frequency(Str[1:], obj)


Str="naurangi lal"
result=Count_Alphabet(Str)
print(result)

