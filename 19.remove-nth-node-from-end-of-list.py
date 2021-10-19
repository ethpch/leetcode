#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_left = current_right = head
        nodecount = 0
        while current_right.next is not None:
            current_right = current_right.next
            if nodecount < n:
                nodecount += 1
            else:
                current_left = current_left.next
        if nodecount == n:
            if current_left.next is not None:
                current_left.next = current_left.next.next
            return head
        else:
            return head.next


# @lc code=end
