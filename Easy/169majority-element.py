# Time: O(n) Space: O(n) 
def majorityElement(nums:list[int]):
    d = {} 
    for i in range(len(nums)): 
        if nums[i] in d: 
            d[nums[i]] +=1
        else:
            d[nums[i]] = 1

    maxx = 0
    maxx_i = 0
    for n,m in d.items(): 
        if m>maxx:
            maxx = m 
            maxx_i = n
    
    return maxx_i


# USING MOORE VOTING ALGORITHM: If majority is more than n/2, we select candidate, increase votes if equal to
# candidate, decrease votes if not equal to candidate, when votes is 0 then we select new candidate. ONLY WORKS
# IF GUARANTEED MAJORITY IS MORE THAN N/2

#Time O(n) Space O(1)
def majorityElement2(nums: list[int]): 
    candidate = 0
    votes = 0 

    for num in nums: 
        if candidate == 0: 
            candidate = num
            votes+=1 
        elif num == candidate: 
            votes+=1 
        else:
            votes-=1 

    return candidate


print(majorityElement2([2,3,2,2,3,4]))
