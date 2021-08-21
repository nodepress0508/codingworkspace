"""
98. Validate Binary Search Tree


Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
"""
intuition:
DFS go deep, for each node we check if there left child is less than root node and right child is larger than root node

ref:
https://leetcode.com/problems/validate-binary-search-tree/discuss/32178/Clean-Python-Solution

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
recursive 
TC:O(N)
SC:O(N)
"""
class Solution:
    def isValidBST(self, root, floor = float('-inf'), ceilling = float('inf')):
        if not root:
            return True 
        if not floor < root.val < ceilling:
            return False
        # if root.val<= floor or root.val >= ceilling:
        #     return False
        # in the left branch, root val will be the new ceil; in the right branch new floor will be root val
        return self.isValidBST(root.left,floor,root.val) and self.isValidBST(root.right,root.val, ceilling)
        
