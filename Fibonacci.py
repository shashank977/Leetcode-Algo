# (1)
def fib(n,memoize={0:0,1:1,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib(n-1,memoize) + fib(n-2,memoize)
            return memoize[n]
# time: o(n)    space: o(n)




#(2)
def fib(N):
        
    lastTwo=[0,1]
    counter=2
        
    if N==0:
        return 0 
    
        
    while counter <= N:
            
        nextFib = lastTwo[0]  + lastTwo[1]
        lastTwo[0]=lastTwo[1]
        lastTwo[1]=nextFib    
        counter+=1
    return lastTwo[1]
