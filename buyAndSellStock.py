def buyAndSell(arr):
    min_ = arr[0]
    profit = 0
    for i in range(len(arr)):
        cost = arr[i] - min_
        profit = max(profit, cost)
        min_ = min(min_, arr[i])
    print(profit)
    return profit

arr = [7,1,5,3,6,4]
buyAndSell(arr)