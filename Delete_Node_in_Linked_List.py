def deleteNode(node):
  """
  :type node: ListNode
  :rtype: void Do not return anything, modify node in-place instead.
  """
  if node is not None:
    node.val = node.next.val
    node.next = node.next.next
