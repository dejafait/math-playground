#include <gmp.h>
#include <stddef.h>
size_t abi_item(int i) { switch(i) {
case 0:return sizeof(__mpz_struct); case 1:return sizeof(__mpq_struct);
case 2:return offsetof(__mpz_struct,_mp_alloc); case 3:return offsetof(__mpz_struct,_mp_size);
case 4:return offsetof(__mpz_struct,_mp_d); case 5:return offsetof(__mpq_struct,_mp_num);
case 6:return offsetof(__mpq_struct,_mp_den); case 7:return sizeof(mp_limb_t)*8;
case 8:return __GNU_MP_VERSION; case 9:return __GNU_MP_VERSION_MINOR;
case 10:return __GNU_MP_VERSION_PATCHLEVEL; default:return 0; }}
const char* linked_version(void) {return gmp_version;}
