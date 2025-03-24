# def maxProfit(prices: list[int]):
#     if len(prices)  == 1: 
#         return 0
     
#     buy = 0 
#     sell = 1
#     profit = prices[sell]-prices[buy]

#     while sell< len(prices):   
#         if prices[buy] > prices[sell]: 
#             buy = sell

#         elif prices[buy] < prices[sell] and prices[sell]-prices[buy] > profit: 
#             profit = prices[sell] - prices[buy]
        
#         sell+=1
    
#     return 0 if profit<=0 else profit 

# Time Complexity: O(n) , Space Complexity: O(1)
def maxProfit(prices: list[int]): 
    buy = prices[0] 
    profit = 0

    for i in range(1, len(prices)): 
        if prices[i]<buy: 
            buy = prices[i]
        elif prices[i] - buy >profit: 
            profit = prices[i] - buy
    
    return profit

print(maxProfit([6,2,3,5,1,2]))
print(maxProfit([6,2,3,5,1,7]))
print(maxProfit([0,1,3,5,2,7]))    
print(maxProfit([3,5,1,3,2,8,1]))   
print(maxProfit([7,6,4,2,1]))     


