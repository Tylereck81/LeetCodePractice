#Time: O(len(s)) Space: O(1) - fixed space dictionary 
def romanToInt(s: str) ->int:
    r = { 
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
    }
    num = 0
    i = 0
    while i<len(s):
        if s[i] == 'I' and i+1<len(s) and s[i+1] == 'V':
            num +=4
            i+=1
        elif s[i] == 'I' and i+1<len(s) and s[i+1] == 'X':
            num+=9
            i+=1
        elif s[i] == 'X' and i+1<len(s) and s[i+1] == 'L':
            num+=40
            i+=1
        elif s[i] == 'X' and i+1<len(s) and s[i+1] == 'C':
            num+=90
            i+=1
        elif s[i] == 'C' and i+1<len(s) and s[i+1] == 'D':
            num+=400
            i+=1
        elif s[i] == 'C' and i+1<len(s) and s[i+1] == 'M':
            num+=900
            i+=1
        else: 
            num+= r[s[i]]
        i+=1
    return num

#cleaner, same compleixity - idea is for 'IV' - we subtract the number if its less than the one after, 
# "IV" - num = -1, num = -1+5 = 4 
def romanToInt(s: str) ->int:
    r = { 
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
    }
    num = 0
    for i in range(len(s)): 
        if i+1<len(s) and r[s[i]] < r[s[i+1]]:
            num-=r[s[i]]
        else: 
            num+=r[s[i]]
    return num

print(romanToInt('IV'))