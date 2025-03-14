# Need to do it in O(log(n)) so we use binary search since its already sorted
def searchInsert(nums: list[int], target: int)-> int:
    left = 0 
    right = len(nums)-1
    middle = int((left+right)/2)

    while left<=right: 
        middle = int((left+right)/2)
        if nums[middle] == target: 
            return middle
        elif nums[middle] < target: 
            left = middle+1
        else:
            right = middle-1
    
    return left


print(searchInsert([1,3,5,7],4))
