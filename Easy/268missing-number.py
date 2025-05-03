def missingNumber(nums: list[int]) -> int:
    nums.sort() 

    j = 0
    for i in range(len(nums)): 
        if nums[i] !=j: 
            break 
        j+=1
        
    return j 