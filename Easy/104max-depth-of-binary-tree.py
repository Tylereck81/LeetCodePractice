class TreeNode(object): 
    def __init__(self, val = 0 , left = None, right = None): 
        self.val = val 
        self.left = left 
        self.right = right 

def maxDepth(root: TreeNode):
    if root is None: 
        return 0 
    left = maxDepth(root.left) 
    right = maxDepth(root.right)

    return max(left,right)+1

# Tree with depth of 4
l1 = TreeNode(1,TreeNode(2,TreeNode(4), TreeNode(5)),TreeNode(3))
print(maxDepth(l1))
# Tree with depth of 5 
l1 = TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(5,TreeNode(6)))))
print(maxDepth(l1))

# l1 = TreeNode(1,TreeNode(2,TreeNode(4), TreeNode(5)),TreeNode(3))
# l1 = TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(2,None,TreeNode(3)))
# l1 = TreeNode(1,TreeNode(2, TreeNode(2)),TreeNode(2,TreeNode(2)))
