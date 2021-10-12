#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get(self):
        _ = self
        li = []
        while _.next is not None:
            li.append(_.val)
            _ = _.next
        li.append(_.val)
        return li


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        _l1 = []
        _l2 = []
        while l1 is not None:
            _l1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            _l2.append(l2.val)
            l2 = l2.next
        li = []
        for i in range(min(len(_l1), len(_l2))):
            li.append(_l1[i] + _l2[i])
        if len(_l1) > len(_l2):
            li.extend(_l1[len(_l2):])
        elif len(_l1) < len(_l2):
            li.extend(_l2[len(_l1):])
        for i in range(len(li) - 1):
            if li[i] >= 10:
                li[i] -= 10
                li[i + 1] += 1
        if li[-1] >= 10:
            li[-1] -= 10
            li.append(1)
        cursor = root = ListNode()
        for i in li:
            cursor.next = ListNode(i, ListNode())
            cursor = cursor.next
        cursor.next = None
        return root.next
# @lc code=end
