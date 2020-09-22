# Brute force

def maxProfit(stocks):
    profit = 0
    for i in range(len(stocks)-1):
        for j in range(i+1, len(stocks)):
            if stocks[j] - stocks[i] > profit:
                max_profit = stocks[j] - stocks[i]
    return profit





def maxProfit(self, prices: List[int]) -> int:
    answer = 0
    smallest = float("inf")
        
    for i in range(len(prices)):
        if prices[i] > smallest:
            answer = max(answer, prices[i] - smallest)
        else:
            smallest = prices[i]
        
    return answer
