#include <stdio.h>

int main (void) {
    int a, b;

    printf ("Bilangan pertama: ");
    scanf ("%d", &a);
    printf ("Bilangan kedua: ");
    scanf ("%d", &b);

    if (a % 2 == 0) {
        printf ("Genap\n");
    } else {
        printf ("Ganjil\n");
    }

    if (b != 0) {
        printf ("%d / %d = %d\n", a, b, a / b);
        printf ("%d %% %d = %d\n", a, b, a % b);
    } else {
        printf ("Tidak bisa dibagi nol\n");
    }
    return 0;
}