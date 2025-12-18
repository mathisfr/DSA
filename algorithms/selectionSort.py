class SmallestNode:
    def __init__(self):
        self.smallestValue = 0
        self.smallestItemIndex = 0

    def setSmallest(self, dataArray, sindex):
        self.smallestValue = dataArray[sindex]
        self.smallestItemIndex = sindex

    def getSmallestValue(self):
        return self.smallestValue
    def getSmallestItemIndex(self):
        return self.smallestItemIndex

def sort(dataArray):
    smallest = SmallestNode()
    for index in range(len(dataArray)):
        hasSmallest = False
        smallest.setSmallest(dataArray, index)
        for offset in range(index + 1, len(dataArray)):
            if dataArray[offset] < smallest.getSmallestValue():
                smallest.setSmallest(dataArray, offset)
                hasSmallest = True
        if hasSmallest:
            dataArray[index], dataArray[smallest.getSmallestItemIndex()] =  dataArray[smallest.getSmallestItemIndex()], dataArray[index]
            