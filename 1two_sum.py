
# METHOD 1 - BRUTE FORCE - O(n^2) - inefficient 
# def two_sum(nums : list[int], target: int) -> list[int]: 
    
#     for i in range(len(nums)): 
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j] == target: 
#                 return [i,j]
#     return None


#METHOD 2 - Hash set - O(n)

def two_sum(nums: list[int], target: int) -> list[int]: 
    d = {} 
    for i in range(len(nums)): 
        complement = target - nums[i]

        if complement in d: 
            return [d[complement], i]
            
        d[nums[i]] = i
        

print(two_sum([3,2,4],6))

