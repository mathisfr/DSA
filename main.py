from sort import bubbleSort
from sort import insertionSort
from sort import mergeSort
from sort import selectionSort
from sort import quickSort

from backtracking import combinaison

from search import binarySearch
from search import depthFirstSearch
from search import breadthFirstSearch

from tree import binaryTree
from graph import graphList

from utils import utils
import sys

# TYPLE CONST
SORTED_ARRAY_CACHE = None 
GRAPH_VALUE_TARGET = 6
BACKTRACKING_COMBINAISON = "123"

def main():

    '''
        VALIDATION ARGS PROGRAM
    '''
    if (len(sys.argv) < 2 or len(sys.argv) > 3):
        print("Wrong command...\n\tpython3 main.py [ARRAY SIZE]\n\tpython3 main.py [ARRAY SIZE] [MAX INT]")
        sys.exit(0)
    if len(sys.argv) == 2:
        randomValueArray = utils.arrayGenerator(int(sys.argv[1]))
    else:
        randomValueArray = utils.arrayGenerator(int(sys.argv[1]), int(sys.argv[2]))
    timer = utils.Timer()



    utils.SECTION = utils.Section.SORT.name
    '''
        SORT ALGORITHMS
    '''
    # PYTHON SORT FUNCTION
    utils.printTitle("PYTHON SORT FUNCTION")
    utils.printArray(randomValueArray)

    sortedArray = randomValueArray.copy()
    timer.setTimer()
    sortedArray.sort()
    timer.getTimer()

    utils.printArray(sortedArray, True)
    SORTED_ARRAY_CACHE = (sortedArray)

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

    root = binaryTree.BinaryTree()
    if (len(sortedArray) > 0):
        timer.setTimer()
        root = binaryTree.BinaryTree(sortedArray[0])
        root.insertArrayOfValue(sortedArray[1:])
        timer.getTimer()

    dataArrayTemp = []
    binaryTree.BinaryTree.sort(root, dataArrayTemp)
    utils.printArray(dataArrayTemp, True)



    utils.SECTION = utils.Section.SEARCH.name
    '''
        SEARCH
    '''
    # BINARY
    utils.printTitle("BINARY SEARCH")
    utils.printArray(SORTED_ARRAY_CACHE, True)

    value = utils.randomValueInArray(SORTED_ARRAY_CACHE)
    print(f"\nSEARCH: {value}")
    timer.setTimer()
    idFind = binarySearch.search(SORTED_ARRAY_CACHE, value)
    timer.getTimer()

    if idFind != None:
        print(f"VALUE FIND: {SORTED_ARRAY_CACHE[idFind]} AT ID: {idFind}")

    # DFS & BFS
    gm = graphList.GraphList(
        [0, 1, 2, 3, 4, 5, 6],
        [
            [1,2,3],
            [0,2,4],
            [6,0,1],
            [0,2,6,5],
            [1,5],
            [4,3],
            [3,2]
        ]
    )
    #gm.debug()
    utils.printTitle("DFS SEARCH")
    print(f"VALUE TARGET {GRAPH_VALUE_TARGET}")
    if depthFirstSearch.search(gm, GRAPH_VALUE_TARGET):
        print(f"VALUE FIND {GRAPH_VALUE_TARGET}")
    utils.printTitle("BFS SEARCH")
    print(f"VALUE TARGET {GRAPH_VALUE_TARGET}")
    if breadthFirstSearch.search(gm, GRAPH_VALUE_TARGET):
        print(f"VALUE FIND {GRAPH_VALUE_TARGET}")


    utils.SECTION = utils.Section.BACKTRACKING.name
    '''
        BACKTRACKING
    '''
    # COMBINAISON
    utils.printTitle("COMBINAISON")
    combinaison.combinaison(BACKTRACKING_COMBINAISON)
    


if __name__ == '__main__':
    main()