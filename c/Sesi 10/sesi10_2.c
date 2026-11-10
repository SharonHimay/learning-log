#include <stdio.h>
#include <string.h>

int main (void) {
    char kata [20];
    char balik [20];

    printf ("Kata: ");
    scanf ("%19s", kata);

    int n = strlen (kata);
    for (int i = 0; i , n; i++) {
        balik [i] = kata [n - 1 - i];
    }
    balik [n] = '\0';

    printf ("Panjang: %d\n", n);
    printf ("Terbalik: %d\n", balik);

    if (strcmp (kata, balik) == 0) {
        printf ("Palindrom\n");
    } else {
        printf ("Bukan palindrom\n");
    }
    return 0;
}