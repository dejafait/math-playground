#!/usr/bin/env python3
"""Independent arithmetic checks and complete, non-overwriting L767/L768 replay.

Analytic hypotheses and scope are proved in the canonical lemmas.  This
checks all finite evidence; the replay alone does not prove analyticity.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import decimal
from decimal import Decimal as D
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
OUT = HERE / 'audit-397.json'
REPLAY = HERE / 'compact-replay-397.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module():
    path = HERE / 'compact-certificate-395.py'
    spec = importlib.util.spec_from_file_location('certificate395', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def encode(x):
    if isinstance(x, F):
        return str(x)
    raise TypeError(type(x))


def save(path, value):
    path.write_text(json.dumps(value, default=encode, indent=2) + '\n')


def bivariate_product(a, b, cutoff):
    """Exact epsilon/q polynomials, independent of tail_attempt's sums."""
    out = {}
    for (i, j), v in a.items():
        for (k, l), w in b.items():
            if i + k <= cutoff:
                index = (i+k, j+l)
                out[index] = out.get(index, F(0)) + v*w
    return {index: v for index, v in out.items() if v}


def integrate_coefficients(poly, p, cutoff):
    out = [F(0)] * (cutoff+1)
    for (i, j), v in poly.items():
        out[i] += v*factorial(j)/factorial(p)
    return out


def independent_tail(degree=20, epsilon=F(1,32), loose_L=False):
    order = degree+1
    roots = [F(1)]
    for i in range(1, order+1):
        roots.append(roots[-1]*(F(1,4)-i+1)/i)
    lexact = {(i, i+1): F((-1)**i, i+1) for i in range(order+1)}
    uexact = {(i, i): b for i, b in enumerate(roots)}
    vexact = {(0,0): F(1)}
    vexact.update({(i,1): F(3,2)**(i-1) for i in range(1,order+1)})
    lmajor = {(i,i+1): F(1) if loose_L else F(1,i+1)
              for i in range(order+1)}
    umajor = {(0,0): F(1), (0,1): epsilon/4}
    umajor.update({(i,i): abs(b) for i,b in enumerate(roots) if i})
    vmajor = {(0,0): F(1), (0,1): epsilon/(1-F(3,2)*epsilon)}
    vmajor.update({(i,1): F(3,2)**(i-1)/(1-F(3,2)*epsilon)**(i+1)
                   for i in range(1,order+1)})
    power = {(0,0): F(1)}
    major_power = {(0,0): F(1)}
    rows, remainders = [], []
    for p in range(5):
        poly = bivariate_product(bivariate_product(power, uexact, order), vexact, order)
        maj = bivariate_product(bivariate_product(major_power, umajor, order), vmajor, order)
        rows.append(integrate_coefficients(poly,p,order)[:degree+1])
        remainders.append(integrate_coefficients(maj,p,order)[order])
        power = bivariate_product(power,lexact,order)
        major_power = bivariate_product(major_power,lmajor,order)
    return rows, remainders


def primitive_checks(module):
    # All endpoint sign branches, including nonrepresentable rational results.
    balls = [module.Ball(*pair) for pair in [
        ('-9.7','-1.1'), ('-0.3','0'), ('0','0'), ('0','2.7'),
        ('0.1','3.9'), ('-2.3','4.1'), ('1e-120','7e-120'),
        ('-8e-120','-3e-120'),
        ('1.234567890123456789012345678901234567890123456789012345',
         '1.234567890123456789012345678901234567890123456789012346')]]
    checks = 0
    def enclosed(actual, lo, hi):
        nonlocal checks
        assert F(actual.lo) <= lo <= hi <= F(actual.hi)
        checks += 1
    for a in balls:
        al, ah = F(a.lo), F(a.hi)
        enclosed(-a,-ah,-al)
        for b in balls:
            bl, bh = F(b.lo), F(b.hi)
            enclosed(a+b,al+bl,ah+bh)
            enclosed(a-b,al-bh,ah-bl)
            values = [al*bl, al*bh, ah*bl, ah*bh]
            enclosed(a*b,min(values),max(values))
            if bl*bh>0:
                values = [al/bl,al/bh,ah/bl,ah/bh]
                enclosed(a/b,min(values),max(values))
        for n in range(6):
            values = [al**n,ah**n]
            if n>0 and n%2==0 and al<=0<=ah:
                values.append(F(0))
            enclosed(a**n,min(values),max(values))
    # Rational series independently check a nontrivial exp and ln enclosure.
    # exp(1): after n=180, remaining ratios <=1/182, hence geometric bound.
    n=180
    e_lower=sum((F(1,factorial(k)) for k in range(n+1)),F(0))
    e_upper=e_lower+F(1,factorial(n+1))/(1-F(1,n+2))
    v=module.Ball(1).exp()
    assert F(v.lo)<=e_lower<e_upper<=F(v.hi)
    # log(2)=2 sum (1/3)^(2k+1)/(2k+1); positive tail ratio <=1/9.
    l_lower=2*sum((F(1,3)**(2*k+1)/(2*k+1) for k in range(100)),F(0))
    l_upper=l_lower+2*F(1,3)**201/F(201)/(1-F(1,9))
    v=module.Ball(2).log()
    assert F(v.lo)<=l_lower<l_upper<=F(v.hi)
    return dict(rational_interval_checks=checks, rational_exp_ln_checks=2,
                exp1_series_interval=[e_lower,e_upper],log2_series_interval=[l_lower,l_upper])


def check_finite_tree(value, stats):
    if isinstance(value,dict):
        if set(value)=={'lower','upper'}:
            a,b=F(value['lower']),F(value['upper'])
            assert a<=b
            stats['ordered_intervals']+=1
        for child in value.values():
            check_finite_tree(child,stats)
    elif isinstance(value,list):
        for child in value:
            check_finite_tree(child,stats)


def main():
    originals = {name:digest(HERE/name) for name in [
        'tail-certificate-394.py','tail-certificate-394.json',
        'compact-certificate-395.py','compact-certificate-395.json']}
    audit=dict(status='IN_PROGRESS',failures=[],runtime=dict(
        python=sys.version,libmpdec=decimal.__libmpdec_version__,
        exp_contract=D.exp.__doc__,ln_contract=D.ln.__doc__),original_sha256=originals)
    save(OUT,audit)
    m=load_module()
    audit['interval_primitive_checks']=primitive_checks(m)
    prior=json.loads((HERE/'compact-certificate-395.json').read_text())
    tail=m.tail_attempt(32,20)
    assert tail==prior['tail_trials'][0]
    cs,rs=independent_tail()
    assert cs==[[F(v) for v in row] for row in tail['coefficients']]
    assert rs==list(map(F,tail['remainders']))
    # Re-execute the older complete rational certificate into a fresh path.
    old_source=HERE/'tail-certificate-394.py'
    namespace={'__name__':'tail_audit_replay','__file__':str(HERE/'tail-replay-397.py')}
    exec(compile(old_source.read_text(),str(old_source),'exec'),namespace)
    old=namespace['result']
    assert old==json.loads((HERE/'tail-certificate-394.json').read_text())
    cs2,rs2=independent_tail(2,F(1,4),loose_L=True)
    assert [row[1] for row in cs2]==list(map(F,old['entry_expansions']['a']))
    assert [row[2] for row in cs2]==list(map(F,old['entry_expansions']['b']))
    assert rs2==list(map(F,old['entry_expansions']['integrated_remainders']))
    audit['independent_tail_checks']=dict(
        coefficient_counts=[15,105],remainder_counts=[5,5],
        degree20_coefficients=cs,degree21_majorants=rs,
        degree2_coefficients=cs2,degree3_majorants=rs2,
        original_rational_certificate_exact_match=True,
        coarse_tail_lower=tail['coarse_signed_lower'],
        coarse_tail_relative=tail['coarse_relative_upper'])
    replay=dict(tail_trials=[tail],cells=[])
    save(OUT,audit)
    for index,a in enumerate(range(3,32)):
        row=m.cell_certificate(a)
        assert row==prior['cells'][index],f'Full replay mismatch at cell {a}'
        assert row['a']==a and row['b']==a+1 and row['passed']
        q=row['quadrature']
        assert q['degree']==36 and q['Q']==96 and len(q['panels'])==96
        for j,panel in enumerate(q['panels']):
            assert F(panel['q_center'])==F(2*j+1,2)
            assert len(panel['integrals'])==len(panel['remainder_bounds'])==5
        assert len(q['moments'])==len(q['tail_bounds'])==5
        assert len(row['local_taylor_coefficients'])==5
        assert all(len(v)==65 for v in row['local_taylor_coefficients'])
        assert len(row['signed_polynomial_coefficients'])==193
        assert len(row['all_theta_tail_entries'])==5
        lower=F(row['signed_base']['lower'])
        upper=F(row['determinant_tail_error']['upper'])
        ratio=F(row['relative_upper'])
        assert lower*a**3>F(1005239,10**7)>F(1,10)
        assert upper/lower<=ratio<F(364211,10**6)<F(37,100)<F(1,2)
        replay['cells'].append(row)
        if a==3 or a%5==0 or a==31:
            save(REPLAY,replay)
            print(f'Full replay cell [{a},{a+1}]: exact match; '
                  f'x^3 base > {float(lower*a**3):.9g} (required >0.1); '
                  f'relative <= {float(ratio):.9g} (required <0.5).',flush=True)
    assert len(prior['cells'])==len(replay['cells'])==29
    stats={'ordered_intervals':0}
    check_finite_tree(replay,stats)
    flags={}
    for name,ctx in [('DOWN',m.DOWN),('UP',m.UP),('NEAR',m.NEAR),('DEFAULT',decimal.getcontext())]:
        bad=[signal.__name__ for signal,value in ctx.flags.items()
             if value and signal not in (decimal.Inexact,decimal.Rounded)]
        assert not bad,(name,bad)
        flags[name]=dict(precision=ctx.prec,rounding=ctx.rounding,Emin=ctx.Emin,Emax=ctx.Emax,
                        flags=[s.__name__ for s,value in ctx.flags.items() if value])
    for name,value in originals.items():
        assert digest(HERE/name)==value,f'Original changed: {name}'
    lower=min(F(row['signed_base']['lower'])*row['a']**3 for row in replay['cells'])
    ratio=max(F(row['relative_upper']) for row in replay['cells'])
    audit.update(status='COMPLETE_AUDIT_FINITE_EVIDENCE_PASS',
        summary=dict(cells=29,panels=2784,**stats,all_recorded_arrays_exact_match=True,
            compact_lower_times_x_cubed=lower,required_base='>1/10',
            compact_relative_upper=ratio,required_relative='<1/2',
            proved_uniform_relative='<37/100',coverage='[3,32] and [32,infinity)',
            original_files_unchanged=True),context_audit=flags,
        limitations=['Analytic proof and software-contract reasoning are in L767/L768.',
            'Full fixed pair r=3,m=5 only; all-order smoothing and edge transfer remain open.'])
    save(REPLAY,replay)
    audit['replay_sha256']=digest(REPLAY)
    save(OUT,audit)
    print('Audit PASS; failures: []; all original artifacts unchanged.')
    print('Full evidence:',OUT,'; full replay:',REPLAY,flush=True)


if __name__=='__main__':
    try:
        main()
    except Exception as exc:
        result=json.loads(OUT.read_text()) if OUT.exists() else {}
        result.update(status='FAILED',failures=[repr(exc)])
        save(OUT,result)
        print('Audit FAILED:',repr(exc),'; evidence:',OUT,flush=True)
        raise
