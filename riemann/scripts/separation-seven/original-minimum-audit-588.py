#!/usr/bin/env python3
"""Audit C999o's unchanged finite minimum. No old writes, solve or tuning.

Reconstruct all entry centers, re-enclose exact neutral coordinates at 80
digits, check full saved factors, and evaluate all trial products and all
center-gradient coordinates by integer arithmetic. Analytic accuracy still
uses C744v/w and C999n Section4's explicitly retained contracts.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import math
from decimal import Context, Decimal, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
OUT = BASE / 'original-minimum-audit-588.json'
checks, evidence, bounds = [], {}, {}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        raise AssertionError(label)


def dyadics(values):
    pairs = [float(x).as_integer_ratio() for x in values]
    den = max(d for _, d in pairs)
    return [n * (den // d) for n, d in pairs], den


def exact_matvec(matrix, vector):
    vn, vd = dyadics(vector)
    out = []
    for row in matrix:
        mn, md = dyadics(row)
        out.append(Q(sum(x*y for x, y in zip(mn, vn)), md*vd))
    return out


def exact_sqnorm(array):
    array = np.asarray(array)
    rows = array if array.ndim == 2 else array.reshape(1, -1)
    total = Q(0)
    for row in rows:
        ns, den = dyadics(row)
        total += Q(sum(n*n for n in ns), den*den)
    return total


def rational_record(q):
    return dict(numerator=str(q.numerator), denominator=str(q.denominator))


def main():
    old = json.loads((BASE/'original-galerkin-586.json').read_text())
    pin_names = list(old['input_hashes']) + [
        'original-galerkin-586.py', 'original-galerkin-586.json',
        'original-galerkin-586.npz', 'original-galerkin-first-pass-586.py',
        'original-galerkin-first-pass-586.json']
    pins = {p: sha(BASE/p) for p in pin_names}
    check(old['archive']['sha256'] == pins['original-galerkin-586.npz'], 'original full archive hash')
    check(old['script_sha256'] == pins['original-galerkin-586.py'], 'original generator hash')
    for name, digest in old['input_hashes'].items():
        check(pins[name] == digest, 'original input hash '+name)
    check(not old['failures'] and len(old['checks']) == 24 and
          all(x['passed'] for x in old['checks']), 'all original checks and failures inspected')
    with np.load(BASE/'original-galerkin-586.npz') as archive:
        data = {key: archive[key].copy() for key in archive.files}
    with np.load(BASE/'endpoint-complement-locator-581.npz') as archive:
        frozen = {key: archive[key].copy() for key in archive.files}
    manifest = json.loads((BASE/'endpoint-complement-locator-581.json').read_text())
    check(manifest['archive']['sha256'] == pins['endpoint-complement-locator-581.npz'], 'frozen endpoint manifest hash')
    check(np.array_equal(data['free_numerators'], frozen['free_numerators']), 'all unchanged endpoint numerators')
    check(data['free_numerators'].dtype.kind == 'i' and
          np.max(np.abs(data['free_numerators'])) < 2**53, 'exact endpoint integer conversion range')

    spec = importlib.util.spec_from_file_location('interval588', BASE/'complete-schur-531.py')
    a = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(a)
    a.DOWN = Context(prec=80, rounding=ROUND_FLOOR)
    a.UP = Context(prec=80, rounding=ROUND_CEILING)
    a.NEAR = Context(prec=80, rounding=ROUND_HALF_EVEN)
    I = a.I

    def qi(q):
        return I(q.numerator)/q.denominator

    def exact(x):
        return I(Decimal(float(x)))

    def ab(x):
        return max(x.lo.copy_abs(), x.hi.copy_abs())

    def sq(x):
        return I(0, a.UP.multiply(ab(x), ab(x))) if x.lo <= 0 <= x.hi else x*x

    def inflate(x, error):
        return x+I(ab(error).copy_negate(), ab(error))

    def l1(xs):
        return sum((I(ab(x)) for x in xs), I(0))

    def gamma(n):
        t = I(n)/2**53
        return t/(1-t)

    def power(x, n):
        result = I(1)
        for _ in range(n):
            result *= x
        return result

    def atan(q):
        x = I(1)/q
        result = sum((((-1)**j)*power(x, 2*j+1)/(2*j+1) for j in range(80)), I(0))
        return inflate(result, power(x,161)/161)

    pi, ell = 16*atan(5)-4*atan(239), I(3).ln()/2
    k = [n*pi/ell for n in range(1024)]
    ratios = [(I(2).sqrt() if n % 2 == 0 else I(1))
              *(I('.25')+sq(k[n % 2]))/(I('.25')+sq(k[n])) for n in range(2,1024)]
    Z = data['neutral_coordinate_center']
    expected_Z = np.zeros((1024,1022)); expected_Z[2:] = np.eye(1022)
    rh = -Z[np.arange(2,1024) % 2, np.arange(1022)]
    expected_Z[np.arange(2,1024) % 2, np.arange(1022)] = -rh
    check(np.array_equal(Z,expected_Z), 'entire neutral-coordinate sparsity and identity')
    for n, (r, prev) in enumerate(zip(ratios, old['details']['exact_neutral_ratio_intervals']), 2):
        check(Decimal(prev['lo']) <= r.lo <= r.hi <= Decimal(prev['hi']), '80-digit ratio inside original interval '+str(n))
    dz = sum((sq(I(ab(r-exact(c)))) for r,c in zip(ratios,rh)), I(0)).sqrt()
    z = (1+sum((sq(r) for r in ratios),I(0))).sqrt()

    v = data['middle_free_dyadic']
    check(v.shape == (1022,) and np.isfinite(v).all() and np.isrealobj(v), 'all fixed middle trial dyadics')
    vf, vh = np.zeros(1022),np.zeros(1022)
    vf[510:] = data['free_numerators'][:512]/2**40
    vh[510:] = data['free_numerators'][512:]/2**40
    profiles, deltas, ls = {}, {}, {}
    centers = {'f':data['endpoint_f_center'],'h':data['endpoint_h_center'],'g':data['middle_raw_center']}
    interval_keys = {'f':'exact_neutral_f_intervals','h':'exact_neutral_h_intervals','g':'exact_neutral_middle_intervals'}
    for name, free in [('f',vf),('h',vh),('g',v)]:
        raw = [I(0),I(0)]+[exact(t) for t in free]
        for j,n in enumerate(range(2,1024)):
            raw[n % 2] -= ratios[j]*exact(free[j])
        check(centers[name].shape == (1024,) and np.array_equal(centers[name][2:], free), 'all free physical coordinates '+name)
        saved = old['details'][interval_keys[name]]
        check(len(saved) == 1024 and all(Decimal(t['lo']) <= r.lo <= r.hi <= Decimal(t['hi']) for r,t in zip(raw,saved)), 'all80-digit neutral physical intervals '+name)
        profiles[name] = raw
        deltas[name] = sum((I(ab(r-exact(c))) for r,c in zip(raw,centers[name])),I(0))
        ls[name] = l1(raw)
    evidence['neutral_ratios'] = [r.json() for r in ratios]
    evidence['exact_neutral_profiles'] = {key:[r.json() for r in raw] for key,raw in profiles.items()}

    # Complete entry replay; stop before selection, any solve, or any write.
    source = (BASE/'endpoint-complement-locator-581.py').read_text()
    marker = '# Exact object Z'
    check(source.count(marker) == 1, 'unique non-writing generator boundary')
    prefix = source.split(marker)[0]
    oldidx = 'idx = np.r_[0, 1, np.arange(N, J)]'
    check(prefix.count(oldidx) == 1, 'unique full-rectangle expansion')
    prefix = prefix.replace(oldidx,'idx = np.arange(J)')
    env = dict(__file__=str(BASE/'endpoint-complement-locator-581.py'),__name__='audit588_entries')
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        exec(compile(prefix,'entry_replay588','exec'),env)
    evidence['entry_replay_stdout'] = capture.getvalue()
    M,T,Ts,U = [data[key] for key in ['local_matrix','t_entries','ts_entries','u_entries']]
    for key,mat,generated in [('M',M,env['L']),('T',T,env['T']),('Ts',Ts,env['Ts']),('U',U,env['U'])]:
        check(mat.shape == (1024,1024) and np.isfinite(mat).all() and np.abs(mat).max()<400, 'all complete matrix entries and magnitudes '+key)
        check(np.array_equal(mat,generated), 'every replayed entry '+key)
    check(np.array_equal(T,Ts.T) and np.array_equal(U,env['Us'].T), 'both complete adjoints')
    check(np.array_equal(env['shift'](0.),np.eye(1024)), 'full exact zero-delay identity')
    prime_list=[]
    for p in range(2,3784):
        if any(p%d==0 for d in range(2,math.isqrt(p)+1)):
            continue
        n=p
        while n*n < 3**15:
            if n*n > 3**13:
                prime_list.append((n,p))
            n*=p
    prime_list.sort()
    check(prime_list==env['powers'] and len(prime_list)==334, 'independent334-power enumeration')
    check([(n,p) for n,p in prime_list if n*n==3**14]==[(2187,3)], 'unique remote zero delay')
    remote=[]
    for (n,p),dc,wc in zip(prime_list,env['delays'],env['weights']):
        di=I(0) if n==2187 else 14*ell-I(n).ln()
        wi=I(p).ln()/I(n).sqrt()
        check(ab(di-exact(dc))<Decimal('1e-16') and ab(wi-exact(wc))<Decimal('1e-16') and ab(di)<ell.lo and (n==2187 or di.lo*di.hi>0), 'remote weight/delay/overlap '+str(n))
        remote.append(dict(n=n,prime=p,delay=di.json(),weight=wi.json()))
    check(len(env['con']['weights'])==16, 'all16 nearest translations')
    evidence['remote_constants']=remote

    # Changed-range ledger on the entire square; no old operator norm used.
    gap=pi/ell
    cancellation=Q(1023**2+1022**2,1023**2-1022**2)
    check(cancellation<1024, 'maximal unequal-index cancellation ratio')
    rmax=I(2).sqrt()/(6*I('64.25')*I('64.25'))
    cj=I('131072.5')
    diagerr=1/(cj*cj)+2*sq(k[-1])*(1/(6*cj*cj*cj)+1/(cj*cj*cj*cj))
    offerr=4*rmax/gap
    response_tail=I(8)/(3**64)/(1-I(1)/3)/(I('128.5')*I('128.5'))
    continuous_tail=I(1)/(3**49*I(3).sqrt()*I('16.5')*(1-I(1)/729))
    local_cap=rmax+8*diagerr+offerr+I('1e-7')+response_tail
    check(local_cap.hi<Decimal('.000097173') and local_cap.hi<Decimal('.0001'), 'complete local cap<.0001')
    check(continuous_tail.hi<Decimal('1.465e-25'), 'full continuous tail')
    dotcap=400*(2*gamma(1024)+sq(gamma(1024)))
    check(dotcap.hi<Decimal('1e-8'), 'complete two-dot allowance')
    evidence['analytic_ledger']={key:val.json() for key,val in dict(local_cap=local_cap,rmax=rmax,diagonal_error=diagerr,off_diagonal_error=offerr,response_tail=response_tail,continuous_tail=continuous_tail,two_dot_cap=dotcap).items()}

    # Exact rational Frobenius norms also check every inflated norm allowance.
    A,F=data['neutral_matrix'],data['lower_factor']
    check(A.shape==(1022,1022) and np.array_equal(A,A.T), 'entire Hermitian center')
    check(F.shape==(1022,1022) and np.isfinite(F).all(), 'entire proposed factor')
    Araw=Z.T@M@Z
    check(np.array_equal(A,(Araw+Araw.T)/2), 'complete neutral center assembly')
    f,h,g=[centers[key] for key in ['f','h','g']]
    wc=M@g-T@f-Ts@h
    cc=Z.T@wc
    check(np.array_equal(cc,data['center_gradient']), 'all center-gradient coordinates replay')
    reconstruction=A-.5*np.eye(1022)-F@F.T
    norms={}
    evidence['exact_squared_norms']={}
    evidence['minimum_nonzero_entries']={}
    for name,array in dict(M=M,T=T,Ts=Ts,U=U,Z=Z,A=A,F=F,f=f,h=h,g=g,wc=wc,cc=cc,reconstruction=reconstruction).items():
        q=exact_sqnorm(array)
        norms[name]=qi(q).sqrt() if q else I(0)
        old_norm=exact(float(np.linalg.norm(array)))*I('1.00000001')+I('1e-30')
        check(norms[name].hi <= old_norm.lo, 'inflated norm covers exact dyadic norm '+name)
        nz=np.abs(array[np.nonzero(array)])
        check(not len(nz) or float(nz.min())>1e-130, 'normal stored nonzero range '+name)
        evidence['minimum_nonzero_entries'][name]=float(nz.min()) if len(nz) else None
        evidence['exact_squared_norms'][name]=rational_record(q)
    check(gamma(1024*1024).hi<Decimal('1e-8'), 'largest norm-sum gamma below inflation')
    underflow=I('1e-290') # dominates the inherited <=1e-300 absolute charges
    factor_error=norms['reconstruction']+gamma(2048)*sq(norms['F'])+gamma(8)*(norms['A']+I('.5')*I(1022).sqrt()+sq(norms['F'])+1)+underflow
    assembly=gamma(4096)*sq(norms['Z'])*norms['M']+I('1e-7')
    analytic_A=sq(z)*1024*I('.0001')
    coordinate_A=dz*(2*z+dz)*norms['M']
    alpha=I('.5')-factor_error-assembly-analytic_A-coordinate_A
    check(factor_error.hi<Decimal('1.249e-9'), 'entire factor reconstruction bound')
    check(alpha.lo>Decimal('.3960752074'), 'exact finite coercivity>.3960752074')

    # Exact integer matvecs, hence every trial product and gradient coordinate.
    actions={name:exact_matvec(mat,vec) for name,mat,vec in
             [('Mf',M,f),('Mh',M,h),('Mg',M,g),('Uf',U,f),('Tf',T,f),('Tsh',Ts,h)]}
    products={}
    for name,x,action in [('fMf',f,'Mf'),('hMh',h,'Mh'),('gMg',g,'Mg'),('hUf',h,'Uf'),('gTf',g,'Tf'),('gTsh',g,'Tsh')]:
        products[name]=sum((Q(float(t))*q for t,q in zip(x,actions[action])),Q(0))
    mats={'fMf':(f,M,f),'hMh':(h,M,h),'gMg':(g,M,g),'hUf':(h,U,f),'gTf':(g,T,f),'gTsh':(g,Ts,h)}
    for name,(x,mat,y) in mats.items():
        radius=I('1e-8')*l1([exact(t) for t in x])*l1([exact(t) for t in y])
        iv=inflate(exact(float(x@mat@y)),radius)
        check(Q(iv.lo)<=products[name]<=Q(iv.hi), 'original scalar enclosure contains exact product '+name)
    E=products['fMf']+products['hMh']+products['gMg']-2*(products['hUf']+products['gTf']+products['gTsh'])
    lf,lh,lg=[ls[key] for key in ['f','h','g']]
    df,dh,dg=[deltas[key] for key in ['f','h','g']]
    entry_energy=I('.0001')*(sq(lf)+sq(lh)+sq(lg))+2*I('.000001')*(lf*lh+lg*lf+lg*lh)
    coordinate_energy=I(401)*(df*(2*lf+df)+dh*(2*lh+dh)+dg*(2*lg+dg)+2*(df*lh+dh*lf+df*dh+dg*lf+df*lg+df*dg+dg*lh+dh*lg+dh*dg))
    trial=inflate(qi(E),entry_energy+coordinate_energy+underflow)
    exact_w=[m-t-s for m,t,s in zip(actions['Mg'],actions['Tf'],actions['Tsh'])]
    exact_c=[exact_w[n]-Q(float(rh[n-2]))*exact_w[n % 2] for n in range(2,1024)]
    cw_norm=qi(sum((q*q for q in exact_w),Q(0))).sqrt()
    center_norm=qi(sum((q*q for q in exact_c),Q(0))).sqrt()
    w_round=qi(sum(((q-Q(float(t)))**2 for q,t in zip(exact_w,wc)),Q(0))).sqrt()
    arith_w=gamma(4096)*(norms['M']*norms['g']+norms['T']*norms['f']+norms['Ts']*norms['h']+1)
    check(w_round.hi<arith_w.lo, 'full exact physical residual verifies arithmetic allowance')
    exact_cc=[Q(float(wc[n]))-Q(float(rh[n-2]))*Q(float(wc[n % 2])) for n in range(2,1024)]
    c_round=qi(sum(((q-Q(float(t)))**2 for q,t in zip(exact_cc,cc)),Q(0))).sqrt()
    arith_c=gamma(2048)*norms['Z']*norms['wc']
    check(c_round.hi<arith_c.lo, 'full exact outer residual verifies arithmetic allowance')
    physical_entry=32*(I('.0001')*lg+I('.000001')*(lf+lh))
    physical_coord=norms['M']*dg+32*400*(df+dh)
    # Exact dyadic center gradient: no floating matvec error in this new bound.
    gradient=center_norm+z*(physical_entry+physical_coord)+dz*cw_norm+underflow
    debt=sq(gradient)/alpha
    minimum=I(a.DOWN.subtract(trial.lo,debt.hi),trial.hi)
    check(gradient.hi<Decimal('.001740921499'), 'exact full gradient below original bound')
    check(debt.hi<Decimal('.000007652102'), 'complete gradient debt below original bound')
    check(minimum.lo>Decimal('.42327662') and minimum.hi<Decimal('.42418215'), 'unchanged strict original finite interval upheld')
    check(minimum.lo>=Decimal(old['bounds']['finite_minimum']['lo']) and minimum.hi<=Decimal(old['bounds']['finite_minimum']['hi']), 'independent interval contained in original full interval')
    evidence['exact_scalar_products']={key:rational_record(q) for key,q in products.items()}
    evidence['exact_center_energy']=rational_record(E)
    evidence['exact_physical_residual']=[rational_record(q) for q in exact_w]
    evidence['exact_coordinate_residual']=[rational_record(q) for q in exact_c]
    for key,val in dict(coercivity=alpha,factor_error=factor_error,matrix_arithmetic_error=assembly,analytic_matrix_error=analytic_A,coordinate_matrix_error=coordinate_A,neutral_coordinate_error=dz,neutral_coordinate_norm=z,trial_energy=trial,trial_entry_error=entry_energy,trial_coordinate_error=coordinate_energy,exact_center_gradient_norm=center_norm,physical_entry_error=physical_entry,physical_coordinate_error=physical_coord,physical_arithmetic_actual=w_round,physical_arithmetic_allowance=arith_w,outer_arithmetic_actual=c_round,outer_arithmetic_allowance=arith_c,gradient_bound=gradient,gradient_debt=debt,finite_minimum=minimum).items():
        bounds[key]=val.json()
    evidence['coefficient_bounds']={key:{'l1':ls[key].json(),'l1_error':deltas[key].json()} for key in ['f','h','g']}
    for name,digest in pins.items():
        check(sha(BASE/name)==digest, 'prior artifact preserved '+name)
    evidence['input_hashes']=pins


try:
    main()
except Exception as error:
    evidence['exception']=repr(error)
    if not any(not c['passed'] for c in checks):
        checks.append(dict(label='audit execution',passed=False))
finally:
    failures=[c['label'] for c in checks if not c['passed']]
    report=dict(target="Critically audit C999o's frozen original three-cell finite minimum enclosure, including exact neutrality, complete entry bounds, finite coercivity and the complex Galerkin residual direction.",passed=not failures,checks=checks,failures=failures,bounds=bounds,evidence=evidence,required='unchanged finite interval (.42327662,.42418215), complete entry/coordinate/coercivity/residual evidence',qualifications='C744v/w analytic and IEEE754/Decimal contracts; C744z whole-core and unreplayed c_* retained; finite positivity is not an infinite-middle lower bound',script_sha256=sha(Path(__file__)))
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print('C999o audit: '+str(sum(c['passed'] for c in checks))+'/'+str(len(checks))+' checks; failures='+str(failures))
    print('Actual/required: '+json.dumps({key:bounds.get(key) for key in ['finite_minimum','coercivity','gradient_debt']})+'; required finite interval (.42327662,.42418215)')
    print('Full certificate: '+str(OUT.relative_to(BASE.parent.parent)))
    if failures:
        raise SystemExit(1)
