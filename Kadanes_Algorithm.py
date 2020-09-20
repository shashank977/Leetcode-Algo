
# Space : O(1)     Time : O(N)
def maxSubArraySum(array):
  maxSumHere = array[0]
  maxSoFar = array[0]
  for num in array[1:]:
    maxSumHere = max(num, maxSumHere + num)
    maxSoFar = max(maxSoFar, maxSumHere)
  return maxSumHere
