#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = ['' for i in range(numRows)]
        ptr = [0, 0]
        direction = 0
        for i in range(len(s)):
            arr[ptr[0]] += s[i]
            if numRows == 1:
                ptr[0] = 0
                ptr[1] += 1
            else:
                if ptr[0] == 0:
                    direction = 0
                elif ptr[0] == numRows - 1:
                    direction = 1
                if direction == 0:
                    ptr[0] += 1
                elif direction == 1:
                    ptr[0] -= 1
                    ptr[1] += 1
        return ''.join(arr)


# @lc code=end

