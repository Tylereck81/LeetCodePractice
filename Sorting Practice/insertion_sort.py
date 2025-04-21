def insertion_sort(nums:list[int]): 
    for i in range(1,len(nums)): 
        key = nums[i]
        j = i-1
        while j>=0 and key<nums[j]: 
            nums[j+1] = nums[j]
            j = j-1 
        
        nums[j+1] = key 

l = [9,5,1,4,3]
insertion_sort(l) 
print(l)