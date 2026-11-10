#include <stdio.h>

int main (void) {
    int n, total = 0, jumlah_ganjil = 0;

    printf ("n = ");
    scanf ("%d", &n);

    for (int i = 1; i <= n; i++) {
        total += 1;
        if (i % 2 == 0) {
            continue;
        }
        jumlah_ganjil += i;
    }
    printf ("Jumlah semua: %d\n", total);
    printf ("Jumlah ganjil: %d\n", jumlah_ganjil);
    return 0;
}