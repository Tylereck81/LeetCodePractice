# Time: O(n) 
# Space: O(1) 
def numberOfArrays(differences: list[int], lower: int, upper: int) -> int:
    # BRUTE FORCE - too slow 
    # count = 0
    # for i in range(lower, upper+1): 
    #     flag = 1
    #     curr = i
    #     for j in range(len(differences)): 
    #         curr = curr+differences[j] 
    #         if curr<lower or curr>upper: 
    #             flag = 0
    #             break
    #     if flag: 
    #         count+=1
    # return count


    total = (upper - lower)+1
    LOW = lower
    HIGH = upper
    curr1 = lower
    curr2 = upper
    for i in range(len(differences)):
        curr1 = curr1+differences[i]
        if curr1 < LOW: 
            LOW = curr1

        curr2 = curr2+differences[i]
        if curr2 > HIGH: 
            HIGH = curr2 

    low_val = abs(lower-LOW)
    high_val =abs(HIGH-upper)
    ans = total-low_val-high_val

    return ans if ans>0 else 0
