class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = [i for i in range(0, 1001)]
        for j in x:
            if n == 2 ** x[j]:
                return True
            if j == 1000:
                return False
