# Longest Common Subsequence 
# Method: Dynamic Programming: Tabular Approach (Bottom-Up)
# Logic: We create a 2x2 matrix (n+1)x(m+1) size to fill in our sub calculations 
# We check if at specific points i,j if they have the same letter. If so, we increase the previous longest
# subsequence by 1. Finally, if they are not the same, the current place inherits the previous longest 
# subsequence fom either 1 string or the other string (thats why its max of i-1,j and i,j-1)
# Time Complexity: O(m*n) 
# Space Complexity: O(m*n)
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m = len(text1)
    n = len(text2)
    dp = [0]*(m+1)
    for i in range(len(dp)): 
        dp[i] = [0]*(n+1)
    
    for i in range(1,m+1): 
        for j in range(1,n+1):
            if text1[i-1] == text2[j-1]: 
                dp[i][j] = dp[i-1][j-1] +1
            else: 
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    
    return dp[m][n]

# Space Optimized method: We only store the previous row instead of the entire matrix because that is all we need 
# Create a current row that we fill in for the inner loop and replace prev row with curr row when loop is finished 
# Time Complexity: O(m*n) 
# Space Complexity: O(m)
def LCS(s1: str, s2: str): 
    m = len(s1) 
    n = len(s2) 

    prev = [0] * (m+1) 

    for i in range(1,m+1): 
        curr= [0] * (m+1)
        for j in range(1,n+1): 
            if s1[i-1] == s2[j-1]:
                curr[j] = prev[j-1] +1
            else: 
                curr[j] = max(prev[j], curr[j-1])
        prev = curr

    return prev[m]

print(LCS("ABB","ACB"))