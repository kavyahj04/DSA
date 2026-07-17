def kokoEatingBanans(arr, h):
    l, r = 1, max(arr)
    ans = float("-inf")
    while l <= r:
        mid = (l + r) // 2
        total = checkTime(arr, mid)
        if total <= h:
            ans = min(mid, ans)
            r = mid - 1
        else:
            l = mid + 1
    return ans


def checkTime(arr, mid):
    hours = 0
    for i in range(len(arr)):
        hours += ceil(arr[i]//mid)
        return hours
