def isomorphic(s, t):
    strs = {}
    if len(s) != len(t):
        return false

    for i in range(len(s)):
        if s[i] in strs and strs[s[i]] != t[i]:
            print(False)
            return False
        strs[s[i]] = t[i]
    print(strs)
    print(True)
    return True
    
            

s = "paper"
t = "title"

isomorphic(s, t)