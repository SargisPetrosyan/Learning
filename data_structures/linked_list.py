class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value: int) -> None:
        node = Node(value, self.head)
        self.head = node

    def append(self, value: int) -> None:
        itr = self.head

        while itr:
            if itr.next is None:
                itr.next = Node(data=value, next=None)
                return
            itr = itr.next

    def length(self) -> None:
        itr = self.head
        length = 0
        if itr.next is None:
            print("0")

        while itr:
            length += 1
            itr = itr.next

        print(length)

    def insert_at(
        self,
        index: int,
        value: int,
    ) -> None:
        if index == 0:  # Special case: inserting at the beginning
            self.head = Node(value, self.head)
            return

        itr = self.head
        index_number = 0

        while itr:
            if index_number + 1 == index:
                itr.next = Node(value, itr.next)
                return
            index_number += 1
            itr = itr.next
        print("index is invalid.")

    def delete_by_value(self, value):
        itr = self.head

        while itr:
            if itr.next is None:
                print("value doesn't exist in list")
            if itr.data == value:
                self.head = itr.next
                return
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next

    def print(self) -> None:
        if self.head is None:
            print("List is empty")
            return

        itr = self.head
        llist = ""

        while itr:
            llist += str(itr.data) + "-->"
            itr = itr.next
        print(llist)


ll = LinkedList()

ll.insert_at_beginning(value=3)
ll.insert_at_beginning(value=5)
ll.append(6)
ll.append(11)
ll.append(610)
ll.append(8)
ll.insert_at(index=8, value=12345)
ll.delete_by_value(5)
ll.length()
ll.print()
