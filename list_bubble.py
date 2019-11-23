class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

    def __str__(self):
        return self.dataval


class SLinkedList:
    def __init__(self):
        self.headval = Node()

    def remove(selfself, dataval=None):
        pass

    def append(self, dataval=None):
        tmp = self.headval  # Pointing at the first Node
        if tmp is None:
            self.headval = Node(dataval)
        else:
            while tmp.nextval is not None:
                tmp = tmp.nextval
            tmp.nextval = Node(dataval)

    def printlist(self):
        tmp = self.headval
        if tmp.nextval is None:
            print("The list is empty")
        else:
            tmp = tmp.nextval
            while tmp is not None:
                print(tmp.dataval)
                tmp = tmp.nextval


list = SLinkedList()
#list.headval = Node("1")
list.append("1")
list.printlist()



