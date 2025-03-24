
def singleNumber(nums: list[int]): 
    result = 0
    for i in range(len(nums)): 
        result ^=nums[i]
    print(result)

    return result

singleNumber([1,2,4,1,4])