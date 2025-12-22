class GraphList:
    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.data = []
        for vertexId in range(len(vertex)):
            self.data.append([])
            for edgeId in range(len(edge[vertexId])):
                self.data[vertexId].append(edge[vertexId][edgeId])
    def debug(self):
        for vertexId in range(len(self.data)):
            print(f'[{self.vertex[vertexId]}]:', end=' ')
            for edgeId in range(len(self.data[vertexId])):
                print(f'{self.data[vertexId][edgeId]}', end=' ')
            print(f'')