#include <stdio.h>
#include <string.h>

typedef struct {
    char nama[20];
    double suhu;
    double lembap;
} Sensor;

const char *status(Sensor s) {
    if (s.suhu > 35 || s.lembap > 80) {
        return "BAHAYA";
    } else if (s.suhu >= 28 && s.suhu <= 35) {
        return "WASPADA";
    } else {
        return "AMAN";
    }
}

void hitung_status(const Sensor s[], int n, int *aman, int *waspada, int *bahaya) {
    *aman = 0;
    *waspada = 0;
    *bahaya = 0;

    for (int i = 0; i < n; i++) {
        const char *st = status(s[i]);
        if (strcmp(st, "AMAN") == 0) {
            (*aman)++;
        } else if (strcmp(st, "WASPADA") == 0) {
            (*waspada)++;
        } else if (strcmp(st, "BAHAYA") == 0) {
            (*bahaya)++;
        }
    }
}

int main() {
    Sensor data[3] = {
        {"A", 25, 50},
        {"B", 30, 50},
        {"C", 40, 50}
    };

    int a, w, b;
    hitung_status(data, 3, &a, &w, &b);

    printf("aman = %d, waspada = %d, bahaya = %d\n", a, w, b);
    return 0;
}