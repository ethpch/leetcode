#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ptr1 = ptr2 = 0
        arr = []
        while True:
            if ptr1 == len(nums1):
                arr.extend(nums2[ptr2:])
                break
            elif ptr2 == len(nums2):
                arr.extend(nums1[ptr1:])
                break
            else:
                if nums1[ptr1] >= nums2[ptr2]:
                    arr.append(nums2[ptr2])
                    ptr2 += 1
                else:
                    arr.append(nums1[ptr1])
                    ptr1 += 1
        med = int(len(arr) / 2)
        if len(arr) % 2 == 0:
            return (arr[med - 1] + arr[med]) / 2
        else:
            return arr[med]

# @lc code=end
