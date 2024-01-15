

def min_cost_ofPath(twoDArray,row,col,cost):
    if cost>0:
        return 0
    elif row==0 and col==0:
        if twoDArray[0][0]-cost==0:
            return 1
        else:
            return 0
    elif row==0:
        return min_cost_ofPath(twoDArray,0,col-1,cost-twoDArray[row][col])
    elif col==0:
        return min_cost_ofPath(twoDArray,row-1,0,cost-twoDArray[row][col])
    else:
        op1=min_cost_ofPath(twoDArray,row-1,col,cost-twoDArray[row][col])
        op2=min_cost_ofPath(twoDArray,row,col-1,cost-twoDArray[row][col])
        return op1+op2


twoDArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result=min_cost_ofPath(twoDArray,2,8,10)
print(result)