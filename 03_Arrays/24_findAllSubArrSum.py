def findAllSubSum(arr, k):
    prefix_sum = 0
    count = 0
    elements = {0:1}
    for i in range(len(arr)):
        prefix_sum += arr[i]
        remove = prefix_sum - k
        count += elements.get(remove, 0)
        elements[prefix_sum] = 1 + elements.get(prefix_sum, 0)
    print(count)
    return count

arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
findAllSubSum(arr, 3)