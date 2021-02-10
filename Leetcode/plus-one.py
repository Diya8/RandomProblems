# Source: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        flag = True
        while flag:
            if digits[i] < 9:
                digits[i] += 1
                flag = False
            elif i == -(len(digits)):
                digits[i] = 0
                digits.insert(0, 1)
                flag = False
            else:
                digits[i] = 0
                i -= 1
        return digits