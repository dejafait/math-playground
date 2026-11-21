"""L917 bounded audit: replay every finite quadrature record, without refinement.

Uses the inspected L037 interval/jet primitives and the original preparation;
this is a separately written integration loop, not an independent Decimal
implementation. Complete evidence is written beside this script.
"""
import hashlib
import importlib.util
import json
import platform
from decimal import Decimal, DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('producer195', HERE/'low-time-h2-uniform-195.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
I, base = p.I, p.base
OUT = HERE/'low-time-h2-audit-197.json'


def main():
    data = json.loads((HERE/'low-time-h2-uniform-195.json').read_text())
    p.checks()
    pi = base.pi_bounds()
    spatial, theta, tail = p.tilted_tail()
    assert pi.data() == data['pi']
    assert {k:v.data() for k,v in zip(('spatial','theta','total'),(spatial,theta,tail))} == data['tails']
    cached, weights, remainder_weight = p.prepare(pi)
    assert len(cached) == 64
    assert all(center.lo == center.hi == Decimal(2*j+1)/64
               and domain.lo == Decimal(2*j)/64 and domain.hi == Decimal(2*j+2)/64
               for j,(center,domain,_,_) in enumerate(cached))
    # Exact positive-series witnesses for the geometric-tail premises.
    beta = F(119,40)
    assert sum((F(9)**j/p.factorial(j) for j in range(5)), F(0)) > 32
    assert 11*beta > 9
    assert sum((F(4)**j/p.factorial(j) for j in range(8)), F(0)) > 50
    inputs = [Path(__file__), HERE/'low-time-h2-uniform-195.py',
              HERE/'low-time-h2-uniform-195-check.py', HERE/'low-time-h1-uniform-180-check.py',
              HERE.parent/'hankel/certify_hankel.py', HERE/'low-time-h2-uniform-195.json']
    report = {'status':'running','python':platform.python_version(),
              'scope':'Complete finite quadrature replay with inspected shared Decimal/jet primitives; no independent library verification or refinement',
              'input_sha256':{str(f.relative_to(HERE.parent.parent)):hashlib.sha256(f.read_bytes()).hexdigest() for f in inputs},
              'pi_and_tail_records_equal':True,'exact_tail_premises_passed':True,
              'spatial_closed_partition_checked':True,'failures':[],'panels':[]}
    for index, saved in enumerate(data['panels']):
        lam = I.rational(F(index,5120))
        lam = I(lam.lo, I.rational(F(index+1,5120)).hi)
        assert lam.data() == saved['lambda']
        totals, errors = {}, {}
        for order in p.ORDERS:
            total, error_sum = I(0), I(0)
            for center, domain, midpoint, rectangle in cached:
                mid = base.multiply(midpoint[order], p.tilt_jet(center,lam))
                full = base.multiply(rectangle[order], p.tilt_jet(domain,lam))
                error = I(full[8].magnitude()) * remainder_weight
                polynomial = sum((mid[j]*weights[j] for j in (0,2,4,6)), I(0))
                total = total + polynomial + I(error.hi.copy_negate(),error.hi)
                error_sum = error_sum + error
            totals[str(order)] = (total + I(0,tail.hi)).data()
            errors[str(order)] = error_sum.data()
        assert totals == saved['moments'], f'moment mismatch on {index}'
        assert errors == saved['quadrature_error_bounds'], f'remainder mismatch on {index}'
        report['panels'].append({'index':index,'lambda':lam.data(),
                                  'moments':totals,'quadrature_error_bounds':errors,
                                  'all_saved_records_equal':True})
        if (index+1)%32 == 0:
            OUT.write_text(json.dumps(report,indent=2)+'\n')
            print(f'Audited {index+1}/256 complete panels',flush=True)
    signals=(DivisionByZero,InvalidOperation,Overflow,Underflow,Subnormal)
    report['arithmetic']={name:{'precision':ctx.prec,'rounding':ctx.rounding,
                          'traps':{s.__name__:ctx.traps[s] for s in signals},
                          'exceptional_flags':{s.__name__:ctx.flags[s] for s in signals}}
                         for name,ctx in (('DOWN',base.DOWN),('UP',base.UP),('NEAR',base.NEAR))}
    assert report['arithmetic'] == data['arithmetic']
    report['summary']={'panels_checked':len(report['panels']),
                       'moment_intervals_equal':256*7,'remainder_intervals_equal':256*7,
                       'required_equal_counts':1792,'failures':0,
                       'no_refinement':True,'arithmetic_contract_conditional':True}
    report['status']='passed'
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report['summary']))
    print(f'Full evidence: {OUT.relative_to(HERE.parent.parent)}')


if __name__ == '__main__':
    main()
