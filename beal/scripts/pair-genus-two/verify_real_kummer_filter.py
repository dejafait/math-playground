"""Independent exact replay of the fixed real-place certificate.

Reuses audited ideal data; does not rerun relation enumeration or upstream audits.
Norms use power-basis multiplication/Gaussian determinants; signs additionally
use Bernstein polynomials; F_2 ranks use exhaustive spans in five coordinates.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import comb, prod
from pathlib import Path
import json
import traceback

HERE = Path(__file__).resolve().parent
OUT = HERE / 'real-kummer-verification.json'
R = dict(completed=False, failures=[], checks=0, bindings={}, verified_rows=[],
         bounds=dict(rational_bits_cap=4096, max_rational_bits=0))


def need(condition, label):
    R['checks'] += 1
    if not condition:
        raise AssertionError(label)


def size(x):
    if isinstance(x, (int, F)) and not isinstance(x, bool):
        f = F(x)
        b = max(abs(f.numerator).bit_length(), f.denominator.bit_length())
        R['bounds']['max_rational_bits'] = max(b, R['bounds']['max_rational_bits'])
        if b > 4096:
            raise ArithmeticError('4096-bit replay cap')
    elif isinstance(x, (list,tuple)):
        for y in x:
            size(y)
    return x


def plus(x,y):
    return size(x+y)


def times(x,y):
    return size(x*y)


def over(x,y):
    return size(F(x)/F(y))


def load(filename):
    raw = (HERE / filename).read_bytes()
    R['bindings'][filename] = sha256(raw).hexdigest()
    return json.loads(raw)


def point(p,x):
    terms = [times(c,size(x**i)) for i,c in enumerate(p)]
    z = 0
    for t in terms:
        z = plus(z,t)
    return z


def box_horner(p,a,b):
    # Recursive interval recurrence, checking all four rectangle corners.
    if len(p) == 1:
        return [F(p[0]),F(p[0])]
    l,h = box_horner(p[1:],a,b)
    corners = [times(a,l),times(a,h),times(b,l),times(b,h)]
    return [plus(p[0],min(corners)),plus(p[0],max(corners))]


def bernstein(p,a,b):
    n = len(p)-1
    width = plus(b,-a)
    c = []
    for j in range(n+1):
        t = 0
        for i in range(j,n+1):
            v = times(p[i],comb(i,j))
            v = times(v,size(a**(i-j)))
            v = times(v,size(width**j))
            t = plus(t,v)
        c.append(t)
    result = []
    for k in range(n+1):
        t = 0
        for j in range(k+1):
            t = plus(t,over(times(c[j],comb(k,j)),comb(n,j)))
        result.append(t)
    return result


def norm(p,g):
    # Column j is multiplication of p(alpha) by alpha^j, reduced modulo g.
    cols = []
    for j in range(4):
        u = [F(0)]*j + list(p)
        u += [F(0)]*(7-len(u))
        for degree in range(6,3,-1):
            for k in range(4):
                u[degree-4+k] = plus(u[degree-4+k],-times(u[degree],g[k]))
            u[degree] = F(0)
        cols.append(u[:4])
    m = [[cols[j][i] for j in range(4)] for i in range(4)]
    det = F(1)
    for i in range(4):
        pivot = next(j for j in range(i,4) if m[j][i])
        if pivot != i:
            m[pivot],m[i] = m[i],m[pivot]
            det = -det
        v = m[i][i]
        det = times(det,v)
        for j in range(i+1,4):
            factor = over(m[j][i],v)
            for k in range(i,4):
                m[j][k] = plus(m[j][k],-times(factor,m[i][k]))
    return det


def span(rows):
    values = {0}
    for row in rows:
        values |= {x ^ row for x in values}
    need(len(values) in (1,2,4,8,16,32), 'span cardinality')
    return values


def verify_elimination(rows,saved):
    pivots = {}
    need(len(rows) == len(saved['records']), 'complete elimination domain')
    for i,(row,record) in enumerate(zip(rows,saved['records'])):
        z, combo, used = row,1 << i,[]
        for k,(v,w) in sorted(pivots.items()):
            if (z >> k) & 1:
                z ^= v
                combo ^= w
                used.append(k)
        k = min(j for j in range(5) if (z>>j)&1) if z else None
        need(record == dict(input=row,used=used,output=z,pivot=k,combination=combo), 'every row operation')
        reconstructed = 0
        for j,r in enumerate(rows):
            if (combo>>j)&1:
                reconstructed ^= r
        need(reconstructed == z, 'full original-row combination')
        if z:
            need(k not in pivots, 'distinct pivots')
            pivots[k] = (z,combo)
    need(saved['pivots'] == {str(k):list(v) for k,v in pivots.items()}, 'all final pivots')
    need(saved['rank'] == len(pivots) == len(span(rows)).bit_length()-1, 'independent exhaustive rank')


def main():
    d = load('real-kummer-certificate.json')
    need(d['completed'] and not d['failures'], 'complete producer')
    originals = {filename:load(filename) for filename in d['bindings']}
    for filename,digest in d['bindings'].items():
        need(R['bindings'][filename] == digest, 'entire source binding ' + filename)
    expected = {
        'quartic-class-certificate.json':'c5363d1b846188e37fc53590b61de34923bb981da25ddd895cd82e14dda9b73b',
        'quartic-parity-certificate.json':'fdb376f96717188690de8c849197d8b64834afdcdc56d789f427f2cf186c5501',
        'localized-parity-certificate.json':'eb7e393e385bf994d7398ed8162d307b3f2ff2d9f593b0133cf024684ea5e76f',
        'odd-model-support-certificate.json':'22315e6ebcbaa4ff063206432a958935aeb01b07ea6652bcc51d851c45162193'}
    for filename,digest in expected.items():
        need(R['bindings'][filename] == digest, 'accepted canonical hash')
    for stem in ('quartic-class','quartic-parity','localized-parity','odd-model-support'):
        a = originals[stem+'-audit.json']
        flag = 'status' if stem == 'odd-model-support' else 'completed'
        need(a[flag] == ('PASS' if flag == 'status' else True) and not a['failures'], 'audit accepted')
        need(all(c.get('pass',c.get('passed')) is True for c in a['checks']), 'all prior audit comparisons')
        prefix = 'scripts/pair-genus-two/' if flag == 'status' else ''
        binding = a['bindings'] if flag == 'status' else a['input_sha256']
        need(binding[prefix+stem+'-certificate.json'] == expected[stem+'-certificate.json'], 'audit/certificate identification')
    base = originals['quartic-class-certificate.json']
    par = originals['quartic-parity-certificate.json']
    loc = originals['localized-parity-certificate.json']
    mod = originals['odd-model-support-certificate.json']
    accepted = [e for e in par['elements'] if e['decision'] == 'accepted']
    need(accepted == d['input_accepted_records'] and len(accepted) == 182, 'all 182 full source records')
    need([e['tuple_id'] for e in accepted] == par['accepted_ids'] == loc['accepted_ids'], 'all accepted IDs')
    need([e['valuations'] for e in accepted] == loc['accepted_valuations'], 'all complete valuation vectors')
    need(d['input_primes'] == base['generators'] == par['primes'], 'all ordered prime lattices')
    S = {1,26,27,28,29,30,31}
    need(set(d['S_indices']) == set(loc['selected_indices']) == S, 'same support')
    need([base['generators'][i] for i in sorted(S)] == loc['selected_primes'], 'full supported prime records')
    g = [-109375,-32500,150,64,1]
    need(d['g'] == mod['field']['alpha_polynomial'] == g, 'same field polynomial')
    B = [[F(x) for x in row] for row in d['basis']]
    need(B == [[F(x) for x in row] for row in base['order']['basis']] ==
         [[F(x) for x in row] for row in mod['field']['O_basis_in_alpha']], 'full actual basis')
    need(B == [[1,0,F(1,2),F(31,30)],[0,1,F(7,25),F(179,750)],
               [0,0,F(1,50),F(239,18750)],[0,0,0,F(1,18750)]], 'literal basis')
    G = mod['model']['G']
    need(d['G'] == G and mod['model']['linear_root'] == 9075, 'actual quintic')
    retained, rejected = [],[]
    for e in accepted:
        v = e['valuations']
        need(len(v)==32 and all(type(x) is int and x>=0 for x in v), 'complete exact valuations')
        bad = [i for i in range(32) if i not in S and v[i] % 2]
        if bad:
            rejected.append(dict(tuple_id=e['tuple_id'],excluded_odd_indices=bad))
        else:
            retained.append(e)
    need(d['excluded'] == rejected, 'all disqualified elements and reasons')
    need(len(d['witnesses']) == len(retained)+5 <= 187, 'fixed witness domain')
    intervals = [[F(x) for x in b] for b in d['initial_intervals']]
    need(intervals == [[-48,-47],[-34,-33],[-4,-3],[20,21]], 'L135 initial intervals')
    need(intervals == [[F(z[0]) for z in b] for b in base['signature']['intervals']], 'source interval identities')
    counts = [0]*4
    for i,(lo,hi) in enumerate(intervals):
        need(point(g,lo)*point(g,hi) < 0, 'initial root sign change')
    for rec in d['refinements']:
        k = rec['root']
        lo,hi = intervals[k]
        mid = over(plus(lo,hi),2)
        v = point(g,mid)
        need(rec['before'] == [str(lo),str(hi)] and F(rec['midpoint']) == mid and F(rec['value']) == v,
             'complete bisection evidence')
        need(v != 0, 'no unhandled rational root')
        intervals[k] = [lo,mid] if point(g,lo)*v < 0 else [mid,hi]
        need(intervals[k] == [F(x) for x in rec['after']], 'retained sign-change half')
        counts[k] += 1
        need(counts[k] <= 64, 'bisection cap')
    need(intervals == [[F(x) for x in b] for b in d['alpha_intervals']] and counts == d['bisections'], 'all final intervals')
    for k,(lo,hi) in enumerate(intervals):
        need(lo < hi < 50 and point(g,lo)*point(g,hi) < 0, 'unique isolated real root by degree four')
        if k:
            need(intervals[k-1][1] < lo, 'disjoint alpha roots')
    eta = [[over(907500,plus(50,-t)) for t in b] for b in intervals]
    roots = [[F(9075)]*2]+eta
    need(eta == [[F(x) for x in b] for b in d['eta_intervals']], 'actual eta transport')
    need(roots == [[F(x) for x in b] for b in d['root_intervals']], 'all five root intervals')
    need(all(roots[i][1] < roots[i+1][0] for i in range(4)), 'strict complete root order')
    need(d['coordinate_order'] == ['rational-9075','alpha-0','alpha-1','alpha-2','alpha-3'], 'coordinate permutation')
    for k,w in enumerate(d['witnesses']):
        if k < len(retained):
            e = retained[k]
            need(w['id'] == 'tuple-'+str(e['tuple_id']) and w['coefficients'] == e['coefficients'] and w['valuations'] == e['valuations'], 'every retained element')
        else:
            a = (-1,2,3,5,11)[k-len(retained)]
            need(w['id']=='rational-'+str(a) and w['coefficients']==[a,0,0,0], 'only five appended rational elements')
            need(w['support_reason']=='rational with primes only in S', 'rational support proof')
        a = w['coefficients']
        p = [sum(times(B[j][i],a[i]) for i in range(4)) for j in range(4)]
        size(p)
        need(p == [F(x) for x in w['power_coefficients']], 'exact basis polynomial')
        n = norm(p,g)
        need(n.denominator == 1 and n == w['signed_norm'] != 0, 'independent signed field norm')
        need(over(1,n) == F(w['inverse_norm']), 'inverse norm pair')
        if k < len(retained):
            v = w['valuations']
            need(abs(n) == e['norm'] == prod(P['p']**t for P,t in zip(base['generators'],v)), 'full norm/valuation identity')
            powers = {str(p):sum(v[i] for i,P in enumerate(base['generators']) if P['p']==p)
                      for p in sorted({P['p'] for P in base['generators']})}
            need(powers == w['norm_prime_exponents'] and all(t%2==0 for p,t in powers.items() if int(p) not in (2,3,5,11)), 'entire rational support')
        signs, bern = [],[]
        for i,(lo,hi) in enumerate(intervals):
            enclosure = box_horner(p,lo,hi)
            need(enclosure == [F(x) for x in w['alpha_value_intervals'][i]], 'entire saved interval evaluation')
            bs = bernstein(p,lo,hi)
            need(all(x>0 for x in bs) or all(x<0 for x in bs), 'independent Bernstein sign certificate')
            bit = int(bs[0]<0)
            need((enclosure[0]>0 and bit==0) or (enclosure[1]<0 and bit==1), 'both sign algorithms agree')
            signs.append(bit)
            bern.append(bs)
        bits = [int(n<0)] + signs
        mask = sum(b<<i for i,b in enumerate(bits))
        need(bits == w['sign_bits'] and sum(bits)%2==0 and mask==w['mask'], 'all five signs and norm parity')
        R['verified_rows'].append(dict(id=w['id'],signed_norm=int(n),sign_bits=bits,mask=mask,bernstein=bern))
    local = []
    need(len(d['gaps'])==6 and d['infinity_mask']==0, 'all real gaps plus infinity')
    for j,rec in enumerate(d['gaps']):
        x = F(rec['sample'])
        need((j==0 or roots[j-1][1]<x) and (j==5 or x<roots[j][0]), 'sample strictly in correct gap')
        v = point(G,x)
        bits = [int(x < lo) for lo,hi in roots]
        mask = sum(b<<i for i,b in enumerate(bits))
        need(rec == dict(gap=j,sample=str(x),G_value=str(v),real_point=v>0,sign_bits=bits,mask=mask), 'full gap evaluation and signs')
        need(v!=0 and (v<0)==bool(sum(bits)%2), 'exact quintic sign')
        if v>0:
            local.append(mask)
    local.append(0)
    need(d['local_rows']==local, 'complete Stoll generating set')
    verify_elimination(local,d['local_elimination'])
    rows = local + [w['mask'] for w in d['witnesses']]
    verify_elimination(rows,d['combined_elimination'])
    A,U = span(local),span(rows)
    need(len(A)==4 and len(U)==16 and all(x.bit_count()%2==0 for x in U), 'real image and full real norm kernel')
    quotient = (len(U)//len(A)).bit_length()-1
    need(quotient==2, 'certified quotient rank two')
    # Exhaust every possible real norm-kernel signature and its quotient coset.
    norm_kernel = {x for x in range(32) if x.bit_count()%2==0}
    need(U == norm_kernel, 'all possible real norm signatures covered')
    representatives = []
    covered = set(A)
    for w in d['witnesses']:
        if w['mask'] not in covered:
            representatives.append(w['id'])
            covered |= {x^w['mask'] for x in covered}
    need(len(representatives)==2 and covered==U, 'explicit independent global witnesses')
    expected_result = dict(accepted=182,retained_box=len(retained),rejected_box=len(rejected),rational_appended=5,
                           witnesses=len(d['witnesses']),coordinates=5,matrix_columns=len(rows),local_rank=2,
                           combined_rank=4,quotient_rank=2,ambient_dimension_constant=11,filtered_dimension_constant=9,
                           class_contribution_upper_bound=2,rank_bound_constant=8,unconditional_rank_upper_bound=10,
                           required_rank_upper_bound=1)
    need(d['result']==expected_result, 'every reported bound and threshold')
    need(len(rows)<=192 and len(rows)==43 and max(counts)<=64, 'all fixed-domain caps')
    need(d['bounds']['max_rational_bits']<=4096, 'reported producer bit cap')
    R.update(result=expected_result, quotient_basis_ids=representatives,
             local_span=sorted(A), full_real_norm_kernel=sorted(U), bisections=counts,
             completed=True)


try:
    main()
except Exception as exc:
    R['failures'].append(dict(error=str(exc),traceback=traceback.format_exc()))
finally:
    OUT.write_text(json.dumps(R,default=str,indent=2)+'\n')
    print(json.dumps(dict(completed=R['completed'],checks=R['checks'],result=R.get('result'),
                          quotient_basis_ids=R.get('quotient_basis_ids'),bounds=R['bounds'],
                          failures=R['failures'],verification=str(OUT))))
if not R['completed']:
    raise SystemExit(1)
