def search(dataArray, value):
    return binarySearch(dataArray, value, 0, len(dataArray) - 1)
def binarySearch(dataArray, value, l, r):
    if l > r:
        return None
    mid = l + ((r - l) // 2)
    if dataArray[mid] == value :
        return mid
    if  value > dataArray[mid]:
        return binarySearch(dataArray, value, mid + 1, r)
    else:
        return binarySearch(dataArray, value, l, mid)