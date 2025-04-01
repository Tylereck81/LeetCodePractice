def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    for i in range(len(nums)):
        if i+indexDiff <= len(nums):
            sub_arr = nums[i:i+indexDiff+1]
            # TOO SLOW - n^3
            # for j in range(len(sub_arr)): 
            #     for k in range(j+1, len(sub_arr)): 
            #         if abs(sub_arr[j]-sub_arr[k]) <= valueDiff:
            #             flag = 1 

            # ALSO TOO SLOW - n
            # sub_arr.sort()
            # print(sub_arr)
            # for j in range(len(sub_arr)-1): 
            #     if abs(sub_arr[j] - sub_arr[j+1]) <= valueDiff: 
            #         return True
            #  
    return False

# print(containsNearbyAlmostDuplicate([-2,3],2,5))
# print(containsNearbyAlmostDuplicate([1,2,3,1],3,0))
# print(containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))
# print(containsNearbyAlmostDuplicate([1,2,2,3,1],3,0))
