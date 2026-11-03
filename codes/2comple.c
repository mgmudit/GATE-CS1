
#include <stdio.h>

void print_binary(unsigned long long value, int bits)
{
    // Print each bit from the most significant to the least significant
    for (int i = bits - 1; i >= 0; i--)
    {
        printf("%d", (int)((value >> i) & 1));

        // Add a space after every group of 4 bits
        if (i > 0 && i % 4 == 0)
            printf(" ");
    }
}

void twos_complement(long long number, int bits)
{
    // Keep only the lowest 8 or 16 bits of the number
    unsigned long long value = (unsigned long long)number;
    unsigned long long mask = (1ULL << bits) - 1;
    value &= mask;

    printf("\n%d-bit representation: ", bits);
    print_binary(value, bits);
    printf("\n");
}

int main(void)
{
    long long number;

    printf("Enter an integer: ");

    // Read and validate the user's input
    if (scanf("%lld", &number) != 1)
    {
        printf("Invalid input.\n");
        return 1;
    }

    // Check whether the number fits in a signed 16-bit integer
    if (number < -32768 || number > 32767)
    {
        printf("Number is outside the signed 16-bit range.\n");
        return 1;
    }

    // Warn if the number cannot be represented as a signed 8-bit integer
    if (number < -128 || number > 127)
        printf("Warning: number is outside the signed 8-bit range.\n");

    // Display the 2's complement bit patterns
    twos_complement(number, 8);
    twos_complement(number, 16);

    return 0;
}

