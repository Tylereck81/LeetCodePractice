def sumOfNumberAndReverse(num: int) -> bool:
    for i in range(num+1): 
        if int(str(i))+int(str(i)[::-1]) == num:
            # print(str(i), str(i)[::-1])
            return True 
    return False

print(sumOfNumberAndReverse(181))