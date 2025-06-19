# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None



    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    # Delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty.")
        else:
            self.head = self.head.next




    # Delete from end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty.")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty.")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")





# Menu-driven Model Code
def menu():
    obj = LinkedList()
    while True:
        print("\n===== Singly Linked List Menu =====")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete from Beginning")
        print("4. Delete from End")
        print("5. Display")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            data = int(input("Enter value to insert at beginning: "))
            obj.insert_at_beginning(data)
        elif choice == '2':
            data = int(input("Enter value to insert at end: "))
            obj.insert_at_end(data)
        elif choice == '3':
            obj.delete_from_beginning()
        elif choice == '4':
            obj.delete_from_end()
        elif choice == '5':
            obj.display()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
menu()
