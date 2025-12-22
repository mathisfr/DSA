from graph import graphList

def search(graph: graphList, value):
    currentIndex = 0
    stack = []
    visited = []
    stack.append(currentIndex)
    while stack: 
        currentIndex = stack.pop()
        print(f"POP INDEX: {currentIndex}")
        if graph.vertex[currentIndex] == value : return True
        visited.append(currentIndex)
        for childIndex in range(len(graph.data[currentIndex])):
            child = graph.data[currentIndex][childIndex]
            if child not in stack and child not in visited:
                stack.append(child)
        print(stack)
    return False