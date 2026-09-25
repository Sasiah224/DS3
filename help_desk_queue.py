# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def print_queue(self):
        current = self.front
        while current:
            print(current.data)
            current = current.next
    


def run_help_desk():
    # Create an instance of the Queue class
    help_desk_queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            help_desk_queue.enqueue(name)
            print(f"{name} added to the queue.")
            
            
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            value = help_desk_queue.dequeue()
            if value is not None:
                print(f"Helping customer: {value}")
            else:
                print("No customers in the queue.")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            val = help_desk_queue.peek()
            if val is not None:
                print(f"Next customer to be helped: {val}")
            else:
                print("No customers in the queue.")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            help_desk_queue.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
