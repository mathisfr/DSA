class BinaryTree():
    def __init__(self, data: int = 0):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data
    def setParent(self, parent: BinaryTree):
        self.parent = parent
    def setLeft(self, left: BinaryTree):
        self.left = left
    def setRight(self, right: BinaryTree):
        self.right = right
    def insertNode(self, node: BinaryTree):
        if node == None: return
        if node.data <= self.data:
            if self.left == None:
                self.setLeft(node)
            else:
                self.left.insertNode(node)
        else:
            if self.right == None:
                self.setRight(node)
            else:
                self.right.insertNode(node)
        node.setParent(self)
    def insertValue(self, data: int = 0):
        node = BinaryTree(data)
        self.insertNode(node)
    def insertArrayOfValue(self, dataArray):
        for data in dataArray:
            self.insertValue(data)
    def printSort(node: BinaryTree):
        if node == None: return
        BinaryTree.printSort(node.left)
        print(node.data, end=' ')
        BinaryTree.printSort(node.right)
    def sort(node, dataArray):
        if node == None: return
        BinaryTree.sort(node.left, dataArray)
        dataArray.append(node.data)
        BinaryTree.sort(node.right, dataArray)