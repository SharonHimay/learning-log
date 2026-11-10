#include <stdio.h>

void tukar(int *a, int *b) {
    int sementara = *a;
    *a = *b;
    *b = sementara;
}

void ringkasan(const float data[], int n, float *kecil, float *besar, float *rata) {
    *kecil = data[0];
    *besar = data[0];
    float total = 0;
    for (int i = 0; i < n; i++) {
        if (data[i] < *kecil) { *kecil = data[i]; }
        if (data[i] > *besar) { *besar = data[i]; }
        total += data[i];
    }
    *rata = total / n;
}

int main(void) {
    int x = 3, y = 7;
    tukar(&x, &y);
    printf("x = %d, y = %d\n", x, y);

    float suhu[] = {28.5f, 30.1f, 27.8f, 31.4f, 29.0f};
    float kecil, besar, rata;
    ringkasan(suhu, 5, &kecil, &besar, &rata);
    printf("Terendah: %.1f, tertinggi: %.1f, rata-rata: %.2f\n", kecil, besar, rata);
    return 0;
}