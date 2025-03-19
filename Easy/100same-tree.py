class TreeNode(object): 
    def __init__(self, val = 0, left = None, right = None): 
        self.val = val 
        self.left = left 
        self.right = right 


def isSameTree(p, q):

    def traverse(p,q): 
        if p== None and q == None:
            return True

        if p == None or q == None or p.val != q.val: 
            return False 
        
        return traverse(p.left,q.left) and traverse(p.right, q.right)
    
    return traverse(p,q)

    
t1 = TreeNode(1,TreeNode(2),TreeNode(3))
t2 = TreeNode(1,TreeNode(2),TreeNode(3))

print(isSameTree(t1,t2))