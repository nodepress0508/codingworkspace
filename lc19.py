"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
"""
解題思路:
同向雙指針(快慢指針題型)
由於N是變數,所以先使用for 循環讓快指針先走N 步,之後快慢指針各走一步,當fast.next 是none 時
把慢指針的next 換到下下一個點就完成
注意的地方是要建立dummy node 作為開頭然後把他接到head node
然後把快慢指針都只向dummy node從dummy開始走

時空複雜度:
    時:O(n)
    空:O(1)

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return None

        dummy = ListNode(0)
        dummy.next = head
        #快慢指針都從dummy節點開始走
        slow = fast = dummy
        # 快指針先走n步
        for i in range (n):
            fast = fast.next
        
        while fast.next != None:
            #快慢指針各走一步直到快指針的下一步為none
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next