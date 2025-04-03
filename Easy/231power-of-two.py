import math 

def isPowerOfTwo(n: int) -> bool:
    # METHOD 1 - turn n into binary form, power of two numbers only have one "1" bit in it 
    if n<=0: 
        return False
    l = str(bin(n)) 
    count = 0
    for i in range(len(l)): 
        if l[i] == '1':
            count+=1
    return count == 1

    # METHOD 2 - check if log2(n) is an integer 2^x = integer number
    # if n <= 0: 
    #     return False 
    # return math.log2(n).is_integer()


print(isPowerOfTwo(-16))