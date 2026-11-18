#include <stdio.h>
#include <math.h>

/* Regresi linear: suhu CPU dari beban CPU (%) dan suhu ruangan (C) */
float prediksi_suhu_cpu(float beban, float suhu_ruang) {
    return 12.7433f + 0.2816f * beban + 0.9288f * suhu_ruang;
}

/* Regresi logistik: peluang status PANAS dari suhu (C) dan kelembapan (%) */
float peluang_panas(float suhu, float kelembapan) {
    float z = -17.2295f + 0.6278f * suhu - 0.0298f * kelembapan;
    return 1.0f / (1.0f + expf(-z));
}

int main(void) {
    printf("Regresi linear:\n");
    printf("(0, 27)   -> %.2f\n", prediksi_suhu_cpu(0, 27));
    printf("(50, 27)  -> %.2f\n", prediksi_suhu_cpu(50, 27));
    printf("(100, 27) -> %.2f\n", prediksi_suhu_cpu(100, 27));
    printf("(50, 33)  -> %.2f\n", prediksi_suhu_cpu(50, 33));
    printf("(80, 30)  -> %.2f\n", prediksi_suhu_cpu(80, 30));

    printf("\nRegresi logistik:\n");
    float uji[][2] = {{25, 60}, {29, 60}, {30, 60}, {32, 60}, {35, 60}, {30, 80}};
    for (int i = 0; i < 6; i++) {
        float p = peluang_panas(uji[i][0], uji[i][1]);
        printf("suhu=%.0f kelembapan=%.0f  P(PANAS)=%.3f  -> %s\n",
               uji[i][0], uji[i][1], p, p >= 0.5f ? "PANAS" : "NORMAL");
    }
    return 0;
}