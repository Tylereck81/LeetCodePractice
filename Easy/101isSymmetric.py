class TreeNode(object): 
    def __init__(self, val = 0 , left = None, right = None): 
        self.val = val 
        self.left = left 
        self.right = right 

def isSymmetric(root: TreeNode): 

    def traverse(l,r): 
        # Both subtrees are empty
        if not l and not r: 
            return True
        
        #Either on or the other is empty 
        if not l or not r: 
            return False

        return l.val == r.val and traverse(l.left, r.right) and traverse(l.right, r.left)

    return traverse(root.left,root.right)


l1 = TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(2,None,TreeNode(3)))
# l1 = TreeNode(1,TreeNode(2, TreeNode(2)),TreeNode(2,TreeNode(2)))

# l1 = TreeNode(1,TreeNode(2, TreeNode(2)),TreeNode(2,None, TreeNode(2)))

print(isSymmetric(l1))
