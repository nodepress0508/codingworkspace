"""
437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
Memoization

intuition:
1.In order to optimize from the brutal force solution, we will have to think of a clear way to memorize the intermediate result. Namely in the brutal force solution, we did a lot repeated calculation. For example 1->3->5, we calculated: 1, 1+3, 1+3+5, 3, 3+5, 5.
2.This is a classical 'space and time tradeoff': we can create a dictionary (named cache) which saves all the path sum (from root to current node) and their frequency.
3.Again, we traverse through the tree, at each node, we can get the currPathSum (from root to current node). If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target.
4.We just need to add the frequency of the oldPathSum to the result.
5.During the DFS break down, we need to -1 in cache[currPathSum], because this path is not available in later traverse.

TC:O(n) extra space

SC:O(n) as we just traverse once


"""
class Solution:
    
    def dfs(self, root, target, currentpathsum, cache):
        if not root:
            return
        currentpathsum +=root.val
        oldpathsum = currentpathsum-target
        # update result and cache
        self.result += cache.get(oldpathsum,0)
        cache[currentpathsum] = cache.get(currentpathsum,0)+1#create a dic with key currentsum 
        # dfs break down
        self.dfs(root.left, target, currentpathsum, cache)
        self.dfs(root.right, target, currentpathsum, cache)
        #when move to the different path, the currentsum is no longer available, so remove one
        #another idea is avoid backtracking from child to parent.
        cache[currentpathsum] -= 1

    def pathSum(self, root: TreeNode, sum: int) -> int:

        self.cache = {0:1}
        self.result = 0 

        self.dfs(root,sum, 0, cache)
        return self.result