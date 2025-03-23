class Node(object): 
    def __init__(self, val = 0 , next = None): 
        self.val = val 
        self.next = next 

class LinkedList(object):
    def __init__(self, *args): 
        if len(args) == 0: 
            self.head = 0

        elif isinstance(args[0], Node): 
            self.head = args[0] 

        else: 
            self.head = Node(args[0][0])
            t = self.head
            for i in range(1,len(args[0])): 
                n = Node(args[0][i])
                t.next = n
                t = t.next

    def print_list(self): 
        h = self.head
        if h == None: 
            print("Empty List")
        while h: 
            print(h.val,end=" ")
            h = h.next
        print()
    
    def length(self): 
        h = self.head
        c = 0 
        while h: 
            c+=1
            h = h.next 
        return c

    def insert(self, val, pos): 
        l = self.length()
        if pos>l: 
            print("Position larger than list")
            return -1 
     
        n = Node(val)         
        
        if pos == 0:
            n.next = self.head
            self.head = n
        else: 
            t = self.head 
            c = 1
            while c!=pos: 
                t = t.next 
                c+=1
            n.next = t.next 
            t.next = n
        print("Inserted:", val)
        return 1
    
    def remove(self, val): 
        t = self.head 
        prev = self.head
        while t: 
            if t.val == val: 
                break 
            prev = t
            t = t.next
        if t: 
            if t == self.head: 
                self.head = t.next 
            elif t.next == 0: 
                prev.next = 0
            else: 
                prev.next = t.next 
            print("Removed:",val)
            return 1 
        else: 
            print("No such element")
            return -1 
        


n1 = Node(1, Node(2, Node(3)))
l1 = LinkedList(n1) 
# l1.insert(4,3)
# l1.print_list()

# l1.remove(5)
# l1.print_list()
# l1.remove(3)
# l1.print_list()

l2 = LinkedList([1,2,4,2])
l2.print_list()
l2.remove(2) 
l2.remove(4)
l2.remove(1) 
l2.remove(2)
l2.print_list()
l2.insert(2,0)
l2.print_list()
