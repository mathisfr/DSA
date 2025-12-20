def sort(dataArray):
    mergeSort(dataArray, 0, len(dataArray)-1)

def mergeSort(dataArray, left, right):
    if (left >= right):
        return

    mid = left + ((right - left) // 2)
    mergeSort(dataArray, left, mid)
    mergeSort(dataArray, mid + 1, right)
    merge(dataArray, left, mid, right)

def merge(dataArray, left, mid, right):
    tempArray = []  #(right - left) + 1

    offsetA = 0
    offsetB = 0
    while (left + offsetA) <= mid and (mid + 1 + offsetB) <= right:
        if (dataArray[left + offsetA] < dataArray[mid + 1 + offsetB]):
            tempArray.append(dataArray[left + offsetA])
            offsetA += 1
        else:
            tempArray.append(dataArray[mid + 1 + offsetB])
            offsetB += 1

    while left + offsetA <= mid:
        tempArray.append(dataArray[left + offsetA])
        offsetA += 1
    while mid + 1 + offsetB <= right:
        tempArray.append(dataArray[mid + 1 + offsetB])
        offsetB += 1

    offset = 0
    while offset <= right - left:
        dataArray[left + offset] = tempArray[offset]
        offset += 1