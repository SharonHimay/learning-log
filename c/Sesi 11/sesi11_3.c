#include <stdio.h>

typedef struct {
    char id[16];
    float suhu;
    float kelembapan;
} Sensor;

const char *status(const Sensor *s) {
    if (s->suhu > 35 || s->kelembapan > 80) {
        return "BAHAYA";
    } else if (s->suhu >= 28 && s->suhu <= 35) {
        return "WASPADA";
    }
    return "AMAN";
}

float rata_suhu(const Sensor s[], int n) {
    float total = 0;
    for (int i = 0; i < n; i++) {
        total += s[i].suhu;
    }
    return total / n;
}

void naikkan_suhu(Sensor *s, float delta) {
    s->suhu += delta;
}

void cetak(const Sensor *s) {
    printf("%s: %.1f C, %.1f %%, %s\n", s->id, s->suhu, s->kelembapan, status(s));
}

int main(void) {
    Sensor sensors[3] = {
        {"ESP32-01", 25.0f, 50.0f},
        {"ESP32-02", 33.2f, 58.0f},
        {"ESP32-03", 38.0f, 85.0f}
    };

    for (int i = 0; i < 3; i++) {
        cetak(&sensors[i]);
    }
    printf("Rata-rata suhu: %.2f\n", rata_suhu(sensors, 3));

    naikkan_suhu(&sensors[0], 5.0f);
    cetak(&sensors[0]);
    return 0;
}