"""Fixed-domain interface supplement to L147's conceptual audit.

No search and no imports of producer/replay arithmetic. The separately
reviewed replay checks all lattice, residue and field identities. Here we
bind the accepted inputs, check every domain/shape and quotient, and bind
the full printed conclusions. Complete evidence is written to disk.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'odd-membership-35-audit.json'
R = dict(completed=False, failures=[], checks=[], bindings={})


def read(name):
    raw = (ROOT / name).read_bytes()
    R['bindings'][name] = sha256(raw).hexdigest()
    return json.loads(raw)


def check(name, condition):
    R['checks'].append(dict(name=name, passed=bool(condition)))
    assert condition, name


def span(columns):
    values = {0}
    for x in columns:
        values |= {v ^ x for v in values}
    return values


def combo(columns, c):
    z = 0
    for j, x in enumerate(columns):
        if c >> j & 1:
            z ^= x
    return z


def rank(columns):
    piv = {}
    for x in columns:
        while x:
            k = (x & -x).bit_length() - 1
            if k not in piv:
                piv[k] = x
                break
            x ^= piv[k]
    return len(piv)


def elimination(name, rec, columns):
    n = len(columns)
    k = rank(columns)
    check(name + ' exact dimensions', rec['rank'] == k == len(rec['pivots'])
          and len(rec['kernel']) == n-k and len(rec['trace']) == n)
    coeffs = rec['kernel'] + [t['coefficients'] for t in rec['trace']]
    coeffs += [v[1] for v in rec['pivots'].values()]
    check(name + ' coefficient domains', all(type(c) is int and 0 < c < 2**n for c in coeffs))
    check(name + ' full independent kernel', rank(rec['kernel']) == n-k
          and all(combo(columns, c) == 0 for c in rec['kernel']))
    check(name + ' all traces', all(t['input'] == columns[j]
          and combo(columns, t['coefficients']) == t['reduced']
          for j, t in enumerate(rec['trace'])))
    check(name + ' authentic triangular pivot basis',
          all(v > 0 and int(i) == v.bit_length()-1 and combo(columns, c) == v
              for i, (v, c) in rec['pivots'].items()))


def pair_shape(name, rec, p, primes):
    check(name + ' all components', len(rec['quartic']) == len(primes)
          and 0 <= rec['rational']['mask'] < 4)
    combined = rec['rational']['mask']
    for j, (f, pr) in enumerate(zip(rec['quartic'], primes)):
        check(name + ' exact integral coordinates ' + str(j),
              len(f['integral']) == 4 and all(Q(x).denominator == 1 for x in f['integral'])
              and type(f['denominator']) is int and f['denominator'] > 0)
        ic = f['integral_class']
        check(name + ' residue and depth ' + str(j),
              type(ic['valuation']) is int and 0 <= ic['valuation'] < len(pr['powers'])-1
              and 1 <= ic['residue'] < p and 0 <= f['mask'] < 4)
        combined |= f['mask'] << (2+2*j)
    check(name + ' disjoint bit packing', rec['mask'] == combined
          and 0 <= combined < 2**(2+2*len(primes)))


def main():
    c = read('odd-membership-35-certificate.json')
    replay = read('odd-membership-35-verification.json')
    prior = read('odd-membership-35-preaudit-verification.json')
    sources = {n: read(n) for n in c['bindings']}
    check('completed original and replay', c['completed'] and replay['completed']
          and not c['failures'] and not replay['failures'])
    check('replay unchanged in full', replay == prior)
    check('all source hashes', all(R['bindings'][n] == h for n, h in c['bindings'].items())
          and all(R['bindings'][n] == h for n, h in replay['bindings'].items()))
    check('all original checks pass', all(x['passed'] for x in c['checks']))
    base = sources['quartic-class-certificate.json']
    model = sources['odd-model-support-certificate.json']
    two = sources['two-adic-filter-certificate.json']
    da = sources['two-adic-filter-audit.json']
    ca = read('quartic-class-audit.json')
    ma = read('odd-model-support-audit.json')
    check('accepted maximal-order prime list', ca['completed'] and not ca['failures']
          and ca['input_sha256']['quartic-class-certificate.json'] == R['bindings']['quartic-class-certificate.json'])
    check('accepted actual model', ma['status'] == 'PASS' and not ma['failures']
          and ma['bindings']['scripts/pair-genus-two/odd-model-support-certificate.json']
          == R['bindings']['odd-model-support-certificate.json'])
    check('accepted dyadic and previous interfaces', da['completed'] and not da['failures']
          and da['bindings']['two-adic-filter-certificate.json'] == R['bindings']['two-adic-filter-certificate.json'])
    check('same complete basis and table', c['model']['basis'] == base['order']['basis']
          == model['field']['O_basis_in_alpha'] and c['table'] == base['order']['table'])
    check('printed eta coordinates', list(map(Q, c['model']['eta_O'])) == [17160,220,-440,1320])
    witnesses = two['witnesses']
    check('exact fixed domain', len(witnesses) == 39)
    support = {1,26,27,28,29,30,31}
    for j, w in enumerate(witnesses):
        src = w['source']
        check('source norm ' + str(j), len(src['coefficients']) == 4
              and Q(src['inverse_norm']) * Q(src['signed_norm']) == 1)
        vals = src.get('valuations')
        if vals is not None:
            check('source support ' + str(j), len(vals) == 32
                  and all(vals[i] % 2 == 0 for i in range(32) if i not in support))
    real_image, eleven_image, two_image = span([30,24]), span([5]), span([352,208,404])
    oldcols = []
    for j, w in enumerate(witnesses):
        check('old mask domains ' + str(j), 0 <= w['real_mask'] < 32
              and 0 <= w['eleven_mask'] < 16 and 0 <= w['local']['mask'] < 512)
        old = min(w['real_mask'] ^ x for x in real_image)
        old |= min(w['eleven_mask'] ^ x for x in eleven_image) << 5
        dy = min(w['local']['mask'] ^ x for x in two_image)
        check('old exact quotient ' + str(j), old == w['old_quotient'] and dy == w['dyadic_quotient'])
        oldcols.append(old | dy << 9)
    elimination('old', c['old_conditions'], oldcols)
    places = {}
    for p, indices, spaceids, pis, es, expected_masks in (
        (3, [27,28], [185,208], [[1,0,0,1],[0,3,0,0]], [3,1], [7,13]),
        (5, [29,30,31], [990,997,1066], [[0,0,1,2],[1,0,0,1],[1,0,0,4]], [1,1,2], [102,19,68])):
        P = c['places'][str(p)]
        primes = P['primes']
        check(str(p) + ' exact prime domain', [pr['index'] for pr in primes] == indices
              and [pr['source'] for pr in primes] == [base['generators'][i] for i in indices]
              and [pr['source']['space_id'] for pr in primes] == spaceids)
        check(str(p) + ' printed local fields', [pr['uniformizer'] for pr in primes] == pis
              and [pr['rational_prime_class']['valuation'] for pr in primes] == es
              and P['ramification_indices'] == es and P['local_factor_count'] == 1+len(primes)
              and all(pr['source']['lattice']['norm'] == p for pr in primes))
        for pr in primes:
            for n, lat in enumerate(pr['powers']):
                gen_count = 4 if n < 2 else 16
                check('ideal lattice exact domains '+str((p,pr['index'],n)),
                      len(lat['rows']) == len(lat['forward']) == 4
                      and all(len(r) == 4 and all(Q(v).denominator == 1 for v in r) for r in lat['rows'])
                      and all(len(r) == gen_count and all(Q(v).denominator == 1 for v in r) for r in lat['forward']))
        check(str(p) + ' exact witness and generator lengths', len(P['witnesses']) == 39
              and len(P['generators']) == len(primes))
        for j, w in enumerate(P['witnesses']):
            check(str(p) + ' complete ordered source ' + str(j), w['id'] == witnesses[j]['id']
                  and w['source'] == witnesses[j]['source'])
            pair_shape(str((p,'witness',j)), w['evaluation'], p, primes)
        check(str(p) + ' all tests counted', P['tests'] == len(P['samples'])+len(P['rejected'])
              and P['tests'] <= 200000)
        xs = [Q(x['X']) for x in P['samples']+P['rejected']]
        check(str(p) + ' distinct nonbranch tests', len(set(xs)) == len(xs) and Q(9075) not in xs)
        for j, s in enumerate(P['samples']):
            pair_shape(str((p,'sample',j)), s['evaluation'], p, primes)
            check(str((p,'sample depth',j)), -4 <= s['grid_depth'] <= 16 and Q(s['Y_squared']) != 0)
        for j, g in enumerate(P['generators']):
            check(str((p,'generator type',j)), (j == 0 and g['type'] == 'rational_branch'
                  and Q(g['X']) == 9075) or (j > 0 and g['type'] == 'local_point'
                  and 0 <= g['sample'] < len(P['samples'])
                  and g['evaluation'] == P['samples'][g['sample']]['evaluation']))
            pair_shape(str((p,'generator',j)), g['evaluation'], p, primes)
        masks = [g['evaluation']['mask'] for g in P['generators']]
        check(str(p)+' printed image and saturation', masks == expected_masks
              and rank(masks) == P['required_dimension'] == len(primes) and P['image_complete'])
        elimination(str(p)+' image', P['image'], masks)
        image = span(masks)
        for j, w in enumerate(P['witnesses']):
            check(str((p,'canonical quotient',j)), w['quotient'] == min(w['evaluation']['mask'] ^ x for x in image))
        cols = [w['quotient'] for w in P['witnesses']]
        elimination(str(p)+' restriction', P['condition_on_old_kernel'],
                    [combo(cols,k) for k in c['old_conditions']['kernel']])
        places[str(p)] = dict(prime_indices=indices, ramification=es, image=sorted(image),
            tests=P['tests'], test_cap=200000, samples=len(P['samples']), rejected=len(P['rejected']),
            image_dimension_actual=rank(masks), image_dimension_required=len(primes),
            ideal_depth_actual=max(len(pr['powers'])-1 for pr in primes), ideal_depth_cap=64)
    expected_points = [(3,1,6,-476336355067224210384,4,1),
                       (5,1,10,-475572171659352250000,6,1),
                       (5,2,100,-458626786603600000000,8,4)]
    for p,j,x,y2,v,u in expected_points:
        P = c['places'][str(p)]
        s = P['samples'][P['generators'][j]['sample']]
        check('printed local point '+str((p,x)), Q(s['X']) == x and Q(s['Y_squared']) == y2
              and s['square_certificate']['valuation'] == v and s['square_certificate']['residue'] == u)
    missing = [c['places']['3']['witnesses'][j]['quotient']
               | c['places']['5']['witnesses'][j]['quotient'] << 6 for j in range(39)]
    allcols = [oldcols[j] | missing[j] << 18 for j in range(39)]
    restricted = [combo(missing,k) for k in c['old_conditions']['kernel']]
    elimination('all', c['all_conditions'], allcols)
    elimination('new', c['combined_new_conditions'], restricted)
    check('three printed independent losses', c['new_condition_witnesses'] ==
          [dict(coefficients=22,quotient=9058),dict(coefficients=34,quotient=674),dict(coefficients=1038,quotient=881)]
          and rank(restricted) == rank([9058,674,881]) == 3)
    for w in c['new_condition_witnesses']:
        check('old-kernel witness '+str(w['coefficients']), combo(oldcols,w['coefficients']) == 0
              and combo(missing,w['coefficients']) == w['quotient'])
    local_columns = [[w['real_mask'],w['eleven_mask'],w['local']['mask'],
                      c['places']['3']['witnesses'][j]['evaluation']['mask'],
                      c['places']['5']['witnesses'][j]['evaluation']['mask']]
                     for j,w in enumerate(witnesses)]
    images = [real_image,eleven_image,two_image,span([7,13]),span([102,19,68])]
    printed = [(165,[0,2,5,7],Q(1,2405700000000000000),[458232,67632,251664,-472680],1713291454),
               (132102,[1,2,10,17],Q(1,26730000000000),[-73548,-2988,-56376,138360],1713217696)]
    check('exact selected pair count', len(c['selected_pair']) == 2)
    pair_records = []
    for a,(mask,indices,q,b,detection) in zip(c['selected_pair'],printed):
        check('entire selected representative '+str(mask), a['coefficients'] == mask
              and a['indices'] == indices == [i for i in range(39) if mask>>i&1]
              and Q(a['rational']) == q and list(map(Q,a['quartic_O'])) == b
              and a['local_detection'] == detection and combo(allcols,mask) == 0)
        local = [combo([row[i] for row in local_columns],mask) for i in range(5)]
        check('selected all local memberships '+str(mask), all(v in im for v,im in zip(local,images)))
        check('selected tuple packing '+str(mask), sum(v << s for v,s in zip(local,[0,5,9,18,24])) == detection)
        pair_records.append(dict(coefficients=mask,local_tuple=local,detection=detection))
    check('global independence detected', rank([x['detection'] for x in pair_records]) == 2)
    cases = [dict(c=i,old_dimension_upper=6+i,selmer_dimension_upper=3+i,
                  rank_upper=2+i,sufficient=1,shortfall=1+i) for i in range(3)]
    check('formal dimensions only', rank(oldcols) == 5 and rank(allcols) == 8
          and c['result']['old_coefficient_dimension'] == 34
          and c['result']['all_membership_coefficient_dimension'] == 31
          and c['result']['all_membership_masks'] == c['all_conditions']['kernel']
          and not c['result']['global_basis_certified'])
    check('resource bounds', c['bounds']['max_rational_bits'] == replay['max_rational_bits'] == 116
          and c['bounds']['rational_bits_cap'] == 8192)
    R.update(completed=True, places=places, selected_pair=pair_records, rank_cases=cases,
        replay_checks=replay['checks'], replay_identical=True,
        bounds=dict(witness_columns_actual=39,witness_columns_required=39,
                    old_kernel_actual=34,old_kernel_required=34,joint_kernel_actual=31,joint_kernel_required=31,
                    additional_rank_actual=3,additional_rank_required=3,rational_bits_actual=116,rational_bits_cap=8192))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        R['failures'].append(dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
    R['source_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(R,indent=2)+'\n')
    print(json.dumps(dict(completed=R['completed'],checks=len(R['checks']),
        failures=[x['message'] for x in R['failures']],places=R.get('places'),bounds=R.get('bounds'),path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)
