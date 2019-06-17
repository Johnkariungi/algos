#include<stdio.h>
#include<stdlib.h>
/** two pointers, when slow meets fast */
/** LL Node */
struct Node {
    int data;
    struct Node* next;
};

/** function to find middle of LL */
void printMiddle(struct Node *head) {
    /* start pointers at head */
    struct Node *slow_ptr = head;
    struct Node *fast_ptr = head;

    if (head != NULL) {
        while (fast_ptr != NULL && fast_ptr->next != NULL) {
            fast_ptr = fast_ptr->next->next;
            slow_ptr = slow_ptr->next;
        }
        printf("The middle element is [%d]\n\n", slow_ptr->data);
    }
}

void push(struct Node** head_ref, int new_data) {
    /** allocate node 
     * The malloc() function allocates a block of uninitialized memory and 
     * returns a void pointer to the first byte of the allocated memory block.
    */
    struct  Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    /* put in the data */
    new_node->data = new_data;
    /* link old list off the new node */
    new_node->next = (*head_ref);
    /* move head to point to new node */
    (*head_ref) = new_node;
}
/* utlility print */
void printList(struct Node *ptr) {
    while (ptr != NULL) {
        printf("%d->", ptr->data);
        ptr = ptr->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node* head = NULL;
    int i;

    for (i = 5; i > 0; i--) {
        push(&head, i);
        printList(head);
        printMiddle(head);
    }
    return 0;
}

