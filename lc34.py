"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
"""
解題思路:
    按照二分法模版，必須注意中間值等於目標的情形,
    在額外使用兩個指針,一個為mid - 1, 另一個為 mid + 1 
    當等於目標值時就往兩邊走直到不等於目標值
    此題也可以用線性的方法去解題但時間為O(n),沒有二分快

算法流程：
    
時空複雜度:
    時:O(logn) 
    空:O(1) 沒有開闢額外空間

"""
"""
二分法
"""
class Solution:
    """
    @param nums: the array of integers
    @param target: 
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        if not nums: return [-1, -1]
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if nums[mid] == target:
                #當二分中間等於時由於目標有可能重複在列表內,不知道分到的位置在哪
                #所以必須要特別的處理,兩個指針一個向左跑一個向右跑直到找到第一個目標值和最後一個目標值相等的位置
                i = mid - 1#往左找,直到找到第一個目標值
                while i >= 0 and nums[i] == target:
                    i -= 1 
                    
                j = mid + 1 #往右找,直到找到最後一個目標值
                while j < len(nums) and nums[j] == target:
                    j += 1 
                return [i + 1, j - 1]

            elif nums[mid] < target:
                start = mid 
            else:
                end = mid
        # when exit while loop ,we compare two result with our target value 
        if nums[start] == target and nums[end] == target:
            return [start, end]
        elif nums[start] == target:
            return [start, start]
        elif nums[end] == target:
            return [end, end]
        else:
            return [-1, -1]



"""
線性(leetcode官方答案)
"""

class Solution:
    def searchRange(self, nums, target):
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]

"""
二分(leetcode官方答案)
"""
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]