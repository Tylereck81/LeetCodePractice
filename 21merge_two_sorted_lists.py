class ListNode(object): 
    def __init__(self, val = 0, next = None): 
        self.val = val 
        self.next = next 

def mergeTwoLists(l1: ListNode, l2: ListNode): 
    h1 = l1
    h2 = l2 

    if l1 == None: return l2
    if l2 == None: return l1
    
    while h2:
        bef = None 
        while h1: 
            if h2.val>=h1.val: 
                bef = h1
                h1 = h1.next
            else: break

        h1 = bef

        #position in front  
        if h1 == None:
            temp = h2.next 
            h2.next = l1
            l1 = h2
            h2 = temp
        #position at the end 
        elif h1.next == None:
            temp = h2.next
            h1.next = h2 
            h2.next = None
            h2 = temp
        #in the middle
        else: 
            temp1 = h1.next
            temp2 = h2.next
            h1.next = h2 
            h2.next = temp1 
            h2 = temp2
        h1 = l1

        # while h1: 
        #     # print(h1.val)
        #     h1 = h1.next
        # h1 = l1
    
    h1 = l1 
    return h1

    
# l1 = ListNode(1)
# l2 = ListNode(2) 
# l3 = ListNode(3) 
# l4 = ListNode(4) 
# l5 = ListNode(5) 
# l6 = ListNode(6) 

# l1.next = l3
# l3.next = l5 

# l2.next = l4
# l4.next = l6

l1 = ListNode(2) 
l2 = ListNode(1)

mergeTwoLists(l1, l2)
