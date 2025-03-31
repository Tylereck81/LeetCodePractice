def intToRoman(num):
    r ={ 
        1: 'I', 
        5: 'V', 
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D', 
        1000: 'M'
    }
    
    s=""
    c = 0
    while num>0: 
        d = (num%10)*(10**c)
        print(d)
        t = ""
        if d == 4 or d == 9 or d == 40 or d == 90 or d == 400 or d == 900:
            t += r[1*(10**c)]+r[d+(10**c)] 
        else: 
            if d>=5*(10**c): 
                t += r[5*10**c]
                for i in range(d-(5*10**c),0,-1*(10**c)):
                    t +=r[10**c]
            else: 
                for i in range(d,0,-1*(10**c)):
                    t += r[10**c] 
        c+=1
        s = t+s
        num = num//10

    return s

print(intToRoman(3749))
