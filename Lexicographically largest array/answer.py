class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        X, Y = [], []
        i, j = 0, n - 1 
        index = 99
        while 1:
            if A[i] > A[j]:
                X.append(A[i])
                i += 1
                if i>j:
                    break
            else:
                index = i # finding break point
                break
        if index == 0:
            return A[::-1]
        return A[:index] + A[n-1:index-1:-1]
