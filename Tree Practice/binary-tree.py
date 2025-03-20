class TreeNode(object): 
    def __init__(self, val = 0 , left = None, right = None): 
        self.val = val 
        self.left = left 
        self.right = right 
    
# DEPTH FIRST SEARCHES (DFS) - recursively goes from the deepest node in lowest depth to higher depthed nodes
def inOrder(root: TreeNode): 
    if root: 
        inOrder(root.left) 
        print(root.val,end="") 
        inOrder(root.right)

def postOrder(root: TreeNode): 
    if root: 
        postOrder(root.left) 
        postOrder(root.right)
        print(root.val,end="") 

def preOrder(root: TreeNode): 
    if root: 
        print(root.val,end="") 
        preOrder(root.left) 
        preOrder(root.right)

# BREADTH FIRST SEARCH (BFS)- uses a queue and goes through each level of nodes from parent to child
# LEVEL ORDER
def bfs(root: TreeNode):
    if root is None: 
        return 
    queue = [root]
    while queue: 
        node = queue.pop(0)
        print(node.val,end="")
        if node.left: 
            queue.append(node.left)
        if node.right: 
            queue.append(node.right)
    
def get_depth(root: TreeNode): 

    def traverse(node:TreeNode):
        if node == None: 
            return -1 
        
        l = traverse(node.left) 
        r = traverse(node.right)

        return max(l,r)+1


    return traverse(root)


   


if __name__ == "__main__": 

    # l1 = TreeNode(1,TreeNode(2,TreeNode(4), TreeNode(5)),TreeNode(3))
    # l2 = TreeNode(1,TreeNode(2))

    l1 = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4,TreeNode(3)),TreeNode(3)))

    # inOrder(l1)
    # print()
    # postOrder(l1)
    # print()
    # preOrder(l1)
    # print()
    # bfs(l1)
    
    print(get_depth(l1))