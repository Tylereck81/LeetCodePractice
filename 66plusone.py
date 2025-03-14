def plusone(digits: list) -> list: 
    
    #don't go through loop unless we need to
    if digits[len(digits)-1]+1<=9: 
        digits[len(digits)-1] +=1
        return digits

    c = 0 
    for i in range(len(digits)-1,-1, -1):
        if i == len(digits)-1:
            d = digits[i]+1+c
        else: 
            d = digits[i] +c
        if d>=10: 
            c = 1
            digits[i] = d%10
        else: 
            c = 0
            digits[i] = d
            break
    
    if c == 1: 
        l = [1] 
        for i in range(len(digits)): 
            l.append(digits[i])
        return l
    
    return digits
            
print(plusone([9,9,9,9,9,9]))
        
