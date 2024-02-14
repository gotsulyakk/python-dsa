class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head  # start at the head
        while temp is not None:  # while we are not at the tail
            print(temp.value)  # print the value
            temp = temp.next  # move to the next node

    def append(self, value):
        """Append a node to the end of the list

        1. Create a new node with the value passed to the function
        2. If the linked list is empty:
            a. Set the head to be the new node
            b. Set the tail to be the new node
        3. If the linked list is not empty:
            a. Set the next property on the tail to be that node
        4. Increment the length by 1
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # if the linked list is empty
        if self.length == 0:
            return None

        # if the linked list contains 2 or more items
        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        # if the linked list contained 1 item head and tail still are pointing to that node, so, make it None
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp  # return popped item

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True


if __name__ == "__main__":
    # Create a new Linked List
    ll = LinkedList(1)
    ll.print_list()

    # Append
    ll.append(2)
    ll.print_list()

    # Pop
    popped = ll.pop()
    print("Popped item:", popped.value)
    print("Updated linked list:")
    ll.print_list()

    # Prepend
    value = 5
    print("Prepend", value)
    ll.prepend(value)
    print("Linked List after prepend:")
    ll.print_list()

    # Pop first
    print("Pop first")
    ll.pop_first()
    ll.print_list()

    # Get
    ll.append(54)
    ll.append(109)
    ll.append(6)
    index = 2
    value = ll.get(index)
    print(f"Got value {value.value} on index {index}")

    # Set value
    value = 666
    ll.set_value(index, value)
    print(f"New value of index {index} is {ll.get(index).value}")

    # Insert
    index = 2
    value = 777
    print(f"Insert {value} on index {index}")
    print("Before insert:")
    ll.print_list()
    ll.insert(index, value)
    print("After insert:")
    ll.print_list()
