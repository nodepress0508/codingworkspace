"""
33. Search in Rotated Sorted Array

You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
"""
"""
解題思路:
題目一定是沒有重複的數才可以進行二分,有重複的數就只能O(n)去解決
先進行數據的具象化,找出哪一段是有序的要馬是起點到中間有序或是中點到尾巴有序
然後開始進行二分,確認目標值是否在有序區間,然後再繼續縮小範圍進行二分直到跳出while循環
對start or end 進行判斷看哪一個為目標值

算法流程：
1.二分搜索时每次都是把数组分成两部分，先判段哪一部分是有序的
2.如果target在有序的那一部分，那么继续二分
3.如果在无序的那一部分，重复第一步

時空複雜度:
    時:O(logn)n为nums的长度。同二分查找的时间复杂度。
    空:O(1)個人認為没有使用额外空间。但是九章給的答案似乎是O(logn)

"""
"""
使用一次二分法的方法
"""
class Solution:
    def search(self, nums, target):
        #corner case
        if not nums: return -1
        #binary search template
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            #compare mid with start and end, and find out which part is sorted
            #Either start -> middle or middle -> end since it's RSA(rotate sorted array)
            if nums[mid] >= nums[start]:#acheck the start to mid section has order
                if nums[start] <= target <= nums[mid]:#check if target is between start and middle
                    end = mid
                else:
                    start = mid
            else:#middle to end section has order 
                if nums[mid] <= target <= nums[end]:#check if target between middle and end section
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1