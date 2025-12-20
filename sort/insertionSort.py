def sort(dataArray):
    for index in range(1, len(dataArray)):
        cursorArray = index
        while cursorArray > 0 and dataArray[cursorArray - 1] > dataArray[cursorArray]:
            dataArray[cursorArray - 1], dataArray[cursorArray] = dataArray[cursorArray], dataArray[cursorArray - 1]
            cursorArray -= 1