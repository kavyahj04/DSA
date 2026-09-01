def reverseWords(s):
    out = []
    in_ = []
    s = s.split()
    
    for i in range(len(s)-1,-1,-1):
        out.append(s[i])
    return " ".join(out)


s = " the  sky  is pink"
reverseWords(s)


# leetcode sol 

def reverseWords(self, s: str) -> str:
    return " ".join(s.split()[::-1])