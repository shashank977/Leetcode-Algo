from collections import Counter

def findLucky(arr):
  return max([j for i,j in Counter(arr).items() if i==j], default =-1)
