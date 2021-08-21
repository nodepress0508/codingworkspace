"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
"""
解題思路
找出兩數和有兩種方法,一個為使用哈希表,另一個方法為使用排序+相向雙指針

時空複雜度:
1.哈希表
    時:O(n)
    空:O(n)
2.排序+雙指針
    時:O(nlogn)
    空:O(1)
"""
nums = [2,7,11,15], target = 9
"""
哈希表
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #異常檢測
        if not nums:
            return [-1, -1]
        #哈希表
        hashtable = {}
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return hashtable[target - nums[i]], i
            hashtable[nums[i]] = i
        return [-1, -1]


"""
排序+雙指針
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #異常檢測
        if not nums:
            return [-1, -1]
        #枚舉法
        numbers = [ (number,index) for index, number in enumerate(nums)]
        #排序,帶著他的index一起排序
        numbers.sort()
        #相向雙指針
        left, right = 0, len(nums) - 1
        while  left < right:
            if numbers[left][0] + numbers[right][0] > target:
                right -= 1
            elif numbers[left][0] + numbers[right][0] < target:
                left += 1
            else:
                return sorted([numbers[left][1], numbers[right][1]])
        return [-1, -1]