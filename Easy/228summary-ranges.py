def summaryRanges(nums):
    l = []
    a = 0
    while a < len(nums): 
        current = nums[a]
        b = a+1
        while b<len(nums): 
            if nums[b] == current+1:
                current+=1
                b+=1
            else:
                break
        #didnt move, single number
        if b == a+1: 
            l.append(str(nums[a]))
        else: 
            l.append(str(nums[a])+"->"+str(nums[b-1]))
        
        a = b
    return l

print(summaryRanges([0,1,2,4,5,7]))
print(summaryRanges([0,2,3,4,6,8,9]))