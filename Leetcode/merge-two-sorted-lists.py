# Source: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        if l1 == None and l2 == None:
            return None
        result = res
        val = 0
        flag = False
        while l1 != None and l2 != None:
            if flag:
                res.next = ListNode()
                res = res.next
            if l1.val < l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            res.val = val
            flag = True
        while l1 != None:
            if flag:
                res.next = ListNode()
                res = res.next
            res.val = l1.val
            flag = True
            l1 = l1.next
        while l2 != None:
            if flag:
                res.next = ListNode()
                res = res.next
            
            res.val = l2.val
            flag = True
            l2 = l2.next
        return result