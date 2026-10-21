#!/usr/bin/env python3
"""L040 fixed-instance audit; complete replay plus exact-endpoint enclosure.

No additional truncation/precision pair is used. Source applicability is
proved in L040; this script does not prove the imported source theorems.
"""
import copy
import importlib.util
import json
import shutil
import subprocess
import sys
from fractions import Fraction as F
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'critical-audit'


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(exist_ok=True)
    originals = OUT / 'originals'
    originals.mkdir(exist_ok=True)
    inputs = ['certify.py', 'verify.py', 'certificate.json', 'verification.json', 'audit.py']
    hashes = {name: digest(HERE / name) for name in inputs}
    for name in inputs:
        dst = originals / name
        if dst.exists():
            assert digest(dst) == hashes[name], ('preserved input differs', name)
        else:
            shutil.copyfile(HERE / name, dst)
    write(OUT / 'pre-replay-manifest.json', hashes)
    # Replay in a separate directory so existing evidence is never overwritten.
    replay = OUT / 'replay'
    replay.mkdir(exist_ok=True)
    for name in ('verify.py', 'certificate.json'):
        shutil.copyfile(originals / name, replay / name)
    proc = subprocess.run([sys.executable, str(replay / 'verify.py')],
                          capture_output=True, text=True)
    (OUT / 'replay.log').write_text(proc.stdout + proc.stderr)
    assert proc.returncode == 0, 'full replay failed; see replay.log'
    fresh = json.loads((replay / 'verification.json').read_text())
    assert fresh == json.loads((originals / 'verification.json').read_text())
    cert = json.loads((originals / 'certificate.json').read_text())
    assert len(cert['attempts']) == 1 and cert['selected_attempt'] == 0
    data = cert['attempts'][0]
    assert (data['T'], data['bits']) == (128, 48)
    S = 2**48

    def enc(x):
        return [str(t) for t in x]

    def add(x, y):
        return [x[0]+y[0], x[1]+y[1]]

    def sub(x, y):
        return [x[0]-y[1], x[1]-y[0]]

    def mul(x, y):
        z = [a*b for a in x for b in y]
        return [min(z), max(z)]

    def div(x, y):
        assert y[0] > 0
        return mul(x, [1/y[1], 1/y[0]])

    def scalar(x, a):
        return sorted([a*x[0], a*x[1]])

    def const(n):
        return [F(n), F(n)]

    def ceil(x):
        return -((-x.numerator)//x.denominator)

    def outward(x):
        return [(S*x[0]).__floor__(), ceil(S*x[1])]

    def sqrt_interval(x):
        assert 0 <= x[0] <= x[1]
        low = isqrt((x[0]*S*S).__floor__())
        high = isqrt((x[1]*S*S).__floor__())
        if F(high*high, S*S) < x[1]:
            high += 1
        result = [F(low, S), F(high, S)]
        assert result[0]**2 <= x[0] <= x[1] <= result[1]**2
        return result

    # Replay verified exact Machin/Taylor brackets. Keep all subsequent
    # sums, products and quotients as exact rationals; round only square roots.
    pi = [F(t) for t in data['pi']['exact_bracket']]
    rho = [F(t) for t in data['exponential']['exact_bracket']]
    # Round rho once to keep endpoint powers compact; no successive products
    # or termwise rounding. This differs from both original routines.
    rho = [F(t, S) for t in outward(rho)]
    coeff = data['coefficients']
    assert coeff[121] == 1
    terms = []
    total = const(0)
    for n in range(1, 129):
        power = [rho[0]**n, rho[1]**n]
        term = scalar(power, F(2*(0, 1, -1, -1, 1)[n % 5]*coeff[n], n))
        total = add(total, term)
        terms.append({'n': n, 'power': enc(power), 'term': enc(term),
                      'partial': enc(total)})
    tail = 2*rho[1]**129/(1-rho[1])
    L = [total[0]-tail, total[1]+tail]
    assert tail <= F(data['series']['tail_upper'], S)

    # Locate the unique root independently by integer evaluation, without
    # consuming the stored midpoint/sign trace.
    def H(k):
        return 4*k**3-4*k*k*S-40*k*S*S-79*S**3
    lo, hi = 4*S, 5*S
    roots = []
    while hi-lo > 1:
        mid = (lo+hi)//2
        val = H(mid)
        roots.append([mid, str(val)])
        assert val != 0
        if val < 0:
            lo = mid
        else:
            hi = mid
    assert H(lo) < 0 < H(hi)
    assert [lo, hi] == data['period']['real_root']
    r = [F(lo, S), F(hi, S)]
    v2 = scalar(sub(sub(scalar(mul(r, r), 3), scalar(r, 2)), const(41)), F(1, 4))
    d = scalar(sub(scalar(r, 3), const(1)), F(1, 2))
    assert v2[0] > 0 and d[0] > 0
    R = sqrt_interval(add(mul(d, d), v2))
    A = sqrt_interval(R)
    G = sqrt_interval(scalar(add(R, d), F(1, 2)))
    agm = [{'A': enc(A), 'G': enc(G)}]
    for _ in range(12):
        A, G = scalar(add(A, G), F(1, 2)), sqrt_interval(mul(A, G))
        agm.append({'A': enc(A), 'G': enc(G)})
    bracket = [min(A[0], G[0]), max(A[1], G[1])]
    omega = div(div(pi, bracket), sqrt_interval(const(5)))
    q = div(L, omega)
    ranges, candidates = [], []
    for b in range(1, 11):
        lower, upper = ceil(b*q[0]), (b*q[1]).__floor__()
        ranges.append([b, lower, upper])
        for a in range(lower, upper+1):
            if gcd(a, b) == 1:
                candidates.append(str(F(a, b)))
    assert candidates == ['5'] and q[0] < 5 < q[1]
    assert q[1]-q[0] < F(1, 100)
    assert outward(q)[0] >= data['isolation']['ratio'][0]
    assert outward(q)[1] <= data['isolation']['ratio'][1]
    independent = {'method': 'exact rational endpoints; rounding only at square roots and initial rho',
                   'bits': 48, 'T': 128, 'pi': enc(pi), 'rho': enc(rho),
                   'terms': terms, 'tail': str(tail), 'L': enc(L),
                   'root_signs': roots, 'root': enc(r), 'v_squared': enc(v2),
                   'd': enc(d), 'R': enc(R), 'agm_states': agm,
                   'agm_bracket': enc(bracket), 'omega_twist': enc(omega),
                   'q': enc(q), 'ratio_outward': outward(q),
                   'width_outward': str(F(outward(q)[1]-outward(q)[0], S)),
                   'required_width': '1/100', 'denominator_ranges': ranges,
                   'candidates': candidates, 'failures': []}
    write(OUT / 'independent-enclosure.json', independent)

    spec = importlib.util.spec_from_file_location('l040_replay', originals / 'verify.py')
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    mutations = [('bad-prime-square', ('coefficients', 121), -10),
                 ('tail', ('series', 'tail_upper'), 0),
                 ('period-component', ('period', 'omega_total'), [2*t for t in data['period']['omega_total']]),
                 ('agm-bound', ('period', 'agm_bracket'), [1, 1]),
                 ('rational-existence', ('isolation', 'candidates'), ['6'])]
    rejected = []
    for name, keys, value in mutations:
        changed = copy.deepcopy(data)
        changed[keys[0]][keys[1]] = value
        try:
            verifier.run(changed)
        except AssertionError:
            rejected.append(name)
        else:
            raise AssertionError(('mutation accepted', name))
    assert len(rejected) == len(mutations)
    assert all(digest(HERE / name) == hashes[name] for name in inputs)
    report = {'source_sha256': hashes, 'certificate_sha256': hashes['certificate.json'],
              'complete_replay': fresh, 'independent_enclosure_sha256': digest(OUT / 'independent-enclosure.json'),
              'independent_ratio_outward': outward(q),
              'independent_width_outward': independent['width_outward'],
              'required_width': '1/100', 'q': '5', 'mutations_rejected': rejected,
              'original_inputs_unchanged': True, 'external_theorems_verified_by_script': False,
              'failures': []}
    write(OUT / 'audit.json', report)
    print('Full replay: 7 groups; independent q=5; a_121=1; rejected mutations:', len(rejected))
    print('Independent outward ratio:', outward(q), '/', S,
          'width:', independent['width_outward'], 'required < 1/100; failures: []')
    print('Evidence:', OUT.relative_to(HERE.parents[2]) / 'audit.json')


if __name__ == '__main__':
    main()
