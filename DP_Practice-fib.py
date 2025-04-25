# Time Complexity: (2^n) - when draw tree, we make double each level with recursion and repeat calculations are made
# Space Complexity: O(n) - store recursive calls on stack
def fib(n): 
    if n<=1: 
        return 1 
    
    return fib(n-1)+fib(n-2)

# When we incomportate MEMOIZATION TABLE, we add another base case to check if value is already in table to avoid recalculations
# Due to the tree stack traversal of BFS, we go down all the way to fib(1) on left side and fill in MEMO with values we calculated 
# Because of this, Time Complexity is now O(n) because we only calculate values ONCE and store in table 
# Space complexity is now O(n) for the memo table
def fib2(n): 

    def rec(n, memo): 
        if n <=1: 
            return n
        
        if memo[n] != -1:
            return memo[n]
        
        memo[n] = rec(n-1, memo) + rec(n-2, memo) 
        
        return memo[n]

    memo = [-1]*(n+1)
    return(rec(n, memo))
    
print(fib2(5))


# Bottom Up Approach- Instead of recursion, we iterate through and use a dp array to build up (from the bottom up) to the answer 
# What results is the last value of the array being the value n we want to return. 
# Time Complexity: O(n)
# Space Complexity: O(n)
def fib3(n): 
    if n<=1: 
        return n 
    
    dp = [0] * (n+1)

    dp[0] = 0 
    dp[1] = 1 

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(fib3(5))

# Space Optimized approach - Logic is that we only need the previous two values of the fib sequence to get the current value 
# So we build up to it like the bottom up approach, but ONLY STORE the last two values each time 
# Time Complexity: O(n) 
# Space Complexity: O(1)
def fib4(n): 
    if n == 1:
        return 1 
    if n == 2: 
        return 2 
    
    n1 = 1
    n2 = 2
    sum = 0

    for i in range(3, n):
        sum = n1+n2
        n1 = n2 
        n2 = sum 
    
    return sum
    
