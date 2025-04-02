def letterCombinations(digits):
    phone = { 
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z']
    }
    l = []
    for i in range(len(str(digits))): 
        d = int(str(digits)[i])
        if l == []: 
            l = phone[d]
        else: 
            curr = phone[d]
            new_list = []
            for i in range(len(l)): 
                for g in curr:
                    new_list.append(l[i]+g)
            l = new_list
    return l


letterCombinations(342)