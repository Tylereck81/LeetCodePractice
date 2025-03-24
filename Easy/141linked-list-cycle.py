
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Time Complexity: O(n) Space Complexity: O(n)
def hasCycle(head):
    t = head
    d = {}
    flag = 0
    while t: 
        if t not in d: 
            d[t] = t
        else:
            flag = 1 
            break
        t = t.next
    
    return bool(flag)

# Time Complexity: O(n) Space Complexity: O(1)
def hasCycle2(head): 
    slow = head
    fast = head
    flag = 0 
    while fast.next and fast.next.next: 
        slow = slow.next  
        fast = fast.next.next

        if slow == fast:
            flag = 1
            break
    
    return bool(flag)


#Generate a linked list with a cycle in it for test case 
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print(hasCycle2(head)) # True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
print(hasCycle2(head)) # True

# Regular linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(hasCycle2(head)) # False