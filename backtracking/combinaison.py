def combinaison(dataArray):
    stack = []
    backtracking(dataArray, 0, stack)


def backtracking(dataArray, depth, stack):
    if depth >= len(dataArray): return
    for index in range(0, len(dataArray)):
        if dataArray[index] in stack : continue
        stack.append(dataArray[index])
        if depth == len(dataArray) - 1:
            printStack(stack)
        backtracking(dataArray, depth + 1, stack)
        stack.pop()

def printStack(stack):
    for value in stack:
        print(value, sep="-" , end='')
    print('')

'''
def backtracking(dataArray, currentIndex):
    if currentIndex >= len(dataArray): return
    print(dataArray[currentIndex], end=' ')
    backtracking(dataArray, currentIndex + 1)
'''