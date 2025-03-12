# Naive Approach - cast to string and test characters against itself - FASTER
def palindrome_number(x: int)->bool: 
    if x<0: 
        return False
    else: 
        s = str(x)
        flag = 1
        for i in range(int(len(s)/2)): 
            if s[i]!=s[len(s)-1-i]: 
                flag = 0 
                break 
    return flag 


#Forming new number and then comparing with old one using ints - SLOWER
def palindrome_number2(x: int) ->bool:
    if x<0: 
        return False 
    else: 
        num1 = 0
        num2 = x
        base = 1*(10**(len(str(x))-1))
        while x>0:
            digit = int(x%10)
            num1 += int(digit*base)
            base = int(base/10) 
            x = int(x/10)

        return num1 == num2

def palindrome_number3(x: int) ->bool:
    if x<0: 
        return False 
    else: 
        rev = 0
        temp = x 
        while temp != 0: 
            rev = (rev*10) + (temp%10)
            temp = temp //10
        
        return rev == x
    
print (palindrome_number3(1021))
