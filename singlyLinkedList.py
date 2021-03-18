class Node:
    """Creating a Node class and Function to initialize the Node Object,
        
    """
    def __init__(self,data):
        """ assign data and initialize next as null

        Parameters
        ----------
        data : int
            here i have taken integer data type 
        """
        self.data = data
        self.next = None

class LinkedList:
    """Creating a Linked List class and function to initialize the linked list object
    """
    def __init__(self):
        """ Function to initialize head
        """
        self.head = None

    def display(self):
        """ Display functions prints the content of Linked List
            starting from head
        """
        if self.head is None:
            print("LinkedList is empty")               
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end = " ")
                n = n.next

    def add_beg(self,data):
        """ This function add the data in the begining of the linked list

        Parameters
        ----------
        data : int
            here we have taken integer data type
        """
        new_node = Node(data) 
        new_node.next = self.head  
        self.head = new_node

    def add_end(self,data):
        """This function add the data at the end of the linked list

        Parameters
        ----------
        data : int
             integer data type
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:  
            n = self.head             
            while n.next is not None:      
                n = n.next
            n.next = new_node

    def add_after(self,data,item):
        """Insert a new node after the given node

        Parameters
        ----------
        data : int
            integer data type
        item : int
            integer data type
        """
        n = self.head
        while n is not None:
            if item == n.data:
                break
            n = n.next
        if n is None:
            print("Node is not Present.")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self,data,item):
        """Insert a new node before the given node

        Parameters
        ----------
        data : int
                integer data type
        item : int
            integer data type
        """
        if self.head is None:
            print("LL is empty.")
            return
        if self.head.data == item:
            new_node = Node(data)  
            new_node.next = self.head  
            self.head = new_node    
            return
        n = self.head
        while n.next is not None:
            if n.next.data == item:
                break
            n = n.next
        if n.next is None:
                print("Node is not Present.")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def insertion_in_EmptyLL(self,data):
        """ Inserting data in an empty Linked list

        Parameters
        ----------
        data : int
                integer type
        """
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            print("LinkedList is not empty")


    def delete_from_beg(self):
        """delete the first occurence of node in linked list 
        """
        if self.head is None:
            print("Linked List is Empty")
        else:
            self.head = self.head.next

    def delete_from_end(self):
        """delete the last occurence of node in linked list 
        """
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def delete_by_value(self,item):
        """Delete the node by given value 
           Search for the node to be deleted, keep track of the 
           previous node as we need to change 'prev.next' 

        Parameters
        ----------
        item : int
            integer data type
        """
        if self.head is None:
            print("Linked List is Empty")
            return
        if item == self.head.data:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if item == n.next.data:
                break
            n = n.next
        if n.next is None:
                print("Node is not Present.")
        else:
            n.next = n.next.next


if __name__ == "__main__":
    
    LL1 = LinkedList()

    #Insertion at Beg
    LL1.add_beg(10)
    LL1.add_beg(20)

    #insertion at end
    LL1.add_end(30)
    LL1.add_end(40)

    #insertion after node
    LL1.add_after(50,40)

    #insertion before node
    LL1.add_before(0,10)
    LL1.add_before(453,90)

    #insertion_in_EmptyLL
    LL1.insertion_in_EmptyLL(56)

    #delete_from_beg(self)
    LL1.delete_from_beg()
    LL1.delete_from_beg()

    #delete_from_end
    LL1.delete_from_end()

    #delete_by_value
    LL1.delete_by_value(30)
    LL1.delete_by_value(20)

    #Display The Linked List
    LL1.display()