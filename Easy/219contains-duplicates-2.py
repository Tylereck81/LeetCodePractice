def containsDuplicates2(nums:list[int], k: int)-> bool: 
    d ={} 
    flag = 0
    for i in range(len(nums)): 
        if nums[i] not in d: 
            d[nums[i]] = i
        else: 
            if abs(d[nums[i]] - i)<=k:
                flag = 1
                break 
            else: 
                d[nums[i]] = i
    return bool(flag)

print(containsDuplicates2([1,0,4,1],1))