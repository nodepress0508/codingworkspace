"""
74. Search a 2D Matrix


Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
"""
解題思路:
此題第一個想法可能會從column 開始(第一個元素)然後再開始去找列
所以是相當於我們要做兩次二分,第一次是先從直的進行二分,第二次是從橫的進行二分
雖然是二維數組,但是在系統存取的順序上其實是連續的
题目提到，给定的数组已经排序，若是一个一维数组，直接一次二分查找即可。
现在题目给了一个二维数组，那么处理一下数组的下标，仍然按照一维数组二分即可
二分查找常用于查找有序数组中目标数target的位置，
用left和right记录target所在的区间端点，每次将区间的中间位置值和target作比较，然后移动区间端点。
可以看作是一个有序数组被分成了n段，每段就是一行。因此依然可以二分求解。
对每个数字，根据其下标i，j进行编号，每个数字可被编号为0～n*n-1
相当于是在一个数组中的下标。然后直接像在数组中二分一样来做。
取的mid要还原成二位数组中的下标，i = mid/n, j = mid%n
套用二分法模板,使用子函數get 進行座標轉換

算法流程：
*将数组matrix[i][j]下标转换为 i*col + j， 问题即转换为一维数组二分查找问题
*将区间赋值为整个数组区间（left = 0, right = n*m - 1），取中间位置mid
*若a[mid] < target，则将区间缩小到原区间的右区间(left = mid + 1)
*若a[mid] > target，则将区间缩小至原区间的左区间(right = mid)
*若a[mid] = target，返回true
*当left >= right 时，若a[right] = target则返回true, 否则返回false

時空複雜度:
    時:O(lognm). 即将二维数组看作一个n*m大小的一维数组，二分查找值。 
    空:O(1) 查找不需要开辟新的空间，只需在原数组基础上进行查找即可

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False 
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if self.get_value(matrix, mid) < target:
                start = mid
            else:
                end = mid
        #check if start or end match the target
        if self.get_value(matrix, start) == target:
            return True 
        if self.get_value(matrix, end) == target:
            return True
        return False
    #2維數組取下標的方法    
    def get_value(self, matrix, index):
        x_value = index // len(matrix[0])#取整數
        y_value = index % len(matrix[0])#取餘數
        return matrix[x_value][y_value]