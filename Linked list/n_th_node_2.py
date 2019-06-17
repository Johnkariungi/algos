# method 2 using two pointers space time complexity[O(n)]
class Node:
   def __init__(self, new_data):
       self.data = new_data
       self.next = None

class LinkedList:
    def __init__(self): # initialize head
        self.head = None

    def push(self, new_data): # add to the end
        new_node = Node(new_data)
        # next node to head
        new_node.next = self.head
        self.head = new_node

    def printNthFromLast(self, n):
        # initialize ptrs
        main_ptr = self.head
        ref_ptr = self.head

        count = 0
        if (self.head is not None):
            while (count < n):
                if (ref_ptr is None):
                    print(f"{n} is greater than the no. pf nodes in the list")
                    return
                ref_ptr = ref_ptr.next # move ptr
                count += 1 # increase the count
        while (ref_ptr is not None):
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
        print(f"Node no.{n} from last is {main_ptr.data}")
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(35)
    print('the created linked list is:', end=" "),llist.printList()
    print()
    llist.printNthFromLast(4)

