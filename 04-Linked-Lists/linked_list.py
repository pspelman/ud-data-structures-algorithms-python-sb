class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.__dict__)


class LinkedList:

    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        print(f"Creating new node vor value {value}")
        new_node = Node(value)
        print(f"Attempting to append {value}")
        # check if there is no head
        # if there is no head, this node is the head
        # if there IS a head, iterate to the end of the list
        append_success = False
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            append_success = True
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            append_success = True

        print(f"After appending {value}:\nHEAD: {self.head}\nTAIL: {self.tail}\nLENGTH: {self.length}")

    def get(self, index):
        # quick return if the index is out of bounds
        pass

    def set_value(self, index, value):
        # quick return if the index is out of bounds
        pass

    def pop(self) -> Node | None:
        # TODO: decrement length by 1
        # if AFTER popping, the length is 0, make sure head and tail point to None
        pass

    def prepend(self, value):
        # if the length is 0, this node becomes the head and tail
        # if the length is greater than 0, this node becomes the head
        # TODO: don't forget to increment the length by 1

        pass

    def __repr__(self) -> str:
        print("Printing linked")
        return "Linked List"


linked_list = LinkedList(10)
linked_list.append(5)
linked_list.append(7)
