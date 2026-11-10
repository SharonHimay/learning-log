#include <stdio.h>

int main(void) {
    int a, b;
    printf("Bilangan pertama: ");
    scanf("%d", &a);
    printf("Bilangan kedua: ");
    scanf("%d", &b);

    printf("Pembagian bulat: %d\n", a / b);
    printf("Pembagian desimal: %.2f\n", (float)a / b);
    printf("Sisa bagi: %d\n", a % b);
    return 0;
}