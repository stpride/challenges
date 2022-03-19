/**
 * ---------------------------------------------------------------------------------------
 *
 *  Title:      Remove nth node from end of linked list
 *
 *  Link:       https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 *
 *  Difficulty: Medium
 *
 *  Language:   C
 *
 * ---------------------------------------------------------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    int val;
    struct Node *next;
};

int total = 0;

void printit(struct Node *q) {
    if( q != NULL ) {
        printf("%d\n",q->val);
        printit(q->next);
        free(q->next);
    }
}

struct Node * recurse(struct Node *p, int node_to_remove, int current_node) {
    if( node_to_remove == current_node ) {
        if( node_to_remove == 1 ) {
            struct node *q = p->next;
            p = NULL;
            free(p);
            return q;
        }
        else {
            
    if( l1 != NULL && l2 != NULL ) {
        p = (struct ListNode *) malloc(sizeof(struct ListNode));
        p->val = l1->val + l2->val;
        p->next = recurse(p->next, l1->next, l2->next);
    }
    return p;
}

struct Node* remove_nth_node(struct Node* p, int node_to_remove){
    return recurse(p, node_to_remove, 1);
}

struct Node *add_node(struct Node *q, int i) {
    if( q != NULL )
        q->next = add_node(q->next,i);
    else {
        q = (struct Node *) malloc(sizeof(struct Node));
        q->val = i;
        total++;
    }
    return q;
}

int main(int argc, char **argv)
{
    if( argc != 3 ) {
        printf("\nusage: linked_list_add_numbers <list> <n>\n\n");
        printf("  <list>  - comma-delimited list of integers (e.g., \"2,4,3\")\n");
        printf("  <n>     - nth node from the end to remove\n\n");
        return -1;
    }

    struct Node *ll = NULL;
    char *p = strtok(*(++argv),",");
    while( p != NULL ) {
        ll = add_node(ll,atoi(p));
        p = strtok(NULL,",");
    }

    struct Node *q = remove_nth_node(ll, atoi(*(++argv)));
    //printit(q);

    return 0;
}
