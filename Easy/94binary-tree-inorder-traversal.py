class TreeNode(object): 
    def __init__(self, val = 0, left = None, right = None): 
        self.val = val 
        self.left = left 
        self.right = right 
                 

def inOrderTraversal(root: TreeNode)->list[int]: 
    r = [] 

    def traverse(root: TreeNode): 
        if root: 
            traverse(root.left)
            r.append(root.val)
            traverse(root.right)

    traverse(root)
    if root: 
        return r


