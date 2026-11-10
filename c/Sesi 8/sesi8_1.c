#include <stdio.h>

int main() {
    char inisial;
    int umur;

    printf("Inisial: ");
    scanf(" %c", &inisial);
    printf("Umur: ");
    scanf("%d", &umur);

    printf("Inisial: %c, umur: %d\n", inisial, umur);
    return 0;
}