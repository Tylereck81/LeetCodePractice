# Time Complexity = O(n+m) , n = len(a) and m = len(b)
def addBinary(a: str,b:str): 
    a = [int(a[i]) for i in range(len(a)-1,-1,-1)]
    b = [int(b[i]) for i in range(len(b)-1,-1,-1)]
    
    #ensures b is smallest
    if len(a)<len(b): 
        temp = a 
        a = b
        b = temp

    carry = 0
    for i in range(len(b)):
        digit = a[i] + b[i] + carry
        if digit == 2: 
            a[i] = 0
            carry = 1
        elif digit == 3: 
            a[i] = 1
            carry = 1
        else: 
            a[i] = digit
            carry = 0
    
    if carry == 1:
        for i in range(len(b),len(a)): 
            digit  = a[i] + carry
            if digit == 2: 
                a[i] = 0 
                carry = 1
            else: 
                a[i] = digit
                carry = 0
                break 

        if carry == 1:
            a.append(1)

    b = ""
    a = [str(a[i]) for i in range(len(a)-1, -1, -1)]
    for i in a: 
        b+=i
    return b
        
# Cleaner version of the above code
# Time Complexity = O(n+m) , n = len(a) and m = len(b)
def addBinary2(a:str, b:str): 
    return bin(int(a,2)+int(b,2)).replace("0b","")

