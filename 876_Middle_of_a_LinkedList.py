# (1) Output to Array  

def middleNode(self, head):
  L = [head]
  while L[-1].next:                   
    L.append(L[-1].next)
  return L[len(L) // 2]        # Time: O(N)  ,  Space: O(N)





# (2) Using slow and fast pointer

def middleNode(self, head):
  slow = head 
  fast = head
  
  while fast.next:                    
    if not fast.next.next:    
      return slow.next
    slow = slow.next      
    fast = fast.next.next  
  return slow                  # Time: O(N)  ,  Space: O(1)
