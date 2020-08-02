def myPow (x, n):
    if n==0:
        return 1
    if n % 2==0:
        return (x*x)**(n/2)
    else:
        return x*(x**2)**((n-1)/2)
