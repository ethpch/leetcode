#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        i1 = i2 = i3 = i4 = i5 = i6 = i7 = 0

        def check(first, second, three, string):
            ptr = len(string) - 1
            ix = iy = 0
            if string.endswith(three + first):
                ix = 1
                iy = 4
                ptr -= 2
            else:
                if string.endswith(three + second):
                    iy = 4
                    ptr -= 2
                elif string.endswith(second):
                    ix = 1
                    ptr -= 1
                elif string.endswith(three):
                    count = 0
                    for i in range(ptr, -1, -1):
                        if string[i] == three:
                            count += 1
                        elif string[i] == second:
                            ix = 1
                            ptr -= 1
                            break
                        else:
                            break
                    iy = count
                    ptr -= count
            return ix, iy, string[:ptr + 1]

        i2, i1, s = check('X', 'V', 'I', s)
        i4, i3, s = check('C', 'L', 'X', s)
        i6, i5, s = check('M', 'D', 'C', s)
        i7 = len(s)
        return i1 * 1 + i2 * 5 + i3 * 10 + i4 * 50 + i5 * 100 + i6 * 500 + i7 * 1000


# @lc code=end

