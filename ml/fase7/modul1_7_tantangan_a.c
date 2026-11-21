#include <stdio.h>
#include <math.h>

#define N_MASUK 2
#define N_TERSEMBUNYI 4

/* Parameter hasil latihan Keras (jaringan 2-4-1, ReLU), kelas positif: ALARM */
static const float RATA[N_MASUK]    = {26.6680f, 55.6391f};
static const float SIMPANG[N_MASUK] = {10.0817f, 19.8694f};

static const float W1[N_MASUK][N_TERSEMBUNYI] = {
    { 3.7379f, 1.9953f, -4.0407f, 4.0284f},
    { 0.0057f, 0.3895f,  0.1353f, 0.1160f}
};
static const float B1[N_TERSEMBUNYI] = {-1.0618f, 2.9494f, -1.0180f, -1.1710f};
static const float W2[N_TERSEMBUNYI] = {4.3202f, -2.3297f, 3.4305f, 4.0505f};
static const float B2 = -1.2419f;

float peluang_alarm(float suhu, float kelembapan) {
    float x[N_MASUK] = {
        (suhu - RATA[0]) / SIMPANG[0],
        (kelembapan - RATA[1]) / SIMPANG[1]
    };

    float z2 = B2;
    for (int j = 0; j < N_TERSEMBUNYI; j++) {
        float z1 = B1[j];
        for (int i = 0; i < N_MASUK; i++) {
            z1 += x[i] * W1[i][j];
        }
        float a1 = z1 > 0.0f ? z1 : 0.0f;        /* ReLU */
        z2 += a1 * W2[j];
    }
    return 1.0f / (1.0f + expf(-z2));            /* sigmoid */
}

int main(void) {
    float contoh[6][2] = {
        {15.0f, 50.0f}, {27.0f, 50.0f}, {38.0f, 50.0f},
        {21.0f, 60.0f}, {33.5f, 40.0f}, {19.5f, 80.0f}
    };
    for (int i = 0; i < 6; i++) {
        float p = peluang_alarm(contoh[i][0], contoh[i][1]);
        printf("(%.1f, %.0f)  P(ALARM)=%.3f  -> %s\n",
               contoh[i][0], contoh[i][1], p, p >= 0.5f ? "ALARM" : "AMAN");
    }
    return 0;
}