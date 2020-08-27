# using dynamic programming

def climbStairs(self, n: int) -> int:
    stairs = [1, 2]  
    stepping = 3
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
        
    while stepping <= n:
        ways =  stairs[1] + stairs[0]
        stairs[0] = stairs[1]
        stairs[1] = ways
        stepping +=1
    return stairs[1]
