# Merging overlapping sub intervals

def mergingIntervals(intervals):
    ans = [intervals[0]]
    print(ans)
    index = 0
    for i in range(1, len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]

        if start <= ans[index][1]:
            ans[index][1] = max(ans[index][1], end)
        else:
            ans.append(intervals[i])
            index += 1
    print(ans)
    return ans

intervals = [[1,3],[2,6],[8,10],[15,18]]
mergingIntervals(intervals)
        
    