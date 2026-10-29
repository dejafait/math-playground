"""Fixed-domain L149 audit. No producer/replay imports or witness search.

Accepted local maps and complete ideal equalities are imported inputs;
this checks their exact bindings and every interface actually used by L149.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import isqrt, prod
from pathlib import Path
import json
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'surviving-witness-span-audit.json'
R = dict(completed=False, failures=[], bindings={}, checks=[], sources=[],
         kernel_memberships=[], products=[], comparisons=[], max_rational_bits=0)
A = [-109375, -32500, 150, 64, 1]
B = [[Q(1), Q(0), Q(1, 2), Q(31, 30)],
     [Q(0), Q(1), Q(7, 25), Q(179, 750)],
     [Q(0), Q(0), Q(1, 50), Q(239, 18750)],
     [Q(0), Q(0), Q(0), Q(1, 18750)]]
ONE = [Q(1), Q(0), Q(0), Q(0)]


def check(name, ok):
    R['checks'].append(dict(name=name, passed=bool(ok)))
    assert ok, name


def observe(v):
    for x in v:
        x = Q(x)
        bits = max(abs(x.numerator).bit_length(), x.denominator.bit_length())
        R['max_rational_bits'] = max(bits, R['max_rational_bits'])
        assert bits <= 8192, 'arithmetic bit cap'
    return v


def read(name):
    raw = (ROOT / name).read_bytes()
    R['bindings'][name] = sha256(raw).hexdigest()
    return json.loads(raw)


def bound_inputs(c):
    for field in ('bindings', 'input_sha256'):
        entries = c.get(field, {})
        if not isinstance(entries, dict):
            continue  # Some older replays store a single input digest here.
        for name, expected in entries.items():
            if name.endswith('.json'):
                name = Path(name).name
                check('input hash ' + name,
                      sha256((ROOT / name).read_bytes()).hexdigest() == expected)


def power(v):
    return observe([sum(B[i][j] * Q(v[j]) for j in range(4)) for i in range(4)])


def multiply(u, v):
    # Literal power-basis arithmetic, independent of both other modules.
    p = [Q(0)] * 7
    for i, x in enumerate(u):
        for j, y in enumerate(v):
            p[i+j] += x*y
    for k in range(6, 3, -1):
        for j in range(4):
            p[k-4+j] -= p[k]*A[j]
    return observe(p[:4])


def det(m):
    m = [list(map(Q, row)) for row in m]
    d = Q(1)
    for i in range(len(m)):
        k = next((k for k in range(i, len(m)) if m[k][i]), None)
        if k is None:
            return Q(0)
        if k != i:
            m[i], m[k] = m[k], m[i]
            d = -d
        pivot = m[i][i]
        d *= pivot
        for k in range(i+1, len(m)):
            t = m[k][i]/pivot
            for j in range(i, len(m)):
                m[k][j] -= t*m[i][j]
            observe(m[k])
    observe([d])
    return d


def norm(v):
    cols = [multiply(v, [Q(i == j) for i in range(4)]) for j in range(4)]
    return det(list(zip(*cols)))


def span(vs):
    out = {0}
    for v in vs:
        out |= {x ^ v for x in out}
    return out


def rank(vs):
    rows = {}
    for v in vs:
        while v:
            k = v.bit_length()-1
            if k not in rows:
                rows[k] = v
                break
            v ^= rows[k]
    return len(rows)


def combo(vs, mask):
    out = 0
    for i, v in enumerate(vs):
        if mask >> i & 1:
            out ^= v
    return out


def rational_local(q, p):
    v = 0
    while q.numerator % p == 0:
        q /= p
        v += 1
    while q.denominator % p == 0:
        q *= p
        v -= 1
    modulus = 8 if p == 2 else p
    residue = q.numerator * pow(q.denominator, -1, modulus) % modulus
    bit = {1: 0, 7: 2, 5: 4, 3: 6}[residue] if p == 2 else 2*int(pow(residue, (p-1)//2, p) != 1)
    return v % 2 + bit


def main():
    c = read('surviving-witness-span-certificate.json')
    replay = read('surviving-witness-span-verification.json')
    check('successful saved producer and replay', c['completed'] and replay['completed']
          and not c['failures'] and not replay['failures'])
    check('producer script hash', c['source_sha256'] == sha256((ROOT/'surviving_witness_span.py').read_bytes()).hexdigest())
    for name in ('surviving_witness_span.py', 'verify_surviving_witness_span.py'):
        R['bindings'][name] = sha256((ROOT/name).read_bytes()).hexdigest()
    # Authenticate every mathematical input named by either implementation.
    for saved in (c, replay):
        bound_inputs(saved)
    inputs = {name: read(name) for name in c['bindings'] if name.endswith('.json')}
    for name, record in inputs.items():
        check('accepted success ' + name, (record.get('completed') is True or record.get('status') == 'PASS')
              and record['failures'] == [])
        bound_inputs(record)
    old = inputs['odd-membership-35-certificate.json']
    two = inputs['two-adic-filter-certificate.json']
    model = inputs['odd-model-support-certificate.json']
    base = inputs['quartic-class-certificate.json']
    real = inputs['real-kummer-certificate.json']
    check('actual full field and basis', c['alpha_polynomial'] == model['field']['alpha_polynomial'] == A
          and [[Q(x) for x in row] for row in c['order_basis']] == B
          and [[Q(x) for x in row] for row in model['field']['O_basis_in_alpha']] == B
          and old['model']['basis'] == base['order']['basis'] == model['field']['O_basis_in_alpha'])
    check('actual full quintic', old['model']['G'] == model['model']['G']
          and old['model']['H'] == model['model']['H'] and Q(old['model']['r']) == 9075)
    table = base['order']['table']
    check('accepted whole multiplication table', old['table'] == table)
    for i in range(4):
        for j in range(4):
            check('literal basis product ' + str((i, j)),
                  multiply([B[k][i] for k in range(4)], [B[k][j] for k in range(4)]) == power(table[i][j]))
    witnesses = two['witnesses']
    check('full source domain', len(witnesses) == len(real['witnesses']) == 39)
    check('all seven support primes', real['S_indices'] == [1,26,27,28,29,30,31]
          and real['input_primes'] == base['generators']
          and [i for i, pr in enumerate(base['generators']) if pr['p'] in (2,3,5,11)] == real['S_indices'])
    accepted = {v['tuple_id']: v for v in real['input_accepted_records']}
    images = [span([30,24]), span([5]), span([352,208,404]), span([7,13]), span([102,19,68])]
    widths, shifts = [5,4,9,6,8], [0,5,9,18,24]
    loc, quot, source = [], [], []
    for j, w in enumerate(witnesses):
        s = w['source']
        expected = real['witnesses'][j]
        check('entire accepted supported source ' + str(j), s == expected)
        b, q = power(s['coefficients']), Q(s['inverse_norm'])
        check('signed source norm ' + str(j), norm(b) == Q(s['signed_norm']) and q*norm(b) == 1)
        if j < 34:
            e = accepted[int(s['id'].split('-')[1])]
            vals = s['valuations']
            check('complete accepted ideal input ' + str(j), e['decision'] == 'accepted'
                  and s['coefficients'] == e['coefficients'] and vals == e['valuations']
                  and len(vals) == 32 and all(type(v) is int and v >= 0 for v in vals)
                  and all(v % 2 == 0 for i, v in enumerate(vals) if i not in real['S_indices']))
            check('full ideal norm binding ' + str(j), abs(norm(b)) == e['norm'] == e['supported_norm']
                  == prod(pr['p']**v for pr, v in zip(base['generators'], vals)))
            # Complete ideal equality is imported from audited L136/L140,
            # not inferred from this norm comparison.
            check('literal principal matrix ' + str(j),
                  all(power(row) == multiply(b, [B[k][i] for k in range(4)])
                      for i, row in enumerate(e['principal'])))
        else:
            a = [-1,2,3,5,11][j-34]
            check('exact appended rational source ' + str(j), s['coefficients'] == [a,0,0,0] and q == Q(1,a**4))
        p3, p5 = [old['places'][str(p)]['witnesses'][j] for p in (3,5)]
        check('whole ordered source at every new place ' + str(j),
              s == p3['source'] == p5['source'] and w['id'] == p3['id'] == p5['id'])
        masks = [w['real_mask'], w['eleven_mask'], w['local']['mask'], p3['evaluation']['mask'], p5['evaluation']['mask']]
        check('complete full mask widths ' + str(j), all(type(m) is int and 0 <= m < 2**n for m,n in zip(masks,widths)))
        check('independent rational localization ' + str(j), masks[0] & 1 == int(q < 0)
              and all(masks[k] & ((1 << (3 if p == 2 else 2))-1) == rational_local(q,p)
                      for k,p in ((1,11),(2,2),(3,3),(4,5))))
        reductions = [min(m ^ x for x in im) for m, im in zip(masks,images)]
        check('all five actual image quotient maps ' + str(j), w['old_quotient'] == reductions[0] | reductions[1] << 5
              and w['dyadic_quotient'] == reductions[2]
              and p3['quotient'] == reductions[3] and p5['quotient'] == reductions[4])
        loc.append(sum(m << t for m,t in zip(masks,shifts)))
        quot.append(sum(m << t for m,t in zip(reductions,shifts)))
        source.append((q,b))
        R['sources'].append(dict(index=j,id=w['id'],rational=q,quartic_power=b,
                                 full_local=masks,quotient=reductions,support='accepted full ideal equality' if j<34 else 'rational S-element'))
    ker = old['all_conditions']['kernel']
    check('entire source columns', c['full_local_columns'] == loc and c['quotient_columns'] == quot)
    check('entire coefficient kernel', c['kernel'] == ker and len(ker) == rank(ker) == 31 and rank(quot) == 8)
    for k in ker:
        full = combo(loc,k)
        masks = [(full >> t) & ((1 << n)-1) for t,n in zip(shifts,widths)]
        check('all actual local images for kernel ' + str(k), 0 < k < 2**39 and combo(quot,k) == 0
              and all(m in im for m,im in zip(masks,images)))
        R['kernel_memberships'].append(dict(mask=k,full_local=masks,quotient=combo(quot,k)))
    def reconstruct(k):
        q,b = Q(1),ONE[:]
        for j,(qj,bj) in enumerate(source):
            if k >> j & 1:
                q *= qj
                b = multiply(b,bj)
        check('product norm ' + str(k), q*norm(b) == 1)
        return q,b
    refs = {}
    check('reference domain', [r['mask'] for r in c['references']] == [0,165,132102,132259])
    for rec in c['references']:
        k = rec['mask']; q,b = reconstruct(k)
        check('full reference product ' + str(k), Q(rec['rational']) == q and list(map(Q,rec['quartic_power'])) == b
              and rec['full_local'] == combo(loc,k))
        refs[k] = (q,b)
    check('reference XOR product class', 132259 == 165 ^ 132102)
    for s in old['selected_pair']:
        q,b = refs[s['coefficients']]
        check('accepted independent reference binding', q == Q(s['rational']) and b == power(s['quartic_O'])
              and combo(loc,s['coefficients']) == s['local_detection'])
    check('reference independence', rank([combo(loc,165),combo(loc,132102)]) == 2)
    check('tested prefix and stop', [r['mask'] for r in c['products']] == ker[:4] == [118,165,296,3109]
          and c['outside_generator_index'] == 3 and c['outside_mask'] == 3109)
    products = []
    for rec in c['products']:
        k = rec['mask']; q,b = reconstruct(k)
        check('complete saved tested product ' + str(k), Q(rec['rational']) == q and list(map(Q,rec['quartic_power'])) == b
              and Q(rec['norm']) == norm(b) and rec['quotient'] == combo(quot,k) == 0 and rec['full_local'] == combo(loc,k))
        products.append((q,b))
        R['products'].append(dict(mask=k,rational=q,quartic_power=b,norm=norm(b),full_local=combo(loc,k)))
    check('literal nu and exact norm', products[3] == (Q(1,524880000000000000),list(map(Q,['90688','99088/5','-1403152/625','-33968/625'])))
          and norm(products[3][1]) == 524880000000000000)
    expected = [(0,0,'unequal'),(0,165,'unequal'),(0,132102,'equal'),(1,0,'unequal'),(1,165,'equal'),
                (2,0,'equal')] + [(3,k,'unequal') for k in refs]
    check('all ten comparison domains and first outside order',
          [(r['generator_index'],r['reference_mask'],r['decision']) for r in c['comparisons']] == expected)
    for rec in c['comparisons']:
        i,k = rec['generator_index'],rec['reference_mask']
        q,b = products[i]; rq,rb = refs[k]; t = q/rq
        n,d = isqrt(abs(t.numerator)),isqrt(t.denominator)
        yes = t >= 0 and n*n == t.numerator and d*d == t.denominator
        sq = rec['rational_test']; diff = combo(loc,ker[i]) ^ combo(loc,k)
        check('complete rational test ' + str((i,k)), Q(sq['value']) == t and sq['square'] == yes
              and (sq['numerator_floor'],sq['denominator_floor']) == (n,d)
              and rec['local_difference'] == diff and rec['mask'] == ker[i])
        if rec['decision'] == 'equal':
            root = list(map(Q,rec['quartic_root_power']))
            ratio = list(map(Q,rec['quartic_ratio_power']))
            check('exact full-group roots ' + str((i,k)), Q(sq['root'])**2*rq == q
                  and multiply(multiply(root,root),rb) == b and multiply(root,root) == ratio)
        else:
            check('conclusive negative comparison ' + str((i,k)), bool(diff) or not yes)
        if i == 3:
            check('rational-only outside proof ' + str(k), not yes)
        R['comparisons'].append(dict(generator=ker[i],reference=k,rational_ratio=t,
            numerator_floor=n,denominator_floor=d,full_difference=diff,decision=rec['decision']))
    check('all literal outside ratios', [products[3][0]/rq for rq,rb in refs.values()]
          == list(map(Q,['1/524880000000000000','55/12','11/216000','3403125/16'])))
    check('printed strict bounds', 724486024**2 < 524880000000000000 < 724486025**2
          and 1844**2 < 3403125 < 1845**2)
    check('printed earlier roots', c['comparisons'][2]['quartic_root_power'] == ['31/15','-361/375','74/9375','16/9375']
          and c['comparisons'][5]['quartic_root_power'] == ['-341/15','-1609/375','1211/9375','49/9375'])
    # Positive/negative exact certificates decide every comparison; proposals
    # and unused factorization caps have no role in mathematical acceptance.
    bounds = c['bounds']
    check('bounded complete outcome', c['outcome'] == replay['outcome'] == 'outside' and not c['unresolved']
          and bounds['comparisons_actual'] == len(c['comparisons']) == 10 <= bounds['comparisons_cap'] == 124
          and bounds['generators_decided'] == 3 and bounds['generators_required'] == 31
          and bounds['trager_shifts_actual'] == bounds['fallback_candidates_actual'] == 0)
    R.update(completed=True,result='L149 accepted within imported interfaces',
             bounds=dict(sources_actual=39,sources_required=39,kernel_actual=31,kernel_required=31,
                         products_actual=4,products_required=4,comparisons_actual=10,comparisons_required=10,
                         outside_comparisons_actual=4,outside_comparisons_required=4,comparisons_cap=124,
                         rational_bits_cap=8192),outside_mask=3109,
             limitations='No global generation, rational Kummer quotient, pairing or rank improvement.')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        R['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=R['completed'],checks=len(R['checks']),bounds=R.get('bounds'),
                         max_rational_bits=R['max_rational_bits'],required_bit_cap=8192,
                         failures=[v['message'] for v in R['failures']],path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)
