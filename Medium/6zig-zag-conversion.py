def convert(s, numRows):
    if numRows == 1 or numRows>=len(s): 
        return s
    n = [] 
    c = 0
    inc = 1
    for i in range(len(s)): 
        if c == 0: 
            f = 1 
        elif c == numRows-1: 
            f = 0 

        n.append(c)
        if f: 
            c+=1
        else: 
            c-=1
    output = ""
    for i in range(numRows): 
        for j in range(len(n)): 
            if i == n[j]:
                output+=s[j]
    return output


# print(convert("AB",1))
print(convert("TYLERISAWESOME",15))