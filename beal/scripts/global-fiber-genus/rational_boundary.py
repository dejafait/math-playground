"""Exact bounded evidence for L108; not a full residue-field factorization."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json

out = Path(__file__).with_name('rational-boundary-certificate.json')
checks = {}
def check(name, value):
    checks[name] = bool(value)
def mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c
phi = [1]
for _ in range(5):
    phi = mul(phi, [1,1,3])
phi = mul(phi, [1,-5])
h = [55,165,594,1100,2145,2475,2970,1782,1215]
check('phi_minus_one_is_minus_T_cubed_h', phi == [1,0,0]+[-c for c in h])
check('octic_Eisenstein_eleven', all(c % 11 == 0 for c in h[:-1])
      and h[-1] % 11 != 0 and h[0] % 121 != 0)
check('zero_slope_numerator_norm', 11**2+11*5**2 == 396)
check('zero_slope_norm_v3_exactly_two', 396 % 9 == 0 and 396 % 27 != 0)
check('zero_split_prime_simple', (1**2+11) % 3 == 0 and 2 % 3 != 0)
check('zero_numerator_zero_denominator_unit_at_d_one',
      (11-5) % 3 == 0 and (11+5) % 3 != 0)
eta = Fraction(3,12)
check('one_normalized_unit', eta == Fraction(1,4))

labels = [(r,a,b) for r in range(11)
          for a,b in combinations([i for i in range(11) if i != r],2)]
check('label_cap', len(labels) == 495 <= 1000)
def category_zero(L):
    r,a,b = L
    cluster = lambda i: 'g' if i == 10 else ('a' if i < 5 else 'b')
    R,A,B = map(cluster, (r,a,b))
    if R == 'g':
        return 'r_gamma_pair_same_cluster' if A == B else 'r_gamma_pair_mixed_clusters'
    if 'g' in (A,B):
        other = B if A == 'g' else A
        return 'r_cluster_pair_gamma_same' if other == R else 'r_cluster_pair_gamma_other'
    if A == B == R:
        return 'all_same_cluster'
    if A == B:
        return 'r_cluster_pair_other_cluster'
    return 'r_cluster_pair_same_and_other'
def category_one(L):
    r,a,b = L
    Z = lambda i: i < 3
    n = Z(a)+Z(b)
    return ('r_zero_' if Z(r) else 'r_simple_')+str(n)+'_pair_zero'

def branches(perm, cat):
    unseen = set(labels)
    result = []
    while unseen:
        start = min(unseen)
        cycle, cur = [], start
        while cur in unseen:
            unseen.remove(cur)
            cycle.append(cur)
            r,a,b = cur
            cur = (perm[r], *sorted((perm[a],perm[b])))
        check('cycle_closes_'+str(start)+'_'+cat.__name__, cur == start)
        kinds = {cat(L) for L in cycle}
        check('category_constant_'+str(start)+'_'+cat.__name__, len(kinds) == 1)
        result.append({'labels':cycle, 'e':len(cycle), 'category':kinds.pop()})
    return result
zero = branches([1,2,3,4,0,6,7,8,9,5,10], category_zero)
one = branches([1,2,0,3,4,5,6,7,8,9,10], category_one)
zero_counts = dict(Counter(b['category'] for b in zero))
one_counts = dict(Counter(b['category'] for b in one))
check('zero_99_index_five', len(zero) == 99 and all(b['e']==5 for b in zero))
check('zero_category_counts', zero_counts == {
    'r_gamma_pair_same_cluster':4, 'r_gamma_pair_mixed_clusters':5,
    'r_cluster_pair_gamma_same':8, 'r_cluster_pair_gamma_other':10,
    'all_same_cluster':12, 'r_cluster_pair_other_cluster':20,
    'r_cluster_pair_same_and_other':40})
check('one_category_counts', one_counts == {
    'r_simple_0_pair_zero':168, 'r_simple_1_pair_zero':56,
    'r_simple_2_pair_zero':8, 'r_zero_0_pair_zero':28,
    'r_zero_1_pair_zero':16, 'r_zero_2_pair_zero':1})
check('one_indices', Counter(b['e'] for b in one) == {1:168,3:109})
check('weighted_degree_zero', sum(b['e'] for b in zero) == 495)
check('weighted_degree_one', sum(b['e'] for b in one) == 495)

# At infinity inertia translates all three labels. Setting r=0 leaves
# pairs of distinct nonzero exponents. Cyclotomic descent multiplies them.
pairs = set(combinations(range(1,11),2))
infinity = []
while pairs:
    i,j = min(pairs)
    orbit = sorted({tuple(sorted(((m*i)%11,(m*j)%11))) for m in range(1,11)})
    check('infinity_orbit_disjoint_'+str((i,j)), set(orbit) <= pairs)
    pairs.difference_update(orbit)
    stab = [m for m in range(1,11) if sorted(((m*i)%11,(m*j)%11)) == [i,j]]
    infinity.append({'representative':[i,j], 'orbit':orbit, 'stabilizer':stab,
                     'residue_degree':len(orbit), 'e':11})
check('infinity_residue_degrees', sorted(b['residue_degree'] for b in infinity)==[5,10,10,10,10])
check('infinity_weighted_degree', sum(b['e']*b['residue_degree'] for b in infinity)==495)
check('infinity_stabilizers', all(b['stabilizer'] == ([1,10] if sum(b['representative'])==11 else [1]) for b in infinity))
check('infinity_no_rational_residue_point', all(b['residue_degree']>1 for b in infinity))

failures = [name for name, value in checks.items() if not value]
record = {'scope':'L108 rational boundary selection; nonrational field splitting incomplete',
          'phi_ascending':phi, 'h_ascending':h,
          'zero_slope':{'E':'Q(d), d^2=-11', 'C':'-(11-5d)/(11+5d)',
                        'v_at_split_three_d_one':2, 'required_for_fifth_power':'multiple of 5'},
          'one_normalized_eta':str(eta), 'zero_branches':zero, 'one_branches':one,
          'zero_counts':zero_counts, 'one_counts':one_counts,
          'infinity_arithmetic_orbits':infinity,
          'nonrational_field_decomposition_complete':False,
          'checks':checks,'failures':failures}
out.write_text(json.dumps(record,indent=2)+'\n')
print(f'{sum(checks.values())}/{len(checks)} checks; failures={failures}')
print('Labels 495 <= cap 1000; weighted degrees 495/495/495 required 495 each.')
print('Infinity residue degrees [5,10,10,10,10]; at one eta=1/4; at zero v=2, required 0 mod 5.')
print('Nonrational field decomposition incomplete. Certificate:', out.relative_to(Path.cwd()))
if failures:
    raise SystemExit(1)
