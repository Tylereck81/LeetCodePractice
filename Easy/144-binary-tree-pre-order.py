class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root):
    l = []
    def traverse(root): 
        if root: 
            l.append(root.val)
            traverse(root.left)
            traverse(root.right)
    traverse(root) 
    return l