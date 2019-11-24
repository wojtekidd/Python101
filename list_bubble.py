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
        iterator = self.headval
        while iterator.nextval is not None:
            current = self.headval  # current jest 'zerowany' na headvalu
            while current.nextval.nextval is not None:
                if current.nextval.dataval > current.nextval.nextval.dataval:
                    temp = current.nextval  # przypisanie wartości tymczasowej do nextval
                    current.nextval = current.nextval.nextval  # pierwsza zamiana
                    temp.nextval = temp.nextval.nextval  # druga zamiana
                    current.nextval.nextval = temp  # trzecia zamiana
                current = current.nextval  # przejście pętli
            iterator = iterator.nextval


list = SLinkedList()
list.append(27)
list.append(19)
list.append(88)
list.append(85)
list.append(213)
list.append(34)
list.sort_list()
list.print_list()



