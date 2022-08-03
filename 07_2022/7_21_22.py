# https://leetcode.com/problems/reverse-linked-list/
# Starter code -- LL builder class
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def insert(self, val):
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
# Building list for example 1
head1 = ListNode(1)
head1.insert(2)
head1.insert(3)
head1.insert(4)
head1.insert(5)
# Building list for example 2
head2 = ListNode(1)
head2.insert(2)
# Your code here
# O(n) Time | O(1) Space where n == len of LL
def reverseList(head):
    if not head:
        return None
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

print(reverseList(head2).next.val)

