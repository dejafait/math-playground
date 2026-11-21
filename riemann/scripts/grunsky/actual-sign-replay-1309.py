"""Replay saved finite sign evidence without running the adaptive search.

Uses separately implemented rational endpoint arithmetic; direct witness
evaluation is independent of the transformed polynomial sign decision.
The1307 actual-input enclosure and Decimal contract remain imported.
"""
import hashlib
import importlib.util
import json
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE/'actual-sign-certificate-1309.json'
OUT = HERE/'actual-sign-replay-1309.json'
PRIMITIVE = HERE.parent/'heat/low-time-h1-uniform-180-check.py'
spec = importlib.util.spec_from_file_location('rational_intervals', PRIMITIVE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
R = module.R


def data(v):
    return {'lower': str(v.lo), 'upper': str(v.hi)}


def sign(v):
    return 1 if v.lo > 0 else -1 if v.hi < 0 else 0


def horner(p, value):
    ans = R(0)
    for c in reversed(p):
        ans = ans*value+c
    return ans


def main():
    source = json.loads(SOURCE.read_text())
    assert source['status'] == 'completed' and not source['failures']
    for relative, digest in source['inputs'].items():
        assert hashlib.sha256((ROOT/relative).read_bytes()).hexdigest() == digest
    assert all(r['zero'] and not r['terms'] for r in source['formal']['residuals'].values())
    params = {k: R.read(v) for k, v in source['parameters'].items()}
    A, B, C, D, E = params.values()
    assert all(v.lo > 0 for v in params.values())
    prior = json.loads((HERE/'actual-singleton-certificate-1307.json').read_text())
    for index, box in enumerate(params.values(), 2):
        actual = R.read(prior['S'][str(index)])
        assert box.lo < actual.lo <= actual.hi < box.hi
    polynomials = {k: [R.read(c) for c in v] for k, v in source['polynomials'].items()}
    # Recompute all saved Bernstein coefficients from the power coefficients
    # using a single direct weighted sum, rather than the producer's two stages.
    previous = F(0)
    checked = []
    for row in source['cells']:
        a, b = map(F, row['z'])
        assert a == previous and 0 <= a < b <= 1
        assert b-a == F(1, 2**row['depth']) and row['depth'] <= 16
        previous = b
        computed_signs = {}
        for name, p in polynomials.items():
            d = len(p)-1
            beta = []
            for i in range(d+1):
                weights = [sum((F(comb(j, t)*comb(i, t), comb(d, t))*a**(j-t)*(b-a)**t
                                for t in range(min(i, j)+1)), F(0)) for j in range(d+1)]
                assert all(w >= 0 for w in weights)
                beta.append(R(sum(c.lo*w for c, w in zip(p, weights)),
                              sum(c.hi*w for c, w in zip(p, weights))))
            assert all(data(v) == saved for v, saved in zip(beta, row['bernstein'][name]))
            hull = R(min(v.lo for v in beta), max(v.hi for v in beta))
            assert data(hull) == row['ranges'][name]
            computed_signs[name] = sign(hull)
        assert computed_signs == row['signs']
        s = computed_signs
        failed = [k for k in ('n', 'v', 'j') if s['l'] and s[k] == -s['l']]
        failed += ['h'] if s['h'] == -1 else []
        feasible = s['l'] != 0 and s['h'] == 1 and all(s[k] == s['l'] for k in ('n', 'v', 'j'))
        assert failed == row['failed_numerators']
        status = 'excluded' if failed else 'feasible' if feasible else 'unresolved'
        assert status == row['status']
        checked.append({'z': row['z'], 'status': status, 'five_polynomial_signs_checked': True})
    assert previous == 1 and len(checked) <= 256
    ell, n = polynomials['l'], polynomials['n']
    root = (-ell[0])/ell[1]
    nr = horner(n, root)
    assert data(root) == source['exceptional']['unique_l_root_z']
    assert 0 < root.lo <= root.hi < 1 and nr.lo > 0
    assert F('0.065') < root.lo <= root.hi < F('0.066') and nr.lo > F('6e-7')
    assert ell[0].lo > 0 > ell[1].hi
    assert source['descartes']['coefficient_signs_ascending'] == [1, -1]
    assert source['descartes']['positive_roots_with_multiplicity'] == 1
    assert data(nr) == source['exceptional']['n_at_every_possible_l_root']
    w = source['witness']
    z, x = F(w['z']), F(w['x'])
    assert 0 < z < 1 and x == 2-1/z < 1
    cell = next(r for r in source['cells'] if r['z'] == w['cell'])
    assert cell['status'] == 'feasible' and F(cell['z'][0]) < z < F(cell['z'][1])
    X = R(x)
    k = A/(2*C)
    L = -E*k*(1+X)+E*X*B/D+(R(1)-X)*B**2/(2*A)
    N = A*(X**2+X+1)/3-E*k**2*(1+X)**2
    assert sign(L) and data(L) == w['L'] and data(N) == w['N']
    p = N/L
    V = p-k*(1+X)
    J = V-X*B/D
    H = p*J-X*V*C/E+(R(1)-X)*p*B**2/(2*A*E)
    vals = {'p': p, 'V': V, 'J': J, 'H': H, 'tau': (R(1)-X)/A}
    assert all(data(v) == w['values'][name] for name, v in vals.items())
    assert all(v.lo > F(w['strict_rational_lower_margins'][name]) > 0 for name, v in vals.items())
    counts = dict(Counter(row['status'] for row in checked))
    assert counts == source['summary']['cell_counts']
    assert source['summary']['strict_actual_witness']
    assert source['summary']['common_L_N_zero_excluded']
    assert source['cells'][0]['status'] == source['cells'][-1]['status'] == 'excluded'
    assert not source['summary']['full_solution_set_classified']
    # Extra scope check: the certified excluded cells cover [1/4,1),
    # hence in particular x>=-1 (z>=1/3). No univalence theorem is applied.
    assert all(row['status'] == 'excluded' for row in source['cells'] if F(row['z'][1]) > F(1, 4))
    report = {'status': 'passed', 'failures': [],
              'input_sha256': {str(f.relative_to(ROOT)): hashlib.sha256(f.read_bytes()).hexdigest()
                               for f in (SOURCE, Path(__file__), PRIMITIVE)},
              'checks': {'cells': len(checked), 'polynomial_cell_signs': 5*len(checked),
                         'full_domain_partition': True, 'both_tails_excluded': True,
                         'common_root_absent': True, 'direct_actual_witness': True,
                         'strict_rational_margins': True, 'coefficient_box_inclusion': True,
                         'x_in_minus1_to1_excluded': True},
              'cell_checks': checked, 'direct_witness': {k: data(v) for k, v in vals.items()},
              'unresolved': [r['z'] for r in source['cells'] if r['status'] == 'unresolved'],
              'scope': 'finite evidence replay, not independent quadrature/Decimal or proof audit'}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('PASS:', len(checked), 'cells;', 5*len(checked), 'polynomial sign bounds; direct strict witness; failures=0')
    print('Unresolved cells:', report['unresolved'], 'CERTIFICATE:', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
