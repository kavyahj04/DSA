def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMost(k):
            res = []
            if k == 0:
                return 0
            l, cnt, freq = 0, 0, {}
            for r in range(len(nums)):
                freq[nums[r]] = 1 + freq.get(nums[r], 0)
                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                cnt += r - l + 1
            return cnt
            
        return atMost(k) - atMost(k - 1)