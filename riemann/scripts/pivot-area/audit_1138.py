#!/usr/bin/env python3
"""Bounded C750g audit: unchanged replay and independent decimal LDL/solves.

Source analytic enclosures are audited in C750g; this program checks the
complete serialized matrix data and all nine/seven finite claims. It does
not infer analytic correctness from numerical overlap or extrapolate.
"""
from contextlib import redirect_stdout
import ctypes
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
DOWN = Context(prec=110, rounding=ROUND_FLOOR)
UP = Context(prec=110, rounding=ROUND_CEILING)


class J:
    def __init__(self, lo=0, hi=None):
        self.lo, self.hi = D(lo), D(lo if hi is None else hi)
        assert self.lo.is_finite() and self.hi.is_finite() and self.lo <= self.hi

    @classmethod
    def load(cls, pair):
        return cls(*pair)

    @staticmethod
    def cast(x):
        return x if isinstance(x, J) else J(x)

    def __add__(self, other):
        b = self.cast(other)
        return J(DOWN.add(self.lo, b.lo), UP.add(self.hi, b.hi))

    __radd__ = __add__

    def __neg__(self):
        return J(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, b):
        return self + -self.cast(b)

    def __rsub__(self, b):
        return self.cast(b) - self

    def __mul__(self, other):
        b = self.cast(other)
        pairs = [(x, y) for x in (self.lo, self.hi) for y in (b.lo, b.hi)]
        return J(min(DOWN.multiply(x, y) for x, y in pairs),
                 max(UP.multiply(x, y) for x, y in pairs))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = self.cast(other)
        assert b.lo > 0 or b.hi < 0
        return self * J(DOWN.divide(D(1), b.hi), UP.divide(D(1), b.lo))

    def __rtruediv__(self, b):
        return self.cast(b) / self

    def square(self):
        if self.lo <= 0 <= self.hi:
            return J(0, max(UP.multiply(self.lo, self.lo), UP.multiply(self.hi, self.hi)))
        return J(min(DOWN.multiply(self.lo, self.lo), DOWN.multiply(self.hi, self.hi)),
                 max(UP.multiply(self.lo, self.lo), UP.multiply(self.hi, self.hi)))

    def abs(self):
        if self.lo >= 0:
            return self
        if self.hi <= 0:
            return -self
        return J(0, max(self.lo.copy_negate(), self.hi))

    def sqrt(self):
        assert self.lo >= 0
        # Decimal.sqrt is correctly rounded to nearest irrespective of the
        # context mode. One adjacent representable step gives an enclosure.
        result = J(max(D(0), DOWN.next_minus(DOWN.sqrt(self.lo))),
                   UP.next_plus(UP.sqrt(self.hi)))
        # Verify the endpoint-square inequalities with exact rationals;
        # enclosure does not depend solely on sqrt's rounding behavior.
        assert Fraction(result.lo)**2 <= Fraction(self.lo)
        assert Fraction(result.hi)**2 >= Fraction(self.hi)
        return result

    def intersect(self, b):
        return J(max(self.lo, b.lo), min(self.hi, b.hi))

    def overlaps(self, b):
        return max(self.lo, b.lo) <= min(self.hi, b.hi)

    def dump(self):
        return [str(self.lo), str(self.hi)]


def dot(a, b):
    assert len(a) == len(b)
    return sum((x*y for x, y in zip(a, b)), J())


def main():
    original_path = HERE / 'certificate-1136.json'
    before = original_path.read_bytes()
    old = json.loads(before)
    script = HERE / 'certify_1136.py'
    digest = hashlib.sha256(script.read_bytes()).hexdigest()
    assert digest == old['script_sha256']
    # Execute an identical copy, keeping the original certificate untouched.
    with tempfile.TemporaryDirectory(prefix='pivot-audit-1138-') as tmp:
        tmp_path = Path(tmp)
        copy = tmp_path / script.name
        shutil.copyfile(script, copy)
        spec = importlib.util.spec_from_file_location('pilot1138', copy)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        log = io.StringIO()
        with redirect_stdout(log):
            module.main()
        replay_bytes = (tmp_path / original_path.name).read_bytes()
        (HERE / 'replay-1138.json').write_bytes(replay_bytes)
        replay = json.loads(replay_bytes)
        assert replay == old, 'unchanged replay differs'
        # Compile against the same installed C header used by this platform.
        abi_source = r'''
#include <stddef.h>
#include <stdio.h>
#include <mpfr.h>
int main(void) {
  printf("%zu %zu %zu %zu %zu %zu %zu %zu %d %d\n",
    sizeof(__mpfr_struct), sizeof(mpfr_prec_t), sizeof(mpfr_exp_t),
    sizeof(mp_limb_t), offsetof(__mpfr_struct,_mpfr_prec),
    offsetof(__mpfr_struct,_mpfr_sign), offsetof(__mpfr_struct,_mpfr_exp),
    offsetof(__mpfr_struct,_mpfr_d), MPFR_RNDD, MPFR_RNDU);
}
'''
        exe = tmp_path / 'abi'
        subprocess.run(['cc', '-I/opt/homebrew/include', '-x', 'c', '-', '-o', str(exe)],
                       input=abi_source, text=True, capture_output=True, check=True)
        actual_abi = list(map(int, subprocess.check_output([str(exe)], text=True).split()))
        expected_abi = [ctypes.sizeof(module.Raw), ctypes.sizeof(ctypes.c_long),
                        ctypes.sizeof(ctypes.c_long), ctypes.sizeof(ctypes.c_ulong),
                        module.Raw.prec.offset, module.Raw.sign.offset,
                        module.Raw.exp.offset, module.Raw.limbs.offset, module.DOWN, module.UP]
        assert actual_abi == expected_abi
    assert original_path.read_bytes() == before
    assert old['P'] == 101 and old['tested_j'] == list(range(2, 9))
    assert not old['failures'] and old['mpfr_version'] == '4.2.2'
    expected_powers = []
    for n in range(2, 101):
        divisors = [d for d in range(2, n+1) if n % d == 0]
        p, m, k = divisors[0], n, 0
        while m % p == 0:
            m //= p
            k += 1
        if m == 1:
            expected_powers.append((n, p, k))
    assert expected_powers == [(r['n'], r['prime'], r['power']) for r in old['prime_powers']]
    assert len(expected_powers) == 35
    rows = old['source_rows']
    assert [r['q'] for r in rows] == list(range(9))
    u = [J.load(r['u']) for r in rows]
    v = [J.load(r['gamma']) for r in rows]
    # Reconstruct off-diagonals from serialized source rows and intersect
    # only enclosures of the same exact entry. Diagonals are complete
    # source enclosures whose analytic/implementation proof is audited.
    A = [[J.load(pair) for pair in row] for row in old['matrix']]
    for q in range(9):
        A[q][q] = A[q][q].intersect(J.load(rows[q]['Aqq']))
        for r in range(q):
            entry = (u[q]*v[r]-v[q]*u[r])/(q*q-r*r)
            A[q][r] = A[r][q] = entry.intersect(A[q][r]).intersect(A[r][q])
    channels = {k: [J.load(x) for x in vals] for k, vals in old['source_u_channels'].items()}
    for q in range(9):
        assert sum((vals[q] for vals in channels.values()), J()).overlaps(u[q])
    L = [[J(int(i == j)) for j in range(9)] for i in range(9)]
    pivots = []
    consistency = []
    for k in range(9):
        d = A[k][k] - sum((L[k][h].square()*pivots[h] for h in range(k)), J())
        assert d.lo > D(old['claims']['positive_pivots'][k]['lower'])
        assert d.overlaps(J.load(old['LDL_pivots'][k]))
        pivots.append(d)
        for i in range(k+1, 9):
            L[i][k] = (A[i][k] - sum((L[i][h]*L[k][h]*pivots[h]
                                      for h in range(k)), J()))/d
            assert L[i][k].overlaps(J.load(old['LDL_L'][i][k]))

    def solve(b):
        n = len(b)
        y = []
        for i in range(n):
            y.append(b[i]-dot(L[i][:i], y))
        z = [y[i]/pivots[i] for i in range(n)]
        x = [J() for _ in range(n)]
        for i in reversed(range(n)):
            x[i] = z[i]-sum((L[h][i]*x[h] for h in range(i+1, n)), J())
        return x

    tests = []
    for j, original in zip(range(2, 9), old['tests']):
        assert original['j'] == j and original['status'] == 'PASS'
        m = [A[q][j] for q in range(j)]
        sm, su, sv = solve(m), solve(u[:j]), solve(v[:j])
        cross = dot(u[:j], sv).intersect(dot(v[:j], su))
        G = [[dot(u[:j], su), cross], [cross, dot(v[:j], sv)]]
        r = [u[j]-dot(u[:j], sm), v[j]-dot(v[:j], sm)]
        p = (A[j][j]-dot(m, sm)).intersect(pivots[j])
        assert p.lo > 0 and G[0][0].lo > 0 and G[1][1].lo > 0
        E = G[1][1]*r[0].square()-2*cross*r[0]*r[1]+G[0][0]*r[1].square()
        H = 101**2*(j+1)**5*p
        ratio = E/H
        residual = {k: vals[j]-dot(vals[:j], sm) for k, vals in channels.items()}
        U = (G[1][1].sqrt()*sum((x.abs() for x in residual.values()), J())
             + G[0][0].sqrt()*r[1].abs()).square()
        budget = U/H
        target = old['claims']['pilot_and_budget'][j-2]
        assert ratio.hi < D(target['ratio_upper']) < D('.6')
        assert budget.lo > D(target['budget_ratio_lower']) >= D('1e7')
        if j == 8:
            assert budget.lo > D('4e25')
        margin = H-E
        assert margin.lo > 0
        # Consume ALL original solves, Gram entries, residuals, pivots and
        # budgets. Overlap is a consistency check, NOT the proof of inclusion.
        pairs = [(a, J.load(b)) for a, b in zip(m, original['m'])]
        for key, new in [('solve_m', sm), ('solve_u', su), ('solve_v', sv), ('r', r)]:
            pairs += [(a, J.load(b)) for a, b in zip(new, original[key])]
        pairs += [(G[a][b], J.load(original['G'][a][b])) for a in range(2) for b in range(2)]
        for key, new in [('pivot', p), ('lhs', E), ('rhs', H), ('margin', margin),
                         ('ratio', ratio), ('area_increment', E/p),
                         ('separate_channel_upper_budget', U),
                         ('separate_channel_budget_over_rhs', budget)]:
            pairs.append((new, J.load(original[key])))
        pairs += [(val, J.load(original['u_residual_channels'][k])) for k, val in residual.items()]
        assert all(a.overlaps(b) for a, b in pairs)
        consistency.append({'j': j, 'full_interval_pairs_checked': len(pairs)})
        tests.append({'j': j, 'solve_m': [x.dump() for x in sm],
                      'solve_u': [x.dump() for x in su], 'solve_v': [x.dump() for x in sv],
                      'G': [[x.dump() for x in row] for row in G],
                      'r': [x.dump() for x in r], 'pivot': p.dump(),
                      'E': E.dump(), 'H': H.dump(), 'margin': margin.dump(),
                      'ratio': ratio.dump(), 'U': U.dump(), 'budget_ratio': budget.dump(),
                      'channels': {k: x.dump() for k, x in residual.items()},
                      'required_ratio_upper': target['ratio_upper'],
                      'required_budget_lower': target['budget_ratio_lower']})
    out = {'schema': 'pivot-area-audit1138-v1', 'original_sha256': hashlib.sha256(before).hexdigest(),
           'script_sha256': digest, 'replay_identical': True, 'original_preserved': True,
           'abi_actual': actual_abi, 'abi_expected': expected_abi, 'abi_c_source': abi_source,
           'decimal_precision': 110, 'prime_power_count': 35,
           'sqrt_endpoints_squared_checked_with_exact_rationals': True,
           'LDL_L': [[x.dump() for x in row] for row in L],
           'pivots': [x.dump() for x in pivots], 'tests': tests,
           'consistency_checks': consistency, 'failures': [],
           'qualification': 'Analytic inclusion uses C750g proof; overlaps only check consistency. No universal claim.'}
    path = HERE / 'audit-1138.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('Unchanged replay identical; original preserved; MPFR ABI matches:', actual_abi)
    print('Independent 110-digit decimal intervals: 9/9 positive pivots; 35/35 prime powers')
    for t in tests:
        print(f"j={t['j']}: E/H upper < {t['required_ratio_upper']} < .6; "
              f"U/H lower > {t['required_budget_lower']}; margins positive")
    print('Failures: []; full audit:', path.relative_to(HERE.parent.parent))
    print('Full unchanged replay: scripts/pivot-area/replay-1138.json')


if __name__ == '__main__':
    main()
