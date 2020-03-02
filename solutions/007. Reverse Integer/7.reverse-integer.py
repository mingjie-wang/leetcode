#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sign = (x>0)-(x<0)
        rx = int(str(sign*x)[::-1])
        return sign*rx*(rx<2**31)
# @lc code=end

