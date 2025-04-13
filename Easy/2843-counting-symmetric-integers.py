def countSymmetricIntegers(low: int, high: int) -> int:
    c = 0
    for i in range(low, high+1): 
        n = len(str(i)) 
        if n%2 == 0: 
            
            l = int(n/2)
            n1 = int(str(i)[0:l])
            n2 = int(str(i)[l:])
            
            #1708
            c1 = 0 
            c2 = 0
            while n1>0: 
                c1+=n1%10
                n1//=10
            while n2>0: 
                c2+=n2%10
                n2//=10
            if c1 == c2: 
                c+=1
    return c
                

print(countSymmetricIntegers(100,1782))
                