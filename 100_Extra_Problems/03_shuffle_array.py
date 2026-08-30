class Solution:

    def __init__(self, nums: List[int]):
        self.org = nums.copy()
        self.nums = nums
        

    def reset(self) -> List[int]:
        self.nums = self.org.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums
        