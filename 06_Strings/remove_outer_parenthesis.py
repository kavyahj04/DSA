def removeOuterP(s):
    outer = 0
    count = 0
    new = []
    os = True
    for i in range(1, len(s)):
        if s[i] == "(" and os:
            count += 1
        elif s[i] == ")" and count > 0:
            count -= 1
        elif count == 0 and os:
            new.append(s[outer + 1 :i])
            os = False
            continue
        else:
            outer = i
            os = True
    print("".join(new))

s = "(()())(())(()(()))"
removeOuterP(s)





            
        


