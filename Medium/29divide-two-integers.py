def divide(dividend: int, divisor: int) -> int:
        if abs(divisor)>abs(dividend): 
            return 0
        if dividend == divisor: 
             return 1 
        
        # Returns upper bound 
        if dividend == -2**31 and divisor == -1: 
             return 2**31 - 1

        if divisor == 1: 
             return dividend 
        
        #GET NEGATIVE FLAG
        # ^ - if both are same (00 or 11) then false
        neg = -1 if (divisor<0) ^ (dividend<0) else 1

        a = abs(dividend) 
        b = abs(divisor) 
        quotient = 0

        #WE TAKE FOLLOWING STEPS: ex. 58/5
        #1- find c for 5<<c where 5<<c is less than 58 (first round 5<<3 <58)
        #2- subtract 5<<3 from 58 
        #3- update quotient by adding the 2**c (first time is 2^3, then 2^1, then 2^0)
        
        while a >=b: 
            c = 0   
            while (b<<c+1)<a:
                c+=1

            a-= (b<<c) 
            quotient +=2**c
                 
        return neg*quotient

        
print(divide(58,5))
