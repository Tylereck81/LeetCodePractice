
# Time Complexity: O(m+n) Space: O(m+n)
def merge(nums1, m, nums2, n):
    res = []
    c1 = 0 
    c2 = 0
    while c1<m and c2<n: 
        if nums1[c1] < nums2[c2]: 
            res.append(nums1[c1])
            c1+=1
        else: 
            res.append(nums2[c2])
            c2+=1
    
    
    if c1<m:
        for i in range(c1,m): 
            res.append(nums1[i])

    if c2<n:
        for i in range(c2,n): 
            res.append(nums2[i])  
    
    for i in range(m+n): 
        nums1[i] = res[i]

    return nums1

print(merge([0],0,[1],1))

