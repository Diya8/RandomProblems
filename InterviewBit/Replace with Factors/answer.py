# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        C = A
        while A != None:
            A.val = (A.val//B)*B
            A = A.next
            if A == None:
                break
        return C
