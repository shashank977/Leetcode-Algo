def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
  ##(1)
        k=k%len(nums)
        nums[:]=  nums[-k:] + nums[:-k]
        
        
        
        
  ##(2)
        k=k%len(nums)
        nums[:] = nums[::-1][:k][::-1] + nums[::-1][k:][::-1]
