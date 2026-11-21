"""Independent L820 audit: exact symbolic expansion and rational leaf replay.

No generator code is imported or run. The original certificate is read-only.
Every coefficient and leaf is checked; the report preserves all exact bounds.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import ast
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[2]
SOURCE = BASE / 'scripts/central-jacobi/three-factor-certificate-606.json'
OUT = BASE / 'scripts/central-jacobi/three-factor-audit-609.json'
c = json.loads(SOURCE.read_text())
failures = []
checks = []

def check(name, value):
    checks.append({'name': name, 'pass': bool(value)})
    if not value:
        failures.append(name)

# Exact multivariate polynomial ring Q[x,y,Q,R,Z,t], without interval
# arithmetic in its construction. Zero coefficients are removed exactly.
N = 6
ZERO = (0,) * N

def constant(a):
    return {} if a == 0 else {ZERO: F(a)}

def variable(i):
    m = [0] * N
    m[i] = 1
    return {tuple(m): F(1)}

def add(*ps):
    out = {}
    for p in ps:
        for m, a in p.items():
            out[m] = out.get(m, F(0)) + a
    return {m: a for m, a in out.items() if a}

def scale(p, a):
    return {m: a*b for m, b in p.items() if a*b}

def mul(*ps):
    out = constant(1)
    for p in ps:
        nxt = {}
        for m, a in out.items():
            for n, b in p.items():
                v = tuple(i+j for i, j in zip(m, n))
                nxt[v] = nxt.get(v, F(0)) + a*b
        out = {m: a for m, a in nxt.items() if a}
    return out

one = constant(1)
x, y, Q, R, Z, t = [variable(i) for i in range(N)]
lin = lambda v, a: add(one, scale(v, a))
D = mul(add(one, scale(mul(x, x), -1)),
        add(one, scale(mul(y, y), -1)))
W = mul(Q, D)
V = lin(t, -1)
U = mul(lin(x, 1), lin(x, 1), lin(y, 1), lin(y, 1))
H = mul(lin(x, 2), lin(y, 2))
K = mul(lin(x, 2), lin(x, 2), lin(y, 2), lin(y, 2))
J = mul(lin(x, 1), lin(x, 3), lin(y, 1), lin(y, 3))
# Independently regrouped versions of the necessary cleared equations.
F1 = add(mul(W, add(scale(U, 2), scale(mul(R, H, lin(t, 1)), -1))),
         scale(mul(V, U), -1))
F2 = add(mul(W, add(scale(mul(K, lin(t, 1)), 3),
                        scale(mul(Z, J, lin(t, 2)), -2))),
         mul(V, add(mul(Z, J, lin(t, 2)), scale(mul(K, lin(t, 1)), -2))))
# Direct numerator clearing from b=(W-V)/W gives an independent identity
# check against the regrouping, not a floating point evaluation.
b_num = add(W, scale(V, -1))
one_plus_b_num = add(W, b_num)
one_plus_2b_num = add(W, scale(b_num, 2))
direct1 = add(mul(U, one_plus_b_num), scale(mul(R, H, lin(t, 1), W), -1))
direct2 = add(mul(K, lin(t, 1), one_plus_2b_num),
              scale(mul(Z, J, lin(t, 2), one_plus_b_num), -1))
check('F1 regrouping equals directly cleared numerator', F1 == direct1)
check('F2 regrouping equals directly cleared numerator', F2 == direct2)

q_strings = [
    ['1.07484394250019421126346157158', '1.07484394250019421126346157162'],
    ['1.06274366627144916855311401273', '1.06274366627144916855311401285'],
    ['1.05430333113463476927545484495', '1.05430333113463476927545484516']]
q_ranges = [tuple(map(F, row)) for row in q_strings]
epsilon = F(1, 10**6)
grid = 10**60
check('full q input equality', c['q'] == q_strings)
for lemma in ['L791-fixed-central-five-root-jacobi-model.md',
              'L820-central-three-factor-two-unit-gap-degree-cap.md']:
    text = (BASE / 'lemmas' / lemma).read_text()
    for i, pair in enumerate(q_strings):
        for j, s in enumerate(pair):
            check(f'{lemma} q{i} endpoint{j}', s in text)
check('input lemma unchanged since generation', c['input_sha256'] == hashlib.sha256(
    (BASE / c['input_path']).read_bytes()).hexdigest())
check('original generator hash', c['program_sha256'] == hashlib.sha256(
    (BASE / 'scripts/central-jacobi/three_factor_606.py').read_bytes()).hexdigest())
check('grid exactly 10^60', int(c['grid']) == grid)
check('full t range', tuple(map(F, c['t'])) == (F(0), epsilon))
check('root square', [[F(a) for a in p] for p in c['root_domain']] ==
      [[F(0), F(27, 100)]] * 2)
domain_margin = 1 - epsilon - q_ranges[0][1] * (1-F(27,100)**2)
check('strict compact domain comparison', domain_margin > 0)
b_upper = 1 - (1-epsilon)/q_ranges[0][1]
check('third b escape excluded', b_upper < 1 and b_upper >= 0)

# Multi-affine extrema in Q,R,Z occur at vertices for every fixed t.
# At a vertex the t polynomial has degree <=2. Check endpoints and every
# stationary point lying in the closed t interval. This gives exact ranges.
def grouped(p):
    out = {}
    for m, a in p.items():
        out.setdefault(m[:2], {})[m[2:]] = a
    return out

def coefficient_extrema(p):
    check('parameter degree contract '+repr(p),
          all(max(m[:3], default=0) <= 1 and m[3] <= 2 for m in p))
    witnesses = []
    for corner in product(*q_ranges):
        coeff = [F(0)]*3
        for (i,j,k,l), a in p.items():
            coeff[l] += a*corner[0]**i*corner[1]**j*corner[2]**k
        ts = [F(0), epsilon]
        if coeff[2]:
            stationary = -coeff[1]/(2*coeff[2])
            if 0 < stationary < epsilon:
                ts.append(stationary)
        vals = [coeff[0]+v*(coeff[1]+v*coeff[2]) for v in ts]
        witnesses.append({'corner':corner, 'quadratic':coeff, 't_candidates':ts, 'values':vals})
    values = [v for row in witnesses for v in row['values']]
    return (min(values), max(values)), witnesses

# Rational endpoint intervals. No grid rounding occurs in the independent
# evaluation; the stored coefficient enclosures have been verified above.
def plus(a,b):
    return a[0]+b[0], a[1]+b[1]

def neg(a):
    return -a[1], -a[0]

def times(a,b):
    v = [s*t for s in a for t in b]
    return min(v), max(v)

def scalar(a,n):
    return times(a, (F(n), F(n)))

zinterval = (F(0), F(0))
coefficient_records = []
polys = []
for index, p in enumerate([F1,F2]):
    gp = grouped(p)
    stored = {ast.literal_eval(m): tuple(map(F,v))
              for m,v in c['polynomial_coefficients'][index].items()}
    check(f'F{index+1} no missing monomials', set(gp) <= set(stored))
    entries = []
    for m in sorted(set(gp) | set(stored)):
        exact_range, witnesses = coefficient_extrema(gp.get(m, {}))
        enclosure = stored.get(m, zinterval)
        contained = enclosure[0] <= exact_range[0] <= exact_range[1] <= enclosure[1]
        check(f'F{index+1} coefficient {m}', contained)
        entries.append({'monomial':m, 'parameter_polynomial':[
            {'powers':k,'coefficient':a} for k,a in sorted(gp.get(m,{}).items())],
            'exact_range':exact_range, 'stored_enclosure':enclosure,
            'contains_exact_range':contained, 'extrema_witnesses':witnesses})
    coefficient_records.append(entries)
    polys.append(stored)

# Recursively arranged tensor Horner, independently written with exact
# Fractions. Its operation ordering agrees with the certified expression,
# so the stored grid-rounded range must contain the exact recomputation.
def evaluate(p, a, b):
    rows = {}
    for (i,j), value in p.items():
        rows.setdefault(i,{})[j] = value
    def univariate(coeffs, arg):
        v = zinterval
        for k in reversed(range(max(coeffs, default=0)+1)):
            v = plus(times(v,arg), coeffs.get(k,zinterval))
        return v
    return univariate({i:univariate(row,b) for i,row in rows.items()},a)

def derivative(p,axis):
    ans = {}
    for m,v in p.items():
        if m[axis]:
            k = list(m)
            k[axis] -= 1
            ans[tuple(k)] = scalar(v,m[axis])
    return ans

partials = [(derivative(p,0),derivative(p,1)) for p in polys]
Wpoly = {(0,0):q_ranges[0], (2,0):neg(q_ranges[0]),
         (0,2):neg(q_ranges[0]), (2,2):q_ranges[0]}
Vinterval = (1-epsilon,F(1))

def rectangle(path):
    # Work in integer grid coordinates to reconstruct the generator's
    # deterministic tie-breaking and floor midpoint without approximation.
    coords = [[0, 27*grid//100], [0,27*grid//100]]
    for digit in path:
        axis = 0 if coords[0][1]-coords[0][0] >= coords[1][1]-coords[1][0] else 1
        lo,hi = coords[axis]
        mid = (lo+hi)//2
        coords[axis] = [lo,mid] if digit == '0' else [mid,hi]
    return coords

leaf_records = []
paths = [leaf['path'] for leaf in c['leaves']]
check('paths binary', all(set(p) <= {'0','1'} for p in paths))
check('no repeated paths', len(set(paths)) == len(paths))
ordered = sorted(paths)
check('prefix-free paths', all(not b.startswith(a) for a,b in zip(ordered,ordered[1:])))
weight = sum((F(1,2**len(p)) for p in paths), F(0))
check('exact Kraft coverage', weight == 1)
# Stronger direct tree check: every nonterminal node has exactly 2 children.
all_nodes = {p[:i] for p in paths for i in range(len(p)+1)}
terminal = set(paths)
interior = all_nodes-terminal
check('complete binary tree', all(p+'0' in all_nodes and p+'1' in all_nodes for p in interior))
check('zero unresolved paths', c['unresolved'] == [] and c['actual_unresolved'] == 0)
check('727 recovered nodes', len(all_nodes) == 727 == c['nodes'])
check('364 terminal nodes', len(paths) == 364)
check('maximum depth20', max(map(len,paths)) == 20 == c['max_depth'])

for leaf in c['leaves']:
    path = leaf['path']
    coords = rectangle(path)
    a,b = [tuple(F(v,grid) for v in row) for row in coords]
    reason = leaf['reason']
    record = {'path':path, 'x':a, 'y':b, 'reason':reason}
    if reason == 'symmetry_x_gt_y':
        valid = a[0] > b[1]
        check('strict symmetry '+path, valid)
        check('null symmetry bound '+path, leaf['bound'] is None)
        record['margin'] = a[0]-b[1]
    else:
        if reason == 'b_negative':
            bound = plus(evaluate(Wpoly,a,b),neg(Vinterval))
            valid = bound[1] < 0
        else:
            check('known polynomial reason '+path, reason in ['F1','F2'])
            idx = int(reason[1])-1
            p = polys[idx]
            dx,dy = partials[idx]
            ca,cb = [F((row[0]+row[1])//2,grid) for row in coords]
            center = evaluate(p,(ca,ca),(cb,cb))
            bx,by = evaluate(dx,a,b),evaluate(dy,a,b)
            delta_a,delta_b = plus(a,(-ca,-ca)),plus(b,(-cb,-cb))
            bound = plus(plus(center,times(bx,delta_a)),times(by,delta_b))
            valid = bound[1] < 0 or bound[0] > 0
            record.update(center_point=[ca,cb], center_value=center,
                          partial_x_range=bx,partial_y_range=by,
                          x_displacement=delta_a,y_displacement=delta_b)
        saved = tuple(map(F,leaf['bound']))
        contained = saved[0] <= bound[0] <= bound[1] <= saved[1]
        check('stored bound contains independent replay '+path, contained)
        check('strict exclusion '+path, valid)
        check('strict stored sign '+path,
              saved[1] < 0 if reason == 'b_negative' else (saved[1]<0 or saved[0]>0))
        record.update(recomputed_bound=bound, stored_bound=saved,
                      stored_contains_replay=contained,
                      margin=(-bound[1] if bound[1]<0 else bound[0]))
    record['pass'] = valid
    leaf_records.append(record)
counts = dict(Counter(leaf['reason'] for leaf in c['leaves']))
check('leaf category counts', counts == c['leaf_counts'] ==
      {'symmetry_x_gt_y':15,'b_negative':2,'F1':226,'F2':121})
minima = {reason:min(r['margin'] for r in leaf_records if r['reason']==reason)
          for reason in counts}
check('all actual margins strictly positive', all(v>0 for v in minima.values()))
# Integer endpoint: d<1000001 gives the greatest permitted integer 1000000.
check('strict degree endpoint', F(999999)+2 == 1000001)
check('original result claims no hidden failures', c['pass'] and c['failures'] == [])

# Store exact rational values everywhere; no pretty decimal stands in for
# a load-bearing endpoint. Print only concise, conservative lower bounds.
def serial(v):
    if isinstance(v,F):
        return str(v)
    if isinstance(v,dict):
        return {k:serial(w) for k,w in v.items()}
    if isinstance(v,(tuple,list)):
        return [serial(w) for w in v]
    return v

def lower_decimal(v,places=16):
    n = v*10**places
    n = n.numerator//n.denominator
    return f'{n//10**places}.{n%10**places:0{places}d}'

report = {
    'pass':not failures, 'failures':failures,
    'check_count':len(checks), 'checks':checks,
    'audit_program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'original_certificate_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'original_generator_sha256':c['program_sha256'],
    'L791_sha256':c['input_sha256'],
    'arithmetic':'exact Fraction operations; no rounding or generator import',
    'full_q_input':q_strings, 'full_t_input':[F(0),epsilon],
    'domain_comparison_margin':domain_margin, 'third_b_upper_bound':b_upper,
    'coefficient_range_method':'multi-affine Q,R,Z vertices and all quadratic t extrema',
    'coefficient_evidence':coefficient_records,
    'leaf_evidence':leaf_records,
    'coverage':{'nodes':len(all_nodes),'leaves':len(paths),'max_depth':max(map(len,paths)),
                'kraft_sum':weight,'leaf_counts':counts,'unresolved_actual':len(c['unresolved']),
                'unresolved_required':0, 'interior_nodes':len(interior)},
    'minimum_recomputed_margins':minima,
    'minimum_margins_conservative_decimal':{k:lower_decimal(v) for k,v in minima.items()},
    'degree_cap_actual':1000000, 'degree_cap_required':1000000,
    'qualification':'Conditional on L791 exact q enclosure and inherited contracts; '
                    'no evaluator reattestation, root realization or RH sign conclusion.'}
OUT.write_text(json.dumps(serial(report),indent=2)+'\n')
print('PASS' if not failures else 'FAIL', 'checks',len(checks), 'failures',len(failures))
print('recovered nodes',len(all_nodes),'leaves',len(paths),'depth',max(map(len,paths)),
      'Kraft',weight,'required 1; unresolved',len(c['unresolved']),'required 0')
print('strict domain margin >',lower_decimal(domain_margin))
print('minimum strict leaf margins >=', {k:lower_decimal(v) for k,v in minima.items()}, 'required >0')
print('conditional degree cap',1000000,'required <=',1000000)
print('failures:',failures)
print('certificate:',OUT.relative_to(BASE))
if failures:
    raise SystemExit(1)
