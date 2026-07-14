def xorOperation(self, n: int, start: int) -> int:
        range_ = start + 2 * n
        temp = 0
        for i in range(start,range_,2):
            temp ^= i
        return temp