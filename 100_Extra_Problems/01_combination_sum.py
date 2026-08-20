def combinationSum(candidates, target):
    output = []
    for i in range(len(candidates)):
        k = 1
        val = 1
        while val > 0:
            val = target - candidates[i] * k
            if val in candidates and val >= candidates[i]:
                output.append([candidates[i]] * k + [val])
                break
            elif val == 0:
                output.append([candidates[i]] * k)
                
            k += 1
    return output
candidates = [2,3,5]
target = 8
combinationSum(candidates, target)