#include <stdio.h>

int main(void) {
    float c;
    printf("Suhu (C): ");
    scanf("%f", &c);

    float f = c * 9 / 5 + 32;
    printf("%.1f C = %.1f F\n", c, f);
    return 0;
}