#include <stdio.h>
#include <time.h>

int mcd(int a, int b) {
    if (b == 0) return a;
    return mcd(b, a % b);
}

int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    clock_t inicio = clock();
    int resultado = mcd(a, b);
    clock_t fin = clock();

    printf("MCD(%d, %d) = %d\n", a, b, resultado);
    printf("Tiempo: %f segundos\n", (double)(fin - inicio) / CLOCKS_PER_SEC);
    return 0;
}
