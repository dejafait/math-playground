"""Critical audit of L115 only; preserve inputs and replay to a new file.

No solve, changed box, other-shell test or source discovery. The imported
complete spectral theorem remains the proof input; direct signed subset
counts below independently check its finite normalization.
"""
from collections import Counter
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from math import comb, factorial
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'l115-critical-audit.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(name):
    p = B / name
    if p.suffix == '.gz':
        with gzip.open(p, 'rt') as f:
            return json.load(f)
    return json.loads(p.read_text())


def enc(x):
    return [x.numerator, x.denominator]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    counts = Counter()
    report = dict(stage='in_progress', failures=[], code_sha256=sha(Path(__file__)))

    def save():
        report.update(checks=sum(counts.values()), checks_by_kind=dict(counts))
        OUT.write_text(json.dumps(report, indent=2) + '\n')

    def ck(kind, ok, detail=None):
        counts[kind] += 1
        if not ok:
            report['failures'].append(dict(kind=kind, detail=detail))
            report['stage'] = 'failed'
            save()
            raise AssertionError((kind, detail))

    files = ['fixed-product-five-shell.json', 'fixed-product-five-shell-verification.json',
             'fixed_product_five_shell.py', 'verify_fixed_product_five_shell.py',
             'positive-factor-enclosure.json.gz', 'l112-l113-critical-audit.json',
             'l114-critical-audit.json']
    report['input_sha256'] = {str((B/p).relative_to(ROOT)): sha(B/p) for p in files}
    save()
    spec = importlib.util.spec_from_file_location('l115_replay', B/'verify_fixed_product_five_shell.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.OUT = B/'l115-critical-reverification.json'
    mod.main()
    original = read('fixed-product-five-shell-verification.json')
    replay = read('l115-critical-reverification.json')
    ck('complete_replay_equality', replay == original)
    source = read('fixed-product-five-shell.json')
    z = read('positive-factor-enclosure.json.gz')
    c = list(map(lambda v: F(*v), source['c']))

    # Reuse the retained audits, checking every binding rather than their flags alone.
    for name, code in [('l112-l113-critical-audit.json', 'critical_audit_l112_l113.py'),
                       ('l114-critical-audit.json', 'critical_audit_l114.py')]:
        audit = read(name)
        ck('retained_audit_status_and_code', audit['stage'] == 'verified' and
           not audit['failures'] and audit['code_sha256'] == sha(B/code), name)
        for p, digest in audit['input_sha256'].items():
            ck('retained_audit_input', sha(ROOT/p) == digest, p)
        for p, digest in audit.get('replay_sha256', {}).items():
            ck('retained_audit_replay', sha(B/p) == digest, p)
    lower = read('l114-critical-audit.json')
    ck('complete_lower_rows', len(lower['rows']) == 64)
    for i, row in enumerate(lower['rows'], 5):
        ck('retained_lower_minimum', row['i'] == i and
           F(row['pair_numerator'], row['denominator']) == c[i] and
           row['reconstructed_minimum_numerator'] == 2*row['pair_numerator'] and
           row['distinct_lower_sum_numerator'] == row['required'] == 0, i)
    margins = [min(l+z['radius'], z['radius']-u) for l,u in z['krawczyk_image']]
    ck('retained_root_margins', margins == z['inclusion_margins'] and
       len(margins) == 64 and min(margins) ==
       read('l112-l113-critical-audit.json')['minimum_margin_units'] > 0)

    g = [comb(68,i)*comb(956,i) for i in range(69)]
    S = g[5]
    ck('positive_homogeneous_scale', F(*source['rho']) == F(source['N'], source['H']) > 0)
    ck('canonical_pair_bounds', c[0] == 1 and c[1:5] == [0]*4 and
       all(0 < x <= 1 for x in c[5:]))
    ck('full_dictionary_shape', [(v['r'],v['q']) for v in replay['dictionary']] ==
       [(r,q) for r in range(6) for q in range(6)])
    endpoint_types = Counter()
    for row in replay['dictionary']:
        r,q = row['r'], row['q']
        # Masks 0,...,7 encode membership in A,B,C, with A in bit zero.
        atoms = [951-q, 5-r, q, r, q, r, 5-q, 63-r]
        ck('manuscript_full_atoms', row['atoms'] == atoms, [r,q])
        ck('six_orders', sorted(p['order'] for p in row['presentations']) ==
           [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]], [r,q])
        for p in row['presentations']:
            i,j,t,s = p['orbit']
            h = p['h']
            head = factorial(68)//(factorial(i-t)*factorial(j-t)*factorial(t)*factorial(68-i-j+t))
            tail = factorial(956)//(factorial(i-s)*factorial(j-s)*factorial(s)*factorial(956-i-j+s))
            ck('source_multinomial_normalization', head*tail == p['full_count'] == g[i]*p['D'],
               [r,q,p['order']])
            if min(i,j,h) == 0:
                endpoint_types['coincident' if i == 0 else 'first' if j == 0 else 'second'] += 1
        ck('Boolean_or_null_or_product',
           (row['interval'] == [enc(c[5]),enc(c[5])] if r+q == 0 else
            row['interval'] == [[0,1],[0,1]] if r+q < 5 else
            F(*row['interval'][0]) > 0), [r,q])
    ck('both_endpoints_and_coincidence', endpoint_types == dict(first=2,second=2,coincident=2))

    # Direct action at a five-set containing k designated positive members,
    # no negative partners, and 5-k ordinary members. For a neighboring
    # five-set, let zneg count negative partner choices and b its ordinary
    # intersection. This counts signed subsets, not source beta coefficients.
    action_records = []
    for factor in source['factors']:
        n = factor['n']
        for k in range(6):
            actions = [0]*6
            terms = []
            for zneg in range(k+1):
                for b in range(6-k):
                    r = 5-(k-zneg+b)
                    term = (-1)**zneg*comb(k,zneg)*comb(5-k,b)*choose(n-5-k,5-k-b)
                    actions[r] += term
                    terms.append(dict(negative_choices=zneg, ordinary_intersection=b,
                                      distance=r, signed_count=term))
            ck('signed_subset_action', actions == factor['eigenmatrix'][k], [n,k])
            action_records.append(dict(n=n,k=k,terms=terms,actions=actions))

    modes = replay['modes']
    ck('complete_modes_and_positive_dimensions', [(m['a'],m['b']) for m in modes] ==
       [(a,b) for a in range(6) for b in range(6)] and
       all(m['multiplicity'] > 0 for m in modes) and
       sum(m['multiplicity'] for m in modes) == S == 68643272053310642688)
    normalized = []
    for m in modes:
        a,b = m['a'],m['b']
        correction = S*c[5]**2 if a == b == 0 else F(0)
        lo,hi = map(lambda v:F(*v), m['shell'])
        sl,su = map(lambda v:F(*v), m['schur'])
        ck('full_anchor_and_strict_lower', F(*m['correction']) == correction and
           sl == lo-correction and su == hi-correction and 0 < sl <= su and
           m['schur_over_c5'] == [enc(sl/c[5]),enc(su/c[5])], [a,b])
        normalized.append(sl/c[5])
    minimum = min(normalized)
    ck('exact_manuscript_minimum', normalized.index(minimum) == 24 and
       F(630869,10**6) <= minimum < F(630870,10**6) and
       replay['minimum_normalized_lower']['value'] == enc(minimum))
    # Congruence with vector 1 of squared norm S, not a unit vector:
    # [[1,S*c5],[S*c5,S*e]] -> diag(1,S*(e-S*c5^2)).
    for endpoint in range(2):
        e = F(*modes[0]['shell'][endpoint])
        K = [[F(1),S*c[5]],[S*c[5],S*e]]
        T = [[F(1),-S*c[5]],[F(0),F(1)]]
        congruent = [[sum(T[u][i]*K[u][v]*T[v][j] for u in range(2) for v in range(2))
                      for j in range(2)] for i in range(2)]
        ck('explicit_constant_congruence', congruent ==
           [[F(1),F(0)],[F(0),S*F(*modes[0]['schur'][endpoint])]], endpoint)
    for p, digest in report['input_sha256'].items():
        ck('unchanged_inputs', sha(ROOT/p) == digest, p)
    report.update(stage='verified', replay_checks=replay['checks'],
                  replay_sha256=sha(B/'l115-critical-reverification.json'),
                  signed_subset_actions=action_records, endpoint_presentations=dict(endpoint_types),
                  normalized_lower_endpoints=list(map(enc,normalized)),
                  minimum_normalized_lower=enc(minimum), required_lower_bound=enc(F(630869,10**6)),
                  size=S, relations=36, presentations=216, modes=36,
                  scope='L115 unchanged-box included-anchor distance-five shell only.')
    save()
    print('L115 audit:', sum(counts.values()), 'additional checks; replay:', replay['checks'],
          '; failures:',len(report['failures']))
    print('Relations/presentations/modes: 36/216/36; required: 36/216/36.')
    print('All 36 Schur/c5 lower endpoints >= 630869/1000000 > 0; minimum < 630870/1000000.')
    print('Certificate:',OUT)


if __name__ == '__main__':
    main()
