# Algorithm for sum of branches in a tree

class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = left
        self.right = right

    def branch_Sums(root):
        sums = []
        calculate_Branch_Sums(root, 0 ,sums)
        return sums

    def calculate_Branch_Sums(node, ongoing_sum, sums):
        if node is None:
            return

        newRunningSum = ongoing_sum + node.value
        if node.left is None and node.right is None:
            sums.append(newRunningSum)
            return

        calculate_Branch_Sums(node.right, newRunningSum, sums)
        calculate_Branch_Sums(node.left, newRunningSum, sums)
