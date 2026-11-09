class Solution:
    def countSubstr (self, s, k):
        def atMost(k):
            if k == 0:
                return 0
            l, cnt, freq = 0, 0, {}
            for r in range(len(s)):
                freq[s[r]] = 1 + freq.get(s[r], 0)
                while len(freq) > k:
                    freq[s[l]] -= 1
                    if freq[s[l]] == 0:
                        del freq[s[l]]
                    l += 1
                cnt += r - l + 1
            return cnt
            
        return atMost(k) - atMost(k - 1)