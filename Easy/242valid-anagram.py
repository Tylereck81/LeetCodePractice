def isAnagram(s: str, t: str) -> bool:
    if len(t) != len(s): 
        return False 
    
    # FILL HASH TABLE WITH LETTER COUNT FREQUENCY OF S
    d= {} 
    for letter in s: 
        if letter in d: 
            d[letter]+=1
        else: 
            d[letter] = 1
    
    for letter in t: 
        if letter in d: 
            d[letter]-=1
            if d[letter] <0: 
                return False
        else: 
            return False
        
    return True

print(isAnagram("anagram", "nagaram")) # True
print(isAnagram("rat", "car")) # False