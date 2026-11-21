"""Independent exact-rational algebra and evidence replay; not a quadrature audit.

Derive Newton polynomials by finite log extraction independently, then replay
all interval arithmetic after the moment enclosures with Fraction endpoints.
Independently enclose the complete tail constants by rational exp series.
"""
import importlib.util
import json
import sys
from decimal import Decimal
from fractions import Fraction as F
from math import factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('h1_rational_replay', HERE/'low-time-h1-uniform-180-check.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
R = module.R

class P:
    def __init__(self, value=0):
        self.terms = value if isinstance(value,dict) else ({(0,)*6:F(value)} if value else {})
    @staticmethod
    def lift(v):
        return v if isinstance(v,P) else P(v)
    def __add__(self,other):
        result = self.terms.copy()
        for monomial,c in self.lift(other).terms.items():
            result[monomial] = result.get(monomial,F(0))+c
        return P({m:c for m,c in result.items() if c})
    __radd__=__add__
    def __neg__(self):
        return P({m:-c for m,c in self.terms.items()})
    def __sub__(self,other):
        return self + -self.lift(other)
    def __mul__(self,other):
        result={}
        for m,c in self.terms.items():
            for n,d in self.lift(other).terms.items():
                monomial=tuple(a+b for a,b in zip(m,n))
                result[monomial]=result.get(monomial,F(0))+c*d
        return P({m:c for m,c in result.items() if c})
    __rmul__=__mul__
    def __pow__(self,n):
        result=P(1)
        for _ in range(n): result=result*self
        return result
    def data(self):
        return [{"exponents":list(m),"coefficient":str(c)} for m,c in sorted(self.terms.items())]


def power_sums(e):
    a,b,c,d,e5,f=e
    return [a,a**2-2*b,a**3-3*a*b+3*c,
            a**4-4*a**2*b+2*b**2+4*a*c-4*d,
            a**5-5*a**3*b+5*a*b**2+5*a**2*c-5*b*c-5*a*d+5*e5,
            a**6-6*a**4*b+9*a**2*b**2-2*b**3+6*a**3*c
            -12*a*b*c+3*c**2-6*a**2*d+6*b*d+6*a*e5-6*f]


def formal_check():
    e=[P({tuple(int(j==i) for j in range(6)):F(1)}) for i in range(6)]
    h=[P(0)]+[(-1)**n*e[n-1] for n in range(1,7)]
    # Independent finite-log extraction, truncated after t^6.
    power=[P(1)]+[P(0) for _ in range(6)]
    log=[P(0) for _ in range(7)]
    for r in range(1,7):
        power=[sum((power[j]*h[n-j] for j in range(n+1)),P(0)) for n in range(7)]
        log=[log[n]+F((-1)**(r+1),r)*power[n] for n in range(7)]
    formulas=power_sums(e)
    residuals=[((-n)*log[n]-formulas[n-1]).data() for n in range(1,7)]
    assert all(not residual for residual in residuals)
    return {"method":"finite sum log(1+h)=sum (-1)^(r+1)h^r/r mod t^7",
            "residuals":residuals,"derived_S_polynomials":[p.data() for p in formulas]}


def exp_minus(x,degree=1000):
    term=F(1); partial=term
    for n in range(1,degree+1):
        term=term*x/n
        partial+=term
    nxt=term*x/(degree+1)
    upper=partial+nxt/(1-x/F(degree+2))
    assert 0<=x<degree+2
    return R(1/upper,1/partial)


def tail_check(data):
    beta=F(119,40)
    coefficient=sum((F(factorial(8),factorial(8-j))*50**(8-j)/beta**(j+1) for j in range(9)),F(0))
    spatial=128*exp_minus(50*beta)*coefficient
    theta=3225600000*exp_minus(25*beta-1)
    total=spatial+theta
    for key,val in (("spatial",spatial),("theta",theta),("total",total)):
        assert val.contained_by(data['tails'][key])
    assert total.hi<F('4.389e-23')
    return {"degree":1000,"method":"positive exp series with geometric next-term bound, then reciprocation",
            "spatial":{"lower":str(spatial.lo),"upper":str(spatial.hi)},
            "theta":{"lower":str(theta.lo),"upper":str(theta.hi)},
            "total":{"lower":str(total.lo),"upper":str(total.hi)},
            "outward_tail_intervals_contain_rational_bounds":True}


def main():
    source=HERE/'low-time-h2-uniform-195.json'
    data=json.loads(source.read_text())
    report={"status":"running","failures":[],"formal_algebra":formal_check()}
    assert (data['precision'],data['parameter_panels'],data['spatial_panels'],data['theta_terms'],
            data['spatial_cutoff'],data['taylor_remainder_order'])==(100,256,64,4,2,8)
    assert len(data['panels'])==256
    report['tails']=tail_check(data)
    rows=[]
    for i,panel in enumerate(data['panels']):
        assert panel['index']==i
        lam=R.read(panel['lambda'])
        assert lam.lo==F(i,5120) and lam.hi==F(i+1,5120)
        moments={int(k):R.read(v) for k,v in panel['moments'].items()}
        assert set(moments)==set(range(0,13,2))
        assert all(v.lo>0 for v in moments.values())
        errors={int(k):R.read(v) for k,v in panel['quadrature_error_bounds'].items()}
        assert set(errors)==set(moments) and all(v.lo>=0 for v in errors.values())
        e=[moments[2*n]/(factorial(2*n)*moments[0]) for n in range(1,7)]
        assert all(v.contained_by(panel['normalized_coefficients'][str(n)]) for n,v in enumerate(e,1))
        s=power_sums(e)
        assert all(v.contained_by(panel['S'][str(n)]) for n,v in enumerate(s,1))
        a,b,c,d,e6=s[1:]
        cofactors=[c*e6-d*d,b*e6-d*c,b*d-c*c]
        terms=[a*cofactors[0],-b*cofactors[1],c*cofactors[2]]
        minors=[a,a*c-b*b,sum(terms,R(0))]
        assert all(v.contained_by(panel['determinant_cofactors'][j]) for j,v in enumerate(cofactors))
        assert all(v.contained_by(panel['determinant_terms'][j]) for j,v in enumerate(terms))
        assert all(v.contained_by(panel['leading_minors'][str(n)]) for n,v in enumerate(minors,1))
        expanded=a*c*e6+2*b*c*d-a*d*d-e6*b*b-c*c*c
        assert expanded.contained_by(panel['expanded_determinant'])
        assert max(F(panel['expanded_determinant']['lower']),F(panel['leading_minors']['3']['lower']))<=min(F(panel['expanded_determinant']['upper']),F(panel['leading_minors']['3']['upper']))
        failed=[str(n) for n in range(1,4) if F(panel['leading_minors'][str(n)]['lower'])<=0]
        assert failed==panel['failed_minors']
        assert panel['strict_signs_certified']==(not failed)
        assert panel['status']==('strict_signs_certified' if not failed else 'unresolved_interval_width')
        rows.append({"index":i,"closed_parameter_panel_exact":True,"all_algebra_contained":True,
                     "failed_minors":failed,"complete_moment_and_remainder_records_checked":True})
    failed=[r['index'] for r in rows if r['failed_minors']]
    assert failed==data['failed_panels']
    assert data['status']==('unresolved' if failed else 'certified')
    summary=data['summary']
    assert summary['failed_panel_count']==len(failed) and summary['certified_panel_count']==256-len(failed)
    assert F(summary['minimum_mass_lower'])==min(F(p['moments']['0']['lower']) for p in data['panels'])
    assert F(summary['tail_upper'])==F(data['tails']['total']['upper'])
    for n in ('1','2','3'):
        vals=[R.read(p['leading_minors'][n]) for p in data['panels']]
        saved=summary['leading_minors'][n]
        assert F(saved['minimum_lower'])==min(v.lo for v in vals)
        assert F(saved['maximum_upper'])==max(v.hi for v in vals)
        assert saved['strict_positive_count']==sum(v.lo>0 for v in vals)
        assert saved['zero_containing_count']==sum(v.lo<=0<=v.hi for v in vals)
        assert saved['strict_negative_count']==sum(v.hi<0 for v in vals)
    thresholds={'minimum_mass_lower':F('0.49712'),
                'Delta1_lower':F('3.714e-5'),'Delta2_lower':F('9.7e-16'),
                'Delta2_upper':F('7.026e-15'),'Delta3_lower':F('-7.013e-27'),
                'Delta3_upper':F('6.585e-27')}
    assert F(summary['minimum_mass_lower'])>thresholds['minimum_mass_lower']
    assert F(summary['leading_minors']['1']['minimum_lower'])>thresholds['Delta1_lower']
    assert F(summary['leading_minors']['2']['minimum_lower'])>thresholds['Delta2_lower']
    assert F(summary['leading_minors']['2']['maximum_upper'])<thresholds['Delta2_upper']
    assert F(summary['leading_minors']['3']['minimum_lower'])>thresholds['Delta3_lower']
    assert F(summary['leading_minors']['3']['maximum_upper'])<thresholds['Delta3_upper']
    first=data['panels'][0]
    s6=R.read(first['S']['6']); det=R.read(first['leading_minors']['3'])
    assert F('-8.828e-14')<s6.lo<0<s6.hi<F('1.201e-13')
    assert F('-6.508e-27')<det.lo<0<det.hi<F('6.104e-27')
    m12=R.read(first['moments']['12'])
    assert F('1.776e-9')<m12.hi-m12.lo<F('1.777e-9')
    assert F(first['quadrature_error_bounds']['12']['upper'])<F('6.241e-12')
    assert F(data['tails']['spatial']['upper'])<F('4.447e-50')
    assert F(data['tails']['theta']['upper'])<F('4.388e-23')
    report['rational_conclusion_thresholds_checked']={k:str(v) for k,v in thresholds.items()}
    report['panel0_width_diagnostics_checked']=True
    for ctx in data['arithmetic'].values():
        assert ctx['precision']==100 and all(ctx['traps'].values()) and not any(ctx['exceptional_flags'].values())
    assert [data['arithmetic'][k]['rounding'] for k in ('DOWN','UP','NEAR')]==['ROUND_FLOOR','ROUND_CEILING','ROUND_HALF_EVEN']
    report.update(status='passed',panels_checked=256,panels=rows,failed_sign_panels=failed,
                  summary_recomputed=True,arithmetic_flags_checked=True,
                  scope='Exact algebra/coverage/tail replay; no independent finite quadrature or Decimal.exp verification')
    out=HERE/'low-time-h2-uniform-195-check.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(f'PASS: 256 complete panels replayed; failed sign panels={len(failed)}; replay failures=0')
    print(f'Certificate: {out.relative_to(Path.cwd())}')

if __name__=='__main__': main()
