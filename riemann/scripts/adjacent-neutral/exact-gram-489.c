/* Exact upper-triangular integer Gram products. No floating arithmetic.
 * Input: N K, followed by N rows, each with K integers a then K integers b.
 * Output: N(N+1)/2 lines sum_k a[i,k] b[j,k], i<=j.
 * The Python caller proves symmetry from the power-log moment functional.
 * Build as documented by full-matrix-enclosure-489.py; use installed GMP.
 */
#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

int main(void) {
    size_t n, k;
    if (scanf("%zu %zu", &n, &k) != 2 || !n || !k) return 2;
    mpz_t *a = malloc(n*k*sizeof(mpz_t));
    mpz_t *b = malloc(n*k*sizeof(mpz_t));
    if (!a || !b) return 3;
    for (size_t i=0; i<n*k; ++i) { mpz_init(a[i]); mpz_init(b[i]); }
    for (size_t i=0; i<n; ++i) {
        for (size_t j=0; j<k; ++j)
            if (!mpz_inp_str(a[i*k+j], stdin, 10)) return 4;
        for (size_t j=0; j<k; ++j)
            if (!mpz_inp_str(b[i*k+j], stdin, 10)) return 5;
    }
    mpz_t value; mpz_init(value);
    for (size_t i=0; i<n; ++i) {
        for (size_t j=i; j<n; ++j) {
            mpz_set_ui(value, 0);
            for (size_t r=0; r<k; ++r)
                mpz_addmul(value, a[i*k+r], b[j*k+r]);
            mpz_out_str(stdout, 10, value); putchar('\n');
        }
        fflush(stdout);
    }
    mpz_clear(value);
    for (size_t i=0; i<n*k; ++i) { mpz_clear(a[i]); mpz_clear(b[i]); }
    free(a); free(b);
    return 0;
}
