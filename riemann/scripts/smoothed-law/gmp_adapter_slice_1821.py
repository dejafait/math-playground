"""Bounded GMP adapter check for the unchanged C033z arithmetic seam.

This does not run the C033y/C033z evaluator. It checks unified construction,
saved-value decoding, arithmetic, and lossless encoding on large rationals,
then compares one unchanged quotient instruction slice with Fraction.
"""
from __future__ import annotations

import ctypes as C
import ctypes.util
import ast
from fractions import Fraction
import hashlib
import json
from pathlib import Path


class MPZ(C.Structure):
    _fields_ = [("allocated", C.c_int), ("size", C.c_int), ("limbs", C.c_void_p)]


class MPQ(C.Structure):
    _fields_ = [("numerator", MPZ), ("denominator", MPZ)]


class GMPBackend:
    def __init__(self):
        name = ctypes.util.find_library("gmp")
        if not name:
            raise RuntimeError("GMP shared library not found")
        self.lib = C.CDLL(name)
        self._bind()
        self.library = name

    def _bind(self):
        pz, pq = C.POINTER(MPZ), C.POINTER(MPQ)
        def bind(name, args, result=None):
            fn = getattr(self.lib, "__gmp" + name)
            fn.argtypes, fn.restype = args, result
            return fn
        self.mpq_init = bind("q_init", [pq])
        self.mpq_clear = bind("q_clear", [pq])
        self.mpq_set = bind("q_set", [pq, pq])
        self.mpq_set_str = bind("q_set_str", [pq, C.c_char_p, C.c_int], C.c_int)
        self.mpq_canonicalize = bind("q_canonicalize", [pq])
        self.mpq_add = bind("q_add", [pq, pq, pq])
        self.mpq_sub = bind("q_sub", [pq, pq, pq])
        self.mpq_mul = bind("q_mul", [pq, pq, pq])
        self.mpq_div = bind("q_div", [pq, pq, pq])
        self.mpq_cmp = bind("q_cmp", [pq, pq], C.c_int)
        self.mpz_init = bind("z_init", [pz])
        self.mpz_clear = bind("z_clear", [pz])
        self.mpz_set_str = bind("z_set_str", [pz, C.c_char_p, C.c_int], C.c_int)
        self.mpz_get_str = bind("z_get_str", [C.c_void_p, C.c_int, pz], C.c_void_p)
        self.mpz_sizeinbase = bind("z_sizeinbase", [pz, C.c_int], C.c_size_t)
        self.mpq_get_num = bind("q_get_num", [pz, pq])
        self.mpq_get_den = bind("q_get_den", [pz, pq])

    def from_ints(self, n, d=1):
        n, d = int(n), int(d)
        if d == 0:
            raise ZeroDivisionError("rational denominator is zero")
        q = MPQ()
        self.mpq_init(C.byref(q))
        try:
            # mpq_set_str accepts base 16 and this transfer has no word-size cap.
            text = (format(n, "x") + "/" + format(d, "x")).encode("ascii")
            if self.mpq_set_str(C.byref(q), text, 16) != 0:
                raise ValueError("GMP rejected rational input")
            self.mpq_canonicalize(C.byref(q))
            return GMPQ._owned(self, q)
        except BaseException:
            self.mpq_clear(C.byref(q))
            raise

    def copy(self, other):
        q = MPQ()
        self.mpq_init(C.byref(q))
        self.mpq_set(C.byref(q), C.byref(other._q))
        return GMPQ._owned(self, q)

    def binary(self, op, a, b):
        q = MPQ()
        self.mpq_init(C.byref(q))
        try:
            op(C.byref(q), C.byref(a._q), C.byref(b._q))
            return GMPQ._owned(self, q)
        except BaseException:
            self.mpq_clear(C.byref(q))
            raise

    def integer(self, z):
        x = MPZ()
        self.mpz_init(C.byref(x))
        try:
            if self.mpz_set_str(C.byref(x), format(int(z), "x").encode("ascii"), 16) != 0:
                raise ValueError("GMP rejected integer input")
            nbytes = self.mpz_sizeinbase(C.byref(x), 16) + 3
            buf = C.create_string_buffer(nbytes)
            if not self.mpz_get_str(buf, 16, C.byref(x)):
                raise RuntimeError("GMP integer output failed")
            return int(buf.value, 16)
        finally:
            self.mpz_clear(C.byref(x))

    def parts(self, value):
        n, d = MPZ(), MPZ()
        self.mpz_init(C.byref(n)); self.mpz_init(C.byref(d))
        try:
            self.mpq_get_num(C.byref(n), C.byref(value._q))
            self.mpq_get_den(C.byref(d), C.byref(value._q))
            return self.integer_from_mpz(n), self.integer_from_mpz(d)
        finally:
            self.mpz_clear(C.byref(n)); self.mpz_clear(C.byref(d))

    def integer_from_mpz(self, x):
        nbytes = self.mpz_sizeinbase(C.byref(x), 16) + 3
        buf = C.create_string_buffer(nbytes)
        if not self.mpz_get_str(buf, 16, C.byref(x)):
            raise RuntimeError("GMP integer output failed")
        return int(buf.value, 16)


BACKEND = GMPBackend()


class GMPQ:
    __slots__ = ("backend", "_q", "_closed")

    def __init__(self, numerator=0, denominator=None):
        if isinstance(numerator, GMPQ):
            if denominator is not None:
                raise TypeError("two-argument construction from GMPQ")
            self.backend = numerator.backend
            copied = self.backend.copy(numerator)
            self._q = copied._take()
            self._closed = False
            return
        if isinstance(numerator, Fraction):
            if denominator is not None:
                raise TypeError("two-argument construction from Fraction")
            numerator, denominator = numerator.numerator, numerator.denominator
        elif isinstance(numerator, str) and denominator is None:
            parsed = Fraction(numerator)
            numerator, denominator = parsed.numerator, parsed.denominator
        if denominator is None:
            denominator = 1
        self.backend, self._q = BACKEND, BACKEND.from_ints(numerator, denominator)._take()
        self._closed = False

    @classmethod
    def _owned(cls, backend, q):
        obj = object.__new__(cls)
        obj.backend, obj._q, obj._closed = backend, q, False
        return obj

    def _take(self):
        q = self._q
        self._closed = True
        return q

    def __del__(self):
        if getattr(self, "_closed", True) is False:
            self.backend.mpq_clear(C.byref(self._q))
            self._closed = True

    @staticmethod
    def _coerce(x):
        if isinstance(x, GMPQ):
            return x if x.backend is BACKEND else GMPQ(x.numerator, x.denominator)
        if isinstance(x, Fraction):
            return GMPQ(x.numerator, x.denominator)
        if isinstance(x, int):
            return GMPQ(x)
        return NotImplemented

    @property
    def numerator(self): return BACKEND.parts(self)[0]
    @property
    def denominator(self): return BACKEND.parts(self)[1]

    def _binary(self, other, op):
        other = self._coerce(other)
        if other is NotImplemented: return NotImplemented
        if op is BACKEND.mpq_div and other.numerator == 0: raise ZeroDivisionError
        return BACKEND.binary(op, self, other)
    def __add__(self, x): return self._binary(x, BACKEND.mpq_add)
    def __radd__(self, x): return self + x
    def __sub__(self, x): return self._binary(x, BACKEND.mpq_sub)
    def __rsub__(self, x): return self._coerce(x) - self
    def __mul__(self, x): return self._binary(x, BACKEND.mpq_mul)
    def __rmul__(self, x): return self * x
    def __truediv__(self, x): return self._binary(x, BACKEND.mpq_div)
    def __rtruediv__(self, x): return self._coerce(x) / self
    def __neg__(self): return GMPQ(-self.numerator, self.denominator)
    def __abs__(self): return GMPQ(abs(self.numerator), self.denominator)
    def __pow__(self, exponent):
        if not isinstance(exponent, int): return NotImplemented
        if exponent < 0: return GMPQ(self.denominator, self.numerator) ** (-exponent)
        result, base, k = GMPQ(1), self, exponent
        while k:
            if k & 1: result = result * base
            k >>= 1
            if k: base = base * base
        return result
    def __eq__(self, x):
        x = self._coerce(x)
        return False if x is NotImplemented else BACKEND.mpq_cmp(C.byref(self._q), C.byref(x._q)) == 0
    def __lt__(self, x):
        x = self._coerce(x)
        if x is NotImplemented: return NotImplemented
        return BACKEND.mpq_cmp(C.byref(self._q), C.byref(x._q)) < 0
    def __le__(self, x): return self == x or self < x
    def __gt__(self, x): return not self <= x
    def __ge__(self, x): return not self < x
    def __bool__(self): return self.numerator != 0
    def __floor__(self): return self.numerator // self.denominator
    def __str__(self): return f"{self.numerator}/{self.denominator}"
    def __repr__(self): return f"GMPQ({self.numerator}, {self.denominator})"


F = GMPQ


def encode(value):
    if isinstance(value, GMPQ):
        return {"numerator_hex": hex(value.numerator), "denominator_hex": hex(value.denominator)}
    if isinstance(value, dict): return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)): return [encode(v) for v in value]
    return value


def decode(value):
    if isinstance(value, dict):
        if set(value) == {"numerator_hex", "denominator_hex"}:
            return F(int(value["numerator_hex"], 16), int(value["denominator_hex"], 16))
        return {k: decode(v) for k, v in value.items()}
    if isinstance(value, list): return [decode(v) for v in value]
    return value


def horner(coefficients, x):
    value = coefficients[-1]
    for c in reversed(coefficients[:-1]): value = value*x+c
    return value


def quotient(z, ecoeff, ucoeff):
    t = z*horner(ucoeff, z*z)
    return (horner(ecoeff, z)-t)/(2*(1+z*t))


def load_unchanged_functions(path, names, namespace):
    tree = ast.parse(path.read_text(), filename=str(path))
    selected = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
    if {node.name for node in selected} != set(names):
        raise RuntimeError(f"Could not extract unchanged functions from {path}")
    exec(compile(ast.Module(body=selected, type_ignores=[]), str(path), "exec"), namespace)
    return namespace


def main():
    root = Path(__file__).parent
    legacy_encoder = load_unchanged_functions(root / "direct_positive_real_execution_1808.py",
        {"rational", "encode"}, {"F": F})
    legacy_horner = load_unchanged_functions(root / "direct_positive_real_execution_1808.py",
        {"horner"}, {"F": F})
    legacy_helper = load_unchanged_functions(root / "direct_positive_real_execution_remaining_1808.py",
        {"decode", "quotient"}, {"F": F, "horner": legacy_horner["horner"]})
    old_encode, old_decode = legacy_encoder["encode"], legacy_helper["decode"]
    old_quotient = legacy_helper["quotient"]
    huge_n = (1 << 681_000) + (1 << 4097) + 17
    huge_d = (1 << 680_999) + 91
    samples = [Fraction(0), Fraction(-7, 9), Fraction(12), Fraction(huge_n, huge_d)]
    roundtrip = []
    for value in samples:
        actual = old_decode(old_encode(F(value)))
        assert (actual.numerator, actual.denominator) == (value.numerator, value.denominator)
        roundtrip.append({"numerator_bits": abs(value.numerator).bit_length(),
                          "denominator_bits": value.denominator.bit_length(), "passed": True})

    z0 = Fraction(7, 11)
    ec0 = [Fraction(1, 2), Fraction(-1, 6), Fraction(1, 24)]
    uc0 = [Fraction(1, 6), Fraction(1, 120)]
    ref_t = sum((c*z0**(2*k+1) for k,c in enumerate(uc0)), Fraction(0))
    ref = (sum((c*z0**k for k,c in enumerate(ec0)), Fraction(0)) - ref_t) / (2*(1+z0*ref_t))
    # Same C033z quotient instruction as the approved helper, with the adapter
    # supplying all F values and the serializer accepting precisely that type.
    actual = old_quotient(F(z0), [F(x) for x in ec0], [F(x) for x in uc0])
    assert (actual.numerator, actual.denominator) == (ref.numerator, ref.denominator)
    slice_roundtrip = old_decode(json.loads(json.dumps(old_encode({"result": actual}))))
    assert slice_roundtrip["result"] == actual

    report = {"status": "PASS_BOUNDED_ADAPTER_SLICE", "library": BACKEND.library,
              "round_trips": roundtrip, "instruction_slice": "direct_positive_real_execution_remaining_1808.py: quotient",
              "slice_fraction_match": True, "slice_result": old_encode(actual),
              "scope": "Constructor/decode/GMP arithmetic/encode and one unchanged quotient slice only; no full evaluator replay, radius assertion, scalar or operation-cap result",
              "source_sha256": {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                  for name in ("direct_positive_real_execution_remaining_1808.py", "direct_positive_real_remaining_execution_1816.py")}}
    out = Path(__file__).with_name("gmp_adapter_slice_1821.json")
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(f"{report['status']}; round trips {len(roundtrip)}/{len(roundtrip)}; quotient exact match; full evaluator/radii/cap untested; {out}")


if __name__ == "__main__": main()
