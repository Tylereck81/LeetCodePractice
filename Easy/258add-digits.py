# Digit root - summing digits of a number until you get one digit 
# 1- BRUTE FORCE- iteratively add digits multiple times until you get one digit 
# 2- BRUTE FORCE- RECURSIVELY add digits multiple times until you get one digit 
# 2- Use Digit root rule- if number is 0, return 0, if number is divisible by 9 return 9, else return remainder

# Time Complexity: O(1) 
# Space Complexity: O(1)
def addDigits(num: int) -> int:
    # 1 
    # n = str(num)
    # l = len(n)

    # while l !=1: 
    #     s = 0
    #     for i in range(l): 
    #         s+= int(n[i])
    #     n = str(s)
    #     l = len(n)
    # return int(n)


    # 2
    # if len(str(num)) == 1: 
    #     return num 
    # else: 
    #     s = 0 
    #     for i in range(len(str(num))): 
    #         s += int(str(num)[i])
        
    #     return self.addDigits(int(s))
    

    #3 
    if num == 0: 
        return 0 
    if num%9 == 0: 
        return 9 
    else: 
        return num%9

print(addDigits(11))