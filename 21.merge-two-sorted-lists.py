#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val >= l2.val:
            root = head = l2
        else:
            root = head = l1
        while l1 is not None and l2 is not None:
            if head is l1:
                if getattr(l1.next, 'val', -101) > l2.val:
                    temp = l1.next
                    head.next = l2
                    l1 = temp
                else:
                    l1 = l1.next
            elif head is l2:
                if getattr(l2.next, 'val', -101) > l1.val:
                    temp = l2.next
                    head.next = l1
                    l2 = temp
                else:
                    l2 = l2.next
            if head.next is not None:
                head = head.next
        if l1 is None:
            head.next = l2
        elif l2 is None:
            head.next = l1
        return root


# @lc code=end

