class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


    def __str__(self):
        return self.dataval


class SLinkedList():
    def __init__(self):
        self.headval = None

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
        tmp = self.headval
        if tmp is None:
            self.headval = Node(dataval)
        else:
            while tmp.nextval is not None:
                tmp = tmp.nextval
            tmp.nextval = Node(dataval)

    def print_list(self):
        tmp = self.headval
        if tmp is None:
            print("List is empty")
        else:
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


    def sort_list(self):
        current_node = self.headval
        if current_node.dataval > current_node.nextval.dataval:
            tmp = current_node.nextval
            current_node.nextval = current_node.nextval.nextval
            tmp.nextval = current_node
            self.headval = tmp
            current_node = self.headval
        while current_node.nextval.nextval is not None:
            if current_node.nextval.dataval > current_node.nextval.nextval.dataval:
                temp = current_node.nextval
                current_node.nextval = current_node.nextval.nextval
                temp.nextval = temp.nextval.nextval
                current_node.nextval.nextval = temp
            current_node = current_node.nextval


list = SLinkedList()
list.append(1)
list.append(0)
list.addElement(0,67)
list.append(19)
list.append(88)
list.append(85)
list.append(213)
list.append(34)
list.sort_list()
list.print_list()