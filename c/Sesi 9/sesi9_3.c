#include <stdio.h>

int main(void) {
    float suhu, kelembapan;
    int hasil, c;

    // Minta suhu sampai valid
    while (1) {
        printf("Suhu (C): ");
        hasil = scanf("%f", &suhu);

        if (hasil == EOF) {
            return 1;
        }
        if (hasil != 1) {
            printf("Harus berupa angka.\n");
            while ((c = getchar()) != '\n' && c != EOF) { }
            continue;
        }
        if (suhu >= -10 && suhu <= 80) {
            break;
        }
        printf("Di luar rentang -10 sampai 80.\n");
    }

    // Minta kelembapan sampai valid
    while (1) {
        printf("Kelembapan (%%): ");
        hasil = scanf("%f", &kelembapan);

        if (hasil == EOF) {
            return 1;
        }
        if (hasil != 1) {
            printf("Harus berupa angka.\n");
            while ((c = getchar()) != '\n' && c != EOF) { }
            continue;
        }
        if (kelembapan >= 0 && kelembapan <= 100) {
            break;
        }
        printf("Di luar rentang 0 sampai 100.\n");
    }

    printf("Suhu %.1f C, kelembapan %.1f%%\n", suhu, kelembapan);

    if (suhu > 35 || kelembapan > 80) {
        printf("Status: BAHAYA\n");
    } else if (suhu >= 28 && suhu <= 35) {
        printf("Status: WASPADA\n");
    } else {
        printf("Status: AMAN\n");
    }
    return 0;
}