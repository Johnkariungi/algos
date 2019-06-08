class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # initialize the head
    def __init__(self):
        self.head = None

    # insert new node at beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # delete first occurance of key in linked list with ref to head of the list and key
    def deleteNode(self, key):
        # store head node
        temp = self.head 

		# If head node itself holds the key to be deleted 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return

		# Search for the key to be deleted, keep track of the 
		# previous node as we need to change 'prev.next' 
        while(temp is not None): 
            if temp.data == key: 
                break
            prev = temp 
            temp = temp.next

		# if key was not present in linked list 
        if(temp == None): 
            return

		# Unlink the node from linked list 
        prev.next = temp.next

        temp = None

    # print linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(" %d" %(temp.data), end=" "),
            temp = temp.next

# main
if __name__=='__main__':
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)

    print('Created Linkedlist: ', end=" "), llist.printList()
    number_to_delete = 7
    llist.deleteNode(number_to_delete)
    print('\nLinked list after deletion of (%d): '%number_to_delete, end=" "), llist.printList()

