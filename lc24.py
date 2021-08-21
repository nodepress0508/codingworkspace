"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
"""
intuition:

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#idea from duscussion
#itrative sol
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        #create dummy node
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            firstnode = current.next#initialize first node
            secondnode = current.next.next#initilaize second node
            current.next = secondnode#current pointer to second node 
            firstnode.next = secondnode.next#second node pointer give it to firstnode pointer 
            secondnode.next = firstnode #second node pointer point to first node
            current = current.next.next #move to the next node
#recursive sol
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newnode = head.next.next
        head,head.next = head.next, head
        head.next.next = self.swapPairs(newnode)
        return head