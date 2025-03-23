
def isPalindrome(s):
    a = s.lower().strip().replace(" ","")
    flag = 1
    i = 0
    j = len(a)-1
    
    while i <=j: 
        if a[i].isalnum() and a[j].isalnum():
            if a[i] != a[j]: 
                flag = 0 
                break
            i+=1
            j-=1
            continue 
        if not a[i].isalnum(): 
            i+=1
        if not a[j].isalnum(): 
            j-=1
    return flag


#Cleaner but way slower 
def isPalindrome2(s: str): 
    s="".join(s[i].lower() for i in range(len(s)) if s[i].isalnum())
    i = 0 
    j = len(s) -1

    if len(s) == 0 or len(s) == 1: 
            return True

    flag = 1
    while i < j: 
        if s[i] != s[j]: 
            flag = 0
            break 
        i+=1
        j-=1
    return bool(flag)


print(isPalindrome2("A man, a plan, a canal: Panama"))