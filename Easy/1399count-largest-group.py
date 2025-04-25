# Time Complexity: O(n*log10(n))
# Space Complexity: O(37): Because n <= 9999 constraint makes max sum of digits 37
def countLargestGroup(n: int) -> int:
    d= {}
    largest_groups = 0
    group_size = 0
    for num in range(1, n+1):
        c = 0
        for i in range(len(str(num))): 
            c+=int(str(num)[i])
        if c in d: 
            d[c] +=1 
        else: 
            d[c] = 1

        if d[c] > group_size: 
            group_size = d[c] 
            largest_groups = 1
        elif d[c] == group_size:
            largest_groups+=1

    return largest_groups

print(countLargestGroup(1))