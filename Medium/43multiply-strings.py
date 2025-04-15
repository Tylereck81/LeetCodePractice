def multiply(num1: str, num2: str) -> str:
    if num1=="0" or num2=="0": 
        return "0"
    
    #Ensure num2 is smaller than num1
    if len(num2)> len(num1): 
        temp = num2 
        num2 = num1 
        num1 = temp 

    ans = "0"
    zero = 0
    #Multiply num2 by num1
    for i in range(len(num2)-1, -1,-1): 
        s=""
        carry = 0
        for j in range(len(num1)-1, -1,-1): 
            d1 = int(num2[i])
            d2 = int(num1[j])

            product = (d1*d2)+carry
            if product>9: 
                carry = product//10
            else: 
                carry = 0
            
            value = product%10
            s = str(value)+s
        if carry!=0:
            s = str(carry)+s

        for z in range(zero): 
            s+=str(0)
        
        zero+=1
        print(s)

        # Add ans to s (We know that len(s) will always be len(ans)+1 )
        if ans == "0": 
            ans = s 
        else: 
            carry = 0
            real_sum=""
            s_counter = len(s)-1
            for j in range(len(ans)-1, -1, -1):
                d1 = int(ans[j]) 
                d2 = int(s[s_counter])

                summ = d1+d2+carry
                carry = 1 if summ>9 else 0
                value = summ%10
                real_sum = str(value)+real_sum

                s_counter-=1
            if carry !=0:
                real_sum = str(int(s[s_counter])+carry)+real_sum
                s_counter-=1
            print(real_sum)
            print("S COUNTER",s_counter)
            print(s[s_counter-1])
            # add remainder of s digits to ans
            for j in range(s_counter,-1,-1):
                real_sum = s[j]+ real_sum
            
            print("SUM", real_sum)
            ans  = real_sum
    
    return ans 

print(multiply("65539","83314"))