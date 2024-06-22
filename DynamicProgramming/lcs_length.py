def lcs_length(x,y):
    m=len(x)
    n=len(y)
    c = [[0] * (n + 1) for _ in range(m + 1)] 
    b = [[""] * (n + 1) for _ in range(m + 1)] 

    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i - 1] == y[j - 1]:
                c[i][j]=c[i-1][j-1]+1
                b[i][j]="↖"
            elif c[i][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i][j]="↑"     
            else:
                c[i][j]=c[i][j-1]
                b[i][j]="←"
    return c ,b  
x = ['A', 'B', 'C', 'D', 'B', 'D', 'A', 'B']
y = ['B', 'D', 'C', 'A', 'B', 'A']

c, b = lcs_length(x, y)
print("c array:")
for row in c:
    print(row)
print("b array:")
for row in b:
    print(row)
