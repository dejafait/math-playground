#!/usr/bin/env python3
"""BSD-186: fixed geometry audit; no Fourier sums and no producer imports."""
import copy
import json
import sys
import traceback
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd
from pathlib import Path

from verify_coupled_plan import replay

HERE = Path(__file__).resolve().parent
OUT = HERE / 'geometry-critical-audit'


def egcd(a, b):
    r, s, t, rr, ss, tt = a, 1, 0, b, 0, 1
    while rr:
        q = r // rr
        r, rr = rr, r-q*rr
        s, ss = ss, s-q*ss
        t, tt = tt, t-q*tt
    if r < 0:
        r, s, t = -r, -s, -t
    assert r == 1
    return s, -t  # a*s - b*t = 1


def reconstruct(data, presentation, compressed):
    def check(condition, label):
        if not condition:
            raise AssertionError(label)
    domain = sorted({tuple(e) for pair in presentation['endpoints'] for e in pair},
                    key=lambda e: (e[1], abs(e[0]), e[0]))
    def equivalent(s, v):
        a, m = s; p, q = v
        sr, _ = egcd(a, m); sv, _ = egcd(p, q)
        return (q*sr-m*sv) % gcd(m*q, 36) == 0
    reps = []
    for e in domain:
        if not any(equivalent(s, e) for s in reps):
            reps.append(e)
    check(len(reps) == 12 and reps[0] == (1, 0), 'fresh representatives')
    check(list(map(list, reps)) == data['representatives'] == compressed['representatives'], 'saved representatives')
    pairs = []
    for i in range(12):
        for j in range(i):
            check(not equivalent(reps[i], reps[j]), 'distinct representative pair')
            pairs.append([j, i])
    def assigned(v):
        found = [i for i, s in enumerate(reps) if equivalent(s, v)]
        check(len(found) == 1, 'unique fresh assignment')
        return found[0]
    keys = [(Q(p['x_reduced']), Q(p['y'])) for p in data['primitives']]
    check(len(keys) == len(set(keys)) == 98, 'all primitive keys')
    lookup = {p: i for i, p in enumerate(keys)}
    transports = []
    def correction(row, v, label):
        j = assigned(v)
        check(row['endpoint'] == list(v) and row['representative_id'] == j, label+' assignment')
        t = row['transport']; a, m = reps[j]; p, q = v
        A, B, C, D = t['matrix']
        check(all(type(x) is int for x in (A, B, C, D)), label+' integral matrix')
        check(A*D-B*C == 1 and C % 36 == 0, label+' Gamma0')
        check(q*(A*a+B*m) == p*(C*a+D*m), label+' cusp image')
        if C == 0:
            check(A == D and abs(D) == 1 and Q(B, D).denominator == 1, label+' translation')
            check(t['zero_translation'] is not None and Q(t['zero_translation']) == Q(B,D), label+' zero')
            occ = []
        else:
            check(t['zero_translation'] is None, label+' nonzero branch')
            x, z, y = -Q(D,C), Q(A,C), Q(1,abs(C))
            # Keys obtained directly from the matrix, not saved point IDs/shifts.
            start = (x-(x+Q(1,2)).__floor__(), y)
            end = (z-(z+Q(1,2)).__floor__(), y)
            occ = [[lookup[start], '-1'], [lookup[end], '1']]
            check(t['primitive_ids'] == [lookup[start], lookup[end]], label+' primitive IDs')
        transports.append({'label': label, 'representative': j, 'target': list(v),
                           'matrix': [A,B,C,D], 'occurrences': occ})
        return j, occ
    check(len(data['assignments']) == len(compressed['assignments']) == len(domain) == 67, 'endpoint count')
    endpoints = []
    for i, v in enumerate(domain):
        old, new = compressed['assignments'][i], data['assignments'][i]
        check(old['endpoint'] == new['endpoint'] and old['representative_id'] == new['representative_id'],
              'L053 endpoint assignment unchanged')
        check({k:v for k,v in old['transport'].items() if k != 'primitive_ids'} ==
              {k:v for k,v in new['transport'].items() if k != 'primitive_ids'},
              'L053 geometric witness unchanged')
        check(len(old['transport']['primitive_ids']) == len(new['transport']['primitive_ids']),
              'L053 primitive occurrence count unchanged')
        for old_id, new_id in zip(old['transport']['primitive_ids'],new['transport']['primitive_ids']):
            old_point = compressed['primitives'][old_id]
            check((Q(old_point['x_reduced']),Q(old_point['y'])) == keys[new_id], 'L053 cache key unchanged')
        endpoints.append(correction(data['assignments'][i], v, 'endpoint '+str(i)))
    check(len(data['closures']) == 12, 'closure count')
    adjacency = [[0]*12 for _ in reps]; rhs = []; closure_rows = []
    for i, s in enumerate(reps):
        images = [(1,0)]*6 if s[1] == 0 else [
            (v.numerator, v.denominator) for v in
            [5*Q(*s)]+[(Q(*s)+j)/5 for j in range(5)]]
        c = data['closures'][i]
        check(c['representative'] == list(s) and len(c['images']) == 6, 'six Hecke images')
        occurrences = []
        for k, v in enumerate(images):
            j, occ = correction(c['images'][k], v, 'Hecke '+str(i)+':'+str(k))
            adjacency[i][j] += 1
            occurrences.extend(occ)
        rhs.append(occurrences)
        closure_rows.append({'source': list(s), 'images': list(map(list,images)), 'rhs_occurrences': occurrences})
    sigma = []
    for row in adjacency:
        check(sorted(row) == [0]*11+[6], 'six images in one class')
        sigma.append(row.index(6))
    check(sorted(sigma) == list(range(12)) and all(sigma[sigma[i]] == i for i in range(12)), 'involution')
    # Independent explicit inverse, not elimination or its saved transform.
    weights = [[-Q(int(j == sigma[i]),6) for j in range(12)] for i in range(12)]
    check([[Q(x) for x in row] for row in data['solution_equation_weights']] == weights, 'solution inverse')
    check(data['adjacency'] == adjacency, 'fresh adjacency')
    check(data['matrix'] == [[-x for x in row] for row in adjacency] and data['a_ell'] == 0, 'M=-A')
    check(rhs[0] == [] and sigma[0] == 0, 'actual infinity RHS and primitive zero')
    def scale(occ, factor):
        return [[k, str(Q(w)*factor)] for k,w in occ]
    rep_occ = [scale(rhs[sigma[i]], -Q(1,6)) for i in range(12)]
    check(data['representative_occurrences'] == rep_occ, 'all representative occurrences')
    def vector(occ):
        v = [Q(0)]*98
        for k,w in occ: v[k] += Q(w)
        return v
    solution = list(map(vector,rep_occ))
    for i in range(12):
        check([-6*x for x in solution[sigma[i]]] == vector(rhs[i]), 'actual analytic RHS identity')
    endpoint_occ = [occ+rep_occ[j] for j,occ in endpoints]
    endpoint_index = {v:i for i,v in enumerate(domain)}
    check(len(data['generators']) == len(presentation['endpoints']) == 72, 'generator count')
    rows = []; occurrence_count = 0
    for i, pair in enumerate(presentation['endpoints']):
        a,b = [endpoint_index[tuple(e)] for e in pair]
        occ = scale(endpoint_occ[a],-1)+scale(endpoint_occ[b],1)
        g = data['generators'][i]
        check(g['endpoints'] == pair and g['assignment_ids'] == [a,b], 'original endpoint direction')
        check(g['occurrences'] == occ, 'all uncombined occurrences '+str(i))
        v = vector(occ)
        check(g['combined'] == [[j,str(w)] for j,w in enumerate(v) if w], 'combined row '+str(i))
        W = sum((abs(Q(w)) for _,w in occ), Q(0))
        check(Q(g['absolute_occurrence_weight']) == W, 'absolute weight '+str(i))
        rows.append({'id':i, 'endpoints':pair, 'occurrences':occ, 'absolute_weight':str(W)})
        occurrence_count += len(occ)
    check(occurrence_count == 1316, 'complete occurrence count')
    return {'passed':True, 'failures':[], 'representatives':list(map(list,reps)),
            'inequivalent_pairs':pairs, 'sigma':sigma, 'inverse':[[str(x) for x in row] for row in weights],
            'closure_rows':closure_rows, 'transports':transports,
            'endpoint_occurrences':endpoint_occ, 'generator_rows':rows,
            'counts':{'assignments':67, 'pair_comparisons':66, 'Hecke_images':72,
                      'transports':len(transports), 'endpoint_compositions':144,
                      'generators':72, 'uncombined_occurrences':occurrence_count},
            'infinity_rhs':rhs[0], 'infinity_solution':list(map(str,solution[0]))}


def main():
    OUT.mkdir(exist_ok=True)
    paths = [HERE/name for name in ('coupled_plan.json','coupled_plan_verification.json',
             'compressed_plan.json','presentation.json','build_coupled_plan.py',
             'verify_coupled_plan.py','build_compressed_plan.py','verify_compressed_plan.py')]
    paths += [HERE.parent/'nonunitary-cusp/reduced_phase_certificate.json',
              HERE.parent/'general-relative/verify_certificate.py']
    paths.append(Path(__file__).resolve())
    paths += sorted((HERE.parent.parent/'ATTEMPTS').glob('02[5-8]-*.md'))
    before = {str(p.relative_to(HERE.parent.parent)):sha256(p.read_bytes()).hexdigest() for p in paths}
    data = json.loads((HERE/'coupled_plan.json').read_text())
    pres = json.loads((HERE/'presentation.json').read_text())
    compressed = json.loads((HERE/'compressed_plan.json').read_text())
    report = {'passed':False, 'failures':[]}
    try:
        full = replay(data)
        assert full['replay_passed'] and not full['failures']
        assert all(full['structural_actual'][k] == n for k,n in full['structural_required'].items())
        assert full['structural_actual']['segments'] == 626
        assert full['cutoff_obstruction']['selected_contribution_exceeds_required']
        (OUT/'complete-replay.json').write_text(json.dumps(full,indent=2)+'\n')
        independent = reconstruct(data,pres,compressed)
        (OUT/'independent-identities.json').write_text(json.dumps(independent,indent=2)+'\n')
        tests = []
        for kind in ('assignment','infinity','inverse_sign','occurrence_sign'):
            bad = copy.deepcopy(data)
            if kind == 'assignment': bad['assignments'][1]['representative_id'] = 0
            if kind == 'infinity': bad['closures'][0]['images'].pop()
            if kind == 'inverse_sign': bad['solution_equation_weights'][3][4] = '1/6'
            if kind == 'occurrence_sign':
                row = next(g for g in bad['generators'] if g['occurrences'])
                row['occurrences'][0][1] = str(-Q(row['occurrences'][0][1]))
            try:
                reconstruct(bad,pres,compressed)
            except AssertionError as e:
                tests.append({'case':kind,'rejected':True,'reason':str(e)})
            else:
                raise AssertionError('mutation accepted: '+kind)
        report.update(passed=True, actual=independent['counts'],
                      required={'assignments':67,'pair_comparisons':66,'Hecke_images':72,
                                'transports':139,'endpoint_compositions':144,'generators':72,
                                'uncombined_occurrences':1316},
                      rejections=tests, dyadic_obstruction=full['cutoff_obstruction'],
                      limitations=['supplied L038 structure; its critical audit is pending',
                                   'no finite sums, division, integer isolation or table'])
    except Exception as e:
        report['failures'].append(repr(e)); report['traceback'] = traceback.format_exc()
    after = {str(p.relative_to(HERE.parent.parent)):sha256(p.read_bytes()).hexdigest() for p in paths}
    report['original_sha256'] = before
    report['original_bytes_preserved'] = before == after
    if before != after:
        report['passed'] = False; report['failures'].append('original bytes changed')
    (OUT/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    print('geometry audit=',report['passed'],'actual=',report.get('actual'),
          'required=',report.get('required'),'failures=',report['failures'],
          'originals preserved=',report['original_bytes_preserved'],'report=',OUT/'report.json')
    if 'dyadic_obstruction' in report:
        obstruction = report['dyadic_obstruction']
        print('dyadic selected bound=',obstruction['selected_contribution'],
              'required <=',obstruction['required'], 'cutoff=',obstruction['all_primitive_H'],
              'bound convention fails=',obstruction['selected_contribution_exceeds_required'])
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
