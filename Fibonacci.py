def fib(n,memoize={0:0,1:1,2:1}):
  if n in memoize:
    return memoize[n]
  else:
    memoize[n] = fib(n-1,memoize) + fib(n-2,memoize)
      return memoize[n]
