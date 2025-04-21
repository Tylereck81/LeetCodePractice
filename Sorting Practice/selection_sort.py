# Selection sort is a simple sorting algorithm that finds the min value on each iteration and places
# it at the front of the list. The minimum value is not known until it goes through each iteration 

# Time Complexity: O(n^2) 
# Space Complexity: O(1)

def selection_sort(nums:list[int]): 
    for i in range(len(nums)): 
        min = i 
        for j in range(i+1, len(nums)): 
            if nums[j] <nums[min]: 
                min = j 
        temp = nums[min] 
        nums[min] = nums[i] 
        nums[i] = temp
    
l = [5,2,3,4,1]
print("BEFORE SORT:", l)
selection_sort(l) 
print("AFTER SORT: ", l)