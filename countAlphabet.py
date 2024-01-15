
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

