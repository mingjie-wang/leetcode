#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    
    def twoSum(self, nums:[int], target: int)->[int]:
        map={}
        for i in range(len(nums)):
            if target-nums[i] not in map:
               map[nums[i]] = i
            else: 
                return map[target-nums[i]],i 
        return -1,- 1

# @lc code=end

