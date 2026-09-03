def rotateString(s, goal):
    idx = -1
    for i in range(len(goal)):
        if goal[i] == s[0]:
            idx = i
            print(idx)
    rotations = len(s) - idx
    start = s[0:rotations][::-1]
    end = s[rotations:][::-1]
    s = end[::-1] + start[::-1]
    return s == goal

s = "abcde"
goal = "cdeab"
rotateString(s, goal)