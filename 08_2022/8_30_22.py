def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        for num in range(len(array)-1):
            if array[num] > array[num + 1]:
                swap(num, num+1, array)
                isSorted = False
    return array
