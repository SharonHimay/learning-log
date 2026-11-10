#include <stdio.h>
#include <math.h>

int main(void) {
    int pilihan;
    float nilai;

    printf("Menu:\n");
    printf("1 = Celsius ke Fahrenheit\n");
    printf("2 = Fahrenheit ke Celsius\n");
    printf("3 = dBm ke mW\n");
    printf("Pilihan: ");
    scanf("%d", &pilihan);

    switch (pilihan) {
        case 1:
            printf("Suhu (C): ");
            scanf("%f", &nilai);
            printf("%.1f C = %.1f F\n", nilai, nilai * 9 / 5 + 32);
            break;
        case 2:
            printf("Suhu (F): ");
            scanf("%f", &nilai);
            printf("%.1f F = %.1f C\n", nilai, (nilai - 32) * 5 / 9);
            break;
        case 3:
            printf("Daya (dBm): ");
            scanf("%f", &nilai);
            printf("%.1f dBm = %f mW\n", nilai, pow(10, nilai / 10));
            break;
        default:
            printf("Pilihan tidak valid\n");
            break;
    }
    return 0;
}