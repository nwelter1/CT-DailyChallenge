def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1):
            if array[i] > array[i + 1]:
                swap(i, i+1, array)
                isSorted = False
    return array

# Commented code

# helper function to swap (used in many different sorting algos
# to swap in-place)
def swap(i, j, array):
    # location array[i] = value at array[j]
    # location array[j] = value at array[i]
    # swap the value at i for the value at j
    array[i], array[j] = array[j], array[i]

# optimized bubbleSort O(n^2) Time | O(1) Space
def bubbleSort(array):
    # Assume the array is unsorted before the first pass
    isSorted = False
    # while it is not sorted
    while not isSorted:
        # assume that the array is sorted ( if we make no swaps,
        # we will exit the loop after the current pass)
        isSorted = True
        # loop over the whole array
        for i in range(len(array)-1):
            # if the current value is greater than the value
            # to the right, this is out of order, so swap them
            if array[i] > array[i + 1]:
                # call the helper function
                swap(i, i+1, array)
                # if we made any swaps, assume the order has changed
                # somewhere and we'll have to iterate again
                isSorted = False
    # once we pass through the array with no swaps, we'll exit the loop
    # with a sorted array of integers
    return array