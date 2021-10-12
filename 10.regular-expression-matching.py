#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        return bool(re.match('^' + p + '$', s))
        
# @lc code=end

