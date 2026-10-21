"""Exact finite transcription checks for L028, not an all-horizon proof."""
from fractions import Fraction
import json
from pathlib import Path

OUT = Path(__file__).with_name('certificate.json')
failures = []


def require(condition, context):
    if not condition:
        failures.append(context)


def T(n):
    return (3*n+1)//2 if n % 2 else n//2


def rational(value):
    return [value.numerator, value.denominator]


def slope_case(L):
    records = []
    checked = 0
    maximum = Fraction(0)
    classes = {'h_negative': 0, 'nonnegative_exponents': 0, 'j_negative': 0}
    for s in range(L+1):
        for t in range(L+1):
            r = t if t <= 4 else t-1
            for a in range(s+1):
                checked += 1
                h, j = s-t, r-a
                # Original unreduced expression, independently of sign cases.
                slope = Fraction(2**s*3**r, 2**t*3**a)
                if slope <= 1:
                    continue
                ratio = Fraction(2**s, 1)/(slope-1)
                if h < 0:
                    kind = 'h_negative'
                    require(j > 0, {'L': L, 'triple': [s, t, a], 'test': 'j positive'})
                    intermediate = Fraction(2**t)
                elif j >= 0:
                    kind = 'nonnegative_exponents'
                    require(slope.denominator == 1, {'L': L, 'test': 'integer slope'})
                    intermediate = Fraction(2**s)
                else:
                    kind = 'j_negative'
                    intermediate = Fraction(2**s*3**(-j))
                    require(intermediate < 2**(s+h),
                            {'L': L, 'triple': [s, t, a], 'test': 'strict numerator bound'})
                classes[kind] += 1
                require(ratio <= intermediate <= 4**L,
                        {'L': L, 'triple': [s, t, a], 'test': 'new slope bound'})
                # q>=1 and d<=2**s-1: this is the worst lower bound for c-n.
                lower_difference = (slope-1)*(4**L+1)+slope-2**s
                require(lower_difference > 0,
                        {'L': L, 'triple': [s, t, a], 'test': 'strict order'})
                maximum = max(maximum, ratio)
                records.append({'s': s, 't': t, 'a': a, 'case': kind,
                                'slope': rational(slope), 'ratio': rational(ratio),
                                'intermediate_bound': rational(intermediate),
                                'strict_order_lower_bound': rational(lower_difference)})
    return {'L': L, 'all_exponent_triples_checked': checked, 'case_counts': classes,
            'maximum_ratio': rational(maximum), 'required_ratio_upper_bound': 4**L,
            'slope_above_one_records': records}


def root_case(p, q):
    B = Fraction(p, q)
    # Exact equivalent of L*log(2)>=log(163)+B*log(12), no floating point.
    L = 6
    while 2**(q*L) < 163**q*12**p:
        L += 1
    binary, ternary = 2**(L+1), 3**(L+4)
    binary_residue = -97*pow(81, -1, binary) % binary
    M = binary*ternary
    residue = 47+ternary*((binary_residue-47)*pow(ternary, -1, binary) % binary)
    require(0 <= residue < M, {'B': str(B), 'test': 'canonical residue'})
    H = 4**L
    multiplier = (H-residue)//M+1
    n = residue+M*multiplier
    require(H < n <= H+M < 163*6**L, {'B': str(B), 'test': 'height interval'})
    require(n % ternary == 47 and (81*n+97) % binary == 0,
            {'B': str(B), 'test': 'CRT congruences'})
    require(n % 243 == 47 and n % 32 == 15 and n > 47,
            {'B': str(B), 'test': 'cylinder and exact valuation'})
    # Exponentiating the clock inequality for rational B is exact.
    require(n**q*12**p < 12**(q*L), {'B': str(B), 'test': 'endpoint clock'})
    path = [n]
    for t in range(L):
        require(path[-1] % 2 == (0 if t == 4 else 1),
                {'B': str(B), 't': t, 'test': 'actual input parity'})
        path.append(T(path[-1]))
    return {'B': rational(B), 'L': L, 'root': n, 'required_strict_lower_bound': H,
            'actual_upper_bound': H+M, 'required_strict_upper_bound': 163*6**L,
            'CRT_modulus': M, 'CRT_residue': residue, 'CRT_multiplier': multiplier,
            'clock_actual_exponentiated': n**q*12**p,
            'clock_required_strict_upper_bound': 12**(q*L), 'actual_path': path}


slopes = [slope_case(L) for L in (6, 12, 24, 48)]
roots = [root_case(p, q) for p, q in ((0, 1), (1, 1), (5, 2), (10, 1))]
certificate = {'purpose': 'Finite transcription checks only; all-horizon proof is L028',
               'slope_cases': slopes, 'root_cases': roots, 'failures': failures}
OUT.write_text(json.dumps(certificate, separators=(',', ':'))+'\n')
for case in slopes:
    print('L={L}: checked={all_exponent_triples_checked}; actual maximum ratio='
          '{maximum_ratio}; required <= {required_ratio_upper_bound}; cases={case_counts}'.format(**case))
for case in roots:
    print('B={B}, L={L}: actual root={root}; required > {required_strict_lower_bound}, '
          '< {required_strict_upper_bound}; clock: actual {clock_actual_exponentiated} '
          '< required {clock_required_strict_upper_bound}'.format(**case))
print('Failures:', failures)
print('Full certificate:', OUT)
if failures:
    raise SystemExit(1)
