# (1) Brute force
#   Time: O(N^2)   ,   Space: O(1)

def maxProfit(stocks):
    profit = 0
    for i in range(len(stocks)-1):
        for j in range(i+1, len(stocks)):
            if stocks[j] - stocks[i] > profit:
                max_profit = stocks[j] - stocks[i]
    return profit





# (2) Linear time
# Time:  O(N)   ,    Space: O(1)

def maxProfit(prices):
    if not prices:
        return 0

    min_value = float('inf')
    max_profit = 0
        
    for i in range(len(prices)):
        min_value = min(min_value, prices[i])
        max_profit = max(max_profit, prices[i] - min_value)
    return max_profit      
