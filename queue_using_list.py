queue = []
def enqueue():
    """Function to insert element in Queue
    """
     if len(queue) == n:
        print("List is full")
     else:
        element = input("Enter element to insert : ")
        queue.append(element)
        print(element," is added to Queue")


def dequeue():
    """Function to remove element in queue
    """
    if not queue:
        print("Queue is Empty")
    else:
        deleted = queue.pop(0) 
        print(deleted ,"is removed from Queue")

def display():
    """Function to print the datas in the queue
    """
    if not queue:
        print("Queue is Empty")
    else:
        print(queue)

if __name__ == "__main__":

    n = int(input("Enter the limit of stack: "))
    while True:
        print("Enter your Choice1")
        print("1.Enqueue,2.Dequeue,3.Display,4.Exit")
        choice = int(input())
        if choice == 1:
            enqueue()
        elif choice == 2:
            dequeue()
        elif choice == 3:
            display()
        elif choice == 4:
            break
        else:
            print("Please enter correct operation.")