#!/usr/bin/env python3
"""Exact/dyadic evaluation of a principal block of C744l's Schur matrix.

All 257 projection rows are retained. This is NOT the full 255 by255
certificate. Integer convolution and rational integration pay cancellation;
coefficient uncertainty is charged by explicit L2 bounds. No float decides
an inequality. Run from the notebook root; no environment changes needed.
"""
import ctypes
import gzip
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from math import comb, lcm
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('scalar486', HERE/'power-log-enclosure-486.py')
scalar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scalar)
B, S, ZERO, ONE = scalar.Ball, scalar.SCALE, scalar.ZERO, scalar.ONE
spec = importlib.util.spec_from_file_location('action485', HERE/'action-enclosure-485.py')
action = importlib.util.module_from_spec(spec)
spec.loader.exec_module(action)
INDICES = (2, 3, 256)


# GMP's integer multiplication is only an accelerator. Import/export are
# unsigned, most-significant byte first, size1, no nail bits. Python handles
# the signed coefficient packing and extraction. The exact convolution
# regressions below compare every coefficient against direct multiplication.
class MPZ(ctypes.Structure):
    _fields_ = [('alloc', ctypes.c_int), ('size', ctypes.c_int), ('limbs', ctypes.c_void_p)]


lib = ctypes.CDLL('/opt/homebrew/lib/libgmp.dylib')
zi, zc, zm, zim, zex = [getattr(lib, '__gmpz_'+n) for n in ('init','clear','mul','import','export')]
zi.argtypes = zc.argtypes = [ctypes.POINTER(MPZ)]
zm.argtypes = [ctypes.POINTER(MPZ)]*3
zim.argtypes = [ctypes.POINTER(MPZ),ctypes.c_size_t,ctypes.c_int,ctypes.c_size_t,
               ctypes.c_int,ctypes.c_size_t,ctypes.c_void_p]
zex.argtypes = [ctypes.c_void_p,ctypes.POINTER(ctypes.c_size_t),ctypes.c_int,
               ctypes.c_size_t,ctypes.c_int,ctypes.c_size_t,ctypes.POINTER(MPZ)]


def fastmul(x, y):
    assert x >= 0 and y >= 0
    if not x or not y:
        return 0
    xb = x.to_bytes((x.bit_length()+7)//8, 'big')
    yb = y.to_bytes((y.bit_length()+7)//8, 'big')
    a, b, c = MPZ(), MPZ(), MPZ()
    for z in (a,b,c): zi(ctypes.byref(z))
    try:
        zim(ctypes.byref(a),len(xb),1,1,1,0,xb)
        zim(ctypes.byref(b),len(yb),1,1,1,0,yb)
        zm(ctypes.byref(c),ctypes.byref(a),ctypes.byref(b))
        buf = ctypes.create_string_buffer(len(xb)+len(yb))
        count = ctypes.c_size_t()
        zex(buf,ctypes.byref(count),1,1,1,0,ctypes.byref(c))
        return int.from_bytes(buf.raw[:count.value],'big')
    finally:
        for z in (a,b,c): zc(ctypes.byref(z))


def iconv(a, b):
    """Signed exact integer convolution using nonnegative offset packing."""
    if not a or not b: return []
    ca, cb = max(map(abs,a)), max(map(abs,b))
    size = len(a)+len(b)-1
    if not ca or not cb: return [0]*size
    # Every offset product coefficient <=4 min(len(a),len(b)) ca cb;
    # choose a strictly larger base to prevent all carries between slots.
    width = ((4*min(len(a),len(b))*ca*cb).bit_length()+7)//8
    aa = int.from_bytes(b''.join((x+ca).to_bytes(width,'little') for x in a),'little')
    bb = int.from_bytes(b''.join((x+cb).to_bytes(width,'little') for x in b),'little')
    packed = fastmul(aa,bb).to_bytes(width*size,'little')
    ap, bp = [0], [0]
    for x in a: ap.append(ap[-1]+x)
    for x in b: bp.append(bp[-1]+x)
    out = []
    for k in range(size):
        alo, ahi = max(0,k-len(b)+1), min(len(a)-1,k)
        blo, bhi = max(0,k-len(a)+1), min(len(b)-1,k)
        count = ahi-alo+1
        offset = cb*(ap[ahi+1]-ap[alo])+ca*(bp[bhi+1]-bp[blo])+ca*cb*count
        out.append(int.from_bytes(packed[k*width:(k+1)*width],'little')-offset)
    return out


def midpoint(p):
    m = [(x.lo+x.hi)//2 for x in p]
    r = [max(y-x.lo,x.hi-y) for x,y in zip(p,m)]
    return m, r


def trim(p):
    while len(p)>1 and p[-1].lo==p[-1].hi==0: p.pop()
    return p


def padd(p, q):
    return trim([(p[k] if k<len(p) else ZERO)+(q[k] if k<len(q) else ZERO)
                 for k in range(max(len(p),len(q)))])


def scale(p, a):
    return trim([x*a for x in p])


def rational(x):
    x = F(x)
    return B.rational(x.numerator,x.denominator)


def pconv(p, q):
    pm, pr = midpoint(p)
    qm, qr = midpoint(q)
    m = iconv(pm,qm)
    r1 = iconv(list(map(abs,pm)),qr)
    r2 = iconv(pr,list(map(abs,qm)))
    r3 = iconv(pr,qr)
    return trim([B((x-a-b-c)//S, scalar.ceildiv(x+a+b+c,S))
                 for x,a,b,c in zip(m,r1,r2,r3)])


def compose(p, u, v):
    """p(u+v*t), with interval u,v and full coefficient enclosures."""
    out = [ZERO]
    for x in reversed(p):
        new = [ZERO]*(len(out)+1)
        for k,y in enumerate(out):
            new[k] = new[k]+y*u
            new[k+1] = new[k+1]+y*v
        new[0] = new[0]+x
        out = trim(new)
    return out


def legendre_integer(n):
    # P_n(2v-1) = sum_k (-1)^(n+k) binom(n,k)binom(n+k,k)v^k.
    return [(-1)**(n+k)*comb(n,k)*comb(n+k,k) for k in range(n+1)]


def check_integer_polynomials():
    # Direct recurrence checks at every coefficient for all degrees used.
    prev = [1]
    curr = [-1,2]
    if legendre_integer(0)!=prev or legendre_integer(1)!=curr: return False
    for n in range(1,256):
        left = [0]*(n+2)
        for k,x in enumerate(curr):
            left[k] -= (2*n+1)*x
            left[k+1] += 2*(2*n+1)*x
        for k,x in enumerate(prev): left[k] -= n*x
        nxt = legendre_integer(n+1)
        if left != [(n+1)*x for x in nxt]: return False
        prev,curr = curr,nxt
    return True


def check_kernel_identity():
    # Compare the simplified beta formula with C744k's unsimplified Phi
    # at endpoints/interior, both kernel parities and the highest monomial.
    for j in (0,1,2,95,96):
        for k in (0,1,2,256):
            beta = F(1,(j+k+1)*comb(j+k,j))
            for v in (F(0),F(1,2),F(1)):
                original = sum((F(comb(k,m),j+m+1)*v**(k-m)*(
                    (-1)**m*v**(j+m+1)+(1-v)**(j+m+1))
                    for m in range(k+1)),F(0))
                simplified = sum((F((-1)**l*comb(j,l),j-l+k+1)*v**l
                                  for l in range(j+1)),F(0))
                simplified += (1-(-1)**j)*beta*v**(j+k+1)
                if original != simplified: return False
    return True


def projection_polynomials(u, v):
    # Generate all affine-composed polynomials together by the three-term
    # recurrence, instead of separately composing each power polynomial.
    rows = [[ONE]]
    prev = [ONE]
    curr = [u*B.rational(2)-ONE,v*B.rational(2)]
    rows.append(scale(curr,B.rational(3).sqrt()))
    for n in range(1,256):
        nxt = [ZERO]*(len(curr)+1)
        c0 = (u*B.rational(2)-ONE)*B.rational(2*n+1)
        c1 = v*B.rational(2*(2*n+1))
        for k,x in enumerate(curr):
            nxt[k] = nxt[k]+x*c0
            nxt[k+1] = nxt[k+1]+x*c1
        for k,x in enumerate(prev): nxt[k] = nxt[k]-x*B.rational(n)
        nxt = [x.integer_div(n+1) for x in nxt]
        rows.append(scale(nxt,B.rational(2*n+3).sqrt()))
        prev,curr = curr,nxt
    return rows


def kernel_actions(g, ell, q, h):
    """Exact polynomial kernel formulas from C744k(10).

    mu_m=int w^m g(w) dw. Then Psi_j=sum_l binom(j,l)v^l mu_(j-l).
    Phi_j=sum_l (-1)^l binom(j,l)v^l mu_(j-l)
          +(1-(-1)^j)sum_k g_k j!k!/(j+k+1)! v^(j+k+1).
    The beta factor starts at1/(j+1), recurrence (k+1)/(j+k+2).
    """
    mu = []
    for m in range(97):
        z = ZERO
        for k,x in enumerate(g): z = z+x.integer_div(m+k+1)
        mu.append(z)
    qa, ha = [ZERO]*(len(g)+97), [ZERO]*97
    power = ell
    for j in range(97):
        cq, ch = q[j]*power, h[j]*power
        for l in range(j+1):
            t = mu[j-l]*B.rational(comb(j,l))
            qa[l] = qa[l]+t*cq*B.rational((-1)**l)
            ha[l] = ha[l]+t*ch
        if j%2:
            beta = B.rational(1,j+1)
            for k,x in enumerate(g):
                qa[j+k+1] = qa[j+k+1]+x*cq*beta*B.rational(2)
                beta = (beta*B.rational(k+1)).integer_div(j+k+2)
        power = power*ell
    # Unit-coordinate regular Q and H include the Jacobian ell above.
    return trim(qa), trim(ha)


def build_column(n, const, ratio, q, h):
    e = n%2
    sn, se = B.rational(2*n+1).sqrt(), B.rational(2*e+1).sqrt()
    pn = scale([B.rational(x) for x in legendre_integer(n)],sn)
    pe = scale([B.rational(x) for x in legendre_integer(e)],se)
    correction = scale(pe,ratio)
    g = padd(pn,scale(correction,B.rational(-1)))
    dg = padd(scale(pn,rational(sum((F(1,k) for k in range(1,n+1)),F(0)))),
              scale(correction,B.rational(-e)))
    qa, ha = kernel_actions(g,const['ell'],q,h)
    base = padd(padd(dg,scale(g,B.rational(-183,100))),scale(qa,B.rational(-1,2)))
    car = [ZERO]*n
    for r in range(n):
        z = ZERO
        for k in range(r+1,len(g)): z = z+g[k].integer_div(k-r)
        car[r] = z*B.rational((-1)**r)
    inter = padd(car,scale(ha,B.rational(2)))
    neg_g = [x*B.rational((-1)**k) for k,x in enumerate(g)]
    b = const['split_b']
    half = B.rational(1,2)
    pieces = []
    for j,(u,v) in enumerate(((ZERO,b),(half,b-half),(ONE,-half))):
        gp = compose(g,u,v)
        ng = compose(neg_g,u,v)
        bp = compose(base,u,v)
        ip = compose(inter,u,v)
        if j:
            reflect = compose(g,ONE+b-u,-v)
            ip = padd(ip,scale(reflect,const['a']*B.rational(2)))
        # logarithms are constants plus L_+/- (c*t), with exact log t
        # retained separately as prescribed in C744l Section2.
        if j==0:
            coeffs = ((const['log_b'],ZERO,0,1),
                      (ZERO,b,-1,0),(ZERO,b,1,0))
        elif j==1:
            w = ONE-b*B.rational(2)
            coeffs = ((-const['log2'],w,-1,0),
                      (-const['log2'],w,1,0),
                      (const['log_three_halves'],w.integer_div(3),-1,0))
        else:
            coeffs = ((ZERO,half,-1,0),(-const['log2'],ZERO,0,1),
                      (const['log2'],B.rational(1,4),-1,0))
        logs = []
        for c,z,kind,haslog in coeffs:
            pol = [c]
            power = ONE
            if kind:
                for k in range(1,769):
                    power = power*z
                    sign = -1 if kind==-1 else (-1)**(k+1)
                    pol.append(power.integer_div(k)*B.rational(sign))
            logs.append((pol,haslog))
        signs = {}
        for s in (-1,1):
            p = padd(bp,scale(ip,B.rational(s)))
            logco = (padd(scale(gp,B.rational(-1,2)),scale(ng,B.rational(-s))),
                     scale(gp,B.rational(-1,2)),scale(ng,B.rational(s)))
            logpart = [ZERO]
            for co,(lp,haslog) in zip(logco,logs):
                p = padd(p,pconv(co,lp))
                if haslog: logpart = padd(logpart,co)
            signs[s] = (p,logpart)
        pieces.append({'g':gp,'signs':signs})
    return pieces


def poly_error(p):
    m,r = midpoint(p)
    return sum(map(abs,m)),sum(r)


def action_size_error(pair):
    p,q = pair
    pm,pr = poly_error(p)
    qm,qr = poly_error(q)
    # In L2(0,1), ||log t||=sqrt2<2.
    return pm+2*qm,pr+2*qr


def exact_integral(pair1, pair2):
    """Midpoint integral exactly, interval coefficient error charged in L2."""
    p,q = pair1
    u,v = pair2
    pm,_ = midpoint(p); qm,_ = midpoint(q)
    um,_ = midpoint(u); vm,_ = midpoint(v)
    aa = iconv(pm,um)
    bb = iconv(pm,vm)
    cc = iconv(qm,um)
    dd = iconv(qm,vm)
    limit = max(map(len,(aa,bb,cc,dd)))
    den = 1
    for k in range(1,limit+1): den = lcm(den,k)
    common = den**3
    numerator = 0
    for k in range(limit):
        t = k+1
        numerator += (aa[k] if k<len(aa) else 0)*(common//t)
        numerator -= ((bb[k] if k<len(bb) else 0)+(cc[k] if k<len(cc) else 0))*(common//t**2)
        numerator += 2*(dd[k] if k<len(dd) else 0)*(common//t**3)
    center = B.rational(numerator,common*S*S)
    b1,e1 = action_size_error(pair1)
    b2,e2 = action_size_error(pair2)
    err = scalar.ceildiv(b1*e2+b2*e1+e1*e2,S)
    return B(center.lo-err,center.hi+err)


def power_moments(pair):
    """All int t^k(P+Q log t), k0..256; rational midpoint sums."""
    p,q = pair
    pm,_ = midpoint(p); qm,_ = midpoint(q)
    limit = max(len(p),len(q))+256
    den = 1
    for k in range(1,limit+1): den = lcm(den,k)
    den = den*den
    size,err = action_size_error(pair)
    # ||t^k||<=1; the same L2 error covers every moment.
    out = []
    for k in range(257):
        numerator = sum(x*(den//(m+k+1)) for m,x in enumerate(pm))
        numerator -= sum(x*(den//(m+k+1)**2) for m,x in enumerate(qm))
        c = B.rational(numerator,den*S)
        out.append(B(c.lo-err,c.hi+err))
    return out


def interval_dot(p, q):
    total = ZERO
    for x,y in zip(p,q): total = total+x*y
    return total


def save_interval(x):
    return x.json()


def display(x):
    return {'lower':str(float(F(x.lo,S))), 'upper':str(float(F(x.hi,S)))}


def main():
    started = time.monotonic()
    failures = []
    checks = {}
    checks['all_257_integer_legendre_recurrences'] = check_integer_polynomials()
    checks['all_60_unsimplified_kernel_identity_comparisons'] = check_kernel_identity()
    tests = [([2,-3,7],[-8,1]),([0],[3,-4]),([-4],[-5]),
             ([2**2500,-3,2**2000],[7,-2**2100,4])]
    checks['all_exact_convolution_regressions'] = all(iconv(a,b)==[
        sum(a[i]*b[k-i] for i in range(len(a)) if 0<=k-i<len(b))
        for k in range(len(a)+len(b)-1)] for a,b in tests)
    const,_,ratios,_ = scalar.scalar_inputs()
    q = [rational(x) for x in action.quotient_coefficients(F(1,2),97)[1:]]
    h = [rational(x/2) for x in action.quotient_coefficients(F(-3,2),97)[1:]]
    columns = {}
    for n in INDICES:
        columns[n] = build_column(n,const,ratios[n-2],q,h)
        print(f'Enclosed three-piece coefficients n={n}; elapsed {time.monotonic()-started:.1f}s',flush=True)
    coeff_path = HERE/'matrix-coefficients-487.json.gz'
    arrays = {'precision_bits':scalar.BITS,'indices':list(INDICES),'columns':{}}
    for n,pieces in columns.items():
        arrays['columns'][str(n)] = [{'g':[save_interval(x) for x in piece['g']],
            'signs':{str(s):{'P':[save_interval(x) for x in pair[0]],
                            'Q':[save_interval(x) for x in pair[1]]}
                     for s,pair in piece['signs'].items()}} for piece in pieces]
    with gzip.open(coeff_path,'wt') as fp: json.dump(arrays,fp,separators=(',',':'))
    del arrays
    print(f'Complete selected-column coefficient evidence: {coeff_path.name}',flush=True)
    lengths = (const['split_b'],B.rational(1,2)-const['split_b'],B.rational(1,2))
    transforms = []
    half = B.rational(1,2); b = const['split_b']
    for u,v in ((ZERO,b),(half,b-half),(ONE,-half)):
        transforms.append(projection_polynomials(u,v))
    print(f'Enclosed all 257 projection polynomials on all three pieces; elapsed {time.monotonic()-started:.1f}s',flush=True)
    result = {'precision_bits':scalar.BITS,'interval_denominator':str(S),
        'indices':list(INDICES),'projection_rows':257,
        'coefficient_artifact':str(coeff_path.relative_to(HERE.parent.parent)),
        'coefficient_artifact_sha256':hashlib.sha256(coeff_path.read_bytes()).hexdigest(),
        'scope':'Only a3 by3 principal block; all257 covariance projection rows retained.',
        'full_two_sign_margin_certified':False,'signs':{},'checks':checks}
    for s in (-1,1):
        projected = []
        for n in INDICES:
            moments = [power_moments(piece['signs'][s]) for piece in columns[n]]
            row = []
            for k in range(257):
                z = ZERO
                for j in range(3): z = z+interval_dot(transforms[j][k],moments[j])*lengths[j]
                row.append(z)
            projected.append(row)
        gram, head = [], []
        for n in INDICES:
            grow, hrow = [], []
            for m in INDICES:
                g,hv = ZERO,ZERO
                for j in range(3):
                    ap,bp = columns[n][j]['signs'][s],columns[m][j]['signs'][s]
                    g = g+exact_integral(ap,bp)*lengths[j]
                    hv = hv+exact_integral((columns[n][j]['g'],[ZERO]),bp)*lengths[j]
                grow.append(g); hrow.append(hv)
            gram.append(grow); head.append(hrow)
        sym_head = [[(head[i][j]+head[j][i]).integer_div(2) for j in range(3)] for i in range(3)]
        cov = [[gram[i][j]-interval_dot(projected[i],projected[j]) for j in range(3)] for i in range(3)]
        schur = [[sym_head[i][j]-cov[i][j]*B.rational(250,171) for j in range(3)] for i in range(3)]
        # Exactly dyadic Gershgorin bound for this block only.
        lower = min(schur[i][i].lo-sum(max(abs(schur[i][j].lo),abs(schur[i][j].hi))
                                     for j in range(3) if j!=i) for i in range(3))
        width = max(x.hi-x.lo for matrix in (head,gram,cov,schur) for row in matrix for x in row)
        checks[f'sign_{s}_block_enclosure_width_below_1e_minus_30'] = F(width,S)<F(1,10**30)
        checks[f'sign_{s}_principal_gershgorin_above_one_over_25'] = 25*lower>S
        result['signs'][str(s)] = {
            'projected_moments':[[save_interval(x) for x in row] for row in projected],
            'unsymmetrized_head':[[save_interval(x) for x in row] for row in head],
            'total_gram':[[save_interval(x) for x in row] for row in gram],
            'complete_covariance':[[save_interval(x) for x in row] for row in cov],
            'schur':[[save_interval(x) for x in row] for row in schur],
            'schur_display':[[display(x) for x in row] for row in schur],
            'gershgorin_lower_numerator':str(lower),
            'gershgorin_lower_display':str(float(F(lower,S))),
            'maximum_matrix_interval_width':scalar.frac_json(F(width,S))}
        print(f'sign{s:+}: principal Gershgorin lower {float(F(lower,S)):.12g}; required1/25 (PRINCIPAL ONLY)',flush=True)
        print(f'sign{s:+}: matrix width <= {scalar.up(F(width,S))}; required<1e-30',flush=True)
    result['failures'] = [k for k,v in checks.items() if not v]
    result['checks_pass'] = not result['failures']
    result['unresolved'] = [
        'Columns4..255 and every off-block interaction remain unenclosed.',
        'Positive principal blocks do not lower-bound the full255 by255 matrices.',
        'C744i/j/k/l remain independently unaudited; no full mu or RH conclusion.']
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Checks {sum(checks.values())}/{len(checks)}; failures {result["failures"]}',flush=True)
    print(f'Full certificate: {path}; elapsed {time.monotonic()-started:.1f}s',flush=True)


if __name__=='__main__': main()
