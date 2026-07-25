class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []

        num = n
        while num != 0:
            dig = num % 10
            num = num // 10
            digits.append(dig)
            

        digits.sort()

        return digits[-1]*digits[-2]