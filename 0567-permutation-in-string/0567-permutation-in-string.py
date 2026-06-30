class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        count1 = [0]*26

        for c in s1:
            count1[ord(c)-ord('a')] += 1

        for l in range(0, len(s2)-len(s1)+1):
            r = l + len(s1)
            
            count2 = [0]*26
            for c in s2[l:r]:
                count2[ord(c)-ord('a')] += 1
            
            if count1 == count2:
                return True

        return False
