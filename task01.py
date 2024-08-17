# Task 1
# You need to develop a program that simulates the receipt and processing of requests: 
# the program should automatically generate new requests (identified by a unique number or other data),
# add them to the queue, and then sequentially remove them from the queue for "processing",
# thereby simulating the work of a service center.

from queue import Queue
import random

# Creating the queue
queue = Queue()

# Creating a set to store unique id values
unique_ids = set()


# Generates a new request and adds it to the queue
def generate_request():
    while True:
        request_id = random.randint(1, 10000)
        if request_id not in unique_ids:
            unique_ids.add(request_id)
            print(f"Generated request with ID: {request_id}")
            queue.put(request_id)
            break


# Processes requests from the queue
def process_request():
    if not queue.empty():
        request_id = queue.get()
        print(f"Processing request ID: {request_id}")
        unique_ids.remove(request_id)
    else:
        print("The queue is empty. No requests to process.")


# Main program loop
def main():
    print("Welcome to the service centre!")

    while True:
        command = input("Enter 'generate' to create a new request, 'process' to process a request, or 'close' to exit: ")
        if command.lower() == "close":
            print("Goodbye!")
            break
        elif command.lower() == "generate":
            generate_request()
        elif command.lower() == "process":
            process_request()
        else:
            print("Invalid command. Please enter 'generate', 'process', or 'close'.")

if __name__ == "__main__":
    main()