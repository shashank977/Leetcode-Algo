def maxAscendingSum(nums):
	if not nums:
		return 0
	sum = maxSum = nums[0]

	for i in range(1,len(nums)):
		if nums[i]>nums[i-1]:
			sum+=nums[i]
			maxSum = max(maxSum, sum)
		else:
			sum = nums[i]
	return maxSum

print(maxAscendingSum([100,10,1]))