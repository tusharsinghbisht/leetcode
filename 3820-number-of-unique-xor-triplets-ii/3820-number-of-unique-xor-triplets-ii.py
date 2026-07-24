class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        m = max(nums)
        
        max_xor = 1 << m.bit_length()

        xorPairs = [0]*max_xor
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                xorPairs[nums[i] ^ nums[j]] = 1

        triplets = [False]*max_xor

        for x in range(max_xor):
            if not xorPairs[x]:
                continue
            for v in nums:
                triplets[x^v] = True
        
        return sum(1 for b in triplets if b)