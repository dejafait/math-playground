"""Exact Fraction replay of complete quadrature sums, log and trial arithmetic.

Base jet/exponential inclusion remains conditional on L036/L037. This
checks saved finite arithmetic, not an independent Decimal implementation.
"""
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from math import factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
spec = importlib.util.spec_from_file_location('l917_replay', HERE.parent/'heat/low-time-h2-uniform-195-check.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
R = old.R
SOURCE = HERE/'actual-singleton-certificate-1307.json'
OUT = HERE/'actual-singleton-replay-1307.json'


def data(v):
    return {'lower':str(v.lo), 'upper':str(v.hi)}


def trials(s, xs, saved):
    A,B,C,D,E = (s[n] for n in range(2,7))
    k = A/(2*C)
    rows=[]
    for q,row in zip(xs,saved):
        x, one = R(q), R(1)
        assert x.contained_by(row['x']) and k.contained_by(row['k'])
        L = -E*k*(one+x)+E*x*B/D+(one-x)*B**2/(2*A)
        N = A*(x**2+x+one)/3-E*k**2*(one+x)**2
        assert L.contained_by(row['L']) and N.contained_by(row['N'])
        rational = {'x':str(q), 'L':data(L), 'N':data(N)}
        # Replay the producer's branch using the complete saved L box,
        # never converting zero inclusion into an exact equality claim.
        outer_L = R.read(row['L'])
        if outer_L.lo <= 0 <= outer_L.hi:
            assert row['status']=='undecided_L_contains_zero'
            rational['status']=row['status']
        else:
            assert not L.lo <= 0 <= L.hi
            param = N/L
            V = param-k*(one+x)
            J = V-x*B/D
            H = param*J-x*V*C/E+(one-x)*param*B**2/(2*A*E)
            tau = (one-x)/A
            assert tau.contained_by(row['tau']) and tau.lo>0 and q<1
            vals = {'p':param, 'V':V, 'J':J, 'H':H}
            assert all(v.contained_by(row['values'][name]) for name,v in vals.items())
            boxes = {name:R.read(v) for name,v in row['values'].items()}
            failed=[name for name,v in boxes.items() if v.hi<=0]
            undecided=[name for name,v in boxes.items() if v.lo<=0<v.hi]
            assert failed==row['failed_strict_inequalities']
            assert undecided==row['undecided_inequalities']
            status='rejected' if failed else 'undecided' if undecided else 'certified'
            assert row['status']==status
            rational.update(values={name:data(v) for name,v in vals.items()},tau=data(tau),status=status)
        rows.append(rational)
    return rows


def main():
    source=json.loads(SOURCE.read_text())
    assert source['status']=='completed'
    assert (source['precision'],source['spatial_panels'],source['theta_terms'],
            source['spatial_cutoff'],source['taylor_remainder_order'])==(100,256,4,2,8)
    assert source['lambda']=={'lower':'0','upper':'0'}
    report={'status':'running','failures':[],
            'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'formal_algebra':old.formal_check(),'tails':old.tail_check(source)}
    for relative,digest in source['input_sha256'].items():
        assert hashlib.sha256((ROOT/relative).read_bytes()).hexdigest()==digest
    h=F(1,256)
    weights={j:R(2*h**(j+1)/F(j+1)) for j in (0,2,4,6)}
    rw=R(2*h**9/9)
    assert all(v.contained_by(source['weights'][str(j)]) for j,v in weights.items())
    assert rw.contained_by(source['remainder_weight'])
    totals={k:R(0) for k in range(0,13,2)}
    errors={k:R(0) for k in totals}
    assert len(source['panels'])==256
    for index,panel in enumerate(source['panels']):
        assert panel['index']==index
        center,domain=R.read(panel['center']),R.read(panel['domain'])
        assert center.lo==center.hi==F(2*index+1,256)
        assert domain.lo==F(2*index,256) and domain.hi==F(2*index+2,256)
        assert set(panel['orders'])=={str(k) for k in totals}
        for k in totals:
            saved=panel['orders'][str(k)]
            poly=sum((R.read(saved['midpoint_even_coefficients'][str(j)])*weights[j]
                      for j in weights),R(0))
            assert poly.contained_by(saved['polynomial_integral'])
            eighth=R.read(saved['full_eighth_coefficient'])
            err=R(max(abs(eighth.lo),abs(eighth.hi)))*rw
            assert err.contained_by(saved['remainder_bound'])
            pbox=R.read(saved['polynomial_integral'])
            ebox=R.read(saved['remainder_bound'])
            assert ebox.lo>=0
            totals[k]=totals[k]+pbox+R(-ebox.hi,ebox.hi)
            errors[k]=errors[k]+ebox
    assert all(v.contained_by(source['finite_moments'][str(k)]) for k,v in totals.items())
    assert all(v.contained_by(source['quadrature_error_bounds'][str(k)]) for k,v in errors.items())
    tail=R(0,F(source['tails']['total']['upper']))
    assert all((v+tail).contained_by(source['moments'][str(k)]) for k,v in totals.items())
    moments={int(k):R.read(v) for k,v in source['moments'].items()}
    assert all(v.lo>0 for v in moments.values())
    e=[moments[2*n]/(factorial(2*n)*moments[0]) for n in range(1,7)]
    assert all(v.contained_by(source['normalized_coefficients'][str(n)]) for n,v in enumerate(e,1))
    sums=old.power_sums(e)
    assert all(v.contained_by(source['S'][str(n)]) for n,v in enumerate(sums,1))
    report['rational_S']={str(n):data(v) for n,v in enumerate(sums,1)}
    boxes={int(n):R.read(v) for n,v in source['S'].items()}
    xs=(F(-2),F(-1),F(0),F(1,2))
    assert len(source['trials'])==4
    if all(boxes[n].lo>0 for n in range(2,7)):
        report['rational_trials']=trials(boxes,xs,source['trials'])
    else:
        assert all(row['status']=='undecided_actual_sum_denominator' for row in source['trials'])
    for name,rounding in (('DOWN','ROUND_FLOOR'),('UP','ROUND_CEILING'),('NEAR','ROUND_HALF_EVEN')):
        ctx=source['arithmetic'][name]
        assert ctx['precision']==100 and ctx['rounding']==rounding
        assert all(ctx['traps'].values()) and not any(ctx['exceptional_flags'].values())
    summary=source['summary']
    assert summary['strict_S2_through_S6']==all(boxes[n].lo>0 for n in range(2,7))
    assert summary['trial_statuses']==[r['status'] for r in source['trials']]
    assert summary['certified_witnesses']==sum(r['status']=='certified' for r in source['trials'])
    display_bounds={2:('3.7172599285e-5','3.7172599286e-5'),
                    3:('1.4417393139e-7','1.4417393141e-7'),
                    4:('6.6303168020e-10','6.6303168031e-10'),
                    5:('3.2136641485e-12','3.2136641527e-12'),
                    6:('1.5876934435e-14','1.5876934595e-14')}
    for n,(lo,hi) in display_bounds.items():
        assert 0<F(lo)<boxes[n].lo<=boxes[n].hi<F(hi)
    rejecting_upper_bounds=[('p','-175484.66'),('p','-80930.55'),
                            ('V','-27516.33'),('V','-4838.88')]
    for row,(name,bound) in zip(source['trials'],rejecting_upper_bounds):
        assert F(row['L']['upper'])<0
        assert F(row['values'][name]['upper'])<F(bound)<0
    assert F(source['moments']['0']['lower'])>F('0.49712')
    report['displayed_strict_S_bounds']={str(n):list(bounds) for n,bounds in display_bounds.items()}
    report['displayed_rejection_bounds']=[{'x':str(x),'quantity':name,'strict_upper':bound}
                                         for x,(name,bound) in zip(xs,rejecting_upper_bounds)]
    report.update(status='passed', checks={
        'panels':256, 'moment_orders':7,'panel_integrals':1792,'panel_remainders':1792,
        'complete_positive_tails':True,'all_six_log_polynomials':True,
        'moment_to_log_containment':True,'four_trials_all_values_and_branches':True,
        'canonical_display_bounds_checked':True,'input_hashes_checked':True,
        'strict_signs_and_summary_recomputed':True,'arithmetic_flags_checked':True},
        evidence_limits='No independent jet or Decimal library verification; L036/L037 apply. No other x, zero branch or higher-degree decision.')
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: 1792 panel integrals/remainders, full tails, S1--S6 and four trial branches; replay failures=0')
    print(f'Complete exact-rational certificate: {OUT.relative_to(ROOT)}')


if __name__=='__main__':
    main()
