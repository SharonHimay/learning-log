#include <stdio.h>

int main(void) {
    int a[] = {1, 2, 3, 4, 5};
    int n = sizeof(a) / sizeof(a[0]);

    for (int i = 0; i < n / 2; i++) {
        int sementara = a[i];
        a[i] = a[n - 1 - i];
        a[n - 1 - i] = sementara;
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}