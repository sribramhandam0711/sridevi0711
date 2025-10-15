# Node class to store data and pointer
class Node:
    def __init__(self, data):
        self.data = data      # Data field
        self.next = None      # Pointer to next node


# LinkedList class to handle operations
class LinkedList:
    def __init__(self):
        self.head = None      # Initialize empty list

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"{data} inserted at beginning.")

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"{data} inserted as first node.")
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        print(f"{data} inserted at end.")

    # Delete a node by value
    def delete_node(self, key):
        temp = self.head

        # If head node holds the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                print(f"{key} deleted from list.")
                return

        # Search for key to delete
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # Key not present
        if temp is None:
            print(f"{key} not found in list.")
            return

        # Unlink node from list
        prev.next = temp.next
        temp = None
        print(f"{key} deleted from list.")

    # Search for an element
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                print(f"{key} found in list.")
                return True
            current = current.next
        print(f"{key} not found in list.")
        return False

    # Display the linked list
    def display(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("\n--- Singly Linked List Operations ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete a Node")
        print("4. Search an Element")
        print("5. Display List")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            data = int(input("Enter data: "))
            ll.insert_at_beginning(data)

        elif choice == 2:
            data = int(input("Enter data: "))
            ll.insert_at_end(data)

        elif choice == 3:
            key = int(input("Enter value to delete: "))
            ll.delete_node(key)

        elif choice == 4:
            key = int(input("Enter value to search: "))
            ll.search(key)

        elif choice == 5:
            ll.display()

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter between 1-6.")
