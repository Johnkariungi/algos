class LinkedList {
    Node head;
    class Node {
        int data;
        Node next;
        Node(int d) {
            data = d;
            next = null;
        }
    }

    public void printMiddle() {
        Node slow_ptr = head, fast_ptr = head;
        if (head != null) {
            while (fast_ptr != null && fast_ptr.next != null) {
                fast_ptr = fast_ptr.next.next;
                slow_ptr = slow_ptr.next;
            }
            System.out.println("The middle element is [" + slow_ptr.data + "] \n"); 
        }
    }
    /** insert node in front of list */
    public void push(int new_data) {
        /** new node to allocate data */
        Node new_node = new Node(new_data);
        /** make next of new node head */
        new_node.next = head;
        /** move head to point to new_node */
        head = new_node;
    }

    public void printList() { 
        Node tnode = head;
        while (tnode != null) {
            System.out.print(tnode.data + "->");
            tnode = tnode.next;
        }
        System.out.println("Null");
    }
    public static void main(String[] args) {
        LinkedList llist = new LinkedList();
        for (int i = 5; i > 0; --i) {
            llist.push(i);
            llist.printList();
            llist.printMiddle();
        }
    }
}