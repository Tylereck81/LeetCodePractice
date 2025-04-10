# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root: TreeNode) -> list[str]:
    l = []
    def traverse(root, s): 
        if root is None:
            return 
        if root.left == None and root.right == None: 
            s+=str(root.val)
            l.append(s)

        s+=str(root.val)+"->"
        traverse(root.left,s)
        traverse(root.right,s)
    
    traverse(root, "")

    return l

t1 = TreeNode(1, TreeNode(2,None,TreeNode(5)), TreeNode(3))
t2 = TreeNode(1)
    
print(binaryTreePaths(t1))
print(binaryTreePaths(t2))