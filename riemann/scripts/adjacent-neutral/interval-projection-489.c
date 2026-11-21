/* Complete interval Gram of projected columns, endpoints scaled by2^512.
 * Output endpoints scaled by2^1024. Every sum and product is exact.
 * This independently implements the interval dot products in Python's
 * 2048-bit Ball arithmetic: products of512-bit dyadics need no rounding
 * on that finer grid. No analytic estimate or floating operation occurs.
 */
#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

int main(void) {
    size_t n, k;
    if (scanf("%zu %zu", &n, &k)!=2 || !n || !k) return 2;
    mpz_t *lo=malloc(n*k*sizeof(mpz_t));
    mpz_t *hi=malloc(n*k*sizeof(mpz_t));
    if (!lo || !hi) return 3;
    for (size_t i=0; i<n*k; ++i) {
        mpz_init(lo[i]); mpz_init(hi[i]);
        if (!mpz_inp_str(lo[i],stdin,10) || !mpz_inp_str(hi[i],stdin,10)) return 4;
        if (mpz_cmp(lo[i],hi[i])>0) return 5;
    }
    mpz_t terms[4], lower, upper;
    for (int r=0; r<4; ++r) mpz_init(terms[r]);
    mpz_init(lower); mpz_init(upper);
    for (size_t i=0; i<n; ++i) {
        for (size_t j=i; j<n; ++j) {
            mpz_set_ui(lower,0); mpz_set_ui(upper,0);
            for (size_t r=0; r<k; ++r) {
                mpz_mul(terms[0],lo[i*k+r],lo[j*k+r]);
                mpz_mul(terms[1],lo[i*k+r],hi[j*k+r]);
                mpz_mul(terms[2],hi[i*k+r],lo[j*k+r]);
                mpz_mul(terms[3],hi[i*k+r],hi[j*k+r]);
                int a=0,b=0;
                for (int t=1; t<4; ++t) {
                    if (mpz_cmp(terms[t],terms[a])<0) a=t;
                    if (mpz_cmp(terms[t],terms[b])>0) b=t;
                }
                mpz_add(lower,lower,terms[a]); mpz_add(upper,upper,terms[b]);
            }
            mpz_out_str(stdout,10,lower); putchar(' ');
            mpz_out_str(stdout,10,upper); putchar('\n');
        }
        fflush(stdout);
    }
    for (int r=0; r<4; ++r) mpz_clear(terms[r]);
    mpz_clear(lower); mpz_clear(upper);
    for (size_t i=0; i<n*k; ++i) { mpz_clear(lo[i]); mpz_clear(hi[i]); }
    free(lo); free(hi);
    return 0;
}
