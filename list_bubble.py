class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


    def __str__(self):
        return self.dataval


class SLinkedList():
    def __init__(self):
        self.headval = Node()

    def remove_last(self):
        tmp = self.headval
        if tmp is None:
            pass
        else:
            while tmp.nextval is not None:  # Jesli istnieje nastepna wartosc po tej
                tmp = tmp.nextval  # Przechodzi do nastepnej wartosci
                if tmp.nextval.nextval is None: #  Dochodzimy do przedostatniego
                    break
            tmp.nextval = None


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


    def get_element(self,n):
        counter = 0
        tmp = self.headval
        while tmp.nextval is not None:
            tmp = tmp.nextval
            counter += 1
            if counter == n:
                return tmp.nextval


def addElement(self, count, val):
    tmp = self.headval
    if count == 0:
        if tmp is None:
            self.headval = Node(val)
        else:
            insert_this = Node(val)
            insert_this.nextval = self.headval
            self.headval = insert_this
    else:
        counter = 0
        while counter < count - 1:  # pętla działa póki counter jest mniejszy niż zdefiniowana pozycja wybranej wartości
            counter += 1
            tmp = tmp.nextval
        insert_this = Node(val)  # tworzy element o zdefiniowanej wartości val
        insert_this.nextval = tmp.nextval  # przypisuje tmp.nextval do nextval nowego elementu
        tmp.nextval = insert_this  # podmienia następujące po tmp wartości (czyli jego nextval) utworzonym elementem

list = SLinkedList()
list.addElement(1,"w")
list.addElement(1,"e")
list.addElement(2,"r")
list.printlist()




