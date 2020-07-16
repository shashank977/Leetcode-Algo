from collections import Counter                                         

def findLucky(arr):                                                      
  return max([j for i,j in Counter(arr).items() if i==j], default =-1)     



# First I created a dictionary using Counter(arr)
# Then converted that dictionary into a list with tuples of (i,j) using .items()
# After that finding max, By default if the list is empty return -1.
