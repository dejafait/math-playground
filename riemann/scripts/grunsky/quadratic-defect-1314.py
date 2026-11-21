#!/usr/bin/env python3
"""Exact full-column specialization and one necessary Cauchy test.

No solver, parameter sweep, new quadrature or analytic realization.
The inherited actual-Xi inclusion remains conditional on L037.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'quadratic-defect-certificate-1314.json'
NAMES = ('b1', 'b2', 'b3', 'b4', 'b5', 'A', 'B', 'C', 'D', 'E', 't', 'u', 'v')
ZERO = (0,) * len(NAMES)


class P:
    def __init__(self, x=0):
        self.t = ({e: F(c) for e, c in x.items() if c} if isinstance(x, dict)
                  else ({ZERO: F(x)} if x else {}))

    def __add__(self, q):
        q = q if isinstance(q, P) else P(q)
        d = self.t.copy()
        for e, c in q.t.items():
            d[e] = d.get(e, F(0)) + c
        return P(d)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -c for e, c in self.t.items()})

    def __sub__(self, q):
        return self + (-q if isinstance(q, P) else -P(q))

    def __rsub__(self, q):
        return -self + q

    def __mul__(self, q):
        q = q if isinstance(q, P) else P(q)
        d = {}
        for e, c in self.t.items():
            for h, a in q.t.items():
                key = tuple(x+y for x, y in zip(e, h))
                d[key] = d.get(key, F(0)) + c*a
        return P(d)

    __rmul__ = __mul__

    def __truediv__(self, n):
        return self * (1/F(n))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        p = P(1)
        for _ in range(n):
            p = p*self
        return p

    def record(self):
        return [{'powers': {name: k for name, k in zip(NAMES, e) if k},
                 'coefficient': str(c)} for e, c in sorted(self.t.items())]


def var(i):
    e = list(ZERO)
    e[i] = 1
    return P({tuple(e): F(1)})


def mul_laurent(p, q):
    d = {}
    for i, a in p.items():
        for j, b in q.items():
            d[i+j] = d.get(i+j, P()) + a*b
    return {i: a for i, a in d.items() if a.t}


def mul_mixed(p, q):
    d = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            if i+k <= 3 and j+l <= 15:
                key = (i+k, j+l)
                d[key] = d.get(key, P()) + a*b
    return {e: a for e, a in d.items() if a.t}


def main():
    xs = [var(i) for i in range(len(NAMES))]
    b = {j: xs[j-1] for j in range(1, 6)}
    A, B, C, D, E, t, u, v = xs[5:]
    g = {1: P(1), **{-j: bj for j, bj in b.items()}}
    g2 = mul_laurent(g, g)
    g3 = mul_laurent(g2, g)
    phi = {1: g.copy(), 2: g2.copy(), 3: g3.copy()}
    phi[2][0] = phi[2].get(0, P()) - 2*b[1]
    for k, a in g.items():
        phi[3][k] = phi[3].get(k, P()) - 3*b[1]*a
    phi[3][0] = phi[3].get(0, P()) - 3*b[2]
    columns, checks = {}, {}
    for m in (1, 2, 3):
        checks[f'nonnegative_laurent_part_{m}'] = all(
            not (phi[m].get(k, P()) - (1 if k == m else 0)).t
            for k in range(m+1))
        checks[f'exact_minimum_exponent_{m}'] = min(k for k, a in phi[m].items() if a.t) == -5*m
        columns[m] = {k: phi[m].get(-k, P())/m for k in range(1, 5*m+1)}

    # Independent finite extraction from -log(1-D). Terms of D have
    # both mixed exponents >=1, so only powers 1,2,3 can affect x^m,m<=3.
    mixed_d = {}
    for j, bj in b.items():
        for i in range(1, j+1):
            if i <= 3:
                mixed_d[(i, j+1-i)] = bj
    power, log = {(0, 0): P(1)}, {}
    for n in (1, 2, 3):
        power = mul_mixed(power, mixed_d)
        for key, a in power.items():
            log[key] = log.get(key, P()) + a/n
    comparisons = {}
    for m in (1, 2, 3):
        for k in range(1, 16):
            residual = columns[m].get(k, P()) - log.get((m, k), P())
            comparisons[f'{m},{k}'] = residual.record()
    checks['all_45_log_comparisons_zero'] = all(not r for r in comparisons.values())
    checks['symmetry_on_selected_three_indices'] = all(
        not (columns[m][n]-columns[n][m]).t for m in (1, 2, 3) for n in (1, 2, 3))

    defects, residuals, targets = {}, {}, {}
    ds = {1: P(1), 2: u, 3: v}
    sums = {2: A, 3: B, 4: C, 5: D, 6: E}
    complete_products = {}
    for m in (1, 2, 3):
        for n in range(m, 4):
            products = {str(k): (k*columns[m][k]*columns[n][k]).record()
                        for k in range(1, min(5*m, 5*n)+1)}
            h = P(F(1, m) if m == n else 0) - sum(
                (k*columns[m][k]*columns[n][k] for k in range(1, min(5*m, 5*n)+1)), P())
            key = f'{m},{n}'
            defects[key] = h
            targets[key] = t*ds[m]*ds[n]*sums[m+n]
            residuals[key] = h-targets[key]
            complete_products[key] = products

    h11, h12, h13, h22, h23, h33 = (defects[key] for key in ('1,1','1,2','1,3','2,2','2,3','3,3'))
    invariant = {
        'F22': B**2*h11*h22-A*C*h12**2,
        'F33': C**2*h11*h33-A*E*h13**2,
        'F23': B*C*h11*h23-A*D*h12*h13}
    z11, z12, z13, z22, z23, z33 = (targets[key] for key in ('1,1','1,2','1,3','2,2','2,3','3,3'))
    target_checks = {
        'F22': B**2*z11*z22-A*C*z12**2,
        'F33': C**2*z11*z33-A*E*z13**2,
        'F23': B*C*z11*z23-A*D*z12*z13}
    checks['three_target_invariants_zero'] = all(not p.t for p in target_checks.values())

    # Exactly the fixed1307 outer boxes; no recalculation of Xi moments.
    raw_bounds = {2: ('3.7172599285e-5', '3.7172599286e-5'),
                  3: ('1.4417393139e-7', '1.4417393141e-7'),
                  4: ('6.6303168020e-10', '6.6303168031e-10'),
                  5: ('3.2136641485e-12', '3.2136641527e-12'),
                  6: ('1.5876934435e-14', '1.5876934595e-14')}
    bounds = {n: tuple(map(F, pair)) for n, pair in raw_bounds.items()}
    source = HERE/'actual-singleton-certificate-1307.json'
    saved = json.loads(source.read_text())
    checks['inherited_boxes_strictly_contained_in_fixed_outer_boxes'] = all(
        0 < lo < F(saved['S'][str(n)]['lower']) <= F(saved['S'][str(n)]['upper']) < hi
        for n, (lo, hi) in bounds.items())
    alo, ahi = bounds[2]
    blo, bhi = bounds[3]
    clo, chi = bounds[4]
    rlo, rhi = blo**2/(ahi*chi), bhi**2/(alo*clo)
    checks['ratio_strictly_between_0843_and_0844'] = F('0.843') < rlo <= rhi < F('0.844')
    # At x=y=1/2 the necessary inequality has slack (1-r)/4.
    # This is a witness only for the relaxation in x,y, not for b.
    slack_lo, slack_hi = (1-rhi)/4, (1-rlo)/4
    checks['relaxation_witness_has_strict_slack'] = F('0.039') < slack_lo <= slack_hi < F('0.03925')
    failures = [name for name, ok in checks.items() if not ok]
    report = {
        'status': 'passed' if not failures else 'failed', 'failures': failures,
        'variables': list(NAMES), 'coefficient_encoding': 'exact rational monomials; empty list is zero',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_sha256': {str(source.relative_to(ROOT)): hashlib.sha256(source.read_bytes()).hexdigest()},
        'support_provenance': {
            'g_exponents': [-5,-4,-3,-2,-1,1],
            'Phi1': 'w', 'Phi2': 'w^2-2*b1', 'Phi3': 'w^3-3*b1*w-3*b2',
            'exact_column_upper_bounds': {'1':5,'2':10,'3':15},
            'highest_terms': {'1':'b5','2':'b5^2/2','3':'b5^3/3'},
            'log_power_cutoff': 3, 'log_rectangle': {'x_max':3,'y_max':15}},
        'columns': {str(m): {str(k): p.record() for k, p in col.items()} for m, col in columns.items()},
        'all_45_log_verification_residuals': comparisons,
        'full_weighted_column_products': complete_products,
        'defects': {key: p.record() for key, p in defects.items()},
        'six_equation_residuals': {key: p.record() for key, p in residuals.items()},
        'three_invariants': {key: p.record() for key, p in invariant.items()},
        'three_target_invariant_residuals': {key: p.record() for key, p in target_checks.items()},
        'branch_guards': ['A,B,C,D,E>0','h11,h12,h13>0','F22=F33=F23=0'],
        'reconstruction': {'t':'h11/A','u':'A*h12/(B*h11)','v':'A*h13/(C*h11)'},
        'necessary_test': {
            'outer_boxes': {str(n): {'lower':str(lo),'upper':str(hi)} for n,(lo,hi) in bounds.items()},
            'ratio': 'r=B^2/(A*C)', 'ratio_box': {'lower':str(rlo),'upper':str(rhi)},
            'variables': 'x=h11=t*A, y=2*h22=2*t*u^2*C',
            'required': '0<x<1, 0<y<1, (1-x)*(1-y)>=r*x*y',
            'relaxation_witness_only': {'x':'1/2','y':'1/2'},
            'slack_box': {'lower':str(slack_lo),'upper':str(slack_hi)},
            'decision': 'INCONCLUSIVE: the necessary relaxation is strictly compatible; no b witness or exclusion'},
        'checks': checks,
        'limits': 'Actual inclusion conditional on L037/1307. No full-system feasibility, analytic realization, higher block or RH conclusion.'}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(f'Full column supports: 5,10,15; complete sum cutoffs: 5,5,5,10,10,15; failures={len(failures)}')
    print('Actual required ratio r=B^2/(A*C): 0.843 < r < 0.844; necessary threshold at x=y=1/2 is r<=1')
    print('Relaxation slack: 0.039 < (1-r)/4 < 0.03925; INCONCLUSIVE for full formal feasibility/univalence')
    print(f'Full certificate: {OUT.relative_to(ROOT)}')
    assert not failures


if __name__ == '__main__':
    main()
