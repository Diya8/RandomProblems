# Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) != 0:
            u = nums[0]
        n = len(nums)
        x, i = 1, 1
        while x < n:
            if nums[i] > u:
                u = nums[i]
                i += 1
            else:
                del nums[i]
            x += 1
        return len(nums)
        