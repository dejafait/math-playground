"""Exact-rational checks and insufficiency test for compression-463.json.

The saved one-time floating proposal is frozen below. Fraction checks
its norm, all interval memberships, a negative artificial box member and
the saved LDL recurrences. The artificial matrix is not the physical form.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
PATH = HERE/'compression-463.json'
data = json.loads(PATH.read_text())
checks, failures = [], []


def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})
    if not condition:
        failures.append(name)


def pair(x):
    return F(x['lo']), F(x['hi'])


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[1], -x[0]


def mul(x, y):
    v = [a*b for a in x for b in y]
    return min(v), max(v)


def square(x):
    return (F(0) if x[0] <= 0 <= x[1] else min(x[0]**2, x[1]**2),
            max(x[0]**2, x[1]**2))


def contains(x, y):
    return x[0] <= y[0] <= y[1] <= x[1]


n = data['parameters']['dimension']
prefix = [[pair(x) for x in row] for row in data['prefix_matrix']]
complete = [[pair(x) for x in row] for row in data['complete_entrywise_enclosure']]
check('dimension is unchanged 64', n == 64)
for r in range(n):
    for s in range(n):
        check(f'prefix ordered and symmetric {r},{s}',
              prefix[r][s][0] <= prefix[r][s][1] and prefix[r][s] == prefix[s][r])
        check(f'complete contains prefix {r},{s}', contains(complete[r][s], prefix[r][s]))

ldl = data['interval_ldl']
ell = [[pair(x) for x in row] for row in ldl['partial_unit_lower']]
pivots = [pair(x) for x in ldl['pivots']]
check('exactly ten strictly positive pivots', len(pivots) == 10 and all(x[0] > 0 for x in pivots))
for j in range(len(pivots)+1):
    numerator = prefix[j][j]
    for k in range(j):
        numerator = add(numerator, neg(mul(square(ell[j][k]), pivots[k])))
    got = pivots[j] if j < len(pivots) else pair(ldl['first_unpaid_pivot']['interval'])
    check(f'full exact pivot recurrence {j}', contains(got, numerator))
    if j == len(pivots):
        check('unpaid pivot contains zero', got[0] <= 0 <= got[1])
        break
    for i in range(j+1, n):
        num = prefix[i][j]
        for k in range(j):
            num = add(num, neg(mul(mul(ell[i][k], ell[j][k]), pivots[k])))
        quotient = mul(num, (1/pivots[j][1], 1/pivots[j][0]))
        check(f'full exact lower recurrence {i},{j}', contains(ell[i][j], quotient))

# A proposed negative matrix inside the available entrywise prefix box.
# Off-diagonals are exact rational midpoints; diagonals are lower endpoints.
artificial = [[prefix[r][s][0] if r == s else sum(prefix[r][s])/2
               for s in range(n)] for r in range(n)]
den = 2**44
nums = [
    -3156075698, -48287561532, -235508472256, -14547060069,
    -986260099505, -1450893252061, 386526990493, -2163977902649,
    1303249645913, 266530787696, 1556569891230, -279347514227,
    511380732571, 1377692155778, -991451984913, 81823494753,
    -1343718007144, 745577557445, 280944533654, -591006184718,
    -12549919044864, 227126844596, -3603861078258, -3051133700210,
    9044181007530, -3576896162661, 326509630594, -2885919655041,
    -2646679636477, 649710621980, -615799117123, 550217563032,
    -552033836043, -46937872856, -66839304231, 95225601321,
    44808356777, -3271802681, 10011128487, 7053206060,
    13150426745, -3284846845, -641330598, -1539715569,
    1235839011, -691545451, 103331532, 214911406,
    446035532, 27534382, -8627545, 58953093,
    -19045878, -9298255, -10089670, 59343703,
    -20631553, 10750611, -18710500, 4358653,
    -28647242, 14572169, -12674199, 10404470]
z = [F(x, den) for x in nums]
norm = sum(x*x for x in z)
energy = sum(z[r]*artificial[r][s]*z[s] for r in range(n) for s in range(n))
for r in range(n):
    for s in range(n):
        check(f'artificial exact matrix in complete box {r},{s}',
              contains(complete[r][s], (artificial[r][s], artificial[r][s])))
check('nonzero exact dyadic direction', norm > 0)
check('artificial member energy strictly below -1e-10', energy < -F(1, 10**10))

# Coarse outward rational display bounds; full rational values are saved.
def coarse(x, scale=10**18):
    lo = (x.numerator*scale)//x.denominator
    return {'lo': str(F(lo, scale)), 'hi': str(F(lo+1, scale))}

out = {
    'status': 'CHECKS_PASS' if not failures else 'CHECKS_FAILED',
    'input_sha256': hashlib.sha256(PATH.read_bytes()).hexdigest(),
    'checks': checks, 'failures': failures,
    'negative_artificial_box_member': {
        'definition': 'prefix lower diagonal endpoints, exact rational off-diagonal midpoints',
        'physical_matrix': False, 'numerators': nums, 'denominator': den,
        'norm2_exact': str(norm), 'energy_exact': str(energy),
        'energy_outward_rational': coarse(energy),
        'rayleigh_outward_rational': coarse(energy/norm),
        'conclusion': 'The coarse interval box admits a negative matrix; it cannot establish universal positive definiteness of its members. This is no negative physical direction.'},
    'required_threshold': 'strictly positive actual compression, or strictly negative actual complete directional upper bound; neither established'}
path = HERE/'compression-checks-463.json'
path.write_text(json.dumps(out, indent=2)+'\n')
print('Exact checks:', len(checks), '; failures:', failures)
print('Artificial-member energy outward bounds:', out['negative_artificial_box_member']['energy_outward_rational'])
print('No physical sign inferred. Full report:', path)
assert not failures
