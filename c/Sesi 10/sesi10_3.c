#include <stdio.h>

int main(void) {
    float suhu[] = {26.5f, 27.0f, 28.2f, 29.5f, 31.0f, 32.4f, 33.1f, 32.0f, 30.2f, 28.8f};
    int n = sizeof(suhu) / sizeof(suhu[0]);
    int jam_awal = 8;

    // 1. Tabel
    for (int i = 0; i < n; i++) {
        printf("Jam %02d: %.1f C\n", jam_awal + i, suhu[i]);
    }

    // 2 dan 3. Tertinggi, rata-rata, jumlah di atas 30
    int idx_tertinggi = 0;
    float total = 0;
    int di_atas_30 = 0;

    for (int i = 0; i < n; i++) {
        if (suhu[i] > suhu[idx_tertinggi]) {
            idx_tertinggi = i;
        }
        if (suhu[i] > 30) {
            di_atas_30++;
        }
        total += suhu[i];
    }

    printf("Tertinggi: %.1f pada jam %d\n", suhu[idx_tertinggi], jam_awal + idx_tertinggi);
    printf("Rata-rata: %.2f\n", total / n);
    printf("Jam di atas 30 C: %d\n", di_atas_30);

    // 4. Topik MQTT
    char topik[40];
    int id = 1;
    snprintf(topik, sizeof(topik), "lab/esp32-%02d/suhu", id);
    printf("Topik: %s\n", topik);

    return 0;
}