#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        last = -9999
        minimum_abs = 9999
        for i in range(len(nums) - 2):
            if last == nums[i]:
                continue
            else:
                last = nums[i]
            ptr1 = i + 1
            ptr2 = len(nums) - 1
            while ptr1 < ptr2:
                _ = nums[i] + nums[ptr1] + nums[ptr2]
                t = abs(_ - target)
                if t < minimum_abs:
                    minimum_abs = t
                    minimum = _
                if _ - target > 0:
                    ptr2 -= 1
                elif _ - target < 0:
                    ptr1 += 1
                else:
                    return _
        return minimum

# @lc code=end

