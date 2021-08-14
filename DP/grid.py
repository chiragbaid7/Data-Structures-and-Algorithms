def grid_traveller(m,n):
    if(m==1 and n==1):
        return 1
    if(m==0 or n==0):
        return 0
    return grid_traveller(m-1,n)+grid_traveller(m,n-1)
 
def grid_graveller_table(m,n):  
    grid=[[0 for j in range(n+1)]for i in range(m+1)]
    grid[1][1]=1

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(i==1 and j==1):
                continue
            grid[i][j]=grid[i-1][j]+grid[i][j-1]
    return grid[m][n]

#print(grid_traveller(50,50))
print(grid_graveller_table(50,50))