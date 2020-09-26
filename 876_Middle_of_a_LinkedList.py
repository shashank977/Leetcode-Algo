# (1) Output to Array  

def middleNode(self, head):
  L = [head]
  while L[-1].next:                   # Time: O(N)  ,  Space: O(N)
    L.append(L[-1].next)
  return L[len(L) // 2]



# (2) Using slow and fast pointer

def middleNode(self, head):
  slow = head 
  fast = head
  
  while fast.next:                    # Time: O(N)  ,  Space: O(1)
    if not fast.next.next:    
      return slow.next
    slow = slow.next      
    fast = fast.next.next  
  return slow
                
