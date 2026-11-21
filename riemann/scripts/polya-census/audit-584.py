"""Check saved census evidence exactly; do not import or rerun the census."""
from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction as F
import ast
import decimal
import hashlib
import json
from pathlib import Path
import platform
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
OUT = BASE / 'audit-584.json'


def read(name):
    return json.loads((BASE / name).read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pair(value):
    assert len(value) == 2 and all(Decimal(s).is_finite() for s in value)
    a, b = map(F, value)
    assert a <= b
    return a, b


def mul(a, b):
    values = [x*y for x in a for y in b]
    return min(values), max(values)


def sub(a, b):
    return a[0]-b[1], a[1]-b[0]


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def ratio(a, b):
    assert 0 < b[0]
    return mul(a, (1/b[1], 1/b[0]))


def rat(value):
    return {'numerator': str(value.numerator), 'denominator': str(value.denominator)}


saved = read('census-579.json')
prior = read('audit-581.json')
repair = read('exact-machin-583.json')
original_check = read('certificate-check-579.json')
checks = {}
details = {}
failures = []


def check(name, result):
    checks[name] = bool(result)
    if not result:
        failures.append(name)


check('saved_certificate_hash', sha(BASE/'census-579.json') ==
      prior['saved_certificate_sha256'] == repair['provenance']['saved_certificate_sha256'] ==
      original_check['certificate_sha256'])
check('prior_audit_unchanged', sha(BASE/'audit-581.json') ==
      repair['provenance']['audit581_certificate_sha256'] and
      sha(BASE/'audit-581.py') == repair['provenance']['audit581_script_sha256'])
check('repair_script_unchanged', sha(BASE/'exact-machin-583.py') ==
      repair['provenance']['this_script_sha256'])
check('repaired_pi_endpoints', saved['pi'] == repair['saved_pi'] == prior['pi'])
check('prior_repair_all_checks', all(repair['checks'].values()) and not repair['failures'])
hashes = {}
for name, original in saved['input_sha256'].items():
    data = (ROOT/name).read_bytes()
    if name == 'lemmas/L815-polya-census-real-path-tail-bounds.md':
        start = b'<!-- BEGIN STEP581 AUDIT -->\n'
        end = b'<!-- END STEP581 AUDIT -->\n\n'
        assert data.count(start) == data.count(end) == 1
        before, rest = data.split(start)
        _, after = rest.split(end)
        data = before+after
    hashes[name] = {'original': original, 'reconstructed': hashlib.sha256(data).hexdigest()}
check('all_seven_original_inputs', len(hashes) == 7 and
      all(r['original'] == r['reconstructed'] for r in hashes.values()))
details['original_inputs'] = hashes
check('backend_matches', platform.python_version() == saved['backend']['python'] and
      decimal.__libmpdec_version__ == saved['backend']['decimal'])

# No execution of source: identify interval powers syntactically. All other
# powers are Python integer arithmetic; this claim is also reviewed manually.
tree = ast.parse((BASE/'census-579.py').read_text())
atan = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'atan')
power_sites = [n for n in ast.walk(tree) if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow)]
details['power_sites'] = [{'line': n.lineno, 'expression': ast.unparse(n)} for n in power_sites]
check('interval_power_calls_confined_to_atan',
      all(n in list(ast.walk(atan)) for n in power_sites if ast.unparse(n.left) == 'z') and
      sorted(ast.unparse(n.left) for n in power_sites) == ['-1', 'n', 'z', 'z'])

# Reconstruct only the exact grid (not kernel bins or any transform).
grid = []
for k in range(80):
    a, b = Decimal(k)/2, Decimal(k+1)/2
    grid.append([str(a), str(b)])
    assert F(a) == F(k, 2) and F(b) == F(k+1, 2)
check('ambient_grid_is_exact', getcontext().prec == 28 and
      all(pair(r['x']) == (F(k,2), F(k+1,2)) for k, r in enumerate(saved['cells'])))
check('caps_unchanged', saved['caps'] == dict(u_end=3, n_max=4, u_bins=1024,
      x_cells=80, x_width='0.5', adaptive_refinements=0))
details['grid'] = {'x_cells': grid, 'ambient_precision': getcontext().prec,
                   'u_width_exact': rat(F(3,1024)), 'u_end': 3,
                   'u_vertices_exact': all(F(3*k,1024).denominator <= 1024 for k in range(1025)),
                   'argument_bound': '0 <= x*u <= 120; |mid/256| <= 15/32 < 1'}

f0, s0, normal = (pair(saved[k]) for k in ('F0', 'S0', 'normalization'))
check('normalization_positive', f0[0] > 0 and s0[0] > F(64,1000) and normal[0] > 0)
check('normalization_encloses_full_quotient', contains(normal, ratio(f0, s0)))
nt, ut = pair(saved['n_tail_all_j']), pair(saved['u_tail_all_j'])
check('positive_tail_bounds', 0 < nt[0] <= nt[1] < F(152,10**24) and
      0 < ut[0] <= ut[1] < F(137,10**545))
details['constants'] = {k: saved[k] for k in
    ('pi','F0','S0','normalization','n_tail_all_j','u_tail_all_j')}

rows = []
for i, r in enumerate(saved['cells']):
    assert len(r['F']) == len(r['G']) == 3
    f, g = [pair(v) for v in r['F']], [pair(v) for v in r['G']]
    w, wp = pair(r['W']), pair(r['Wp'])
    same_sign = (f[0][0] > 0 and g[0][0] > 0) or (f[0][1] < 0 and g[0][1] < 0)
    nonzero_w = w[0] > 0 or w[1] < 0
    expected = 'same_sign_event_exclusion' if same_sign else 'W_event_exclusion' if nonzero_w else 'unresolved'
    checks_i = dict(classification=r['kind'] == expected,
                   exact_x_cell=pair(r['x']) == (F(i,2), F(i+1,2)),
                   W_inclusion=contains(w, sub(mul(f[0],g[1]), mul(g[0],f[1]))),
                   Wp_inclusion=contains(wp, sub(mul(f[0],g[2]), mul(g[0],f[2]))))
    rows.append(dict(index=i, x=r['x'], kind=r['kind'], checks=checks_i,
                     F=r['F'], G=r['G'], W=r['W'], Wp=r['Wp']))
    if not all(checks_i.values()):
        failures.append(f'cell_{i}')
check('every_saved_interval_and_cell', len(rows) == 80 and all(all(r['checks'].values()) for r in rows))
check('closed_cover', len(rows) == 80 and pair(rows[0]['x'])[0] == 0 and
      pair(rows[-1]['x'])[1] == 40 and
      all(pair(rows[i]['x'])[1] == pair(rows[i+1]['x'])[0] for i in range(79)))
check('saved_cover_flag', saved['coverage'] is True)
check('classification_counts', Counter(r['kind'] for r in rows) == saved['counts'] ==
      {'same_sign_event_exclusion': 13, 'unresolved': 67})
exclusions = [dict(index=r['index'], x=r['x'], F_lower=r['F'][0][0], G_lower=r['G'][0][0])
              for r in rows if r['kind'] == 'same_sign_event_exclusion']
check('exact_excluded_cells', [r['index'] for r in exclusions] == list(range(13)))
check('no_event_claim', saved['events'] == [])
min_f = min(F(r['F_lower']) for r in exclusions)
min_g = min(F(r['G_lower']) for r in exclusions)
check('positive_margins', min_f > F(1609,10000) and min_g > F(304,10000))
details['margins'] = {'F_min_exact': rat(min_f), 'G_min_exact': rat(min_g),
                     'F_min_cell': min(exclusions,key=lambda r:F(r['F_lower']))['index'],
                     'G_min_cell': min(exclusions,key=lambda r:F(r['G_lower']))['index'],
                     'required': 'both strictly positive',
                     'verified_lower_bounds': ['F > 0.1609', 'G > 0.0304', 'S(0) > 0.064']}

report = dict(step='584', scope='static inclusion audit in L815 plus exact saved-evidence checks; no census replay',
              this_script_sha256=sha(Path(__file__)),
              input_hashes={n:sha(BASE/n) for n in ('census-579.py','census-579.json','audit-581.py',
                           'audit-581.json','exact-machin-583.py','exact-machin-583.json')},
              checks=checks, details=details, exclusions=exclusions, cells=rows,
              failures=failures, conclusion='PASS' if not failures else 'FAIL',
              limitations=['Stored integrals are not independently recomputed or replayed.',
                           'This checker is not by itself an analytic inclusion proof; see L815 step584.',
                           'The original interval power remains invalid; only the saved pi input is repaired.',
                           '[6.5,40] retained as unresolved; no events, orientations or RH conclusion.'])
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(dict(certificate=str(OUT.relative_to(ROOT)), checks_passed=sum(checks.values()),
                     checks_required=len(checks), cells_checked=len(rows), exclusions=len(exclusions),
                     actual_bounds=details['margins']['verified_lower_bounds'],
                     required='F and G lower endpoints > 0 on each excluded closed cell; S0 lower > 0',
                     failures=failures, conclusion=report['conclusion'])))
sys.exit(0 if not failures else 1)
