# Set initial DP table to all 1's as each node has a LIS of 1 (cause it includes itself as its LIS)
# For each element, we need to check for the smallest elements that come before it (because its increasing)
# If it is less, we change the current DP LIS value to the max of the current (in the begining its 1) and the prev+1 
# Logic: LIS[n] = 1 + max(LIS(k): k<n and nums(k)<nums(n))
# If element before is less, then the LIS has to change to a value of +1 
# 1,2,3 
# 1 has LIS of 1 (no before it)
# 2 has LIS of 2 (because LIS is 1->2) - because we find element 1 to the right of 2 , then we know the LIS changes from 1 to 1->2

# Time Complexity: O(n^2)
# Space Complexity: O(n)
def LIS(nums:list[int]): 
    dp = [1]*len(nums)
    prev_pos = [-1]*len(nums)

    for curr in range(1,len(nums)):
        for prev in range(curr): 
            if nums[curr] > nums[prev]: 
                dp[curr] = max(dp[curr],dp[prev]+1)
                prev_pos[curr] = prev if dp[curr] == dp[prev] +1 else prev_pos[curr]
    
    max_val = max(dp)
    j = len(nums)-1
    flag = 0

    start = []
    while j>=0:
        if dp[j] == max_val: 
            flag = 1
        
        if flag: 
            start.append(nums[j])
            if prev_pos[j]== -1: 
                break 
            else:
                j = prev_pos[j]
        else:
            j-=1
            
    print("PATH")
    for i in range(len(start)-1,-1,-1): 
        if i != 0:
            print(start[i],"->",end="")
        else: 
            print(start[i],end="")
    return max(dp)


print(LIS([5,2,8,6,3,6,9,5]))

print(LIS([3,10,2,1,20]))

print(LIS([30,20,10]))
