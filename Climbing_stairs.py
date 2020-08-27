# using dynamic programming

def climbStairs(self, n: int) -> int:
    
    lowerTwo = [1, 2]   
    stair = 3       
    
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
        
    while stair <= n:
        ways =  lowerTwo[1] + lowerTwo[0]
        lowerTwo[0] = lowerTwo[1]
        lowerTwo[1] = ways
        stair += 1
    return lowerTwo[1]
