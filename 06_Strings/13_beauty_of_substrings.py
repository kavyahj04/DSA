def beautySum(self, s: str) -> int:
        total_beauty = 0
        n = len(s)
        
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                min_freq = float('inf')
                max_freq = float('-inf')
                for k in range(26):
                    if freq[k] > 0: 
                        min_freq = min(min_freq, freq[k])
                        max_freq = max(max_freq, freq[k])
                total_beauty += (max_freq - min_freq)
                
        return total_beauty