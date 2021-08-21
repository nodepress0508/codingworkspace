"""
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
TLE:to much recursion called
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not list:
            return 
        if len(lists) ==1:
            return list[0]
        mid = len(lists)//2
        head1 = self.mergeKLists(lists[:mid])
        head2 = self.mergeKLists(lists[mid:])
        return self.sortedmerge(head1,head2)
    def sortedmerge(self,head1,head2):
        tmp = None
        if not head1:
            return head2
        if not head2:
            return head1 
        if head1.val <= head2.val:
            tmp = head1
            tmp.next = self.sortedmerge(head1.next,head2)
        else:
            tmp = head2
            tmp.next = self.sortedmerge(head1,head2.next)
"""
TC:O(nlogn)
SC:O(N)
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        if len(lists) ==1:
            return lists[0]
        mid = len(lists)//2
        head1 = self.mergeKLists(lists[:mid])
        head2 = self.mergeKLists(lists[mid:])
        return self.sortedmerge(head1,head2)
    def sortedmerge(self,head1,head2):
        tmp = cur = ListNode(-1)
        while head1 and head2:
            if head1.val<head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next

            cur = cur.next
        cur.next = head1 or head2
        return tmp.next
