"""
4. Median of Two Sorted Arrays


Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
"""
"""
解題思路:
    此題可以遍歷兩個數組然後在找終點,這樣時間會是O(len(nums1) + len(nums2)),是一個線性的時間複雜度
    通過O(1)的時間把一個O(k)=> O(k/2)的問題
    通過個數組的第k/2的數去判斷如何去除一半的數組,去除的動作是O(1)的,移動一下數組的首指針即可
    题目要求时间复杂度为O(log(m+n))，不难想到二分法。双指针方法中，我们一个一个的排除不可能的元素。如果充分利用数组的有序性，就能一半一半的排除。具体来说，假设我们要找第k小数，通过二分，可以每次循环排除掉k/2个数。
算法流程：
    1.建立辅助函数getKth，参数有数组A，A的起始指针start1和终止指针end1, 相对应的有B、start2和end2，以及整数k，目标是找到A[start1:end1]和B[start2:end2]中第k小的元素。
    2.在主程序中，看m + n的奇偶性，并调用getKth函数。如果是奇数，返回数组A和B的第(m + n) // 2 + 1小元素；如果是偶数，返回数组A和B的第(m + n) // 2小和第(m + n) // 2 + 1小元素的均值。
    3.getKth(nums1, start1, end1, nums2, start2, end2, k)函数的实现方法：
     如果有数组在[start:end]范围内为空，说明该数组已经排除完毕，第k小的元素一定存在于另一数组中，计算好索引位置返回即可。 
     如果k为1，说明已经找到第k小的数，那就是A[start1]和B[start2]中的较小值，直接返回即可。 
     定义指针i和j，分别指向A和B，使得A[start1:i]和B[start2:j]的长度分别为k // 2，通过比较A[i]和B[j]的大小，我们就可以确定排除哪段元素。 如果A[i] > B[j]，说明B[start2:j]不可能为第k小元素。我们对A[start1:end1]和B[j + 1:end2]继续送入getKth进行递归，k应该更新为k - (j - start2 + 1)。 * 反之，说明A[start1:i]不可能为第k小元素。我们对A[i + 1:end1]和B[start2:end2]继续送入getKth进行递归，k应该更新为k - (i - start1 + 1)。
時空複雜度:
    時:O(log(m+n))m和n分别是两个数组的长度。
    空:O(1) 沒有開闢額外空間

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 1:# if it is odd
            return self.getKth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, (m + n) // 2 + 1)
        #if it's even
        left = self.getKth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, (m + n) // 2)
        right = self.getKth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, (m + n) // 2 + 1)
        return (left + right) / 2
    
    def getKth(self, A, A_start, A_end, B, B_start, B_end, k):#找兩數組合併後從小到大第K個數 K 是從1開始的
        lenA = A_end - A_start + 1 
        lenB = B_end - B_start + 1
        
        #A數組排除完了,return B 數組的第K個 
        if (lenA == 0):
            return B[B_start + k - 1]
        #B數組排除完了,return A 數組的第K個 
        if (lenB == 0):
            return A[A_start + k - 1]

        #已經找到第K小的數
        if k == 1:
            return min(A[A_start], B[B_start])

        #開始二分,取個數組的第k/2個數
        #取min(該數組長度,第k除2個數)的原因應該在於避免在找第K/2個數時,
        #找不到,不存在,比如A數組只有一丁點,B數組特別的長
        A_mid = A_start + min(lenA, k // 2) - 1#A數組的第K/2個數
        B_mid = B_start + min(lenB, k // 2) - 1#B數組的第K/2個數
        if (A[A_mid] > B[B_mid]):# move the b pointer to k/2 + 1 
            return self.getKth(A, A_start, A_end, B, B_mid + 1, B_end, k - (B_mid - B_start + 1))
        else:
            return self.getKth(A, A_mid + 1, A_end, B, B_start, B_end, k - (A_mid - A_start + 1))