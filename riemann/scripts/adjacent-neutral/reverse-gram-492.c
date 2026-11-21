/* Audit only: same documented input, reverse summation, separate mul/add.
 * Output upper triangle in the original lexicographic row order. GMP is
 * shared with step489; this is not an independent integer library. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <gmp.h>
int main(void) {
    size_t n,k;
    if(scanf("%zu %zu",&n,&k)!=2 || !n || !k || n>SIZE_MAX/k) return 2;
    size_t count=n*k;
    if(count>SIZE_MAX/sizeof(mpz_t)) return 3;
    mpz_t *a=malloc(count*sizeof(mpz_t)),*b=malloc(count*sizeof(mpz_t));
    if(!a || !b) return 4;
    for(size_t i=0;i<count;i++){mpz_init(a[i]);mpz_init(b[i]);}
    for(size_t row=0;row<n;row++) {
        for(size_t c=0;c<k;c++) if(!mpz_inp_str(a[row*k+c],stdin,10)) return 5;
        for(size_t c=0;c<k;c++) if(!mpz_inp_str(b[row*k+c],stdin,10)) return 6;
    }
    int ch; do {ch=getchar();} while(ch==' ' || ch=='\n' || ch=='\r' || ch=='\t');
    if(ch!=EOF) return 7;
    mpz_t total,term;mpz_init(total);mpz_init(term);
    for(size_t i=0;i<n;i++) {
        for(size_t j=i;j<n;j++) {
            mpz_set_ui(total,0);
            for(size_t c=k;c-->0;){
                mpz_mul(term,b[j*k+c],a[i*k+c]);
                mpz_add(total,term,total);
            }
            mpz_out_str(stdout,10,total);putchar('\n');
        }
        fflush(stdout);
    }
    mpz_clear(total);mpz_clear(term);
    for(size_t i=0;i<count;i++){mpz_clear(a[i]);mpz_clear(b[i]);}
    free(a);free(b);return 0;
}
