def isIsomorphic(s, t): 
    s_index = {}
    t_index = {} 

    for i in range(len(s)): 
        if s[i] not in s_index: 
            s_index[s[i]] = i
        if t[i] not in t_index: 
            t_index[t[i]] = i

        if s_index[s[i]] != t_index[t[i]]: 
            return False
    
    return True

def isIsomorphic1(s,t): 
    d = {} 

    for i in range(len(s)): 
        if s[i] not in d and t[i] not in d.values(): 
            d[s[i]] = t[i]
        else: 
            if s[i] in d: 
                if d[s[i]] != t[i]:
                    return False
            if t[i] in d.values(): 
                for key,value in d.items(): 
                    if value == t[i]: 
                        if key != s[i]:
                            return False 
    return True



print(isIsomorphic1("paper","title"))
print(isIsomorphic1("aaabbaaa","bbbaaabb"))