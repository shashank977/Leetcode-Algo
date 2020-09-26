# Output to Array  

def middleNode(self, head):
  L = [head]
  while L[-1].next:                   # Time: O(N)  ,   Space: O(N)
    L.append(L[-1].next)
  return L[len(L) // 2]
                
