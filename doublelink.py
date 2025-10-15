# Doubly Linked List in Python

# Node class
class Node:
    def __init__(self, data):
        self.data = data      # Data field
        self.prev = None      # Pointer to previous node
        self.next = None      # Pointer to next node


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:   # Empty list
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Delete a node
    def delete_node(self, key):
        temp = self.head

        # Empty list
        if temp is None:
            print("List is empty.")
            return

        # Deleting head node
        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            temp = None
            return

        # Searching for the node
        while temp and temp.data != key:
            temp = temp.next

        # If node not found
        if temp is None:
            print("Node not found.")
            return

        # Unlink the node
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        temp = None

    # Forward traversal
    def display_forward(self):
        temp = self.head
        print("Forward Traversal:", end=" ")
        while temp:
            print(temp.data, end=" ")
            last = temp
            temp = temp.next
        print()

    # Backward traversal
    def display_backward(self):
        temp = self.head
        if temp is None:
            print("List is empty.")
            return
        while temp.next:
            temp = temp.next
        print("Backward Traversal:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()


# --- Example Usage ---
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_beginning(5)
dll.display_forward()
dll.display_backward()

dll.delete_node(20)
dll.display_forward()
dll.display_backward()
