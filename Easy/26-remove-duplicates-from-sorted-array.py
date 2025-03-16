# Time Complexity O(n^2) with the "in" operator searching each time in list 
# Space Complexity O(n) with the extra "n" array used to store 
def removeDuplicates(nums): 
    c = 0
    n = []
    for i in range(len(nums)): 
        if nums[i] not in n: 
            n.append(nums[i])
            c+=1

    # for i in num:
    #     print(i,end=" ")
    # print()
    return c

# Better Version with O(n) - use two pointers - one that points to current location(i) and one that points to
# insertion location (j). One pass through
def removeDuplicates2(nums): 
    j = 0
    for i in range(1, len(nums)): 
        if nums[i] != nums[i-1]: 
            nums[j] = nums[i] 
            j+=1
    return j+1

print(removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))
