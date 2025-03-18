# Uses i to point to value on left and j to point to value on right to replace with 
# Time: O(n)- n=len(nums) Space: O(1) - no extra space used
def removeElement(nums, val):
    j = len(nums)-1
    c = 0
    for i in range(len(nums)): 
        if i>j:
            break
        if nums[i] == val:
            while nums[j] == val and j >=0: 
                j-=1
            
            if j<=i: 
                break
            else: 
                # i points to left val in nums, j points to right candidate to replace with 
                temp = nums[i]
                nums[i] = nums[j] 
                nums[j] = temp
                c+=1
        else: 
            c+=1

    return c
            



print(removeElement([0,1,2,2,3,0,4,2],2))
# print(removeElement([3,3,3,3],3))
# print(removeElement([2],3))
