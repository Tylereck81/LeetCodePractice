class TreeNode(object): 
    def __init__(self, val = 0 , left = None, right = None): 
        self.val = val 
        self.left = left 
        self.right = right 

def t(root):
    L= []
    def maxDepth(root):
        if root is None: 
            return 0
        if root.left is None and root.right is None: 
            return 1
        l = maxDepth(root.left) 
        r = maxDepth(root.right) 
        L.append(max(l,r)+1)

        return max(l,r)+1
    
    maxDepth(root)
    print(L)

    

# Tree with depth of 4
l1 = TreeNode(1,TreeNode(2,TreeNode(4), TreeNode(5)),TreeNode(3))
print(t(l1))
# Tree with depth of 5 
l1 = TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(5,TreeNode(6)))))
print(t(l1))