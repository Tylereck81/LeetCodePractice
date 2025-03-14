# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

def print_ll(l: ListNode):
    head = l 
    while head: 
        print(head.val)
        head = head.next
    
#First Attempt - Time: O(max(n,m)) Space: O(m+n)
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode: 
    h1 = l1 
    h2 = l2

    head = 0
    temp = 0
    carry = 0

    while h1 or h2: 
        #both values are added
        if h1 and h2:
            t1 = h1.val 
            t2 = h2.val 
            t = 0

            if t1+t2+carry > 9: #carry the 1 
                t = ListNode((t1+t2+carry)%10)
                carry = 1    
            else: 
                t = ListNode(t1+t2+carry)
                carry = 0

            if head == 0: #First time adding to list 
                head = t
                temp = t 
            else: 
                temp.next = t 
                temp = t

            h1 = h1.next 
            h2 = h2.next

        #only h1 is longer, add remainder digits 
        elif h1:
            t1 = h1.val

            if t1+carry > 9: #carry the 1 
                t = ListNode((t1+carry)%10)
                carry = 1    
            else: 
                t = ListNode(t1+carry)
                carry = 0

            if head == 0: #First time adding to list 
                head = t
                temp = t 
            else: 
                temp.next = t 
                temp = t

            h1 = h1.next

        #h2 is longer
        else:
            t1 = h2.val

            if t1+carry > 9: #carry the 1 
                t = ListNode((t1+carry)%10)
                carry = 1    
            else: 
                t = ListNode(t1+carry)
                carry = 0

            if head == 0: #First time adding to list 
                head = t
                temp = t 
            else: 
                temp.next = t 
                temp = t

            h2 = h2.next 
    
    if carry: 
        t = ListNode(1)
        temp.next = t
        temp = t

    return head


#Same algorithm but cleaner
def addTwoNumbers2(l1: ListNode, l2: ListNode) -> ListNode: 
    h1 = l1 
    h2 = l2

    head = 0
    temp = 0
    carry = 0

    while l1 or l2 or carry != 0: 

        t1 = l1.val if l1 else 0
        t2 = l2.val if l2 else 0 

        sum = t1 + t2 + carry 
        digit = sum % 10
        carry = sum // 10


        t = ListNode(digit)

        if head == 0: 
            head = t
            temp = t 
        else: 
            temp.next = t 
            temp = t

        l1 = l1.next if l1 else None 
        l2 = l2.next if l2 else None
        
    return head


#Recursive Solution - Time: O(max(m,n)) , Space: O(m+n) & STACK SPACE - uses stack for recursion
def addTwoNumbers2(l1: ListNode, l2: ListNode, carry: int) -> ListNode: 

    #base case
    if l1 is None and l2 is None and carry == 0: return None

    sum = carry
    if l1: 
        sum += l1.val 
    if l2: 
        sum += l2.val 
    
    digit = sum % 10 
    carry = sum // 10
    
    t = ListNode(digit)
    
    t.next = addTwoNumbers(l1.next, l2.next, carry)

    return t

#First Linked List
l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l1.next = l2 
l2.next = l3 

# print_ll(l1)

#Second Linked List
l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)
l4.next = l5 
l5.next = l6

# print_ll(l4)

print_ll(addTwoNumbers(l1,l4))

