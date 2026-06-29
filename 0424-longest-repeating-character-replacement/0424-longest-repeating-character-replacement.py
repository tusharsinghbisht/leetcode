class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n < 2:
            return n

        freq = [0]*26
        l = 0
        r = 1
        freq[ord(s[0])-ord('A')] += 1
        res = 0
        while r < n and l <= r:
            freq[ord(s[r])-ord('A')] += 1
            
            maxc =  max(freq)
            if (r-l+1)-maxc <= k:
                res = max(res, r-l+1)
                r += 1
            else:
                freq[ord(s[l])-ord('A')] -= 1
                freq[ord(s[r])-ord('A')] -= 1 # dec current r else it will be inc by 1 in next iteration as r is not changed
                l += 1

        return res


            



