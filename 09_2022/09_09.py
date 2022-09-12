def func(arr):
    length = len(arr)
    res = [1 for i in range(length)]
    temp = 1
    #left side multiply
    for i in range(length):
        res[i] = temp
        temp *= arr[i]
    temp = 1
    #right side multiply
    for i in range(length-1, -1, -1):
        res[i] *= temp
        temp *= arr[i]
    return res