from graph import graphList
from collections import deque

def search(graph: graphList, value):
    currentIndex = 0
    queue = deque()
    visited = []
    queue.append(currentIndex)
    while queue: 
        currentIndex = queue.popleft()
        print(f"POPLEFT INDEX: {currentIndex}")
        if graph.vertex[currentIndex] == value : return True
        visited.append(currentIndex)
        for childIndex in range(len(graph.data[currentIndex])):
            child = graph.data[currentIndex][childIndex]
            if child not in queue and child not in visited:
                queue.append(child)
        print(queue)
    return False