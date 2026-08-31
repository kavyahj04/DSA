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
        else:
            outer = i
            os = True
    print("".join(new))

s = "(()())(())(()(()))"
removeOuterP(s)

# Time and space comeplexity

# Time 

# O(n) overall. Small correction on the reasoning: each individual slice isn't constant-length, but the slices never overlap — every character in s belongs to at most one slice. So their lengths sum to at most n across the whole loop, not n per iteration. That's why it's O(n) total

# Space 

# O(n)


# Optimal solution 

def removeOuterParentheses(self, s: str) -> str:
        c=0
        res=[]
        for i in s:
            if i=="(":
                if c>0:
                    res.append(i)
                c+=1
            else:
                c-=1
                if c>0:
                    res.append(i)
        return "".join(res)



            
        


