# Time Complexity: O(n) n-length of string 
def lengthOfLastWord(s: str)->int: 
    c = 0

    # start from back, check for first non space and start counting characters. Once it starts counting and
    # hits a space, it will stop counting and break
    flag = 0
    for i in range(len(s)-1,-1,-1): 
        if flag == 0:
            if s[i] != " ":
                flag = 1            
                c+=1
        else: 
            if s[i]!=" ": 
                c+=1 
            else: 
                break
    return c

# Cleaner version using string Python functions, same time complexity
def lengthofLastWord2(s: str)->int: 
    return len(s.split()[-1])



        
