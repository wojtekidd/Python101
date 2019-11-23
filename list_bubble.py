class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def append(self, dataval=None):
        tmp = self.headval
        while tmp.nextval is not None:
            tmp = tmp.nextval
        tmp.nextval = Node(dataval)

list = SLinkedList()  # 1
node1 = Node("a")  # 2
list.headval = node1  # 3
node2 = Node("b")  # 4
node1.nextval = node2  # 5

tmp = list.headval



