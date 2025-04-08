# TIme complexity: O(n^2)
# Space complexity: O(n)
# Pascal's Triangle
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

# Recursive Solution
# Time complexity: O(n^2) 
# Space complexity: O(n)
def generate2(numRows: int): 
    if numRows == 1: 
        return [[1]]
        
    prevRows = generate(numRows -1)
    prevRow = prevRows[-1]
    newRow = [1]*numRows

    for i in range(1,numRows-1): 
        newRow[i]  = prevRow[i] + prevRow[i-1]
    
    prevRows.append(newRow)
    return prevRows

# COMBINATION OF BOTH OR DP SOLUTION 
# TIme complexity: O(n^2)
# Space complexity: O(n)
def generate3(numRows: int): 
    if numRows == 1: 
        return [[1]]

    prevRows = generate3(numRows-1)
    prevRow = prevRows[-1]
    newRow = [1]

    for i in range(0,len(prevRow)-1): 
        newRow.append(prevRow[i]+prevRow[i+1])
    newRow.append(1)

    prevRows.append(newRow)
    return prevRows

print(generate3(5))
print(generate3(4))
print(generate3(3))


