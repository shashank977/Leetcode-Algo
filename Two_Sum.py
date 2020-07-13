#1) using double for loop
# time: O(N^2)     space: O(1)

def twoSum(nums, target):     
    for i in range(len(nums)-1):
        first_num = nums[i]
        for j in range(i+1,len(nums)):
            second_num = nums[j]
                
            if first_num + second_num == target:
                return [nums.index(first_num), nums.index(second_num)]
    return []              


#2) using hash table
# time: O(N)       space: O(N)

def twoSum(nums,target):

    d={}

    for i in nums:
        potentialMatch = target - i
        if potentialMatch in d:
            return [nums.index(potentialMatch), nums.index(i)]
        else:
            d[i] = True

    return []
