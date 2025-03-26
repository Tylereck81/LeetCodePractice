# Time: O(n) Space O(1)
# ord function takes char and converts to unicode (Unicode for 'A' is 65) , so match A -> 1 is ord('A')-64
def titleToNumber(columnTitle):
    s = 0 
    c = 0
    for i in range(len(columnTitle)-1,-1,-1): 
        s+= (26**c)*(ord(columnTitle[i])-64)
        c+=1
    
    return s
