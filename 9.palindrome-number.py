#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        offset = 0
        left = 0
        right = len(s) - 1
        while left + offset < right - offset:
            if s[left + offset] != s[right - offset]:
                return False
            offset += 1
        return True
        
# @lc code=end
print(Solution().isPalindrome(1232))
