def subsequence(s, words): 
    counter = 0
    for word in words: 
        flag = 1
        last_letter = -1
        s_copy = s
        for letter in range(len(word)): 
            if word[letter] in s_copy: 
                print (s_copy)
                # Get positon of letter in s
                for c in range(len(s_copy)): 
                    if word[letter] == s_copy[c]: 
                        if c> last_letter: 
                            s_copy = s_copy.replace(s[c],"",1)
                            last_letter = c
                            break
                        else: 
                            flag = 0 
                            break
            else: 
                flag = 0
                break 
        if flag: 
            counter+=1
    return counter

# print(subsequence("dsahjpjauf",["ahjpjau","ja","ahbwzgqnuk","tnlm"]))
print(subsequence("dsahjpjauf",["ahjpjau"]))