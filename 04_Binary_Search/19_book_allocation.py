def bookAllocationLinear(pages, stds):
    low,high = max(pages), sum(pages)
    for i in range(low, high+1):
        cnt = checkStudentCnt(pages, i)
        # print(i,cnt)
        if cnt == stds:
            print(i)
            return i

def checkStudentCnt(pages, p):
    std = 1
    last = 0
    for i in range(len(pages)):
        if pages[i] + last <= p:
            last += pages[i]
        else:
            std += 1
            last = pages[i]
    return std

pages = [25, 46, 28, 49, 24]
s = 4
bookAllocation(pages, s)

def bookAllocation(pages, stds):
    low,high = max(pages), sum(pages)
    while low <= high:
        mid = (low + high) // 2
        s = checkStudentCnt(pages, mid)
        if s <= stds:
            high = mid - 1
        else:
            low = mid + 1
    return low