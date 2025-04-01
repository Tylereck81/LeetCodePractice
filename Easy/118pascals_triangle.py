def generate(numRows):
    if numRows == 1: 
        return [[1]]
    
    l = [[1],[1,1]]
    for i in range(2,numRows): 
        new_row = [] 
        previous_row = l[i-1]
        new_row.append(1)
        for j in range(len(previous_row)-1): 
            new_row.append(previous_row[j]+previous_row[j+1])
        new_row.append(1)
        l.append(new_row)
    
    return l

print(generate(5))
print(generate(4))
print(generate(3))