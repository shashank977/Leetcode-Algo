# time: O(log(n))      space: O(log(N))

def ClosestValueInBST(tree,target):
    return ClosestValueInBST_Helper(tree,target, float("inf"))

def ClosestValueInBST_Helper(tree,target,closest):
    if tree is None:
        return closest
    if abs(closest-target) > abs(target- tree.value):
        closest = tree.value
    if target < closest:
        return ClosestValueInBST_Helper(tree.left,target,closest)
    elif target > closest:
        return ClosestValueInBST_Helper(tree.right,target,closest)
    else:
        return closest
