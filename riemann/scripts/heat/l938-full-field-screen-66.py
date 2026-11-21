#!/usr/bin/env python3
"""One fixed full-field screen. Floating point output is NOT a certificate.

The exact partition representation is independent of the numerical solver.
All inputs, columns, finite sample values and solver failures are retained.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, prod
from pathlib import Path
import json
import re
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_suffix('.json')
ARRAYS = Path(__file__).with_suffix('.npz')
REPORT = {'scope': 'one finite floating-point screen at E=1/4; not a uniform certificate',
          'checks': [], 'failures': [], 'stage': 'initial'}


def check(name, passed, actual=None, required=None):
    row = {'name': name, 'passed': bool(passed), 'actual': actual, 'required': required}
    REPORT['checks'].append(row)
    if not passed:
        REPORT['failures'].append(row)


def save():
    OUT.write_text(json.dumps(REPORT, indent=2, allow_nan=False)+'\n')


def partitions(n, top=None):
    if n == 0:
        yield ()
        return
    for r in range(min(n, n if top is None else top), 0, -1):
        for rest in partitions(n-r, r):
            yield (r,)+rest


def remove(mu, r):
    out = list(mu)
    out.remove(r)
    return tuple(out)


def symmetric_monomials(values, max_degree, max_length):
    """Positive-coefficient DP; no alternating power-sum cancellation."""
    shapes = [p for d in range(max_degree+1) for p in partitions(d)
              if len(p) <= max_length]
    shape = values.shape[:-1]
    result = {p: np.zeros(shape) for p in shapes}
    result[()] = np.ones(shape)
    # Decreasing degree permits in-place use of the previous-coordinate DP.
    for i in range(values.shape[-1]):
        powers = [np.ones(shape)]
        for r in range(1, max_degree+1):
            powers.append(powers[-1]*values[..., i])
        for p in reversed(shapes[1:]):
            if len(p) > i+1:
                continue
            for r in set(p):
                result[p] += powers[r]*result[remove(p, r)]
    return result


def score(x):
    """Diagnostic double arithmetic, 12 theta terms, no error certification."""
    u = np.sqrt(x)
    kernel, first, second0 = np.zeros_like(x), np.zeros_like(x), 0.0
    kernel0 = 0.0
    for n in range(1, 13):
        z = np.pi*n*n*np.exp(2*u)
        common = np.exp(u/2-z)
        kernel += (8*z*z-12*z)*common
        first += (-16*z**3+60*z*z-30*z)*common
        z0 = np.pi*n*n
        kernel0 += (8*z0*z0-12*z0)*np.exp(-z0)
        second0 += (32*z0**4-224*z0**3+330*z0*z0-75*z0)*np.exp(-z0)
    out = np.full_like(x, second0/(2*kernel0))
    np.divide(first, 2*u*kernel, out=out, where=u > 0)
    return out


def samples():
    points, records = [], []
    def add(weights, label):
        weights = [F(w) for w in weights]
        total = sum(weights)
        point = [w/total for w in weights]
        points.append(list(map(float, point)))
        records.append({'label': label, 't': list(map(str, point))})
    for k in range(1, 13):
        add([1]*k+[0]*(12-k), f'support-{k}-barycenter')
    qs = [F(1,32),F(1,16),F(1,8),F(1,4),F(1,2),F(3,4),
          F(4,3),F(2),F(4),F(8),F(16),F(32)]
    for m in range(1, 7):
        for q in qs:
            add([q]*m+[1]*(12-m), f'two-block m={m} q={q}')
    previous = json.loads((ROOT/'scripts/heat/l938-simplex-gradient-obstruction-65.json').read_text())
    for w in previous['witnesses']:
        lo, hi = map(F, w['root_bracket'])
        add([(lo+hi)/2]*w['m']+[1]*(12-w['m']),
            f'L942 m={w["m"]} root midpoint ONLY')
    rng = np.random.default_rng(938066)
    for alpha in (0.15, 0.5, 2.0, 20.0):
        for i, row in enumerate(rng.gamma(alpha, 1.0, (128,12))):
            integers = np.maximum(1, np.rint(row/row.max()*10**8).astype(np.int64))
            add(list(map(int, integers)), f'rationalized gamma alpha={alpha} index={i}')
    return np.array(points), records


def barrier_screen(a, d):
    """Diagnostic max-margin barrier; all loss of numerical rank is reported."""
    column_scale = np.linalg.norm(a, axis=0)
    a_scaled = a/column_scale
    u, singular, vt = np.linalg.svd(a_scaled, full_matrices=False)
    rank = int(np.sum(singular > singular[0]*1e-13))
    REPORT['numerical_rank'] = {'columns': int(a.shape[1]), 'retained': rank,
                               'relative_cutoff': 1e-13, 'singular_values': singular.tolist(),
                               'qualification': 'discarded directions prevent any full-class inference'}
    check('no direction discarded by numerical rank cutoff', rank==a.shape[1],rank,int(a.shape[1]))
    q = u[:, :rank]
    scale_d = max(1.0, float(np.max(np.abs(d))))
    ds = d/scale_d
    matrix = np.column_stack([q, -np.ones(len(d))])
    objective = np.zeros(rank+1)
    objective[-1] = -1
    z = np.zeros(rank+1)
    z[-1] = float(np.min(ds))-1
    path = []
    last_mu = None
    stop = 'fixed barrier schedule exhausted'
    for mu in (1.0, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001):
        last_mu = mu
        for iteration in range(45):
            slack = ds+matrix@z
            if float(slack.min()) <= 0:
                raise ArithmeticError('lost strict numerical barrier feasibility')
            grad = objective-mu*(matrix.T@(1/slack))
            weighted = matrix/slack[:,None]
            hessian = mu*(weighted.T@weighted)
            try:
                direction = np.linalg.solve(hessian, -grad)
            except np.linalg.LinAlgError:
                stop = 'singular numerical Newton matrix'
                break
            slope = float(grad@direction)
            if not np.isfinite(slope) or slope >= 0:
                stop = 'Newton direction not a finite descent direction'
                break
            if -slope < 1e-11:
                break
            movement = matrix@direction
            negative = movement < 0
            step = min(1.0, float(np.min(-.99*slack[negative]/movement[negative]))
                       if np.any(negative) else 1.0)
            value = float(objective@z-mu*np.log(slack).sum())
            for _ in range(55):
                proposed = z+step*direction
                snew = ds+matrix@proposed
                if np.all(snew > 0):
                    new_value = float(objective@proposed-mu*np.log(snew).sum())
                    if new_value <= value+.01*step*slope:
                        break
                step /= 2
            else:
                stop = 'numerical line search exhausted'
                break
            z = proposed
            if np.max(np.abs(z)) > 1e10:
                stop = 'coefficient magnitude stop; no boundedness conclusion'
                break
        slack = ds+matrix@z
        path.append({'mu': mu, 'iterations': iteration+1,
                     'sample_margin_scaled_P': float(z[-1]*scale_d),
                     'minimum_slack_normalized': float(slack.min()),
                     'gradient_inf': float(np.max(np.abs(objective-mu*matrix.T@(1/slack))))})
        REPORT['barrier_path'] = path
        REPORT['stage'] = 'numerical barrier running'
        save()
        if stop != 'fixed barrier schedule exhausted':
            break
    coeff = (vt[:rank].T@(z[:-1]/singular[:rank]))/column_scale*scale_d
    residual = d+a@coeff
    raw_dual = last_mu/(ds+matrix@z)
    dual = raw_dual/raw_dual.sum()
    REPORT['screen'] = {'stop': stop, 'epsilon_scaled_P': float(z[-1]*scale_d),
                        'actual_minimum_sample_residual_scaled_P': float(residual.min()),
                        'required_uniform_margin': '>0 on the entire simplex and energy interval',
                        'coefficients': coeff.tolist(),
                        'minimum_sample_index': int(np.argmin(residual)),
                        'dual_weights': dual.tolist(),
                        'dual_radial_scaled_P': float(dual@d),
                        'dual_scaled_column_residual_inf': float(np.max(np.abs(a_scaled.T@dual))),
                        'dual_whitened_column_residual_inf': float(np.max(np.abs(q.T@dual))),
                        'proof_status': 'neither a primal certificate nor a dual certificate'}
    REPORT['candidate'] = {'field_basis_coefficients': [str(F(float(c))/10**24) for c in coeff[:-1]],
                           'a0': str(F(float(coeff[-1]))), 'a1': '0',
                           'qualification': 'exact rationalization of diagnostic doubles, unverified on the domain'}
    return residual


def main():
    paths = [ROOT/'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md',
             ROOT/'lemmas/L942-actual-simplex-two-field-divergence-obstruction.md',
             ROOT/'drafts/literature/2026-11-09-l938-simplex-residual-certificate-test-63.md',
             Path(__file__)]
    REPORT['input_sha256'] = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in paths}
    mu_list = [mu for mu in partitions(13) if len(mu) <= 12]
    basis = []
    for mu in mu_list:
        counts = Counter(mu)
        ref = max(counts)
        for r in sorted(counts):
            if r != ref:
                basis.append({'mu': mu, 'r': r, 'n_r': counts[r], 's': ref, 'n_s': counts[ref]})
    REPORT['basis'] = basis
    check('symmetric degree-13 orbit count', len(mu_list)==100, len(mu_list),100)
    check('pointed divisible orbit count', sum(len(set(p)) for p in mu_list)==271,
          sum(len(set(p)) for p in mu_list),271)
    check('tangent kernel dimension', len(basis)==171,len(basis),171)
    check('every normalized orbit column has exactly zero sum',
          all(F(b['n_r'],b['n_r'])-F(b['n_s'],b['n_s'])==0 for b in basis))
    t, records = samples()
    REPORT['samples'] = records
    REPORT['energy'] = '1/4'
    REPORT['polynomial_scale'] = '10^24 * Pbar; positive rational scaling only'
    REPORT['stage'] = 'exact basis built; numerical evaluation pending'
    save()
    full = symmetric_monomials(t, 12, 12)
    excluded = np.stack([np.delete(t,i,axis=1) for i in range(12)],axis=1)
    leave = symmetric_monomials(excluded,12,11)
    h = score(t/4)
    covariants = {}
    bases = {}
    for mu in mu_list:
        counts = Counter(mu)
        for r in counts:
            nu = remove(mu,r)
            if r == 1:
                base = (12-len(nu))*full[nu]
            else:
                lower = tuple(sorted(nu+(r-1,),reverse=True))
                base = lower.count(r-1)*full[lower]
            theta = np.sum(t**r*leave[nu]*h,axis=1)/4
            bases[(mu,r)] = (r-.5)*base/counts[r]
            covariants[(mu,r)] = bases[(mu,r)]+theta/counts[r]
    columns = [covariants[(tuple(b['mu']),b['r'])]-covariants[(tuple(b['mu']),b['s'])] for b in basis]
    raw = re.findall(r'^\|\s*(-?\d+)\s*\|\s*\(([^)]+)\)\s*\|\s*$',paths[0].read_text(),re.M)
    p = np.zeros(len(t))
    row_data = []
    for c, text in raw:
        alpha = tuple(map(int,text.split(',')))
        mu = tuple(sorted((k for k,n in enumerate(alpha) for _ in range(n) if k),reverse=True))
        orbit = factorial(12)//prod(factorial(n) for n in alpha)
        coefficient = F(int(c),orbit*prod(factorial(2*k)**n for k,n in enumerate(alpha)))
        p += float(coefficient*10**24)*full[mu]
        row_data.append({'alpha': alpha,'mu':mu,'coefficient_of_m_mu':str(coefficient)})
    REPORT['Pbar_rows'] = row_data
    check('34 factorial-normalized arithmetic-average rows retained',len(raw)==34,len(raw),34)
    a = np.column_stack(columns+[-p])
    d = (17+np.sum(t*h,axis=1)/4)*p
    REPORT['numeric_notes'] = ['L942 algebraic roots are represented by rational midpoints here, not exact zeros.',
                               'Theta sum uses 12 terms in double arithmetic; no directed rounding or tail certificate.',
                               'No random or finite sample set establishes a uniform inequality.',
                               'At fixed energy the affine scalar has only one effective column.']
    check('all diagnostic matrix entries finite',np.all(np.isfinite(a)) and np.all(np.isfinite(d)))
    np.savez_compressed(ARRAYS,t=t,h=h,Pbar_scaled=p,radial_scaled=d,columns=a)
    REPORT['array_artifact'] = str(ARRAYS.relative_to(ROOT))
    REPORT['stage'] = 'matrix saved; numerical barrier pending'
    save()
    print(f'Exact representation: {len(basis)} field directions; {len(t)} fixed-energy diagnostic points.',flush=True)
    try:
        residual = barrier_screen(a,d)
        np.savez_compressed(ARRAYS,t=t,h=h,Pbar_scaled=p,radial_scaled=d,columns=a,residual=residual)
        # One held-out endpoint evaluation of the same field and constant a;
        # this is not a second fit, a uniform test, or a mathematical proof.
        hh = score(4*t)
        cc = {}
        for mu in mu_list:
            counts=Counter(mu)
            for r in counts:
                cc[(mu,r)]=bases[(mu,r)]+4*np.sum(t**r*leave[remove(mu,r)]*hh,axis=1)/counts[r]
        aa=np.column_stack([cc[(tuple(b['mu']),b['r'])]-cc[(tuple(b['mu']),b['s'])] for b in basis]+[-p])
        dd=(17+4*np.sum(t*hh,axis=1))*p
        rr=dd+aa@np.array(REPORT['screen']['coefficients'])
        j=int(np.argmin(rr))
        REPORT['held_out_endpoint']={'E':'4','constant_a_extension':'a1=0, no second fit',
                                     'minimum_sample_residual_scaled_P':float(rr[j]),
                                     'minimum_sample_index':j,'label':records[j]['label'],
                                     'negative_sample_count':int(np.sum(rr<0)),
                                     'required_uniform_margin':'>0',
                                     'qualification':'floating diagnostic only; not a rigorous disqualification of all affine extensions'}
    except (ArithmeticError,ValueError,np.linalg.LinAlgError,FloatingPointError) as exc:
        REPORT['failures'].append({'name':'numerical screen','message':str(exc)})
    REPORT['stage'] = 'finished'
    REPORT['result'] = 'EXPLORATION: no uniform residual or rigorous full-class dual established'
    save()
    print(REPORT['result'])
    if 'screen' in REPORT:
        s=REPORT['screen']
        print(f"Sample minimum={s['actual_minimum_sample_residual_scaled_P']:.9g}; uniform requirement=>0; stop={s['stop']}")
        print(f"Numerical rank={REPORT['numerical_rank']['retained']}/{a.shape[1]}; dual column defect={s['dual_scaled_column_residual_inf']:.4g}")
    if 'held_out_endpoint' in REPORT:
        endpoint=REPORT['held_out_endpoint']
        print(f"Held-out E=4 sample minimum={endpoint['minimum_sample_residual_scaled_P']:.9g}; required=>0; negative samples={endpoint['negative_sample_count']}")
    print(f"Checks={len(REPORT['checks'])}; failures={len(REPORT['failures'])}; full record={OUT.relative_to(ROOT)}; arrays={ARRAYS.relative_to(ROOT)}")


if __name__=='__main__':
    main()
