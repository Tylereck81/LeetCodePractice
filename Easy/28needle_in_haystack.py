# Complexity : O(n) where n is the length of the haystack 
def strStr(haystack, needle):
    if needle not in haystack: return -1

    n = len(needle)
    l = 0
    for i in range(len(haystack)): 
        if haystack[i:n+i] == needle:
            l = i
            break
    return l

print(strStr("hello", "ll")) 

