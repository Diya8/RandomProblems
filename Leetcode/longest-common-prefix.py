# Source: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        word1 = strs[0]
        n = len(word1)
        for x in range(1,len(strs)):
            p = ""
            for l in range(min(n, len(strs[x]))):
                if word1[l] == strs[x][l]:
                    p += word1[l]
                else:
                    break
            print(p)
            if len(p) == 0:
                return ""
            else:
                if prefix == "" and len(p) > 0:
                    prefix = p
                elif len(p) < len(prefix):
                    prefix = p
        return prefix