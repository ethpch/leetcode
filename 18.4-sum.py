#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        last_left = -9999999999
        for i in range(len(nums) - 3):
            if last_left == nums[i]:
                continue
            else:
                last_left = nums[i]
            last_right = 9999999999
            for j in range(len(nums) - 1, i + 1, -1):
                if last_right == nums[j]:
                    continue
                else:
                    last_right = nums[j]
                ptr1 = i + 1
                ptr2 = j - 1
                while ptr1 < ptr2:
                    _ = nums[i] + nums[ptr1] + nums[ptr2] + nums[j]
                    if _ > target:
                        ptr2 -= 1
                    elif _ < target:
                        ptr1 += 1
                    else:
                        res.append((nums[i], nums[ptr1], nums[ptr2], nums[j]))
                        ptr1 += 1
                        ptr2 -= 1
        return set(res)


# @lc code=end

