def containsDuplicate(nums):
        
  #(1)
        return len(nums) > len(set(nums))
    
    
    
  #(2) By using set
  
        visited = set()
        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)
        return False
        
        
        
  #(3)  By using Dicionary
  
        dic={}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num]=1
        return False
