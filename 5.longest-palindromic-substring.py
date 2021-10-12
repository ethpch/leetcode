#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        centre = 0
        palinsubstr = ''
        lens = len(s)

        def check_plain(s: str) -> bool:
            offset = 0
            left = 0
            right = len(s) - 1
            while left + offset < right - offset:
                if s[left + offset] != s[right - offset]:
                    return False
                offset += 1
            return True

        while centre < lens:
            if len(palinsubstr) > (lens - centre) * 2:
                break
            centre_left = centre_right = centre
            for i in range(centre + 1, lens):
                if s[i] == s[centre]:
                    centre_right = i
                else:
                    break
            offset = 0
            while centre_left - offset >= 0 and centre_right + offset <= lens:
                substr = s[centre_left - offset:centre_right + offset + 1]
                if check_plain(substr):
                    if len(palinsubstr) < len(substr):
                        palinsubstr = substr
                    del substr
                    offset += 1
                else:
                    break
            if centre == centre_right:
                centre += 1
            else:
                centre = centre_right
        return palinsubstr


# @lc code=end

