#include <stdio.h>

int luas(int panjang, int lebar);
float c_ke_f(float c);
float f_ke_c(float f);

int main(void) {
    printf("luas(5, 3) = %d\n", luas(5, 3));
    printf("c_ke_f(100) = %.1f\n", c_ke_f(100));
    printf("f_ke_c(212) = %.1f\n", f_ke_c(212));
    printf("f_ke_c(c_ke_f(-40)) = %.1f\n", f_ke_c(c_ke_f(-40)));
    return 0;
}

int luas(int panjang, int lebar) {
    return panjang * lebar;
}

float c_ke_f(float c) {
    return c * 9 / 5 + 32;
}

float f_ke_c(float f) {
    return (f - 32) * 5 / 9;
}