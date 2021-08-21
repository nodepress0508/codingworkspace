"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
"""
intuition:
TC:O(N^2)
SC:O(1)
"""
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
nums =[-2,0,1,1,2]
nums.sort()
# print (nums)
ans = []
for i in range(len(nums)-2):
    # when i = 0, we don's need to check if it's a duplicate element since it doesn't even have a previous element to compare with
    # nums[i] == nums[i-1] is to prevent checking duplicate again.
    if i> 0 and nums[i] == nums[i-1]:
        continue
    l = i+1
    r = len(nums)-1
    while l < r:
        total = nums[i] + nums[l] + nums[r]
        if total < 0:
            l+=1
        elif total>0:
            r-=1
        else:
            ans.append((nums[i], nums[l], nums[r]))
            while l < r and nums[l] == nums[l+1]:#increment l until nums[l] != nums[l-1]
                l+=1
            while l < r and nums[r] == nums[r-1]:#decrement r and nutil nums[k] != nums[k-1]
                r-=1

            l+=1
            r-=1
print (ans)