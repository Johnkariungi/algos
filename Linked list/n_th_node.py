# find the Nth node from the end, method 1 - using the len of the LL [complexity O(n)]
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    # initialize head
    def __init__(self):
        self.head = None

    # method create node & make LL
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head # make the previous node the head
        self.head = new_node # make the new_node head

    # get nth node from last of LL
    def printNthFromLast(self, n):
        temp = self.head  # assign head to varaible
        length = 0 # initialize len
        while temp is not None:
            temp = temp.next # 1 node
            # increase the value of len
            length += 1
        # print count
        if n > length:
            print('Location is greater than the lenth of LL')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next  # traverse from the head, print all the data
        print("the n'th node is:", temp.data)
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ") # start with the head
            temp = temp.next # print the next node


# driver code
if __name__=='__main__':
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(35)
    print('the created linked list is:', end=" "),llist.printList()
    nth_node = 4
    print()
    llist.printNthFromLast(nth_node)


    
 


    