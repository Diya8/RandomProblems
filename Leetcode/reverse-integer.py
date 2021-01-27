# Source: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        s = list(str(x))
        index = 0
        if s[0] == '-':
            index = 1
        num = s[::-1]
        if index == 1:
            del num[-1]
            num.insert(0, '-')
        m = int(''.join(num))
        if m < -(2**31) or m > (2**31)-1: 
            return 0
        return m