#!/usr/bin/env python3
"""One fixed three-cell test: rigorous scalar bounds; finite diagnostic only.

The full neutral middle inverse and the actual remote block are specified
in C744z. No finite eigenvalue here certifies their infinite-space sign.
Original archives are read only. Full matrices/evidence are saved locally.
"""
import hashlib
import importlib.util
import json
import math
from decimal import Decimal
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
N = 512


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, BASE/filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def remote_scalar():
    mod = load_module('interval543', 'complete-schur-531.py')
    I = mod.I
    ell = I(3).ln()/2
    powers = []
    # Exact integer comparisons implement 3^(13/2)<n<3^(15/2).
    for n in range(2, 4000):
        if not 3**13 < n*n < 3**15:
            continue
        remaining, factors = n, []
        for p in range(2, math.isqrt(n)+1):
            if remaining % p == 0:
                factors.append(p)
                while remaining % p == 0:
                    remaining //= p
        if remaining > 1:
            factors.append(remaining)
        if len(factors) == 1:
            powers.append((n, factors[0]))
    assert 4000**2 > 3**15
    data = [(n,p,I(p).ln()/I(n).sqrt(),I(0) if n==3**7 else 14*ell-I(n).ln())
            for n,p in powers]
    events = [(I(0),'left'),(ell,'right')]
    for n,p,w,delta in data:
        assert -ell.lo < delta.lo <= delta.hi < ell.lo
        if n==3**7:
            continue  # Exact zero delay; both event points are cell endpoints.
        for point,label in [(-delta,f'enter:{n}'),(ell-delta,f'exit:{n}')]:
            if point.lo > 0 and point.hi < ell.lo:
                events.append((point,label))
            else:
                assert point.hi < 0 or point.lo > ell.hi
    events.sort(key=lambda item:item[0].lo)
    rows = []
    for (left,ll),(right,rl) in zip(events,events[1:]):
        assert left.hi < right.lo
        midpoint = mod.NEAR.divide(mod.NEAR.add(left.hi,right.lo),Decimal(2))
        sample,active,total = I(midpoint),[],I(0)
        for n,p,w,delta in data:
            point = sample+delta
            if point.lo > 0 and point.hi < ell.lo:
                active.append(n)
                total += w
            else:
                assert point.hi < 0 or point.lo > ell.hi
        rows.append(dict(left=ll,right=rl,sample=sample.json(),active=active,
                         weight_sum=total.json()))
    row = I(max(Decimal(r['weight_sum']['lo']) for r in rows),
            max(Decimal(r['weight_sum']['hi']) for r in rows))
    # sum_{j>=1} exp(-13ell c_j)/c_j
    # <= 3^(-65/4) / [(5/2)(1-3^-13)].
    kappa = 1/(I(3**16)*I(3).sqrt().sqrt()*I('2.5')*(1-I(1)/3**13))
    # The following is a sufficient floor ONLY; its failure is not
    # a negative Rayleigh value of the actual complementary form.
    h512 = (I(N)/(2*ell)).ln()-2*ell*ell/(9*N*N)
    row_upper = row+kappa
    comparison_floor = h512-I('4.71')-row_upper
    scalar = dict(scope='exact full remote row bound and coarse comparison only',
        ell=ell.json(), powers=[dict(n=n,prime=p,weight=w.json(),delta=d.json())
                               for n,p,w,d in data],
        events=[dict(label=s,interval=x.json()) for x,s in events],
        rows=rows, summary=dict(prime_power_count=len(powers),event_count=len(events),
            row_count=len(rows),prime_row_max=row.json(),continuous_norm_upper=kappa.json(),
            complete_remote_norm_upper=row_upper.json(),diagonal_floor=h512.json(),
            coarse_three_cell_floor=comparison_floor.json(),required_floor='>0',
            scalar_endpoint_rayleigh=(h512-row_upper).json(),
            all_event_order_and_active_set_checks_passed=True),
        failures=[],development_events=[
            'First run stopped at endpoint-event assertion: n=2187 has exactly zero delay.',
            'Zero delay now represented exactly and included as its full scalar identity term.'])
    assert comparison_floor.hi < 0
    return scalar,powers


def finite_diagnostic(powers):
    mod = load_module('entries543','residual-certificate-532.py')
    con = mod.constants()
    ell,pi = con['ell'],con['pi']
    archive_path=BASE/'complete-covariance-532.npz'
    audit=json.loads((BASE/'matrix-tail-audit-541.json').read_text())
    expected=next(r['expected'] for r in audit['input_hashes']
                  if r['path']=='complete-covariance-532.npz')
    actual=digest(archive_path)
    assert actual==expected
    with np.load(archive_path) as old:
        a=old['m0'].copy()
        t=old['mc']+old['mg']
    n=np.arange(N)
    k=n*pi/ell
    norm=np.full(N,np.sqrt(2/ell));norm[0]=1/np.sqrt(ell)
    parity=np.where(n%2==0,1.,-1.)
    moments=np.array([norm*c*(parity*(con['fourth'] if c>0 else 1/con['fourth'])-1)
                      /(c*c+k*k) for c in [.5,-.5]])
    kn,km=k[:,None],k[None,:]
    den=kn*kn-km*km
    den[np.arange(N),np.arange(N)]=1
    signs=np.outer(parity,parity)
    weights,deltas=[],[]
    # This computation is a diagnostic, including these floating logs.
    for power,p in powers:
        weights.append(math.log(p)/math.sqrt(power))
        deltas.append(0. if power==3**7 else 14*ell-math.log(power))
    remote=np.zeros((N,N))
    for (power,p),weight,delta in zip(powers,weights,deltas):
        if power==3**7:
            remote += weight*np.eye(N)
            continue
        sn,cs=mod.sincos(k*delta,pi)
        if delta>0:
            out=(-signs*kn*sn[:,None]+km*sn[None,:])/den
        else:
            out=(kn*sn[:,None]-signs*km*sn[None,:])/den
        diag=np.empty(N);diag[0]=ell-abs(delta)
        diag[1:]=(ell-abs(delta))*cs[1:]/2-np.sign(delta)*sn[1:]/(2*k[1:])
        out[np.arange(N),np.arange(N)]=diag
        remote += weight*out*np.outer(norm,norm)
    for j in range(1,8):
        c=2*j+.5
        decay=math.exp(-ell*c)
        minus=norm*c*(1-parity*decay)/(c*c+k*k)
        plus=norm*c*(parity-decay)/(c*c+k*k)
        remote += math.exp(-13*ell*c)*np.outer(minus,plus)
    basis=np.linalg.qr(moments.T,mode='complete')[0][:,2:]
    aa=basis.T@a@basis;tt=basis.T@t@basis;uu=basis.T@remote@basis
    # This is inversion of a finite neutral compression, NOT the compression
    # of the full neutral inverse. Their equality is never assumed.
    eig,vec=np.linalg.eigh(aa)
    assert eig[0]>0
    invroot=(vec/np.sqrt(eig))@vec.T
    rr=invroot@tt@invroot;vv=invroot@uu@invroot
    eye=np.eye(N-2)
    dleft=eye-rr.T@rr;dright=eye-rr@rr.T
    combined=vv+rr@rr
    residual=np.block([[dleft,-combined.T],[-combined,dright]])
    vals,vectors=np.linalg.eigh(residual)
    # Compare actual remote with the induced coupling; no term is deleted.
    direction=vectors[:,0]
    f,h=direction[:N-2],direction[N-2:]
    mf=invroot@f;mh=invroot@h
    middle=np.linalg.solve(aa,tt@mf+tt.T@mh)
    components=dict(endpoint_diagonal_energy=float(f@f+h@h),
        middle_elimination_debt=float(middle@aa@middle),
        actual_remote_cross=float(-2*mh@uu@mf),
        residual_value=float(direction@residual@direction))
    diagnostic=dict(certified=False,parameters=dict(modes=N,neutral_dimension=N-2,
        separation=7,remote_separation=14,continuous_terms=7),
        input_hash=dict(path=archive_path.name,actual=actual,expected=expected),
        single_cell_min_eigenvalue=float(eig[0]),relative_seven_norm=float(np.linalg.norm(rr,2)),
        relative_fourteen_norm=float(np.linalg.norm(vv,2)),
        left_diagonal_min=float(np.linalg.eigvalsh(dleft)[0]),
        right_diagonal_min=float(np.linalg.eigvalsh(dright)[0]),
        full_endpoint_residual_min=float(vals[0]),required_residual_min=0,
        least_direction_components=components,
        maximum_neutrality_residual=float(np.max(np.abs(moments@basis))),
        failures=[],limitations=['finite neutral inverse is not full neutral inverse',
            'moment projection, new remote entries, eigensolve and arithmetic unverified',
            'entire omitted middle and endpoint covariance unpaid',
            'no exactly neutral compact smooth witness or full-space positivity'],
        full_sign_certified=False)
    matrix_path=BASE/'shared-middle-diagnostic-matrices-543.npz'
    np.savez_compressed(matrix_path,moments=moments,basis=basis,cell=aa,seven=tt,
        fourteen=uu,relative_seven=rr,relative_fourteen=vv,
        left=dleft,right=dright,combined=combined,residual=residual,
        direction=direction,finite_middle=middle,eigenvalues=vals)
    diagnostic['matrices']=dict(path=matrix_path.name,sha256=digest(matrix_path))
    return diagnostic


def main():
    scalar,powers=remote_scalar()
    scalar_path=BASE/'shared-middle-scalar-certificate-543.json'
    scalar_path.write_text(json.dumps(scalar,indent=2)+'\n')
    s=scalar['summary']
    print(f"Scalar checks: {s['prime_power_count']} powers; {s['row_count']} row intervals; failures={scalar['failures']}",flush=True)
    print(f"Remote norm upper={s['complete_remote_norm_upper']['hi']}; coarse floor={s['coarse_three_cell_floor']['lo']} (required >0)",flush=True)
    print(f'Evidence: {scalar_path.relative_to(BASE.parent.parent)}',flush=True)
    diagnostic=finite_diagnostic(powers)
    path=BASE/'shared-middle-diagnostic-543.json'
    path.write_text(json.dumps(diagnostic,indent=2)+'\n')
    print(f"Uncertified finite residual min={diagnostic['full_endpoint_residual_min']}; required >=0; full sign certified=False",flush=True)
    print(f'Evidence: {path.relative_to(BASE.parent.parent)}; matrices={diagnostic["matrices"]["path"]}',flush=True)


if __name__=='__main__':
    main()
