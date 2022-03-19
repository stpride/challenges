/**
 * ---------------------------------------------------------------------------------------
 *
 *  Title:      Add two numbers
 *
 *  Link:       https://leetcode.com/problems/add-two-numbers/
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

struct ListNode {
    int val;
    struct ListNode *next;
};

void printit(struct ListNode *q) {
    if( q != NULL ) {
        printf("%d\n",q->val);
        printit(q->next);
        free(q->next);
    }
}

struct ListNode * recurse(struct ListNode *p, struct ListNode *l1, struct ListNode *l2){
    if( l1 != NULL && l2 != NULL ) {
        p = (struct ListNode *) malloc(sizeof(struct ListNode));
        p->val = l1->val + l2->val;
        p->next = recurse(p->next, l1->next, l2->next);
    }
    return p;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *p;
    return recurse(p,l1,l2);
}

struct ListNode *push(struct ListNode *q, int i) {
    if( q != NULL )
        q->next = push(q->next,i);
    else {
        q = (struct ListNode *) malloc(sizeof(struct ListNode));
        q->val = i;
    }
    return q;
}

int main(int argc, char **argv)
{
    if( argc != 3 ) {
        printf("usage: linked_list_add_numbers <list1> <list2>\n\n");
        printf("  <list1>,<list2>  - comma-delimited list of integers (e.g., \"2,4,3\")\n");
        return -1;
    }

    struct ListNode *l1 = NULL;
    char *p = strtok(*(++argv),",");
    while( p != NULL ) {
        l1 = push(l1,atoi(p));
        p = strtok(NULL,",");
    }

    struct ListNode *l2 = NULL;
    char *r = strtok(*(++argv),",");
    while( r != NULL ) {
        l2 = push(l2,atoi(r));
        r = strtok(NULL,",");
    }

    struct ListNode *q = addTwoNumbers(l1,l2);
    printit(q);

    return 0;
}
