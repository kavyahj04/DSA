def leadersArray(arr):
    max_ = float('-inf')
    leaders = []
    for i in range(len(arr) -1, -1, -1):
        if arr[i] > max_:
            max_ = arr[i]
            leaders.append(arr[i])
    print(leaders[::-1])
    return leaders

arr = [10, 22, 3,12, 4, 0, 6]
leadersArray(arr)

