# Time: O(n) 
# Space: O(n)

def containsDuplicates(nums:list[int])->bool: 
    d ={} 
    flag = 0
    for i in range(len(nums)): 
        if nums[i] not in d: 
            d[nums[i]] = nums[i]
        else: 
            flag = 1
            break 
    return bool(flag)

#Time: O(nlogn(n))- sorting 
#Space: O(1)
def containsDuplicates2(nums:list[int])->bool: 
    nums.sort() 
    flag = 0
    for i in range(len(nums)-1): 
        if nums[i] == nums[i+1]: 
            flag = 1 
            break 

    return bool(flag)

def containsDuplicates3(nums:list[int])-> bool: 
    return True if len(set(nums)) != len(nums) else False


def containsDuplicates4(nums:list[int], k: int)-> bool: 
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


print(containsDuplicates4([1,0,1,1],1))