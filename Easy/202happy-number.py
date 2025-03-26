#Time O(logn) | Space O(logn)
# 1. Create a dictionary to store the number that we have seen before
# 2. Create a flag to check if the number is happy or not
# 3. Create a counter to count the number of iterations
# 4. Create a while loop to iterate through the number
# 5. Create a sum variable to store the sum of the square of the digits
# 6. Iterate through the number and add the square of the digit to the sum
def isHappy(n):
    num = str(n)
    d ={}
    flag = 0
    while 1: 
        s = 0
        for i in range(len(num)):
            s+=int(num[i])**2
        num = str(s)
        if num in d: 
            return False 
        else: 
            d[num] = num
        if num == "1": 
            flag = 1 
            break
            
    
    return bool(flag)
    

print(isHappy(2))