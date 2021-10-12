#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        max_value = 2**31 - 1
        min_value = -2**31
        stri = str(x)
        if stri.startswith('-'):
            ints = -int(''.join(reversed(stri[1:])))
        else:
            ints = int(''.join(reversed(stri)))
        if min_value <= ints <= max_value:
            return ints
        else:
            return 0


# @lc code=end

