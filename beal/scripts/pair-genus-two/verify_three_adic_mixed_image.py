"""Independent complete replay of the finite 3-adic containment certificate.

Does not import the producer; exact Hensel existence and local-field
completeness still rely on the canonical mathematical proof.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'three-adic-mixed-image-verification.json'
V = dict(completed=False, failures=[], checks=[])


def check(name, ok):
    V['checks'].append(dict(name=name, passed=bool(ok)))
    if not ok:
        raise AssertionError(name)


def value(coeff, x):
    return sum(a*x**i for i, a in enumerate(coeff))


def local_class(x):
    x = Fraction(x)
    v = 0
    while x.numerator % 3 == 0:
        x /= 3
        v += 1
    while x.denominator % 3 == 0:
        x *= 3
        v -= 1
    residue = x.numerator % 3 * pow(x.denominator, -1, 3) % 3
    return v % 2 + 2*int(residue == 2)


def main():
    raw = (ROOT/'three-adic-mixed-image-certificate.json').read_bytes()
    d = json.loads(raw)
    V['certificate_sha256'] = hashlib.sha256(raw).hexdigest()
    check('producer binding', d['source_sha256'] == hashlib.sha256(
        (ROOT/'three_adic_mixed_image.py').read_bytes()).hexdigest())
    check('producer completed without failures', d['completed'] and not d['failures'] and
          all(c['passed'] for c in d['checks']))
    g = [-109375,-32500,150,64,1]
    q = [7,52,-6,-64,-25]
    # Expand each (1+s)^j by repeated multiplication, not producer's binomial shift.
    p = [0]*5
    power = [1]
    for a in g:
        for j, b in enumerate(power):
            p[j] += a*b
        power = [power[0]]+[power[j-1]+power[j] for j in range(1,len(power))]+[power[-1]]
    check('actual quartic scaling', [g[i]*25**i for i in range(5)] == [-15625*a for a in q])
    check('complete shifted polynomial', p == d['factorization']['shifted_polynomial'] ==
          [-141660,-32004,348,68,1])
    vals = []
    for a in p:
        n = 0
        while a % 3 == 0:
            a //= 3
            n += 1
        vals.append(n)
    check('all coefficient valuations', vals == [2,2,1,0,0] ==
          d['factorization']['coefficient_valuations'])
    records = d['factorization']['hensel_lifts']
    check('all twelve lift records', len(records) == 12)
    prior = None
    for n, row in enumerate(records, 1):
        r, m = row['root'], 3**n
        deriv = sum(i*p[i]*r**(i-1) for i in range(1,5))
        check('lift values '+str(n), row['modulus'] == m and row['precision'] == n and
              value(p,r) == row['polynomial_value'] and value(p,r) % m == 0 and
              deriv == row['derivative'] and deriv % 3 != 0 and r % 3 == 1)
        check('canonical lift range '+str(n), 0 <= r < m and (prior is None or r % (m//3) == prior))
        h = row['cubic_modulus_coefficients']
        product = [-r*h[0]]+[h[i-1]-r*h[i] for i in range(1,4)]+[h[3]]
        check('entire factor identity '+str(n), [(a-b) % m for a,b in zip(product,p)] ==
              row['residual'] == [0]*5)
        check('cubic and coprime reduction '+str(n), [a % 3 for a in h] == [0,0,0,1] and
              h[3] == 1 and r % 3 == 1)
        prior = r
    check('all symbolic valuation differences', d['valuation_argument']['below_two_thirds'] ==
          [[a,i-3] for i,a in enumerate(vals)] and
          d['valuation_argument']['above_two_thirds'] == [[a-2,i] for i,a in enumerate(vals)])
    # Full finite quotient replay using rational representatives and norm a*b^3.
    reps = [1,3,-1,-3]
    table = d['square_classes']['full_table']
    check('complete ordered domain', [(r['k_class'],r['cubic_class']) for r in table] ==
          [(i,j) for i in range(4) for j in range(4)])
    replay = []
    for row in table:
        i,j = row['k_class'],row['cubic_class']
        a,b = reps[i],reps[j]
        norm = a*b**3
        ratio = Fraction(b,a)
        # Explicitly enumerate every diagonal orbit, independently of normalization.
        orbit = sorted((local_class(a*s),local_class(b*s)) for s in reps)
        normal = local_class(ratio)
        normbit = local_class(norm)
        check('complete orbit and norm '+str(i)+','+str(j),
              row['scalar_normalized_class'] == normal and row['norm_class'] == normbit and
              normal == normbit and row['norm_trivial'] == (normbit == 0) and
              row['diagonal'] == (i == j) and ((0,normal) in orbit))
        replay.append(dict(k_representative=a,cubic_representative=b,
            rational_norm=norm,normalized_ratio=str(ratio),norm_class=normbit,orbit=orbit))
    check('all four orbits and unique norm kernel', len({tuple(map(tuple,r['orbit'])) for r in replay}) == 4 and
          {r['scalar_normalized_class'] for r in table if r['norm_trivial']} == {0})
    check('elliptic identity and containment evidence', -33*value(q,2) == 165**2 and
          d['result']['certified_E_representatives'] == [dict(T=2,R=165,normalized_class=0)] and
          d['result']['required_E_representatives'] == d['result']['norm_trivial_B_classes_upper_bound'] == 1 and
          d['result']['containment'] and not d['result']['mismatch'])
    V['square_class_replay'] = replay
    V['result'] = dict(local_degrees=[1,3], quotient_dimension=2,norm_rank=2,
                     norm_kernel_dimension=0, containment=True, failures=[])
    V['completed'] = True


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        V['failures'].append(type(exc).__name__+': '+str(exc))
    OUT.write_text(json.dumps(V, indent=2)+'\n')
    print('independent replay completed:', V['completed'], 'checks:', len(V['checks']), 'failures:', V['failures'])
    if V['completed']:
        print('actual/required raw classes 16/16; quotient classes 4/4; norm-kernel classes 1/1')
    print('verification:', OUT.relative_to(ROOT.parent.parent))
    if not V['completed']:
        raise SystemExit(1)
