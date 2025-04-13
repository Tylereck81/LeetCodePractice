
def search(nums: list[int], target): 
    shift = 0
    #FIND RIGHT SHIFT OFFSET
    for i in range(1,len(nums)-1): 
        if nums[i-1]>nums[i]: 
            shift = i 
            break
    s = len(nums)
    # NOW DO BINARY SEARCH 
    left = 0
    right = s-1

    while left<=right: 
        mid = (int((right-left)/2 + left) +shift)%s
        if nums[mid] == target: 
            return mid
        
        if nums[mid]<target: 
            left = (mid+1)%s 
        else: 
            right = s-1 if mid-1< 0 else mid-1
        print(left,right,mid)
    return -1

# print(search([0,1,2,3,4,5,6,7],2))
print(search([3,4,5,6,7,0,1,2],2))