
def countAndSay(n: int) -> str:
    if n == 1: 
        return "1"
    else: 
        num = "11"
        for j in range(2,n): 
            s = ""
            c = 1
            for i in range(1,len(num)): 
                if num[i-1] == num[i]: 
                    c+=1 
                else: 
                    s+=str(c)+num[i-1]
                    c = 1  
            
            s+=str(c)+num[len(num)-1]
            num = s

        return num

for i in range(1,11): 
    print(countAndSay(i))
