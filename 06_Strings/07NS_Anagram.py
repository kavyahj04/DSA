def anagram(s, t):
    if len(s) != len(t):
        return False
    sFreq = [0] * 26
    tFreq = [0] * 26

    for i in range(len(s)):
        sFreq[ord(s[i]) - ord('a')] += 1
        tFreq[ord(t[i]) - ord('a')] += 1
    if sFreq == tFreq:
        print(True)
        return True
    print(False)
    return False



s = "anagram"
t = "nagaram"
anagram(s, t)