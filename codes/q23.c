#include <stdio.h>

int main() {
    // Set initial state: Q3 Q2 Q1 Q0 = 0 0 0 0
    int Q3 = 0, Q2 = 0, Q1 = 0, Q0 = 0;
    
    // Store initial values to identify when the full loop completes
    int init_Q3 = Q3, init_Q2 = Q2, init_Q1 = Q1, init_Q0 = Q0;
    int clock = 0;

    // Print table header
    printf("+-------+---------------+---------------+---------------+\n");
    printf("| Clock | Current State |   FF Inputs   |  Next State   |\n");
    printf("|       |  Q3 Q2 Q1 Q0  |  D3 D2 D1 D0  |  Q3 Q2 Q1 Q0  |\n");
    printf("+-------+---------------+---------------+---------------+\n");

    do {
        // Calculate the flip-flop inputs based on feedback connections:
        // D3 = Q2, D2 = Q1, D1 = Q0, D0 = ~Q3
        int D3 = Q2;
        int D2 = Q1;
        int D1 = Q0;
        int D0 = !Q3;

        // Print row values before updating variables
        printf("|  %-4d |   %d  %d  %d  %d   |   %d  %d  %d  %d   |   %d  %d  %d  %d   |\n", 
               clock, Q3, Q2, Q1, Q0, D3, D2, D1, D0, D3, D2, D1, D0);

        // Update values concurrently at the clock edge
        Q3 = D3;
        Q2 = D2;
        Q1 = D1;
        Q0 = D0;

        clock++;
    } while (!(Q3 == init_Q3 && Q2 == init_Q2 && Q1 == init_Q1 && Q0 == init_Q0));

    // Print bottom border
    printf("+-------+---------------+---------------+---------------+\n");
    printf("\nThe circuit returns to the initial state after %d distinct states.\n", clock);

    return 0;
}

