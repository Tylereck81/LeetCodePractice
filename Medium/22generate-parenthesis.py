def generateParenthesis(n: int)->list[int]: 
    res = [] 
    def rec(left, right, s): 
        if len(s) == n*2: 
            res.append(s)
        if left<n: 
            rec(left+1, right, s+"(")
        if right<left: 
            rec(left, right+1, s+")") 
    
    rec(0,0,"")  

    return res

print(generateParenthesis(3))