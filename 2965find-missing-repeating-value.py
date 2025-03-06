
def findMissingAndRepeatedValues(grid: list[list[int]]):
    n = len(grid[0])
    d = []
    for i in range(n*n): 
        d.append(0)
    
    for i in range(n): 
        for j in range(n): 
            d[grid[i][j]-1] +=1
    
    a = 0 
    b = 0
    for i in range(n*n): 
        if d[i] == 2: 
            a = i
        if d[i] == 0: 
            b = i
    return [a+1,b+1]

print(findMissingAndRepeatedValues([[1,3],[2,2]]))