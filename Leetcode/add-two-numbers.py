# Source: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = [], []
        while l1 != None:
            n1.append(str(l1.val))
            l1 = l1.next
        while l2 != None:
            n2.append(str(l2.val))
            l2 = l2.next
        n1 = "".join(n1)
        n2 = "".join(n2)
        res = int(n1[::-1]) + int(n2[::-1])
        res = str(res)[::-1]
        l3 = ListNode(int(res[0]))
        x = l3
        for i in res[1:]:
            l3.next = ListNode(int(i))
            l3 = l3.next
        return x       