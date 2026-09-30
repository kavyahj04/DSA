class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res, path = [], []
        def backtrack(idx, s, res, path):
            if idx == len(s):
                res.append(path.copy())
                return 
            for i in range(idx, len(s)):
                if isPalindrome(s, idx, i):
                    path.append(s[idx:i+1])
                    backtrack(i+1, s, res, path)
                    path.pop()


        def isPalindrome(s,start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start +=1
                end -= 1
            return True
        backtrack(0, s, res, path)
        return res