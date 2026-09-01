def longestaparefix(strs):

    # vertical scanning 

    first = strs[0]
    
    for i in range(len(first)):
        for j in range(1, len(strs)):
            if i == len(strs[j]) or first[i] != strs[j][i]:
                return first[:i]
    return first
    
    # horizaontal scanning

    s = strs[0]
    for i in range(1, len(strs)):
        while not strs[i].startswith(s):
            s = s[:-1]
    return s
