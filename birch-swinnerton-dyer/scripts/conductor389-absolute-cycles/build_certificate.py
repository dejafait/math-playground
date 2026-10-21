#!/usr/bin/env python3
"""Fixed full absolute lattice and independently signed period certificate.

Recovery inputs are L030 fixed structural/dual evidence only. No twist value,
calibrated symbols, BSD, rank or Sha data is loaded. Source contract: approved conductor-389 assessment; L043 mechanism.
"""
import json
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
MOD = 389


def ceilq(x):
    return -((-x.numerator)//x.denominator)


class Interval:
    def __init__(self, bits):
        self.D = 1 << bits

    def out(self, lo, hi=None):
        if hi is None:
            hi = lo
        assert lo <= hi
        return [(lo*self.D).__floor__(), ceilq(hi*self.D)]

    def add(self, x, y):
        return [x[0]+y[0], x[1]+y[1]]

    def sub(self, x, y):
        return [x[0]-y[1], x[1]-y[0]]

    def mul(self, x, y):
        v = [a*b for a in x for b in y]
        return [min(v)//self.D, -((-max(v))//self.D)]

    def scale(self, x, a):
        return self.out(*sorted(F(a)*F(t, self.D) for t in x))

    def div(self, x, y):
        assert y[0] > 0
        v = [F(a, b) for a in x for b in y]
        return self.out(min(v), max(v))


def matmul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def prime(p):
    return p >= 2 and all(p % k for k in range(2, isqrt(p)+1))


def atan(inv, count):
    s = sum((F((-1)**k, (2*k+1)*inv**(2*k+1)) for k in range(count)), F(0))
    t = s+F((-1)**count, (2*count+1)*inv**(2*count+1))
    return sorted([s, t])


def exponential(x, count):
    assert 0 < x < 1
    s = sum(((-x)**k/F(factorial(k)) for k in range(count+1)), F(0))
    return sorted([s, s+(-x)**(count+1)/factorial(count+1)])


def cosine(c, j, pi, degree):
    if j == 0:
        return {'j': 0, 'interval': [c.D, c.D]}
    theta = sorted(2*F(j, MOD)*F(t, c.D) for t in pi)
    mid = sum(theta)/2
    radius = (theta[1]-theta[0])/2
    s = sum((F((-1)**k)*mid**(2*k)/factorial(2*k)
             for k in range(degree+1)), F(0))
    # Taylor remainder of degree 2*degree+1 (odd coefficient is zero),
    # plus Lipschitz error |cos(theta)-cos(mid)| <= |theta-mid|.
    err = abs(mid)**(2*degree+2)/factorial(2*degree+2)+radius
    return {'j': j, 'theta': [str(t) for t in theta], 'midpoint': str(mid),
            'radius': str(radius), 'polynomial': str(s), 'error': str(err),
            'interval': c.out(s-err, s+err)}


INPUTS = [ROOT/'scripts/relative-t2/certificate.json',
          ROOT/'scripts/dual-kernel/conductor389-certificate.json',
          ROOT/'scripts/dual-kernel/conductor389-arithmetic.json']
SCHEDULE = [(256, 64), (1024, 96), (4096, 128)]


def bezout(values):
    # Complete extended gcd; maintains sum z_i values_i = g >= 0.
    g, z = 0, [0]*len(values)
    for i, v in enumerate(values):
        oldr, r, olds, ss, oldt, tt = g, v, 1, 0, 0, 1
        while r:
            q = oldr//r
            oldr, r = r, oldr-q*r
            olds, ss = ss, olds-q*ss
            oldt, tt = tt, oldt-q*tt
        if oldr < 0:
            oldr, olds, oldt = -oldr, -olds, -oldt
        z = [a*olds for a in z]
        z[i] += oldt
        g = oldr
    return g, z


def coefficients(T):
    counts, aps = [], {}
    for ell in range(2, T+1):
        if not prime(ell):
            continue
        if ell == 2:
            row = {'p': ell, 'pairs': [[x, y] for x in range(ell) for y in range(ell)
                    if (y*y+y-x*x*x-x*x+2*x) % ell == 0]}
            count = len(row['pairs'])
        else:
            chars = []
            for x in range(ell):
                disc = (1+4*(x*x*x+x*x-2*x)) % ell
                t = pow(disc, (ell-1)//2, ell)
                chars.append(-1 if t == ell-1 else t)
            row = {'p': ell, 'characters': chars}
            count = ell+sum(chars)
        row.update({'affine': count, 'a_p': ell-count})
        counts.append(row)
        aps[ell] = ell-count
    if 389 in aps:
        assert aps[389] == 1
    coeffs, factors = [0, 1], []
    for n in range(2, T+1):
        rem, value, fs = n, 1, []
        for ell in aps:
            if rem % ell:
                continue
            k = 0
            while rem % ell == 0:
                rem //= ell
                k += 1
            powers = [1, aps[ell]]
            for _ in range(2, k+1):
                powers.append(aps[ell]*powers[-1]-(0 if ell == 389 else ell)*powers[-2])
            value *= powers[k]
            fs.append([ell, k, powers])
        assert rem == 1
        coeffs.append(value)
        factors.append([n, fs])
    return counts, coeffs, factors


def enclosure(matrix, T, bits):
    global MOD
    a, b, MOD, d = matrix
    c = Interval(bits)
    atan_count, exp_count, cos_degree = bits//2+16, 64, 48
    ab = [atan(inv, atan_count) for inv in (5, 239)]
    pi_exact = [16*ab[0][0]-4*ab[1][1], 16*ab[0][1]-4*ab[1][0]]
    pi = c.out(*pi_exact)
    h = c.scale(pi, F(2, MOD))
    ex = [exponential(F(t, c.D), exp_count) for t in h]
    rex = [ex[1][0], ex[0][1]]
    r = c.out(*rex)
    counts, coeffs, factors = coefficients(T)
    # All residues used by both finite series, each with full Taylor evidence.
    residues = sorted({min(k % MOD, MOD-k % MOD)
                       for n in range(1, T+1) for k in (a*n, -d*n)})
    cosines = [cosine(c, j, pi, cos_degree) for j in residues]
    lookup = {row['j']: row['interval'] for row in cosines}
    def cos_residue(k):
        k %= MOD
        return lookup[min(k, MOD-k)]
    power, total, terms = [c.D, c.D], [0, 0], []
    for n in range(1, T+1):
        power = c.mul(power, r)
        diff = c.sub(cos_residue(a*n), cos_residue(-d*n))
        term = c.scale(c.mul(power, diff), F(coeffs[n], n))
        total = c.add(total, term)
        terms.append({'n': n, 'power': power, 'difference': diff, 'term': term, 'partial': total})
    nxt = c.mul(power, r)
    tail = c.div(c.scale(nxt, 2), [c.D-r[1], c.D-r[0]])[1]
    period = [total[0]-tail, total[1]+tail]
    return {'bits': bits, 'scale': c.D, 'T': T, 'atan_count': atan_count,
            'atan_brackets': [[str(t) for t in row] for row in ab],
            'pi_exact': list(map(str, pi_exact)), 'pi': pi, 'height': str(F(1, MOD)), 'h': h,
            'exp_count': exp_count, 'exp_exact': list(map(str, rex)), 'r': r,
            'cos_degree': cos_degree, 'cosines': cosines, 'point_counts': counts,
            'coefficients': coeffs, 'factorizations': factors, 'terms': terms,
            'next_power': nxt, 'tail_upper': tail, 'period_interval': period}


def make():
    structural, dual, arithmetic = [json.loads(p.read_text()) for p in INPUTS]
    p = structural['presentation']
    coords, lifts, sat = [p[k] for k in ('integral_generator_coordinates',
                                       'integral_quotient_basis_lifts', 'saturated_relation_basis')]
    assert arithmetic['model'] == [0, 1, 1, -2, 0] and arithmetic['conductor'] == 389
    assert (len(coords), len(lifts), len(sat)) == (390, 65, 325)
    endpoints = []
    for a, b, cc, d in structural['SL2_lifts']:
        def cusp(num, den):
            if den == 0:
                return [1, 0]
            x = F(num, den)
            return [x.numerator, x.denominator]
        endpoints.append([cusp(b, d), cusp(a, cc)])
    witnesses, raw = [], []
    for pair in endpoints:
        ws, flags = [], []
        for num, den in pair:
            flag = int(den % 389 == 0)
            tp, tq = (1, 0) if flag else (0, 1)
            u = num % 389 if flag else pow(den, -1, 389)
            assert 1 <= u < 389 and (tq-u*den) % 389 == 0 and (u*tp-num) % gcd(den, 389) == 0
            ws.append({'cusp': [num, den], 'class': flag, 'unit': u})
            flags.append(flag)
        witnesses.append(ws)
        raw.append(flags[1]-flags[0])
    B = [sum(x*y for x, y in zip(raw, lift)) for lift in lifts]
    assert B == [0]*64+[1]
    # Unimodular column permutation sends final coordinate to first.
    order = [64]+list(range(64))
    transform = [[int(i == order[j]) for j in range(65)] for i in range(65)]
    inverse = list(map(list, zip(*transform)))
    basis = [[row[j] for row in transform] for j in range(1, 65)]
    raw_basis = [[sum(x*y for x, y in zip(col, rows)) for rows in zip(*lifts)] for col in basis]
    phi = list(map(F, dual['line']['v']))
    image = [sum(x*y for x, y in zip(phi, col)) for col in basis]
    den = 1
    for x in image:
        den = den*x.denominator//gcd(den, x.denominator)
    integers = [int(x*den) for x in image]
    gg, z = bezout(integers)
    assert gg > 0
    gen = F(gg, den)
    values0 = [sum(x*y for x, y in zip(phi, row)) for row in coords]
    candidates = []
    for t in range(1, 389):
        if not values0[t]:
            continue
        cc = pow(389, -1, t) if t > 1 else 1
        if t > 1 and cc > t//2:
            cc -= t
        a = (1-389*cc)//t
        matrix = [a, -1, 389*cc, t]
        if cc < 0:
            matrix = [-x for x in matrix]
        candidates.append((abs(cc), t, matrix))
    candidates.sort()
    cycles = []
    for _, t, matrix in candidates[:3]:
        a, b, C, d = matrix
        assert C > 0 and a*d-b*C == 1 and F(b,d) == F(-1,t)
        rawcycle = [0]*390
        rawcycle[t] = -1
        cyclecoords = [-v for v in coords[t]]
        assert sum(x*y for x,y in zip(B,cyclecoords)) == 0
        cycles.append({'generator_index': t, 'raw': rawcycle, 'coordinates': cyclecoords,
                       'phi': str(-values0[t]), 'path': list(reversed(endpoints[t])),
                       'matrix': matrix, 'alpha': [str(F(-d,C)),str(F(1,C))],
                       'M_alpha': [str(F(a,C)),str(F(1,C))]})
    data = {'schema': 'conductor389-full-absolute-v1',
            'inputs': {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in INPUTS},
            'source_scope': {'model': arithmetic['model'], 'N':389, 'optimal_label':'389a1',
                             'absolute_Manin_constant':1, 'components':2,
                             'published_optimality_qualification':'L031 optimality only; complete isogeny class and two-period comparison'},
            'boundary': {'cusp_order':['zero','infinity'], 'endpoint_witnesses':witnesses,
                         'raw_reduced':raw, 'raw_full':[[-v for v in raw],raw],
                         'quotient_reduced':B, 'quotient_full':[[-v for v in B],B],
                         'source_images':[sum(x*y for x,y in zip(raw,row)) for row in structural['relations']],
                         'saturated_images':[sum(x*y for x,y in zip(raw,row)) for row in sat]},
            'kernel': {'unimodular_transform':transform, 'inverse':inverse,
                       'boundary_after_transform':matmul([B],transform), 'basis_columns':basis,
                       'raw_basis_columns':raw_basis, 'functional_values':list(map(str,image)),
                       'common_denominator':den, 'integer_values':integers, 'gcd':gg, 'bezout':z,
                       'positive_image_generator':str(gen), 'primitive_values':[str(x/gen) for x in image]},
            'candidate_policy':'first three sorted (abs(c),generator index) from all nonzero reversed fixed paths; least absolute inverse c, positive lower-left matrix',
            'candidates':cycles, 'attempts':[], 'selected_attempt':None, 'normalization':None, 'failures':[]}
    # Persist complete lattice and selected cycles before potentially long interval work.
    checkpoint = HERE/'production-checkpoint.json'
    checkpoint.write_text(json.dumps(data,indent=2)+'\n')
    for ci, cycle in enumerate(cycles):
        for si,(T,bits) in enumerate(SCHEDULE):
            f = enclosure(cycle['matrix'],T,bits)
            data['attempts'].append({'candidate_index':ci,'schedule_index':si,'fourier':f})
            checkpoint.write_text(json.dumps(data,indent=2)+'\n')
            print('Attempt',ci,si,'T,b =',T,bits,'period',f['period_interval'],'/',f['scale'],
                  '; required strict exclusion of zero',flush=True)
            interval=f['period_interval']
            if interval[0] > 0 or interval[1] < 0:
                data['selected_attempt']=len(data['attempts'])-1
                psign=1 if interval[0]>0 else -1
                betasign=psign*(1 if F(cycle['phi'])>0 else -1)
                scale=F(betasign)/(2*gen)
                values=[scale*x for x in values0]
                common=1
                for x in values:
                    common=common*x.denominator//gcd(common,x.denominator)
                primes=[ell for ell in range(2,common+1) if prime(ell) and common%ell==0]
                data['normalization']={'beta_sign':betasign,'beta_over_total_period':str(scale),
                                       'generator_values':list(map(str,values)), 'common_denominator':common,
                                       'denominator_primes':primes,
                                       'C_for_p_ge_5_good_ordinary':0 if all(ell<5 for ell in primes) else None}
                return data
    data['failures'].append('bounded orientation schedule exhausted without strict nonzero interval')
    return data


if __name__ == '__main__':
    try:
        data=make()
    except Exception as error:
        failure={'failures':[type(error).__name__+': '+str(error)],
                 'producer_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
        (HERE/'production-failure.json').write_text(json.dumps(failure,indent=2)+'\n')
        print(failure)
        raise
    out=HERE/'certificate.json'
    out.write_text(json.dumps(data,indent=2)+'\n')
    print('Full absolute kernel rank',len(data['kernel']['basis_columns']),'/ required 64; primitive image',data['kernel']['positive_image_generator'])
    print('Normalization:',data['normalization']['beta_over_total_period'] if data['normalization'] else None,
          '; all-generator denominator:',data['normalization']['common_denominator'] if data['normalization'] else None)
    print('Failures:',data['failures'],'; certificate:',out)
