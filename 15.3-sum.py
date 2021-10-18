#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        nums = sorted(nums)
        last = -999999
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if last == nums[i]:
                continue
            else:
                last = nums[i]
            ptr1 = i + 1
            ptr2 = len(nums) - 1
            while ptr1 < ptr2:
                _ = nums[i] + nums[ptr1] + nums[ptr2]
                if _ > 0:
                    ptr2 -= 1
                elif _ < 0:
                    ptr1 += 1
                else:
                    res.append((nums[i], nums[ptr1], nums[ptr2]))
                    ptr1 += 1
                    ptr2 -= 1
        return set(res)


# @lc code=end

