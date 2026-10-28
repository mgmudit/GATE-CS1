#include <stdio.h>
#include <stdlib.h>
#include "List/libs/listgen.h"

int find(int query, sadish *list) {
    sadish *curr = list;
    while (curr != NULL) {
        if ((int)curr->data == query) return 1;
        curr = curr->next;
    }
    return 0;
}

int main() {
    // Open data file with safety check
    FILE *fp = fopen("numbers.dat", "r");
    if (fp == NULL) {
        perror("Error opening numbers.dat");
        return 1;
    }

    // Load data sequentially into vectors v1 and v2 from the same file stream
    sadish *v1 = loadVec(fp, 9);
    sadish *v2 = loadVec(fp, 7);
    fclose(fp);

    // Ensure vectors loaded successfully
    if (v1 == NULL || v2 == NULL) {
        fprintf(stderr, "Error: Failed to load vectors from numbers.dat\n");
        return 1;
    }

    // Handle deletion if the head node itself matches items in v2
    while (v1 != NULL && find((int)v1->data, v2)) {
        v1 = v1->next;
    }

    // Perform operations directly on v1 (L1) for subsequent nodes
    sadish *ptr1 = v1;
    int query;
    while (ptr1 != NULL && ptr1->next != NULL) {
        query = (int)ptr1->next->data;
        if (find(query, v2))
            ptr1->next = ptr1->next->next;
        else
            ptr1 = ptr1->next;
    }

    // Count remaining nodes
    int count = 0;
    sadish *curr = v1;
    while (curr != NULL) {
        count++;
        curr = curr->next;
    }

    // Allocate vectors into avyuh at the end for matrix representation with allocation checks
    avyuh *mat = (avyuh *)malloc(sizeof(avyuh));
    if (mat == NULL) {
        perror("Memory allocation failed");
        return 1;
    }
    mat->vector = v1;
    
    mat->next = (avyuh *)malloc(sizeof(avyuh));
    if (mat->next == NULL) {
        perror("Memory allocation failed");
        return 1;
    }
    mat->next->vector = v2;
    mat->next->next = NULL;

    printf("Number of nodes in L1 after execution: %d\n", count);
    printList(mat);

    return 0;
}
