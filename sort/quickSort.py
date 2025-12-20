def sort(dataArray):
    quicksort(dataArray, 0, len(dataArray))
    return

def quicksort(dataArray, l, r):
    if (l >= r): return

    pivot = l + ((r - l) // 2)
    pivotValue = dataArray[pivot]
    index_l = l
    index_r = r - 1
    while index_l <= index_r:
        while dataArray[index_l] < pivotValue:
            index_l += 1
        while dataArray[index_r] > pivotValue:
            index_r -= 1
        dataArray[index_l], dataArray[index_r] = dataArray[index_r], dataArray[index_l]
        index_l += 1
        index_r -= 1
    quicksort(dataArray, l, index_r + 1)
    quicksort(dataArray, index_l, r)

    