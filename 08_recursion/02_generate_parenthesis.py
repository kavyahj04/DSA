def generateparenthesis(n):
    res = []
    def backtrack(s, o_c, c_c):
        if o_c == n and c_c == n:
            res.append(s)
            return 
        if o_c < n:
            backtrack(s+"(", o_c+1, c_c)
        if c_c < o_c:
            backtrack(s+")", o_c, c_c+1)
    backtrack("",0,0)
    print(res)


generateparenthesis(4)