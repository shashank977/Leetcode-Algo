# time: O(N^2)      space: O(1)

def twoSum(nums, target):
        
  for i in range(len(nums)-1):
    first_num = nums[i]
    for j in range(i+1,len(nums)):
      second_num = nums[j]
                
      if first_num + second_num == target:
        return [nums.index(first_num), nums.index(second_num)]
  return []              
