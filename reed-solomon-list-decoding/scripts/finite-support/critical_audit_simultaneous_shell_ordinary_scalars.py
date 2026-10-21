"""L062 manuscript audit from concrete sets and the complete audited PSD input.

No constructor, optimizer or other notebook program is imported. Prior
PSD verification/audit must be rerun first. Full evidence is saved to disk.
"""
import hashlib
import itertools
import json
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'simultaneous-shell-ordinary-scalars-critical-audit.json'


def enc(v):
    if isinstance(v, Q):
        return [v.numerator, v.denominator]
    if isinstance(v, dict):
        return {str(k): enc(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [enc(x) for x in v]
    return v


def main():
    paths = [ROOT / name for name in [
        'simultaneous-shell-ordinary-scalars-results.json',
        'simultaneous-shell-ordinary-scalars-verification.json',
        'simultaneous-five-six-shell-results.json',
        'simultaneous-five-six-shell-verification.json',
        'simultaneous-five-six-shell-critical-audit.json',
        'full-shell-column-energy-results.json',
        'full-shell-column-energy-critical-audit.json',
        'delsarte-lp-results.json']]
    scalar, verified, original, psd, critical, energy, energy_audit, lp = [
        json.loads(p.read_text()) for p in paths]
    checks, failures, rows, closures, ratios, blocks = [], [], [], {}, [], []

    def check(name, valid):
        checks.append(name)
        if not valid:
            failures.append(name)

    for path, data in zip(paths, [scalar, verified, original, psd, critical, energy, energy_audit, lp]):
        check('no_failures_' + path.name, data['failures'] == [])
        for name, digest in data.get('source_hashes', {}).items():
            check('hash_' + path.name + '_' + name,
                  hashlib.sha256((NB / name).read_bytes()).hexdigest() == digest)
    for name, digest in energy_audit['input_hashes'].items():
        check('energy_input_hash_' + name, hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest)
    for name, digest in energy_audit['manuscript_hashes'].items():
        check('energy_manuscript_hash_' + name, hashlib.sha256((NB/name).read_bytes()).hexdigest() == digest)
    check('PSD_source_hash', psd['source_sha256'] == hashlib.sha256(paths[2].read_bytes()).hexdigest())
    check('all_28_same_coordinates', len(critical['witness']) == 28 and
          critical['witness'] == psd['complete_z'] == original['exact']['z'])
    a = [Q(v['numerator'], v['denominator']) for v in lp['exact']['primal']]
    p = [Q(1)] + [Q(0)]*4 + [x/(2*comb(68,h)*comb(956,h)) for h,x in zip(range(5,69), a)]
    N, M = comb(1024,68), (Q(comb(1024,64),comb(68,64))+1)/2
    rho = M/N
    check('singleton_and_pair_normalization', rho > 0 and scalar['rho'] == enc(rho)
          and scalar['pairs_through_12'] == enc(p[:13]) and 1+sum(a)/2 == M)
    check('all_distinct_pairs_bounded', all(0 <= x <= p[5] for x in p[1:13]))
    expected_types = [(l,m,i,j) for l,m in [(5,5),(5,6),(6,6)]
                      for i,j in itertools.product(range(min(l,m)+1),repeat=2)]
    check('complete_type_domain', [tuple(v['type']) for v in scalar['types']] == expected_types
          and len(critical['complete_regions']) == len(expected_types) == 121)
    seen_distances, boolean, forbidden = set(), 0, 0
    for index, (l,m,i,j) in enumerate(expected_types):
        region = critical['complete_regions'][index]
        saved_type = scalar['types'][index]
        supports = [set(v) for v in region['supports']]
        check(f'actual_representative_{index}', region['layers'] == [l,m]
              and region['intersections'] == [i,j] and all(len(S) == 68 for S in supports)
              and all(S <= set(range(1024)) for S in supports))
        eligible = [Q(*v['moment']) for v in region['presentations'] if v['moment'] is not None]
        check(f'same_complete_PSD_moment_{index}', bool(eligible) and len(set(eligible)) == 1
              and enc(eligible[0]) == saved_type['y'] == psd['completed_presentations'][index]['moment'])
        y = eligible[0]
        check(f'exact_six_orders_{index}', len(saved_type['presentations']) == len(region['presentations']) == 6)
        for k, order in enumerate(itertools.permutations(range(3))):
            A,B,C = [supports[h] for h in order]
            atoms = [sum(4*(x in A)+2*(x in B)+(x in C) == mask for x in range(1024)) for mask in range(8)]
            aa,bb,h = len(A-B),len(A-C),len(B-C)
            t,s = len(A-(B|C)),len((B&C)-A)
            seen_distances.update([aa,bb,h])
            reconstructed = [956-aa-bb+s,bb-s,aa-s,s,t,aa-t,bb-t,68-aa-bb+t]
            check(f'unique_source_atoms_{index}_{k}', atoms == reconstructed and t-s == i-j
                  and h == aa+bb-t-s and min(atoms) >= 0)
            # Factorial count independently of the constructor's binomial chain.
            orbit = factorial(68)*factorial(956)
            denominator = 1
            for size in atoms:
                denominator *= factorial(size)
            orbit, residual = divmod(orbit, denominator)
            check(f'positive_orbit_count_{index}_{k}', residual == 0 and orbit > 0
                  and (N*orbit*rho*y)/(M*orbit) == y)
            saved = saved_type['presentations'][k]
            slacks = [y,p[aa]-y,1+y-p[aa]-p[bb]]
            check(f'every_constructor_field_{index}_{k}', saved == {
                'order': list(order), 'atoms': atoms, 'source_indices': [aa,bb,t,s],
                'third_distance': h, 't_minus_s': t-s, 'orbit_size': orbit,
                'pairs': enc([p[aa],p[bb],p[h]]), 'slacks': enc(slacks)})
            row = {'type': [l,m,i,j], 'order': list(order), 'source_indices': [aa,bb,t,s],
                   'y': enc(y), 'slacks': enc(slacks)}
            check(f'every_independent_scalar_field_{index}_{k}', verified['rows'][6*index+k] == row)
            check(f'all_source_scalar_rows_{index}_{k}', all(x >= 0 for x in slacks)
                  and all(y <= p[d] for d in [aa,bb,h]))
            key = (tuple(sorted([aa,bb,h])),t-s)
            atom_key = min(tuple(v['atoms']) for v in region['presentations'])
            check(f'exhaustive_source_equality_{index}_{k}', key not in closures
                  or closures[key] == (atom_key,y))
            closures[key] = (atom_key,y)
            if 0 in [aa,bb,h]:
                boolean += 1
                check(f'Boolean_reduction_{index}_{k}', len(set(map(frozenset,supports))) == 2
                      and y == p[max(aa,bb,h)])
            else:
                check(f'uniform_lower_bound_{index}_{k}', slacks[2] >= 1-2*p[5] > 0)
                if any(1 <= d <= 4 for d in [aa,bb,h]):
                    forbidden += 1
                    check(f'forbidden_zero_{index}_{k}', y == 0)
                else:
                    ratios.append((y/min(p[d] for d in [aa,bb,h]),[l,m,i,j],list(order)))
            rows.append(dict(row,atoms=atoms,orbit_size=orbit,third_distance=h))
    check('complete_counts_and_pair_range', len(rows) == 726 and boolean == 12
          and forbidden == 228 and seen_distances == set(range(13)))
    maxratio = max(v[0] for v in ratios)
    check('manuscript_exact_scalar_extrema', maxratio == Q(8015622621372853,4480701311136656929120)
          == Q(*verified['summary']['maximum_distinct_upper_ratio']) < Q(2,1000000)
          and min(Q(*s) for row in rows for s in row['slacks']) == 0
          and 1-2*p[5] == Q(34440571829,34440571830))
    check('complete_PSD_domain', [(v['a'],v['b']) for v in critical['complete_blocks']]
          == list(itertools.product(range(7),repeat=2)))
    positive, zero, oldzero = 0,0,0
    S6 = comb(68,6)*comb(956,6)
    total_energy = p[6]**2
    for block, vb in zip(critical['complete_blocks'],psd['complete_blocks']):
        aa,bb = block['a'],block['b']
        x,y,z = [Q(*block[k]) for k in ['C55','C56','C66']]
        r = z-y*y/x if x else z
        check(f'identical_full_Schur_block_{aa}_{bb}', x >= 0 and (x > 0 or y == 0)
              and r >= 0 and enc(r) == block['remainder'] and vb == {
                  'a': aa,'b': bb,'five': enc(x),'cross': enc(y),'six': enc(z),
                  'remainder': enc(r),'normalized_slack': block['slack']})
        check(f'positive_rescaling_{aa}_{bb}', block['D6'] > 0 and Q(*block['N6']) > 0)
        if block['D5'] is not None:
            oldzero += x == 0
            matrix = [[Q(*v) for v in row] for row in block['actual_symmetric_block']]
            P,T,Z = matrix[0][0],matrix[0][1],matrix[1][1]
            check(f'actual_weighted_singular_form_{aa}_{bb}', matrix[1][0] == T and P >= 0
                  and (P > 0 or T == 0) and (Z-T*T/P if P else Z) == Q(*block['N6'])*r/block['D6'])
            e = energy_audit['modes'][6*aa+bb]
            A0,B0,C0 = map(lambda v: Q(*v),e['energy_coefficients_ABC'])
            star = Q(*energy['optimization']['minimizer'])
            actual_energy = A0*star*star+B0*star+C0
            mult = (comb(68,aa)-(comb(68,aa-1) if aa else 0))*(comb(956,bb)-(comb(956,bb-1) if bb else 0))
            expected_energy = p[6]*mult*Q(*block['eta'])/S6
            check(f'load_bearing_energy_mode_{aa}_{bb}', actual_energy == expected_energy)
            total_energy += expected_energy
        positive += r > 0
        zero += r == 0
        blocks.append(block)
    check('singular_and_remainder_counts', oldzero == 20 and (positive,zero) == (20,29))
    check('entire_same_energy', total_energy == Q(*energy['optimization']['minimum_energy']))
    summary = {'checks': len(checks),'failures': len(failures),'types': len(expected_types),
               'presentations': len(rows),'scalar_rows': 3*len(rows),'Boolean': boolean,
               'forbidden': forbidden,'PSD_modes': len(blocks),'old_zero_modes': oldzero,
               'positive_zero_remainders': [positive,zero],'maximum_distinct_upper_ratio': enc(maxratio),
               'required_upper_ratio': [1,1],'minimum_scalar_slack': [0,1],
               'required_scalar_and_PSD_slacks': '>=0','audit_retains_L062': not failures}
    OUT.write_text(json.dumps(enc({'source_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
                                  'summary': summary,'rows': rows,'maximum_ratio_presentations': [v for v in ratios if v[0] == maxratio],
                                  'witness': critical['witness'],'complete_PSD_blocks': blocks,
                                  'check_names': checks,'failures': failures}),indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True))
    print('Certificate:',OUT.relative_to(NB))
    if failures:
        raise SystemExit('Failures: '+str(failures))


if __name__ == '__main__':
    main()
