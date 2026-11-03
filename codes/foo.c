
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 30
#define MAX 5

// Generate a random number between 0 and MAX
int uniform()
{
    return rand() % (MAX + 1);
}

// Fill A with random values
void generate(int A[])
{
    int i;

    for (i = 0; i < N; i++)
        A[i] = uniform();
}

// Function given in the question
// Counts the number of groups of consecutive equal elements
int foo(int S[], int size)
{
    if (size == 0)
        return 0;

    if (size == 1)
        return 1;

    if (S[0] != S[1])
        return 1 + foo(S + 1, size - 1);

    return foo(S + 1, size - 1);
}

int main()
{
    int A[N];
    int i, result;

    // Start random number generator
    srand(time(NULL));

    // Generate input array
    generate(A);

    printf("Input A:\n");

    for (i = 0; i < N; i++)
        printf("%d ", A[i]);

    // Pass array to foo()
    result = foo(A, N);

    printf("\n\nResult of foo() = %d\n", result);

    return 0;
}

