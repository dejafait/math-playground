"""Fixed L081 audit: fresh replay, distinct full line identities, preservation."""
from fractions import Fraction as Q
from pathlib import Path
from math import gcd
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'known-point-seven-307'

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]

def dec(x):
    a, b = x
    assert type(a) is int and type(b) is int and b > 0
    assert gcd(abs(a), b) == 1
    return Q(a, b)

def point(p):
    return None if p is None else tuple(map(dec, p))

def mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c

def curve(p):
    x, y = p
    assert y*y+y-x*x*x-x*x+2*x == 0

def line_check(left, right, output, row):
    # Check the whole cubic substitution against its complete factorization,
    # not a repeated implementation of the addition-coordinate formula.
    a, b, c = map(point, (left, right, output))
    for p in (a, b, c):
        assert p is not None
        curve(p)
    x, y = a
    u, v = b
    z, w = c
    m = dec(row['slope'])
    n = y-m*x
    assert v == m*u+n and -w-1 == m*z+n
    if a == b:
        assert row['branch'] == 'tangent'
        denominator = 2*y+1
        assert denominator != 0 and denominator*m == 3*x*x+2*x-2
    else:
        assert row['branch'] == 'chord' and u != x
        denominator = u-x
        assert denominator*m == v-y
    assert dec(row['denominator']) == denominator
    if 'intercept' in row:
        assert dec(row['intercept']) == n
    actual = [n*n+n, 2*m*n+m+2, m*m-1, Q(-1)]
    factored = [-t for t in mul(mul([-x, 1], [-u, 1]), [-z, 1])]
    assert actual == factored
    return {'branch': row['branch'], 'denominator': enc(denominator),
            'slope': enc(m), 'intercept': enc(n),
            'substituted_cubic': list(map(enc, actual)),
            'factored_cubic': list(map(enc, factored)),
            'residuals': list(map(enc, [a-b for a,b in zip(actual, factored)]))}

def main():
    originals = {p.name: digest(p) for p in sorted(SOURCE.iterdir()) if p.is_file()}
    (HERE/'original-hashes.json').write_text(json.dumps(originals, indent=2)+'\n')
    fresh = HERE/'fresh'
    fresh.mkdir(exist_ok=True)
    for name in ('build_certificate.py', 'verify_certificate.py', 'initial-failed-verifier.py.txt'):
        shutil.copyfile(SOURCE/name, fresh/name)
    for name in ('build_certificate.py', 'verify_certificate.py'):
        p = subprocess.run([sys.executable, str(fresh/name)], capture_output=True, text=True)
        (HERE/(name+'.log')).write_text(p.stdout+p.stderr)
        assert p.returncode == 0, name
    assert (fresh/'certificate.json').read_bytes() == (SOURCE/'certificate.json').read_bytes()
    assert (fresh/'verification.json').read_bytes() == (SOURCE/'verification.json').read_bytes()
    cert = json.loads((fresh/'certificate.json').read_text())
    replay = json.loads((fresh/'verification.json').read_text())
    assert replay['status'] == 'PASS' and replay['failures'] == []
    assert replay['certificate_sha256'] == digest(fresh/'certificate.json')
    assert replay['actual_t_v7'] == replay['required_t_v7'] == 1 and replay['threshold_met']
    binary = [line_check(r['left'], r['right'], r['output'], r) for r in cert['chain']]
    seq = replay['sequential_replay']
    assert len(seq) == 13 and seq[0] == {'scalar': 1, 'output': cert['P'], 'branch': 'identity'}
    sequential = []
    for i in range(1, 13):
        assert seq[i]['scalar'] == i+1
        sequential.append(line_check(seq[i-1]['output'], cert['P'], seq[i]['output'], seq[i]))
    assert seq[-1]['output'] == cert['W']
    # Full translation: (X-1/3)^3+(X-1/3)^2-2(X-1/3)+1/4.
    linear = [-Q(1,3), Q(1)]
    square, cube = mul(linear, linear), mul(mul(linear, linear), linear)
    translated = [cube[i]+(square[i] if i<3 else 0)-2*(linear[i] if i<2 else 0)+(Q(1,4) if i==0 else 0) for i in range(4)]
    assert translated == [Q(107,108), -Q(7,3), 0, 1]
    # Translation preserves O and gives Y(-P)=-Y(P); its inverse is explicit.
    x, y = point(cert['W'])
    t = -x/y
    vals = {}
    for name, q, e, f in [('x',x,0,2), ('y',y,0,3), ('t',t,1,0)]:
        a, b = q.numerator, q.denominator
        assert a % (7**e) == 0 and b % (7**f) == 0
        ua, ub = a//7**e, b//7**f
        assert ua % 7 != 0 and ub % 7 != 0
        assert a == 7**e*ua and b == 7**f*ub
        assert cert['valuations'][name] == {'fraction': enc(q), 'numerator_v7':e, 'denominator_v7':f, 'v7':e-f}
        vals[name] = {'numerator':a, 'denominator':b, 'numerator_power':e,
                      'denominator_power':f, 'numerator_unit':ua, 'denominator_unit':ub,
                      'unit_residues':[ua%7, ub%7], 'valuation':e-f}
    t_unit_mod7 = (t.numerator//7)*pow(t.denominator, -1, 7)%7
    assert t_unit_mod7 != 0
    X,Y,Z = cert['projective']['primitive']
    assert gcd(gcd(abs(X), abs(Y)), Z) == 1 and Q(X,Z)==x and Q(Y,Z)==y
    assert Y*Y*Z+Y*Z*Z-X**3-X*X*Z+2*X*Z*Z == 0
    assert [X%7,Y%7,Z%7] == [0,6,0]
    # Reproduce the historical sign failure, without relabeling it a data-rejection test.
    old = subprocess.run([sys.executable, str(fresh/'initial-failed-verifier.py.txt')], capture_output=True, text=True)
    (HERE/'historical-sign-failure.log').write_text(old.stdout+old.stderr)
    assert old.returncode != 0 and 'assert good(r)' in old.stderr and 'AssertionError' in old.stderr
    after = {p.name: digest(p) for p in sorted(SOURCE.iterdir()) if p.is_file()}
    assert originals == after and len(originals) == 6
    report = {'status':'PASS', 'failures':[], 'fresh_certificate_identical':True,
              'fresh_complete_verification_identical':True, 'binary_lines':binary,
              'sequential_lines':sequential, 'identity_rows':1,
              'translation_coefficients':list(map(enc,translated)), 'valuation_witnesses':vals,
              't_divided_by_7_mod_7':t_unit_mod7, 'projective':cert['projective'],
              'actual_t_v7':1, 'required_t_v7':1,
              'historical_sign_failure_reproduced':True,
              'malformed_certificate_tests_claimed':False,
              'original_files_preserved':len(originals), 'original_hashes':originals}
    out = HERE/'audit.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(f'PASS: fresh full replay; 17 rowwise cubic identities, 1 identity row; v7(t) actual=1 required=1; (t/7) mod 7={t_unit_mod7}; 6 originals preserved; failures=0; {out}')

if __name__ == '__main__':
    main()
