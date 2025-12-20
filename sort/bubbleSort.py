def sort(dataArray):
    lastElementIndex = len(dataArray) - 1
    nextElement = 1
    swapped = True
    
    for substractLenSearch in range(lastElementIndex):
        if swapped == False: break
        swapped = False
        for element in range(lastElementIndex - substractLenSearch):
            if dataArray[element] <= dataArray[element + nextElement]:
                continue
            dataArray[element], dataArray[element + nextElement] = dataArray[element + nextElement], dataArray[element]
            swapped = True
    
    return