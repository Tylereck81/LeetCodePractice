def mySqrt(x: int)->int: 
    if x == 0: return 0

    l = 1
    u = x
    r = 0

    while l <= u:
        m =  (u+l)/2
        if m*m <=x:
            r = m
            l = m+1
        else: 
            u = m-1
        
    return int(r)



print(mySqrt(8))

