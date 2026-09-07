#include <stdio.h>
struct node
{
    int data;
    struct node *next;
};

typedef struct node Node;

int main()
{
    Node a, b, c, d;

    a.data = 1;
    a.next = &b;
}