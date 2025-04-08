#Time Complexity: O(n)
#Space Complexity: O(n) 
def minimumOperations(nums: list[int]) -> int:
    s = set(nums) 
    c=0
    while len(s) != len(nums) and len(nums) != 0: 
        nums = nums[3:]
        s = set(nums)
        c+=1
    
    return c

print(minimumOperations([1,2,3,4,2,3,3,5,7]))