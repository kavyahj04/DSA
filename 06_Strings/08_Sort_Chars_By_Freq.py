def sortCharacterByFreq(s):
    freq_words = [[] for i in range(len(s)+1)]
    count = {}
    for i in range(len(s)):
        count[s[i]] = 1 + count.get(s[i], 0)
    for key, value in count.items():
        freq_words[value].append(key)
    new_word = ""
    for i in range(len(freq_words)-1, -1, -1):
        if len(freq_words[i]) > 0:
            for word in freq_words[i]:
                new_word += word * i
    print(new_word)
    return new_word

s = "tree"
sortCharacterByFreq(s)
