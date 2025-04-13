# Want to find the leftmost and rightmost index of target
# Do binary search on both sides
# Constrained by time complexity of O(log(n))
def searchRange(nums: list[int], target: int) -> list[int]:
        
    def bin_search(nums, target,searching_left): 
        left = 0 
        right = len(nums)-1 
        index = -1

        while left<=right: 
            mid = int((right-left)/2) +left 

            if target < nums[mid]: 
                right = mid-1 
            elif target > nums[mid]: 
                left = mid+1
            else: 
                # Found value, so now we try to find leftmost index of value
                index = mid 
                if searching_left: 
                    right = mid-1
                else: 
                    left = mid+1
        return index 

    start = bin_search(nums, target, 1)
    end =  bin_search(nums, target, 0)

    return [start,end]

print(searchRange([5,8,8,8,8,10],8))

