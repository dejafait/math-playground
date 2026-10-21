"""One capped exact Phase I at L086's frozen columns; no equality reduction.

Reuses the original-data constructor, writing its reconstruction to a new
path. No prior result is overwritten and no old moment is imposed.
"""
import hashlib
import json
import sys
import time
from fractions import Fraction as F
from pathlib import Path

import affine_sign_remaining_modes as original
from verify_simultaneous_eight_shell import enc

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'fixed-sign-column-full-completion-results.json'
RECON = ROOT/'fixed-sign-column-original-reconstruction.json'
INITIAL = ROOT/'fixed-sign-column-full-completion-initial-state.json'
STATE = ROOT/'fixed-sign-column-full-completion-state.json'
PIVOT_CAP, SECONDS = 10000, 300


def dot(a,b):
    assert len(a)==len(b)
    return sum((x*y for x,y in zip(a,b) if x and y),F(0))


def write(path,obj):
    path.write_text(json.dumps(enc(obj),indent=2)+'\n')


def main():
    original.OUT = RECON
    original.main()  # Full keys, ranges, forced/anchor terms and fresh inverses.
    source=json.loads(RECON.read_text())
    audits=['affine-sign-phase-one-critical-audit.json',
            'affine-sign-remaining-modes-critical-audit.json']
    checks,failures=[],[]
    report={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest()
             for p in [RECON,Path(original.__file__),Path(__file__)]+[ROOT/n for n in audits]},
            'limits':{'pivots':PIVOT_CAP,'seconds':SECONDS,'runs':1}}
    def check(name,ok):
        checks.append(name)
        if not ok: failures.append(name)
    def save(stage):
        report.update(stage=stage,checks=checks,failures=failures)
        write(OUT,report)
    check('complete_original_reconstruction',not source['failures'] and len(source['rows'])==81)
    for name in audits:
        obj=json.loads((ROOT/name).read_text())
        check('clean_'+name,not obj['failures'])
        for rel,h in obj['input_hashes'].items():
            check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    A=[[F(*v) for v in r['original_row']] for r in source['rows']]
    b0=[F(*r['bound']) for r in source['rows']]
    n=45
    A += [[F(-int(i==j)) for j in range(n)] for i in range(n)]
    b0 += [F(0)]*n
    m=len(A)
    labels=[{'kind':'mode','index':r['index'],'mode':r['mode']} for r in source['rows']]
    labels += [{'kind':'moment_sign','index':j} for j in range(n)]
    p8=F(16792471,1181138102168120460)
    from verify_simultaneous_eight_shell import C
    free=[(r,q) for r in range(9) for q in range(9) if r+q>=8]
    volumes=[F(C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
    rawA=[[v*V/p8 for v,V in zip(row,volumes)] for row in A]
    signs=[F(1) if v>=0 else F(-1) for v in b0]
    eye=[[F(i==j) for j in range(m)] for i in range(m)]
    standard=[[sg*v for v in row+eye[i]] for i,(row,sg) in enumerate(zip(A,signs))]
    b=[sg*v for sg,v in zip(signs,b0)]
    artificial_start=n+m
    T=[row+eye[i] for i,row in enumerate(standard)]
    basis=list(range(artificial_start,artificial_start+m))
    report.update(point=source['point'],free=free,p8=p8,volumes=volumes,
                  original_matrix=A,original_rhs=b0,row_labels=labels,
                  raw_matrix=rawA,raw_rhs=b0,row_signs=signs,
                  standard_matrix=standard,standard_rhs=b[:],
                  artificial_start=artificial_start,
                  column_order=['45 nonnegative moments','126 slacks','126 artificials'])
    check('full_126_rows',m==126 and all(len(r)==45 for r in A))
    check('positive_raw_scaling',p8>0 and min(volumes)>0)
    save('complete_original_system_before_pivots')
    if failures: raise SystemExit('Pre-pivot reconstruction failure: '+repr(failures))
    trace=[]; started=time.monotonic(); last_print=started
    def state(stage,path=STATE):
        write(path,{'stage':stage,'tableau':T,'rhs':b,'basis':basis,
                    'row_transform':[r[artificial_start:] for r in T],
                    'pivots':trace,'elapsed_seconds':time.monotonic()-started})
    state('initialized_before_any_pivot',INITIAL)
    verdict='UNDECIDED'; stop=''; objective=None; pi=[]
    try:
        while True:
            cb=[F(j>=artificial_start) for j in basis]
            objective=dot(cb,b)
            if objective==0:
                verdict='RATIONAL_FEASIBLE_WITNESS'; stop='zero_artificial_objective'; break
            if time.monotonic()-started>=SECONDS or len(trace)>=PIVOT_CAP:
                stop='time_limit' if time.monotonic()-started>=SECONDS else 'pivot_limit'; break
            nonbasic=set(range(len(T[0])))-set(basis)
            entering=next((j for j in sorted(nonbasic)
                if F(j>=artificial_start)-dot(cb,[r[j] for r in T])<0),None)
            if entering is None:
                pi=[dot(cb,c) for c in zip(*[r[artificial_start:] for r in T])]
                verdict='POSITIVE_PHASE_ONE_OPTIMUM'; stop='all_reduced_costs_nonnegative'; break
            choices=[(b[i]/r[entering],basis[i],i) for i,r in enumerate(T) if r[entering]>0]
            if not choices: stop='exceptional_no_leaving_row'; break
            ratio,leaving,row=min(choices); pivot=T[row][entering]
            pr=[v/pivot for v in T[row]]; pb=b[row]/pivot
            newT=[]; newb=[]
            for i,r in enumerate(T):
                factor=r[entering]
                if i==row: newT.append(pr); newb.append(pb)
                elif factor:
                    newT.append([v-factor*w if w else v for v,w in zip(r,pr)])
                    newb.append(b[i]-factor*pb)
                else: newT.append(r); newb.append(b[i])
                if time.monotonic()-started>=SECONDS:
                    stop='time_limit_during_atomic_pivot'; break
            if stop: break  # Preserve the last complete state.
            T,b=newT,newb; basis[row]=entering
            trace.append({'entering':entering,'leaving':leaving,'row':row,'pivot':pivot,
                          'ratio':ratio,'objective_before':objective})
            if min(b)<0: stop='exceptional_negative_basic_coordinate'; break
            if len(trace)%10==0: state('running_checkpoint')
            if time.monotonic()-last_print>=25:
                print('Fixed-column Phase I:',len(trace),'pivots;',round(time.monotonic()-started,1),
                      'seconds; objective still positive',flush=True)
                last_print=time.monotonic()
    except (KeyboardInterrupt,Exception) as exc:
        stop='interruption_or_exception: '+repr(exc); verdict='UNDECIDED'
    state('terminated_'+stop)
    cb=[F(j>=artificial_start) for j in basis]; objective=dot(cb,b)
    report['phase_one']={'stop':stop,'pivots':len(trace),'objective':objective,
                         'elapsed_seconds':time.monotonic()-started,'trace':trace}
    if verdict=='RATIONAL_FEASIBLE_WITNESS':
        values=[F(0)]*len(T[0])
        for j,v in zip(basis,b): values[j]=v
        z=values[:n]; raw=[p8*v/V for v,V in zip(z,volumes)]
        slack=[v-dot(row,z) for row,v in zip(A,b0)]
        rawslack=[v-dot(row,raw) for row,v in zip(rawA,b0)]
        rawremainders=[F(*r['positive_raw_normalization'])*v for r,v in zip(source['rows'],slack)]
        check('complete_standard_point',min(values)>=0 and not any(values[artificial_start:])
              and [dot(r,values[:artificial_start]) for r in standard]==report['standard_rhs'])
        check('all_126_original_inequalities',min(slack)>=0)
        check('all_raw_inequalities',slack==rawslack and min(raw)>=0 and min(rawremainders)>=0)
        report['witness']={'standard_values':values,'z':z,'raw_moments':raw,
                           'slacks':slack,'raw_scaled_slacks':rawslack,'raw_Schur_remainders':rawremainders}
    elif verdict=='POSITIVE_PHASE_ONE_OPTIMUM':
        lam=[-v*sg for v,sg in zip(pi,signs)]
        coefficient=[dot(lam,c) for c in zip(*A)]
        check('nonnegative_original_weights',min(lam)>=0)
        check('nonnegative_z_reduced_costs',min(coefficient)>=0)
        for j,v in enumerate(coefficient): lam[81+j]+=v
        cancel=[dot(lam,c) for c in zip(*A)]; pairing=dot(lam,b0)
        rawcancel=[dot(lam,c) for c in zip(*rawA)]
        check('positive_phase_one_optimum',objective>0)
        check('complete_original_Farkas',min(lam)>=0 and not any(cancel) and pairing==-objective<0)
        check('complete_raw_Farkas',not any(rawcancel) and dot(lam,report['raw_rhs'])==pairing)
        check('all_reduced_costs_nonnegative',all(F(j>=artificial_start)-dot(cb,[r[j] for r in T])>=0 for j in range(len(T[0]))))
        report['separator']={'phase_one_dual':pi,'nonnegative_z_residual':coefficient,
                             'original_weights':lam,'original_cancellation':cancel,
                             'raw_cancellation':rawcancel,'pairing':pairing}
        verdict='RATIONAL_ORIGINAL_FARKAS_CERTIFICATE'
    report['summary']={'verdict':verdict if not failures else 'FAILED_CERTIFICATE_UNDECIDED',
                        'stop':stop,'pivots':len(trace),'checks':len(checks),'failures':len(failures),
                        'objective_sign':(objective>0)-(objective<0),
                        'required_objective':0,'pivot_cap':PIVOT_CAP,'seconds_cap':SECONDS,
                        'rs_boundary':[955,957]}
    save('completed')
    print('Summary:',report['summary'],flush=True)
    print('Failures:',failures,'; certificate:',OUT.relative_to(NB),'; state:',STATE.relative_to(NB),flush=True)
    if failures: raise SystemExit(1)


if __name__=='__main__': main()
