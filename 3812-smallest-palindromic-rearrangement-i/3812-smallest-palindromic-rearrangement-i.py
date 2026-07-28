class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        cnt = [0]*26

        for c in s:
            cnt[ord(c) - ord('a')] += 1
       
        string = ["-"]*n 
        it = 0
        for i in range(26):
            if cnt[i] == 0:
                continue
                
            ch = chr(ord('a') + i)

            if it <= math.ceil(n/2)-1:
                if cnt[i] % 2 == 1:
                    string[int(n/2)] = ch
                    cnt[i] -= 1
                    while cnt[i] != 0:
                        string[it] = ch
                        string[n-1-it] = ch
                        cnt[i] -= 2
                        it += 1
                else:
                    while cnt[i]!= 0:
                        string[it] = ch
                        string[n-1-it] = ch
                        cnt[i] -= 2
                        it += 1

        return "".join(string)