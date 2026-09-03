class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_str = ""
        for i in range(len(s)):
            odd_pldrm = self.expandAroundCenter(s, i, i)
            if len(odd_pldrm) > len(max_str):
                max_str = odd_pldrm
            even_pldrm = self.expandAroundCenter(s, i, i+1)
            if len(even_pldrm) > len(max_str):
                max_str = even_pldrm
        return max_str
    
    def expandAroundCenter(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]