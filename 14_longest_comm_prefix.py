

def longestCommonPrefix(strs: list[str]) ->str:
    #length of shortest string
    n = 10000
    index = 0
    for i in range(len(strs)): 
        if len(strs[i])<n: 
            n = len(strs[i]) 
            index = i
    flag = 1
    c = -1

    for i in range(n):
        for j in range(len(strs)): 
            if flag:
                if strs[j][i] != strs[index][i]: 
                    flag = 0
        if flag == 0:
            break
        c = i
    
    if c!=-1:
        return strs[index][:c+1]
    else: 
        return []
    
print(longestCommonPrefix(["a"]))
