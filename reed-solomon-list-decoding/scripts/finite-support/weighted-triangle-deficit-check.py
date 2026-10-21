"""One exact common-normalization hypothesis test; no feasibility solve."""
import hashlib
import json
from fractions import Fraction as Q
from math import comb
from pathlib import Path

B = Path(__file__).parent
source = B / 'delsarte-lp-results.json'
out = B / 'weighted-triangle-deficit-results.json'
lp = json.loads(source.read_text())
g = [comb(68, i)*comb(956, i) for i in range(69)]
H = comb(1024, 68)
N = 65537**28//2**128+1
U = Q(comb(1024, 64), comb(68, 64))
alpha = Q(2*(N-1), U-1)
a = [Q(r['numerator'], r['denominator']) for r in lp['exact']['primal']]
c = [Q(1)]+[Q(0)]*4+[alpha*x/(2*g[i]) for i, x in zip(range(5, 69), a)]
demand = [(N-2)*x for x in c[1:]]
cmax = max(c[1:])
divisor = (N-2)*cmax
phi = [Q(0)]+[x/divisor for x in demand]
edges = [0]+[H*g[i]//2 for i in range(1, 69)]
deficit = sum((edges[i]*(1-phi[i]) for i in range(1, 69)), Q(0))
required = H-4
forbidden = sum(edges[1:5])
checks = {
    '69_coordinates': len(c) == 69,
    'positive_N_minus_2': N > 2,
    'mixture': 0 < alpha < 1,
    'positive_permitted_pairs': all(x > 0 for x in c[5:]),
    'forbidden_zero': c[1:5] == [0]*4,
    'objective_N': sum(g[i]*c[i] for i in range(69)) == N,
    'all_edge_products_even': all(H*g[i] % 2 == 0 for i in range(1, 69)),
    'full_unordered_count': sum(edges) == comb(H, 2),
    'normalization_in_unit_interval': all(0 <= x <= 1 for x in phi),
    'normalization_attains_one': max(phi) == 1,
    'closed_deficit_formula': deficit == Q(H, 2)*(H-1-Q(N-1)/cmax),
    'forbidden_bound': deficit >= forbidden >= edges[1],
    'distance_one_formula': edges[1] == 32504*H,
    'strict_failure': deficit > required,
}
def enc(x):
    x = Q(x)
    return {'numerator': x.numerator, 'denominator': x.denominator}
data = dict(input_path=str(source.relative_to(B.parent.parent)),
            input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
            H=H, N=N, U=enc(U), alpha=enc(alpha),
            coordinates=[dict(i=i, g=g[i], c=enc(c[i]),
                              demand=enc((N-2)*c[i]) if i else None,
                              phi=enc(phi[i]) if i else None,
                              unordered_edges=edges[i]) for i in range(69)],
            maximizing_distances=[i for i in range(1, 69) if c[i] == cmax],
            cmax=enc(cmax), optimal_common_divisor=enc(divisor),
            actual_deficit=enc(deficit), required_maximum=required,
            comparison_slack=enc(deficit-required),
            forbidden_deficit=forbidden, distance_one_deficit=edges[1],
            checks=checks, failures=[k for k, ok in checks.items() if not ok])
out.write_text(json.dumps(data, indent=2)+'\n')
print('FAILS missing-weight hypothesis; actual deficit >= 32504*H; required <= H-4')
print('Maximizing half-distances:', data['maximizing_distances'])
print('Checks:', len(checks), 'failures:', data['failures'])
print('Full exact certificate:', out)
assert not data['failures']
