class Solution:
    def isPowerOfThree(self, n: int):
        if n == 1:
            return True
        while True:
            n = n / 3
            if n == 1:
                return True

            elif n == 0:
                return False

            else:
                continue