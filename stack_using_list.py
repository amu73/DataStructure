stack = []
def push():
    """Function for push opertion in Stack
    """

    if len(stack) == n:
        print("Stack is full")

    else:
        item = input("Enter element to push:")
        stack.append(item)
        
def pop():
    """Function for pop operation in stack
    """
    
    if not stack:
        print("Stack is empty.")
        
    else:
        item = stack.pop()
        print("Popped item is",item)
        
def peek():
    """Function to traverse the element
    """
    
    if not stack:
        print("Stack is empty.")
        
    else:
        print(stack)
if __name__ == "__main__":   
    n = int(input("Enter the limit of stack : "))
        
    while True:
        print("select operation : 1.Push 2.Pop 3.Peek  4.Quit")
        choice = int(input())
        
        if choice == 1:
            push()
            
        elif choice == 2:
            pop()
            
        elif choice == 3:
            peek()
            
        elif choice == 4:
            break
        
        else:
            print("Enter correct option")
            