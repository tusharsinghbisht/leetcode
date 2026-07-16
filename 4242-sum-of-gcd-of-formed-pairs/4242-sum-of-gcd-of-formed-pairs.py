class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    def gcdSum(self, nums: list[int]) -> int:
        mx = -1
        prefixGcd = []
        for n in nums:
            mx = max(mx, n)
            prefixGcd.append(self.gcd(mx, n))

        prefixGcd.sort()

        l, r = 0, len(nums)-1
        result = 0
        while r > l:
            result += self.gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1

        return result