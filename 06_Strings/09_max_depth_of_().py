def maxDepth(s):
    count, max_ = 0, float("-inf")
    for c in s:
        if c == "(":
            count += 1
        elif c == ")":
            count += 1
        max_ = max(max_, count)
    return max_