#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        longest = 0
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            while right <= len(s):
                substr = s[left:right]
                substr_without_repeat = set(substr)
                _ = len(substr) - len(substr_without_repeat)
                if _ == 0:
                    if len(substr) > longest:
                        longest = len(substr)
                    right += 1
                elif _ > 0:
                    left += 1
            return longest


# @lc code=end
