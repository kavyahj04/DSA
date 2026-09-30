

def mergeSort(arr, low, high):
    if low >= high:
        return 0
    cnt = 0
    mid = (low + high) // 2
    cnt += mergeSort(arr, low, mid)
    cnt += mergeSort(arr, mid+1, high)
    cnt += merge(arr, low, mid, high)
    print(cnt)
    return cnt

def merge(arr, low, mid, high):
    cnt = 0
    left = low
    right = mid+1
    temp = []
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
          
mergeSort([5,3,2,4,1], 0, 4)