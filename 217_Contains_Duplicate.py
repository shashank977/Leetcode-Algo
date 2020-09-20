# (1)
def containsDuplicate(nums):
    return len(nums) > len(set(nums))
    
    
    
#(2) By using set
def containsDuplicate(nums):
    visited = set()
    for num in nums:
        if num in visited:
            return True
        else:
            visited.add(num)
     return False
        
        
        
#(3)  By using Dicionary
def containsDuplicate(nums):
    dic={}
    for num in nums:
        if num in dic:
            return True
        else:
            dic[num]=1
    return False
