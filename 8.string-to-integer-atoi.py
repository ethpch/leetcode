#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        import re
        reobj = re.match(r'[+-]?\d+', s)
        if reobj:
            res = reobj.group(0)
            if res:
                res = int(res)
                if res > 2**31 - 1:
                    return 2**31 - 1
                elif res < -2**31:
                    return -2**31
                else:
                    return res
        return 0


# @lc code=end
print(Solution().myAtoi("3.14159"))
