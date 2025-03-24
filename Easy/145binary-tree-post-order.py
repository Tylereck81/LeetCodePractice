class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
def postorderTraversal(root):
    l = []
    def traverse(root): 
        if root: 
            traverse(root.left)
            traverse(root.right)
            l.append(root.val)
    traverse(root) 
    return l