from algorithms import bubbleSort
from algorithms import insertionSort
from algorithms import mergeSort
from algorithms import selectionSort
from algorithms import quickSort
from tree import binaryTree
from utils import utils
import sys

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Wrong command...\n\tpython3 main.py [ARRAY SIZE]\n\tpython3 main.py [ARRAY SIZE] [MAX INT]")
        sys.exit(0)

    if len(sys.argv) == 2:
        randomValueArray = utils.arrayGenerator(int(sys.argv[1]))
    else:
        randomValueArray = utils.arrayGenerator(int(sys.argv[1]), int(sys.argv[2]))
    timer = utils.Timer()

    # PYTHON SORT FUNCTION
    utils.printTitle("PYTHON SORT FUNCTION")
    utils.printArray(randomValueArray)

    sortedArray = randomValueArray.copy()
    timer.setTimer()
    sortedArray.sort()
    timer.getTimer()

    utils.printArray(sortedArray, True)

    # BUBBLE
    utils.printTitle("BUBBLE SORT")
    utils.printArray(randomValueArray)

    sortedArray = randomValueArray.copy()
    timer.getTimerFunctionExecution(bubbleSort.sort, sortedArray)
    utils.printArray(sortedArray, True)

    # INSERTION
    utils.printTitle("INSERTION SORT")
    utils.printArray(randomValueArray)

    sortedArray = randomValueArray.copy()
    timer.getTimerFunctionExecution(insertionSort.sort, sortedArray)

    utils.printArray(sortedArray, True)

    # MERGE
    utils.printTitle("MERGE SORT")
    utils.printArray(randomValueArray)

    sortedArray = randomValueArray.copy()
    timer.getTimerFunctionExecution(mergeSort.sort, sortedArray)

    utils.printArray(sortedArray, True)

    # SELECTION
    utils.printTitle("SELECTION SORT")
    utils.printArray(randomValueArray)

    sortedArray = randomValueArray.copy()
    timer.getTimerFunctionExecution(selectionSort.sort, sortedArray)

    utils.printArray(sortedArray, True)

    # QUICK
    utils.printTitle("QUICK SORT")
    utils.printArray(randomValueArray)

    sortedArray = randomValueArray.copy()
    timer.getTimerFunctionExecution(quickSort.sort, sortedArray)

    utils.printArray(sortedArray, True)

    # BINARY TREE
    utils.printTitle("BINARY TREE")
    utils.printArray(randomValueArray)
    
    sortedArray = randomValueArray.copy()

    timer.setTimer()
    root = binaryTree.BinaryTree(sortedArray[0])
    root.insertArrayOfValue(sortedArray[1:])
    timer.getTimer()

    dataArrayTemp = []
    binaryTree.BinaryTree.getSortedArray(root, dataArrayTemp)
    utils.printArray(dataArrayTemp, True)

if __name__ == '__main__':
    main()