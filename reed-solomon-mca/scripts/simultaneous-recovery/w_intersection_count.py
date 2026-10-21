"""Bounded simultaneous count with two d-tags and one fixed normalized Y/Z.

Uses audited L049's complete cubic partition only to enumerate the selected
pair configurations. Classifies all four-supports using L043 (4)-(7).
Not an all-labeling certificate. All arithmetic is exact modulo 97.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import finite_count as fc

P, H, V, SUPPORTS = fc.P, fc.H, fc.V, fc.SUPPORTS
YS, ZS, h = (8, 12), (18, 70), 1
INV = {x: pow(x, -1, P) for x in range(1, P)}
OUT = Path(__file__).with_name('w-intersection-count-result.json')


def classify(d, w):
    b = (h, d, *YS, *ZS)
    u = set(b + w)
    c = {x: fc.root_value([a for a in H if a not in u], x) for x in u}
    excluded = {tuple(sorted((h, d, *YS))), tuple(sorted((h, d, *ZS))),
                tuple(sorted((h, *w))), tuple(sorted(YS + ZS))}
    records, eligible = [], []
    for k in SUPPORTS:
        rec = {'K': k}
        if k in excluded:
            rec['status'] = 'excluded'
            records.append(rec)
            continue
        cols = {x: tuple(fc.root_value(k, x) * V[x][j] % P for j in range(4))
                for x in b}
        fy = tuple(sum(c[x] * cols[x][j] for x in YS) % P for j in range(4))
        fz = tuple(sum(c[x] * cols[x][j] for x in ZS) % P for j in range(4))
        missing = tuple(x for x in (h, d) if x not in k)
        rank, ok, solution = fc.solve([tuple(-a % P for a in fy)] +
                                     [cols[x] for x in missing],
                                     tuple(-a % P for a in fz))
        rec.update(rank=rank, consistent=ok, missing=missing)
        if not ok:
            rec['status'] = 'inconsistent'
        elif solution is None:
            raise AssertionError(('unexpected nonunique system', d, w, k))
        else:
            mu, *beta = solution
            rec.update(mu=mu, beta=beta)
            if mu in (0, P - 1):
                rec['status'] = 'selected_parameter'
            else:
                norm = {x: a * INV[c[x]] % P for x, a in zip(missing, beta)}
                rec.update(status='eligible_equations',
                           required_r=((1 - norm[d]) * INV[1 + mu] % P
                                       if d in missing else None),
                           q_minus_mu_p=norm.get(h))
                eligible.append(rec)
        records.append(rec)
    return {'d': d, 'W': w, 'c': c, 'excluded': sorted(excluded),
            'support_classification': records}, eligible


def enumerate_pairs():
    src = json.loads(Path(__file__).with_name('disjoint-d-pair-result.json').read_text())
    selected = [c for c in src['complete_groups'] if tuple(c['Y']) == YS and tuple(c['Z']) == ZS]
    assert len(selected) == 1
    choice = selected[0]
    seen = set()
    for key, group in choice['groups']:
        if len(group) < 3:
            continue
        for ww in group:
            w = tuple(ww)
            wvals = {x: fc.root_value(w, x) for x in (h, *YS, *ZS)}
            for first, second in combinations([tuple(s) for s in group if s != ww], 2):
                rows = []
                for s in (first, second):
                    vals = {x: fc.root_value(s, x) for x in (h, *YS, *ZS)}
                    u = vals[ZS[0]] * INV[wvals[ZS[0]]] % P
                    mu = -u * wvals[YS[0]] * INV[vals[YS[0]]] % P
                    ah = u * wvals[h] * INV[vals[h]] % P
                    assert all(((-mu if x in YS else 1) * vals[x] - u * wvals[x]) % P == 0
                               for x in YS + ZS)
                    rows.append((mu, ah, u))
                (mu, ah, u), (nu, bh, uu) = rows
                if mu in (0, 96) or nu in (0, 96) or mu == nu:
                    continue
                assert len(set(first) & set(second)) == 1
                assert set(first) & set(second) <= set(w)
                p = (ah - bh) * INV[(nu - mu) % P] % P
                q = (ah + mu * p) % P
                if p * q * (1-p-q) % P == 0:
                    continue
                used = {h, *YS, *ZS, *w, *first, *second}
                for d in H:
                    if d in used:
                        continue
                    identity = (d, w, p, q)
                    if identity in seen:
                        continue
                    seen.add(identity)
                    yield {'d': d, 'W': w, 'S': first, 'SS': second,
                           'mu_nu': [mu, nu], 'scales': [u, uu],
                           'p_q': [p, q], 'ratio_key': key}


def count_pair(pair, eligible):
    p, q = pair['p_q']
    active = [row for row in eligible if row['q_minus_mu_p'] is None or
              (q - row['mu'] * p - row['q_minus_mu_p']) % P == 0]
    baseline = sorted({row['mu'] for row in active if row['required_r'] is None})
    counts = []
    for r in range(2, P):
        mus = sorted({row['mu'] for row in active if row['required_r'] in (None, r)})
        assert set(pair['mu_nu']) <= set(mus)
        counts.append({'r': r, 'mus': mus})
    max_rec = max(counts, key=lambda rec: len(rec['mus']))
    return {'rational_r_cases': counts, 'nonprime_r_mus': baseline,
            'maximum': max(len(max_rec['mus']), len(baseline)),
            'first_maximizer': max_rec,
            'count_histogram': dict(sorted(Counter(len(rec['mus']) for rec in counts).items()))}


def verify(pair, base, count):
    """Independent exhaustive all-mu/all-support moment test at one maximizer."""
    p, q = pair['p_q']
    r = count['first_maximizer']['r']
    c = {int(x): a for x, a in base['c'].items()}
    excluded = set(tuple(k) for k in base['excluded'])
    admitted, actual = [], set()
    for mu in range(1, P-1):
        n = {x: -mu * c[x] % P for x in YS}
        n.update({x: c[x] for x in ZS})
        n[h] = c[h] * (q-mu*p) % P
        n[pair['d']] = c[pair['d']] * (1-(1+mu)*r) % P
        target = fc.moment(n)
        for k in SUPPORTS:
            if k in excluded:
                continue
            omega = tuple(sum(a*b for a, b in zip(row, target[:4])) % P
                          for row in fc.INVERSES[k])
            if all(sum(a * V[x][j] for x, a in zip(k, omega)) % P == target[j]
                   for j in range(4, 8)):
                actual.add(mu)
                admitted.append({'mu': mu, 'K': k, 'omega': omega,
                                 'moments': target, 'full_weight': all(omega)})
    assert sorted(actual) == count['first_maximizer']['mus']
    rho = next(a for a in range(2, P) if all((a - (1-a)*mu) % P for mu in actual))
    e0 = {h: c[h]*p*INV[(1-rho) % P] % P,
          pair['d']: c[pair['d']]*r*INV[(1-rho) % P] % P}
    e0.update({x: c[x]*INV[(1-rho) % P] % P for x in YS})
    e1 = {h: c[h]*q*INV[rho] % P,
          pair['d']: c[pair['d']]*(1-r)*INV[rho] % P}
    e1.update({x: c[x]*INV[rho] % P for x in ZS})
    e2 = {h: -c[h]*(1-p-q) % P}
    e2.update({x: -c[x] % P for x in pair['W']})
    assert all(all(e.values()) for e in (e0, e1, e2))
    intercept, m1, m2 = map(fc.moment, (e0, e1, e2))
    slope = tuple((a-b) % P for a, b in zip(m1, intercept))
    pencil = lambda t: tuple((a+t*b) % P for a, b in zip(intercept, slope))
    assert pencil(rho) == m2
    for rec in admitted:
        e = (rho - (1-rho)*rec['mu']) % P
        t = rho*INV[e] % P
        word = {x: a*INV[e] % P for x, a in zip(rec['K'], rec['omega'])}
        assert t not in (0, 1, rho) and fc.moment(word) == pencil(t)
        rec.update(E=e, T=t, actual_error=word, all_eight_pencil_moments=True)
    assert len({rec['T'] for rec in admitted}) == len(actual)
    return {'p_q_r': [p, q, r], 'gamma': [0, 1, rho], 'lambda': 1,
            'original_errors': [e0, e1, e2], 'intercept': intercept, 'slope': slope,
            'complete_admitted_records': admitted,
            'memberships_checked': 95*(1820-4), 'exact_set_match': True,
            'triple_gates': True, 'all_eight_pencil_moments': True}


def main():
    pairs = list(enumerate_pairs())
    result = {'scope': {'prime': P, 'H': H, 'h': h, 'Y': YS, 'Z': ZS,
                        'two_d_tags_required': True, 'all_labelings': False,
                        'E_exclusion': False, 'fourth_weight_gate': False,
                        'arbitrary_original_chart': True,
                        'nonprime_r_included_by_recovery_equations': True},
              'bases': [], 'cases': [], 'verifications': [], 'failures': []}
    cache = {}
    for i, pair in enumerate(pairs):
        key = (pair['d'], pair['W'])
        if key not in cache:
            base, eligible = classify(*key)
            index = len(result['bases'])
            result['bases'].append(base)
            cache[key] = (index, eligible)
        index, eligible = cache[key]
        count = count_pair(pair, eligible)
        result['cases'].append({'pair': pair, 'base_index': index, 'count': count})
    maximum = max(case['count']['maximum'] for case in result['cases'])
    # Check every global-maximizing pair configuration, not just one support.
    selected = [i for i, case in enumerate(result['cases']) if case['count']['maximum'] == maximum]
    for j, i in enumerate(selected):
        case = result['cases'][i]
        checked = verify(case['pair'], result['bases'][case['base_index']], case['count'])
        result['verifications'].append({'case_index': i, 'verification': checked})
        if (j+1) % 20 == 0 or j+1 == len(selected):
            OUT.write_text(json.dumps(result, separators=(',', ':'))+'\n')
            print(f'verified maximizing configuration {j+1}/{len(selected)}', flush=True)
    result['summary'] = {'pair_weight_configurations': len(pairs), 'base_labelings': len(cache),
                         'classified_supports': 1820*len(cache),
                         'rational_r_cases': 95*len(pairs),
                         'nonprime_r_cases': len(pairs),
                         'maximum': maximum,
                         'case_maximum_histogram': dict(sorted(Counter(c['count']['maximum'] for c in result['cases']).items())),
                         'global_maximizing_configurations_verified': len(selected),
                         'independent_memberships_checked': len(selected)*95*1816,
                         'required_refutation_count': 12, 'uniform_bound_sought': 11,
                         'proves_uniform_bound': False, 'refutes_uniform_bound': maximum >= 12,
                         'failures': []}
    OUT.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps(result['summary'], sort_keys=True))
    print(f'actual maximum {maximum}; required refutation count 12; certificate {OUT}')


if __name__ == '__main__':
    main()
