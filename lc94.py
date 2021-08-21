"""
94. Binary Tree Inorder Traversal


Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up:

Recursive solution is trivial, could you do it iteratively?
"""

"""
解题思路:
中序遍歷 left->root->right
通常考中序遍歷會要求使用iteration(迭代)的方法來進行操作不會考遞規(可能因為代碼量少??)
還不太熟要多練幾次尤其是第二次while node的地方寫法,似乎是特別處理都是依值線向下右子數的案例
令:
精简版本的 inorder traversal iteration code
算法流程:

复杂度分析
时间复杂度：O(N)  since we process each node of the tree exactly once.
空间复杂度：O(N) Arraylist of size n is used.

"""
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
iteration 令胡老師的方法 背下來
"""
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        #corner case 
        if not root: 
            return []
        # 创建一个 dummy node，右指针指向 root
        # 并放到 stack 里，此时 stack 的栈顶 dummy
        # 是 iterator 的当前位置
        dummy = TreeNode(0)
        dummy.right = root 
        stack = [dummy]

        inorder = []
        # 每次将 iterator 挪到下一个点
        # 也就是调整 stack 使得栈顶到下一个点
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)
        return inorder       

"""
另一種iterative 的方法 可能更好懂

1. 添加所有最左边节点到栈。 
2. pop stack 然后添加到结果。 
3. 查找当前node的右边节点是否为空， 如果不为空，重复step 1。
"""
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        
        ans = []
        #迭代的方式需要開闢棧
        stack = []
        #一直往左邊走
        while root:
            stack.append(root)
            root = root.left
        #開始準備彈棧
        while stack:
            currentnode = stack.pop()
            ans.append(currentnode.val)
            #如果當前節點有右子樹
            if currentnode.right:
                currentnode = currentnode.right
                #把右子樹向下的節點都處理,纖纖往左走
                while currentnode:
                    stack.append(currentnode)
                    currentnode = currentnode.left

        return ans
    
"""
recursive的方法

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        self.ans = []
        self.helper(root)
        return self.ans 
    def helper(self, root):
        if not root:
            return 
        self.helper(root.left)
        self.ans.append(root.val)
        self.helper(root.right)