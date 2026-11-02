#!/usr/bin/env python3
"""Capped degree-16 signed spatial enclosure. Exact dyadic interval endpoints.

This is a producer, not an independent certificate audit. See the working
record and canonical result for the real-parameter Taylor specialization.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import factorial, isqrt
import json
import sys

HERE = Path(__file__).resolve().parent
DEST = HERE / 'spatial-signed'
DEST.mkdir(exist_ok=True)
BITS, G, MAXOPS, MAXEVAL, MAXDEPTH = 256, 1 << 256, 1 << 28, 65536, 16
ops = evaluations = 0


class Cap(Exception):
    pass


def tick():
    global ops
    if ops == MAXOPS:
        raise Cap('scalar interval operation cap')
    ops += 1


def ceildiv(a, b):
    return -((-a)//b)


class I:
    def __init__(self, a, b=None, raw=False):
        if raw:
            self.a, self.b = a, b
        else:
            a, b = F(a), F(a if b is None else b)
            self.a = a.numerator*G//a.denominator
            self.b = ceildiv(b.numerator*G, b.denominator)
        assert self.a <= self.b

    def __add__(self, v):
        tick()
        v = iv(v)
        return I(self.a+v.a, self.b+v.b, True)

    __radd__ = __add__

    def __neg__(self):
        tick()
        return I(-self.b, -self.a, True)

    def __sub__(self, v):
        return self+-iv(v)

    def __rsub__(self, v):
        return iv(v)+-self

    def __mul__(self, v):
        tick()
        v = iv(v)
        p = [x*y for x in (self.a, self.b) for y in (v.a, v.b)]
        return I(min(p)//G, ceildiv(max(p), G), True)

    __rmul__ = __mul__

    def __truediv__(self, v):
        tick()
        v = iv(v)
        assert v.a*v.b > 0, 'zero-containing denominator'
        return self*I(G*G//v.b, ceildiv(G*G, v.a), True)

    def __rtruediv__(self, v):
        return iv(v)/self


def iv(v):
    return v if isinstance(v, I) else I(v)


def rat(v):
    assert int(v['denominator']) > 0
    return F(int(v['numerator']), int(v['denominator']))


def read(v):
    return I(rat(v['lower']), rat(v['upper']))


def mag(v):
    tick()
    return max(abs(v.a), abs(v.b))


def sq(v):
    tick()
    return I(0 if v.a <= 0 <= v.b else min(v.a*v.a, v.b*v.b)//G,
             ceildiv(max(v.a*v.a, v.b*v.b), G), True)


def root(v):
    tick()
    assert v.a >= 0
    return I(isqrt(v.a*G), isqrt(v.b*G)+1, True)


def cmul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def norm(z):
    return root(sq(z[0])+sq(z[1]))


elementary = []


def logpt(a):
    assert a > 0
    k, v = 0, F(a, G)
    while v > 2:
        v /= 2
        k += 1
    while v < 1:
        v *= 2
        k -= 1
    z = I((v-1)/(v+1))
    z2, power, total = z*z, z, I(0)
    for j in range(110):
        total += power/(2*j+1)
        power *= z2
    tail = 2*power/(221*(1-z2))
    ans = 2*total+I(0, F(tail.b, G))
    elementary.append(dict(kind='log_mantissa', v=str(v), k=k,
                           sum=total, tail=tail, enclosure=ans))
    return ans+k*LOG2 if k else ans


def logi(v):
    return I(logpt(v.a).a, logpt(v.b).b, True)


def exppt(a):
    # |a/64|<1, absolute Taylor remainder bounded by 3/71!.
    assert abs(a) < 64*G
    u = I(F(a, 64*G))
    term, total = I(1), I(1)
    for k in range(1, 71):
        term = term*u/k
        total += term
    e = I(F(3, factorial(71)))
    ans = total+I(-e.b, e.b, True)
    assert ans.a > 0
    for _ in range(6):
        ans = sq(ans)
    elementary.append(dict(kind='exp', argument=str(a), sum=total,
                           scaled_remainder=e, enclosure=ans))
    return ans


def expi(v):
    return I(exppt(v.a).a, exppt(v.b).b, True)


def cis(v):
    # Exact integer range reduction; any integer is legitimate.
    turns = (v.a+v.b+PI.a+PI.b)//(2*(PI.a+PI.b))
    r = v-2*turns*PI
    assert mag(r) <= 4*G
    term, co, si = I(1), I(0), I(0)
    for k in range(112):
        if k % 4 == 0:
            co += term
        elif k % 4 == 1:
            si += term
        elif k % 4 == 2:
            co -= term
        else:
            si -= term
        term = term*r/(k+1)
    e = ceildiv(mag(r)**112, factorial(112)*G**111)
    co, si = co+I(-e, e, True), si+I(-e, e, True)
    elementary.append(dict(kind='cis', phase=v, turns=turns, reduced=r,
                           remainder_grid=str(e), cosine=co, sine=si))
    return co, si


def encode(v):
    if isinstance(v, I):
        return [str(v.a), str(v.b)]
    if isinstance(v, F):
        return str(v)
    if isinstance(v, dict):
        return {k: encode(w) for k, w in v.items()}
    if isinstance(v, (tuple, list)):
        return [encode(w) for w in v]
    return v


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def write(p, v):
    tmp = p.with_suffix('.tmp')
    tmp.write_text(json.dumps(encode(v), separators=(',', ':'))+'\n')
    tmp.replace(p)


def sigma_eta(x):
    den = 1+x*x
    u = 1/x
    at = I((u-u*u*u/3).a, u.b, True)
    a = PI/2-at
    ls = logi(den)/2-LOG4PI
    return I(F(1, 2))+t*ls/4-t/(2*den), x/2+t*(a/2-3*x/den)/2


def horner(coeff, y):
    ans = coeff[-1]
    for c in reversed(coeff[:-1]):
        ans = ans*y+c
    return ans


report = dict(result='IN_PROGRESS', precision_bits=BITS, degree=16,
              limits=dict(evaluations=MAXEVAL, scalar_interval_ops=MAXOPS,
                          depth=MAXDEPTH, precision_replays=1),
              interval_encoding='integer endpoints times 2^-256',
              independent_audit=False, roots=[], failures=[])
current = None
manifest = DEST/'certificate.json'
resume = None
if '--resume-normalized' in sys.argv:
    resume = json.loads((DEST/'pre-normalization.json').read_text())
    assert resume['result'] == 'IN_PROGRESS' and resume['completed_through'] == 691027
    ops, evaluations = resume['operations'], resume['evaluations']
    report['prior_interrupted_run'] = dict(path='pre-normalization.json',
        sha256=digest(DEST/'pre-normalization.json'),
        partial='pre-normalization-partial-cell.json',
        partial_sha256=digest(DEST/'pre-normalization-partial-cell.json'),
        producer='unnormalized-producer.txt',
        producer_sha256=digest(DEST/'unnormalized-producer.txt'),
        operations=ops,evaluations=evaluations,
        correction='Prior IN_PROGRESS/all-covered banner was interrupted, not a completion claim; normalize before large radius powers.')
    report['roots'] = resume['roots']
    for rr in report['roots']:
        rr['max_cost'] = I(*map(int,rr['max_cost']),raw=True)
try:
    corner = json.loads((HERE/'fixed-corner-two-charge.json').read_text())
    audit = json.loads((HERE/'l499-certificate-audit.json').read_text())
    endpoint = json.loads((HERE/'phase-sensitive-256-block-certificate.json').read_text())
    caudit = json.loads((HERE/'c499c-certificate-audit.json').read_text())
    inputs = {r['path']: r['sha256'] for r in audit['inputs']}
    inputs.update({r['path']: r['sha256'] for r in caudit['inputs']})
    assert inputs['fixed-corner-two-charge.json'] == digest(HERE/'fixed-corner-two-charge.json')
    assert caudit['producer_sha256'] == digest(HERE/'phase-sensitive-256-block-certificate.py')
    assert inputs['phase-sensitive-256-block-certificate.json'] == digest(HERE/'phase-sensitive-256-block-certificate.json')
    for name, h in inputs.items():
        assert digest(HERE/name) == h, name
    report['inputs'] = inputs
    report['endpoint_input_hashes'] = dict(certificate=digest(HERE/'phase-sensitive-256-block-certificate.json'),
                                         audit=digest(HERE/'c499c-certificate-audit.json'))
    t, X, n, N = I('.16836'), I('6000284561421.5'), 691004, 691260
    ell0, eps = I('24.18022820120389'), I('.0000006')
    eps1 = (eps+I('.0000013'))*I('8.770232')/I('.14142')
    r0 = I(F(14176540015048665224252705167939023,
             33554432000000000000000000000000000000))
    assert rat(corner['bounds']['reserve_lower']) == F(14176540015048665224252705167939023,
             33554432000000000000000000000000000000)
    PI = read(corner['elementary_inputs']['pi'])
    LOG2 = logpt(2*G)
    LOG4PI = logi(4*PI)
    R, J, D = [read(corner['bounds'][k]) for k in ('R', 'Jplus', 'product_derivative_cap')]
    h = {row['j']: read(row['log_j']) for row in endpoint['primitive_rows']}
    assert list(h) == list(range(n+1, N+1))
    assert rat(corner['parameters']['x']) == F('6000284561421.5')
    assert rat(corner['parameters']['t']) == F('.16836')
    Y = 4*PI*(N*N-t/16)
    C = {q: 4*PI*(q*q-t/16) for q in range(n, N+1)}
    assert C[n].b <= X.a < C[n+1].a
    domain = t*(read(corner['elementary_inputs']['L'])+(Y-X)/X)
    assert Y.a > X.b and domain.b < I('5.17').a
    sigmaX = read(corner['elementary_inputs']['sigma'])
    wfirst = expi(t*h[n+1]*h[n+1]/4-sigmaX*h[n+1])
    Scap = 256*wfirst
    sumlogs = I(0)
    for row in corner['prime_rows']:
        sumlogs += read(row['log_p'])
    support = h[N]+sumlogs
    K = R*(I(F(53, 3))+Scap)*support
    QX = X*(X*X+5)/sq(1+X*X)
    CX = (7*X*X-5)/sq(1+X*X)
    Us = t*(QX+CX)*K/ell0
    Ur = R*eps/2+2*(D*eps+R*eps1)/ell0
    report['parameters'] = dict(t=t,X=X,n=n,N=N,Y=Y,ell0=ell0,epsilon=eps,
                                epsilon_1=eps1,reserve=r0,domain_upper=domain)
    report['charges'] = dict(R0=R,J0=J,D0=D,S_cap=Scap,support=support,K=K,
                             saddle=Us,remainder=Ur)
    report['empty_initial_cell'] = dict(q=n,left=X,right=C[n+1],B=I(0),
                                        cost=Us+Ur,passed=(Us+Ur).b<r0.a)
    assert report['empty_initial_cell']['passed']
    report['initial_elementary'] = elementary[:]
    elementary.clear()
    write(manifest, report)

    for q in range(n+1,N+1):
        if resume and q <= resume['completed_through']:
            continue
        # Closed outward supersets include both sides' equality tests.
        xb = I(C[q].a, C[q if q == N else q+1].b, True)
        sig, eta = sigma_eta(xb)
        h0 = I((h[n+1].a+h[n+1].b+h[q].a+h[q].b)//4,
               (h[n+1].a+h[n+1].b+h[q].a+h[q].b)//4, True)
        data = []
        for j in range(n+1,q+1):
            delta = h[j]-h0
            weight = expi(t*h[j]*h[j]/4-sig*h[j])
            data.append(dict(j=j,delta=delta,weight=weight))
        current = dict(q=q,x_superset=xb,sigma=sig,eta=eta,h0=h0,terms=data,
                       attempts=[],canonical_left=q,right_comparison=q,
                       canonical_right=q if q==N else q+1)
        rootfile = DEST/f'cell-{q}.json'
        prefactor = 1+2*(h0+J)/ell0

        def remainder(radius):
            rem = I(0)
            remV = I(0)
            for row in data:
                powers = [I(1)]
                scaled_delta = row['delta']*radius
                for k in range(1,18):
                    powers.append(powers[-1]*scaled_delta/k)
                row['normalized_powers'] = powers
                a = row['weight']*I(0, mag(powers[17]), True)
                rem += a
                remV += a*I(0,mag(row['delta']),True)
            return rem,remV

        depth = 0
        while True:
            pieces = 1 << depth
            # Integer dyadic eta endpoints; adjacent cells meet exactly.
            step = ceildiv(eta.b-eta.a,pieces)
            radius = I(F(step,2*G))
            rem, remV = remainder(radius)
            remcost = R*(prefactor*2*rem+4*remV/ell0)
            if remcost.b < (r0.a-(Us+Ur).b)//8 or depth==MAXDEPTH:
                break
            depth += 1

        while True:
            if depth > MAXDEPTH:
                raise Cap('depth cap without strict enclosure')
            pieces = 1 << depth
            step = ceildiv(eta.b-eta.a,pieces)
            radius = I(F(step,2*G))
            rem, remV = remainder(radius)
            attempt = dict(depth=depth,pieces=pieces,step_grid=str(step),radius=radius,
                           remainder=rem,remainder_centered_log=remV,leaves=[],
                           normalized_powers=[row['normalized_powers'] for row in data])
            current['attempts'].append(attempt)
            # Fixed eta grid: the first centre and one step phasor per term.
            centre = I(F(2*eta.a+step,2*G))
            states = []
            for row in data:
                phase = cis(-centre*row['delta'])
                jump = cis(-I(step,step,True)*row['delta'])
                states.append([phase,jump])
            attempt['phase_initial_and_step'] = [[s[0],s[1]] for s in states]
            allpass = True
            for cell in range(pieces):
                if evaluations == MAXEVAL:
                    raise Cap('enclosure evaluation cap')
                evaluations += 1
                ps = [[I(0) for _ in range(17)] for _ in range(4)]
                for row,state in zip(data,states):
                    ar,ai = state[0][0]*row['weight'],state[0][1]*row['weight']
                    for k in range(17):
                        re,im = ar*row['normalized_powers'][k],ai*row['normalized_powers'][k]
                        if k%4==1:
                            re,im=im,-re
                        elif k%4==2:
                            re,im=-re,-im
                        elif k%4==3:
                            re,im=-im,re
                        ps[0][k] += re
                        ps[1][k] += im
                        ps[2][k] += re*row['delta']
                        ps[3][k] += im*row['delta']
                    if cell+1 < pieces:
                        state[0] = cmul(state[0],state[1])
                yy = I(-1,1)
                ranges = [horner(p,yy)+I(-e.b,e.b,True)
                          for p,e in zip(ps,[rem,rem,remV,remV])]
                s,v = norm(ranges[:2]),norm(ranges[2:])
                bg = R*(prefactor*s+2*v/ell0)
                cost = bg+Us+Ur
                passed = cost.b < r0.a
                allpass &= passed
                attempt['leaves'].append(dict(index=cell,coefficients=ps,ranges=ranges,
                    S_modulus=s,V_modulus=v,B=bg,total_cost=cost,passed=passed))
            attempt['passed'] = allpass
            if allpass:
                break
            depth += 1
        current['elementary'] = elementary[:]
        elementary.clear()
        current['passed'] = True
        write(rootfile,current)
        worst = max(attempt['leaves'],key=lambda row:row['total_cost'].b)
        report['roots'].append(dict(q=q,path=rootfile.name,sha256=digest(rootfile),
                                   depth=depth,evaluations=sum(len(a['leaves']) for a in current['attempts']),
                                   max_cost=worst['total_cost']))
        current = None
        report.update(operations=ops,evaluations=evaluations,completed_through=q)
        write(manifest,report)
        if (q-n)%32==0 or q==N:
            print(f'covered through q={q}; evaluations={evaluations}; operations={ops}',flush=True)
    report['result']='PASS'
except Cap as exc:
    report.update(result='INCONCLUSIVE',stop=str(exc))
except KeyboardInterrupt:
    report.update(result='INCONCLUSIVE',stop='interrupted; partial evidence preserved')
except Exception as exc:
    report.update(result='IMPLEMENTATION_FAILURE',stop=f'{type(exc).__name__}: {exc}')
    report['failures'].append(report['stop'])
finally:
    if current is not None:
        current['elementary']=elementary[:]
        write(DEST/'partial-cell.json',current)
        report['partial_cell']=dict(path='partial-cell.json',sha256=digest(DEST/'partial-cell.json'),q=current['q'])
    report.update(operations=ops,evaluations=evaluations,script_sha256=digest(Path(__file__)),
                  precision_replays=0)
    if report['roots']:
        report['maximum_completed_cost']=max((r['max_cost'] for r in report['roots']),key=lambda v:v.b)
    write(manifest,report)
    print(f"{report['result']}: {report.get('stop','all canonical cells covered')}")
    print(f'evaluations={evaluations}/{MAXEVAL}; scalar interval operations={ops}/{MAXOPS}')
    if 'maximum_completed_cost' in report:
        v=report['maximum_completed_cost']
        print('maximum completed cost upper (exact)='+str(F(v.b,G)))
    if 'parameters' in report:
        print('required every cost < reserve lower (exact)='+str(F(r0.a,G)))
    print('certificate=scripts/heat/spatial-signed/certificate.json')
    print('failures='+str(report['failures']))
