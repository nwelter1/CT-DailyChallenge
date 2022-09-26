def findBounds(arr, target):
    low = -1
    hi = -1
    for i in range(len(arr)):
        if arr[i] == target:
            if low == -1:
                low = i
            hi = i
    if low == -1:
        return [-1,-1]
    return [low, hi]

print(findBounds([0,0,0,2,2,3,3,3,4,5],-1) )
