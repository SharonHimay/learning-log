#include <stdio.h>
#include <math.h>

int main(void) {
    float dbm;
    printf("Daya (dBm): ");
    scanf("%f", &dbm);

    float mw = pow(10, dbm / 10);
    printf("%.1f dBm = %f mW\n", dbm, mw);
    printf("Dibulatkan: %.2f mW\n", mw);
    return 0;
}