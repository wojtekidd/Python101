class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

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

    def get_element(self, n):
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
                self.headval = None
            else:
                insert_this = None
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
        iterator = self.headval
        while iterator is not None:
            iterator = iterator.nextval
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

    def queue_push(self, val):
        tmp = Node(val)
        tmp.nextval = self.headval
        self.headval = tmp

    def queue_pull(self):
        tmp = self.headval
        if tmp is None:
            pass
        else:
            while tmp.nextval is not None:  # Jesli istnieje nastepna wartosc po tej
                tmp = tmp.nextval  # Przechodzi do nastepnej wartosci
                if tmp.nextval.nextval is None: #  Dochodzimy do przedostatniego
                    break
            tmp.nextval = None

    def stack_push(self, val):
        tmp = Node(val)
        tmp.nextval = self.headval
        self.headval = tmp

    # def stack_pull(self):
    #     tmp = self.headval
    #     tmp.nextval = self.headval




list = SLinkedList()
list.append(8)
list.append(7)
list.append(6)
list.print_list()
print("*********")
list.queue_push(3)
list.print_list()
print("*********")
list.queue_pull()
list.print_list()