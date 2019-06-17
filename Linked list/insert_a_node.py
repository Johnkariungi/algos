# Node class
class Node:
    # function to initislize the node object
    def __init__(self, data):
        self.data = data # assign the data
        self.next = None # initalize next as null

# Linked list class contains Node object
class LinkedList:
    # function to initialize the linked list object
    def __init__(self):
        self.head = None

    # insert new node at the beginning
    def push(self, new_data):
        # allocate new node and put in the data
        new_node = Node(new_data)
        # make next of new node as head
        new_node.next = self.head
        # move head to point to new node
        self.head = new_node

    # append new node at the end
    def append(self, new_data):
        # create new node, put in the data and set as none
        new_node = Node(new_data)
        # if linked list is empty, make new node as head
        if self.head is None:
            self.head = new_node
            return
        # else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
        # change the next of the last node
        last.next = new_node

    # insert new node after given prev_node
    def insertAfter(slef, prev_node, new_data):
        # check if the given prev_node exists
        if prev_node is None:
            print('The given previous node must inLinkedList.')
            return
        # create new node & put in data
        new_node = Node(new_data)
        # make next to new node as next of prev_node
        new_node.next = prev_node.next
        # make next of prev_node as new_node
        prev_node.next = new_node

    # print linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

# execute code
if __name__=='__main__':
    # start with an empty list
    llist = LinkedList()
    # insert 6, 6->None
    llist.append(6)
    # insert 7 at beginning, 7->6->None
    llist.push(7)
    # insert 1 at beginning, 1->7->6->None
    llist.push(1)
    # append to the end of the LL, 1->7->6->4->None
    llist.append(4)
    # insert 8 after 7, 1->7->8->6->4->None
    llist.insertAfter(llist.head.next, 8)

    # print('Created linked list is:', end=" "), llist.printList()
    print('Created linked list is:' , end=" "), f"{llist.printList()}"
    
    