class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        count1 = {}

        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        count2 =  {}
        for c in s2[0:len(s1)]:
            count2[c] = count2.get(c, 0) + 1

        for l in range(0, len(s2)-len(s1)+1):
            r = l+len(s1)-1
            if l > 0:
                count2[s2[l-1]] -= 1
                if count2[s2[l-1]] == 0:
                    del count2[s2[l-1]]
                count2[s2[r]] = count2.get(s2[r], 0) + 1
            if count1 == count2:
                return True

        return False
