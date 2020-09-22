def maxProfit(self, prices: List[int]) -> int:
    answer = 0
    smallest = float("inf")
        
    for i in range(len(prices)):
        if prices[i] > smallest:
            answer = max(answer, prices[i] - smallest)
        else:
            smallest = prices[i]
        
    return answer
