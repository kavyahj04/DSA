def isomorphic(s, t):
    if len(s) != len(t):
            return False

    s2t, t2s = {}, {}

    for char_s, char_t in zip(s, t):
        # Check if mapping conflicts in either direction
        if (char_s in s2t and s2t[char_s] != char_t) or \
            (char_t in t2s and t2s[char_t] != char_s):
            return False
            
        s2t[char_s] = char_t
        t2s[char_t] = char_s
    return True
isomorphic(s, t)