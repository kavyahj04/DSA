class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0
        idx = 0
        signed_var = 1
        result = 0
        if s[idx] == "-":
            signed_var = -1
            idx += 1
        elif s[idx] == "+":
            signed_var = 1
            idx += 1
            

        while idx < len(s) and s[idx].isdigit():
            result = (result * 10) + int(s[idx])
            idx += 1
            
        if signed_var == -1:
            result = -1 * result

        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
        
        return result
 