# Source: https://leetcode.com/problems/remove-element/submissions/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if val in nums:
            x = nums.count(val)
            length -= x
            i = 0
            while x != 0:
                if nums[i] == val:
                    del nums[i]
                    i -= 1
                    x -= 1
                i += 1
        return length
        