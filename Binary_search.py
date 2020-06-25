def search(nums, target):
        left= 0
        right= len(nums)-1
        

        
        while left <= right:
            middle= (left + right)//2
            
            
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right= middle-1
            else:
                left=middle+1
        return -1
            
        # time:  O(log(n))      
        # space: O(1)
