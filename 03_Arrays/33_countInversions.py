def merge(arr, low, mid, high, cnt):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            cnt += mid - left + 1
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high+1):
        arr[i] = temp[i - low]
    return cnt

def countInversion(arr, low, high):
    cnt = 0
    if low >= high:
        return 0
    mid = (low + high) // 2
    cnt += countInversion(arr, low, mid)
    cnt += countInversion(arr, mid+1, high)
    cnt = merge(arr, low, mid, high, cnt)
    return cnt

arr = [5, 3, 2, 4, 1]
print(countInversion(arr, 0, len(arr) - 1))