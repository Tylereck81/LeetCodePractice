def canJump(nums: list[int]) -> bool:
    curr = 0
    for i in range(len(nums)):  
        if curr < 0: 
            return False 
        elif nums[i] > curr:
            curr = nums[i] 
        curr-=1
    return True
        

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))
print(canJump([2,5,0,0]))
