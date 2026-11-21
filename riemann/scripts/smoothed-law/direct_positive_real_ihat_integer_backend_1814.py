"""Optional local GMP gcd acceleration for independent replay only.

Integer/rational identities and the evaluator are unchanged. The ctypes ABI
matches the installed gmp.h struct and mpz function declarations. Inputs and
outputs cross the boundary as complete base16 integers, never floats.
"""
import ctypes as C
import ctypes.util
import hashlib
import math
from pathlib import Path

ORIGINAL_GCD = math.gcd


class MPZ(C.Structure):
    _fields_ = [("allocated", C.c_int), ("size", C.c_int), ("limbs", C.c_void_p)]


def enable():
    name = ctypes.util.find_library("gmp")
    if not name:
        return {"backend": "Python integer gcd", "accelerated": False}
    library = C.CDLL(name)
    init, clear = getattr(library, "__gmpz_init"), getattr(library, "__gmpz_clear")
    set_string = getattr(library, "__gmpz_set_str")
    get_string = getattr(library, "__gmpz_get_str")
    gcd_function = getattr(library, "__gmpz_gcd")
    pointer = C.POINTER(MPZ)
    init.argtypes = clear.argtypes = [pointer]
    init.restype = clear.restype = None
    set_string.argtypes, set_string.restype = [pointer, C.c_char_p, C.c_int], C.c_int
    get_string.argtypes, get_string.restype = [C.c_void_p, C.c_int, pointer], C.c_void_p
    gcd_function.argtypes, gcd_function.restype = [pointer, pointer, pointer], None

    def binary_gcd(a, b):
        if max(abs(a).bit_length(), abs(b).bit_length()) < 4096:
            return ORIGINAL_GCD(a, b)
        x, y, z = MPZ(), MPZ(), MPZ()
        for value in (x, y, z):
            init(C.byref(value))
        try:
            if set_string(C.byref(x), format(abs(a), "x").encode(), 16) != 0:
                raise ValueError("GMP integer input A rejected")
            if set_string(C.byref(y), format(abs(b), "x").encode(), 16) != 0:
                raise ValueError("GMP integer input B rejected")
            gcd_function(C.byref(z), C.byref(x), C.byref(y))
            buffer = C.create_string_buffer(max(abs(a).bit_length(), abs(b).bit_length())//4+3)
            get_string(buffer, 16, C.byref(z))
            return int(buffer.value, 16)
        finally:
            for value in (x, y, z):
                clear(C.byref(value))

    def exact_gcd(*values):
        result = 0
        for value in values:
            result = binary_gcd(result, value)
        return result

    pairs = [(0, 0), (0, -(2**8192+1)), (2**8192-1, 2**6144-1),
             (-(2**16384+3), 2**12288+7), (48, -18)]
    for a, b in pairs:
        if exact_gcd(a, b) != ORIGINAL_GCD(a, b):
            raise ArithmeticError("GMP bridge disagrees with Python gcd")
    math.gcd = exact_gcd
    header = Path("/opt/homebrew/include/gmp.h")
    return {"backend": "Python exact integers/Fraction; local GMP gcd only",
        "accelerated": True, "library": name,
        "library_sha256": hashlib.sha256(Path(name).read_bytes()).hexdigest(),
        "header": str(header), "header_sha256": hashlib.sha256(header.read_bytes()).hexdigest(),
        "bridge_comparisons_with_original_gcd": len(pairs),
        "scope": "Verifier only; no evaluator, rounding or operation-ledger change"}
