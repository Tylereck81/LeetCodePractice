# # Time Complexity: (2^n) - when draw tree, we make double each level with recursion and repeat calculations are made
# # Space Complexity: O(n) - store recursive calls on stack
# def fib(n): 
#     if n<=1: 
#         return 1 
    
#     return fib(n-1)+fib(n-2)

# # TOP DOWN APPROACH
# # When we incomportate MEMOIZATION TABLE, we add another base case to check if value is already in table to avoid recalculations
# # Due to the tree stack traversal of BFS, we go down all the way to fib(1) on left side and fill in MEMO with values we calculated 
# # Because of this, Time Complexity is now O(n) because we only calculate values ONCE and store in table 
# # Space complexity is now O(n) for the memo table
# def fib2(n): 

#     def rec(n, memo): 
#         if n <=1: 
#             return n
        
#         if memo[n] != -1:
#             return memo[n]
        
#         memo[n] = rec(n-1, memo) + rec(n-2, memo) 
        
#         return memo[n]

#     memo = [-1]*(n+1)
#     return(rec(n, memo))
    


# # Bottom Up Approach- Instead of recursion, we iterate through and use a dp array to build up (from the bottom up) to the answer 
# # What results is the last value of the array being the value n we want to return. 
# # Time Complexity: O(n)
# # Space Complexity: O(n)
# def fib3(n): 
#     if n<=1: 
#         return n 
    
#     dp = [0] * (n+1)

#     dp[0] = 0 
#     dp[1] = 1 

#     for i in range(2,n+1):
#         dp[i] = dp[i-1] + dp[i-2]

#     return dp[n]


# # Space Optimized approach - Logic is that we only need the previous two values of the fib sequence to get the current value 
# # So we build up to it like the bottom up approach, but ONLY STORE the last two values each time 
# # Time Complexity: O(n) 
# # Space Complexity: O(1)
# def fib4(n): 
#     if n == 1:
#         return 1 
#     if n == 2: 
#         return 2 
    
#     n1 = 1
#     n2 = 2
#     sum = 0

#     for i in range(3, n):
#         sum = n1+n2
#         n1 = n2 
#         n2 = sum 
    
#     return sum
    

# GRID TRAVELER PROBLEM: you are given a m*n grid and you are only allowed to move down and right. 
# How many ways can you move to get from the top left square to bottom right square 


# Recursion 
# Time Complexity: O(2^n+m)
# Space Complexity: O(n+m)
def grid_travel(m:int, n:int): 
    if m == 0 or n == 0: 
        return 0

    if m == 1 and n == 1: 
        return 1 
    
    return grid_travel(m,n-1) + grid_travel(m-1,n)

# print(grid_travel(18,18))


# Dynamic Programming  - use Memo dictionary to keep track of keys that have already been calculated 
# Time: O(n+m)
# Space: O(n+m)
def grid_travel(m:int , n:int):
    memo = {}

    def rec(m:int, n:int, memo:list[list]):
        #Cases where it is impossible to reach the bottom right square
        if m == 0 or n == 0: 
            return 0 
        #Case where we do meet the bottom right square
        if m == 1 or n == 1: 
            return 1 
        
        #Memo table keeps track of the 
        key = str(m)+','+str(n)
        if key in memo:
            return memo[key]
        
        memo[key]= rec(m-1,n, memo) + rec(m,n-1, memo)

        return memo[key]

    return rec(m,n,memo)

# print(grid_travel(18,18))


def brackets(n: int): 
    l = []

    def rec(left: int,right:int ,s:str): 
        if len(s) == n*2:
            l.append(s)
        
        if left<n:
            rec(left+1, right,s+'(')

        if right<left:
            rec(left, right+1,s+')')
    
    rec(0,0,"")

    return l

print(brackets(2))