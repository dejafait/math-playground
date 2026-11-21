#include <stddef.h>
#include <stdio.h>
#include <mpfr.h>

int main(void) {
    mpfr_t x;
    mpfr_init2(x, 384);
    mpfr_set_ui(x, 1, MPFR_RNDD);
    printf("{\"version\":\"%s\",\"header_version\":\"%s\","
           "\"sizes\":[%zu,%zu,%zu,%zu,%zu],"
           "\"offsets\":[%zu,%zu,%zu,%zu],"
           "\"rounding\":[%d,%d],\"precision\":%ld,"
           "\"long_size\":%zu,\"int_size\":%zu,\"ulong_size\":%zu}\n",
           mpfr_get_version(), MPFR_VERSION_STRING,
           sizeof(__mpfr_struct), sizeof(mpfr_prec_t), sizeof(mpfr_sign_t),
           sizeof(mpfr_exp_t), sizeof(mp_limb_t),
           offsetof(__mpfr_struct, _mpfr_prec),
           offsetof(__mpfr_struct, _mpfr_sign),
           offsetof(__mpfr_struct, _mpfr_exp),
           offsetof(__mpfr_struct, _mpfr_d),
           MPFR_RNDD, MPFR_RNDU, (long)mpfr_get_prec(x),
           sizeof(long), sizeof(int), sizeof(unsigned long));
    mpfr_clear(x);
    return 0;
}
