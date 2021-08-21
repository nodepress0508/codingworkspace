"""
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
"""
"""
解題思路:
此題求四數之和為target a + b + c + d = target
首先先排序,外圍兩層for循環 一個a  一個 b
內層再使用相向雙指針一個頭 一個偉
虽然题目是四数之和，但是我们可以将他转换为三数之和，再进一步就是二数之和，先进行稳定排序，然后我们准备用四个指针

先用将问题看待为三数之和，即一个指针和三个指针
再将这三个指针看成二数之和，即一个指针和两个指针
那么问题就被化简了，先框定两个指针，再在这个基础上，用双指针解决问题，
当头指针和尾指针的元素之和大于new_target,尾指针-1(因为头指针+1的结果肯定大于new_target),
同理当头指针和尾指针的元素之和小于new_target,头指针+1。


時空複雜度:
    時:O(n^3)
    空:O(n^2)
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #異常檢測
        if not nums or len(nums) < 4:return []
        #排序
        nums.sort()
        #initialize
        ans = []
        for i in range (len(nums) - 3):
            #如果i前面有數而且相鄰兩數兩等,直接往下繼續 
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            #remove duplicate 
            for j in range (i + 1, len(nums) - 2): 
                #如果j前面有數而且相鄰兩數兩等,直接往下繼續
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                #雙指針
                left, right = j + 1, len(nums) - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1 
                        right -= 1
                        #remove duplicate 
                        while left < right and nums[left] == nums[left - 1]: 
                            continue
                        #remove duplicate 
                        while left < right and nums[right] == nums[right + 1]:
                            continue 
                    elif total < target:
                        left += 1 
                    else:
                        right -= 1 
        return ans