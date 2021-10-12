#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        i7, j7 = num // 1000, num % 1000
        i6, j6 = j7 // 500, j7 % 500
        i5, j5 = j6 // 100, j6 % 100
        i4, j4 = j5 // 50, j5 % 50
        i3, j3 = j4 // 10, j4 % 10
        i2, j2 = j3 // 5, j3 % 5
        i1 = j2 // 1
        if i7:
            res += 'M' * i7
        if i6 == 1 and i5 == 4:
            res += 'CM'
        else:
            if i6 == 0 and i5 == 4:
                res += 'CD'
            else:
                if i6:
                    res += 'D'
                if i5:
                    res += 'C' * i5
        if i4 == 1 and i3 == 4:
            res += 'XC'
        else:
            if i4 == 0 and i3 == 4:
                res += 'XL'
            else:
                if i4:
                    res += 'L'
                if i3:
                    res += 'X' * i3
        if i2 == 1 and i1 == 4:
            res += 'IX'
        else:
            if i2 == 0 and i1 == 4:
                res += 'IV'
            else:
                if i2:
                    res += 'V'
                if i1:
                    res += 'I' * i1
        return res


# @lc code=end

