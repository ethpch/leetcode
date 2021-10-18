#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonp = ''
        try:
            for i in range(min([len(s) for s in strs])):
                if len(set([s[i] for s in strs])) == 1:
                    commonp += strs[0][i]
                else:
                    break
        except ValueError:
            pass
        return commonp
# @lc code=end

