def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V" : 5, "X": 10, "L":50, "C":100, "D":500,"M":1000}
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and romans[s[i]] < romans[s[i+1]]:
                total -= romans[s[i]]
            else:
                total += romans[s[i]]
                
        return 


def romanToInt(self, s: str) -> int:
        elements = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        res = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and elements[s[i]] < elements[s[i+1]]:
                res += elements[s[i+1]] - elements[s[i]]
                i += 2
            else:
                res += elements[s[i]]
                i += 1
        return res

