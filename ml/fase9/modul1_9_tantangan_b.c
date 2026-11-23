#include <stdio.h>
#include <math.h>

#define N 100
#define FS 50.0f

typedef struct {
    float rata, simpang, minimum, maksimum;
} StatSumbu;

static StatSumbu hitung_statistik(const float *x, int n) {
    StatSumbu s;
    float jumlah = 0.0f;
    s.minimum = x[0];
    s.maksimum = x[0];
    for (int i = 0; i < n; i++) {
        jumlah += x[i];
        if (x[i] < s.minimum) s.minimum = x[i];
        if (x[i] > s.maksimum) s.maksimum = x[i];
    }
    s.rata = jumlah / n;
    float jumlah_kuadrat = 0.0f;
    for (int i = 0; i < n; i++) {
        float d = x[i] - s.rata;
        jumlah_kuadrat += d * d;
    }
    s.simpang = sqrtf(jumlah_kuadrat / n);          /* simpangan baku populasi (sama dengan numpy) */
    return s;
}

/* Frekuensi dominan lewat DFT langsung (tanpa DC), O(N^2) cukup untuk N kecil */
static void frekuensi_dominan(const float *x, int n, float rata, float *frek, float *amplitudo) {
    float terbaik = 0.0f;
    int idx = 1;
    for (int k = 1; k <= n / 2; k++) {
        float re = 0.0f, im = 0.0f;
        for (int i = 0; i < n; i++) {
            float sudut = 2.0f * (float)M_PI * k * i / n;
            re += (x[i] - rata) * cosf(sudut);
            im -= (x[i] - rata) * sinf(sudut);
        }
        float besar = sqrtf(re * re + im * im);
        if (besar > terbaik) {
            terbaik = besar;
            idx = k;
        }
    }
    *frek = idx * FS / n;
    *amplitudo = terbaik / n;
}

static void cetak_fitur(const char *nama, float a[N][3]) {
    float sumbu[3][N], mag[N];
    for (int i = 0; i < N; i++) {
        for (int s = 0; s < 3; s++) sumbu[s][i] = a[i][s];
        mag[i] = sqrtf(a[i][0] * a[i][0] + a[i][1] * a[i][1] + a[i][2] * a[i][2]);
    }
    printf("%s\n", nama);
    const char *label[3] = {"ax", "ay", "az"};
    StatSumbu st[3];
    for (int s = 0; s < 3; s++) {
        st[s] = hitung_statistik(sumbu[s], N);
        printf("  %s: mean=%.4f std=%.4f min=%.4f max=%.4f\n", label[s],
               st[s].rata, st[s].simpang, st[s].minimum, st[s].maksimum);
    }
    StatSumbu sm = hitung_statistik(mag, N);
    printf("  mag: mean=%.4f std=%.4f\n", sm.rata, sm.simpang);
    float frek, amp;
    frekuensi_dominan(sumbu[2], N, st[2].rata, &frek, &amp);
    printf("  frek_dom=%.2f Hz  amp_dom=%.4f\n", frek, amp);
}

int main(void) {
    static float jalan[N][3], diam[N][3];
    for (int i = 0; i < N; i++) {
        float t = i / FS;
        float osc = sinf(2.0f * (float)M_PI * 2.0f * t);
        jalan[i][0] = 0.6f * 0.4f * osc;
        jalan[i][1] = 0.0f;
        jalan[i][2] = 1.0f + 0.4f * osc;
        diam[i][0] = 0.0f;
        diam[i][1] = 0.0f;
        diam[i][2] = 1.0f + 0.05f * sinf(2.0f * (float)M_PI * 7.0f * t);
    }
    cetak_fitur("Jendela A (osilasi 2 Hz)", jalan);
    cetak_fitur("Jendela B (hampir diam)", diam);
    return 0;
}