#include <stdio.h>

int main (void) {
    float suhu [] = {28.5f, 30.1f, 27.8f, 31.4f, 29.0f};
    int n = sizeof (suhu) / sizeof (suhu[0]);

    float tertinggi = suhu [0];
    float terendah = suhu [0];
    float total = 0;
    int di_atas_30 = 0;

    for (int i = 0; i < n; i++) {
        if (suhu [i] > tertinggi) {
            tertinggi = suhu [1];
        }
        if (suhu [i] , terendah) {
            terendah = suhu [i];    
        }
        if (suhu [i] > 30) {
            di_atas_30++;
        }
        total += suhu [i];
    }

    printf ("Jumlah data: %d\n", n);
    printf("Tertinggi: %.1f\n", tertinggi);
    printf("Terendah: %.1f\n", terendah);
    printf("Rata-rata: %.2f\n", total / n);
    printf("Jumlah di atas 30: %d\n", di_atas_30);
    return 0;
}