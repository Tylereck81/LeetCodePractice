# Bubble Sort: Simple sorting algorithm that swaps neighboring values until largest(or smallest) value is
# at the end of the list. End portion of the list is sorted. 
# Most swaps occur when list is in opposite order. 
# Least swaps occur when list is in order 

#Time Complexity: O(n^2): when list is completely unsorted
#Space Complexity: O(1)
def bubble_sort(nums:list[int]): 
    for i in range(len(nums)): 
        for j in range(0,len(nums)-1-i):
            if nums[j]>nums[j+1]: 
                temp = nums[j] 
                nums[j] = nums[j+1] 
                nums[j+1] = temp 
    return nums 

# SLIGHTLY IMPROVED BUBBLE SORT: 
# Concept: if some iteration doesnt include any swaps, then we break out of algorithm 
# Swapped Flag will be set to "False" and if there is at leadt one swap (elements are out of place) then set to True 
# IF FLAG STAYS FALSE, then we know its already in order. 
# DECREASES EXECUTION TIME, BUT STILL SAME COMPLEXITY
def bubble_sort(nums:list[int]): 
    for i in range(len(nums)): 
        swapped = False
        for j in range(0,len(nums)-1-i):
            if nums[j]>nums[j+1]: 
                swapped = True
                temp = nums[j] 
                nums[j] = nums[j+1] 
                nums[j+1] = temp 
        if not swapped: 
            break

l = [5,2,3,4,1]
print("BEFORE SORT:", l)
bubble_sort(l) 
print("AFTER SORT: ", l)