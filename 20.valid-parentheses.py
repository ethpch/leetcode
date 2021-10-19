#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pair = {')': '(', '}': '{', ']': '['}
        stack = [s[0]]
        for ch in s[1:]:
            try:
                if stack[-1] == pair[ch]:
                    stack.pop()
                else:
                    stack.append(ch)
            except (IndexError, KeyError):
                stack.append(ch)
        return False if stack else True
# @lc code=end

