"""Recover a whole-family lower bound using directed Decimal intervals.

Run from riemann:
OPENBLAS_NUM_THREADS=1 python3 scripts/coupled-flux/certify_rational_schur_dual.py
Floating arithmetic selects rational inputs only. The verification below
uses outward intervals for the full moment equations, inverse residual,
positive weight correction and lower bound. No SDP status is evidence.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json
import time
import numpy as np
from rational_sos_probe import spectral_matrix, monomials

ROOT = Path(__file__).resolve().parent
PRECISION = 90
DOWN = Context(prec=PRECISION, rounding=ROUND_FLOOR)
UP = Context(prec=PRECISION, rounding=ROUND_CEILING)


class I:
    def __init__(self, lo=0, hi=None):
        if isinstance(lo, I): self.lo, self.hi = lo.lo, lo.hi
        else: self.lo, self.hi = D(lo), D(lo if hi is None else hi)
    def __add__(self, other):
        b = I(other)
        return I(DOWN.add(self.lo, b.lo), UP.add(self.hi, b.hi))
    __radd__ = __add__
    def __neg__(self): return I(self.hi.copy_negate(), self.lo.copy_negate())
    def __sub__(self, other): return self + (-I(other))
    def __rsub__(self, other): return I(other) + (-self)
    def __mul__(self, other):
        b = I(other)
        args = [(self.lo,b.lo),(self.lo,b.hi),(self.hi,b.lo),(self.hi,b.hi)]
        return I(min(DOWN.multiply(a,c) for a,c in args), max(UP.multiply(a,c) for a,c in args))
    __rmul__ = __mul__
    def __truediv__(self, other):
        b = I(other)
        if b.lo <= 0 <= b.hi: raise ZeroDivisionError('Interval includes zero')
        return self*I(DOWN.divide(D(1),b.hi), UP.divide(D(1),b.lo))
    def __pow__(self, p):
        assert p >= 0 and int(p) == p
        result = I(1)
        for _ in range(p): result = result*self
        return result
    def absmax(self): return max(self.lo.copy_abs(), self.hi.copy_abs())
    def pair(self): return [str(self.lo), str(self.hi)]


def rational(f):
    return I(str(f.numerator))/I(str(f.denominator))


def dot(a, b): return sum((x*y for x,y in zip(a,b)), I(0))


def inverse_decimal(matrix):
    # This approximate inverse is subsequently validated with outward intervals.
    n = len(matrix)
    with localcontext() as ctx:
        ctx.prec = PRECISION
        a = [[(v.lo+v.hi)/2 for v in row]+[D(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
        for j in range(n):
            p = max(range(j,n), key=lambda k:abs(a[k][j]))
            a[p], a[j] = a[j], a[p]
            pivot = a[j][j]
            if not pivot: raise RuntimeError('Singular chosen correction matrix')
            a[j] = [v/pivot for v in a[j]]
            for k in range(n):
                if k != j:
                    t = a[k][j]
                    a[k] = [v-t*w for v,w in zip(a[k],a[j])]
        return [row[n:] for row in a]


def make_inputs():
    source = ROOT/'rational_schur_probe_stable.json'
    data = json.loads(source.read_text())
    arrays = np.load(ROOT/'rational_schur_probe_stable_maps.npz')
    dual = arrays['dual']
    moments = np.einsum('mij,mijp->pm',dual,arrays['amap'])
    reduced = arrays['change'].T @ moments
    _, _, v = np.linalg.svd(reduced, full_matrices=False)
    work = v.copy()
    selected = []
    for _ in range(46):
        norms = np.sum(work**2, axis=0)
        norms[selected] = -1
        j = int(np.argmax(norms)); selected.append(j)
        e = work[:,j]/np.linalg.norm(work[:,j])
        work -= e[:,None]*(e @ work)[None,:]
    transform = np.array(data['transform'])
    mean = transform[4:,:4] @ np.linalg.inv(transform[:4,:4])
    la = transform[4:,4:]
    def exact_float(a): return format(float(a),'.19e')
    return dict(kind='EXACT RATIONAL INPUTS SELECTED NUMERICALLY; VERIFY BEFORE USE',
                source=source.name, state_integer_denominator=data['state_integer_denominator'],
                state_integers=data['state_integers'],
                mean=[[exact_float(v) for v in row] for row in mean],
                acceleration_transform=[[exact_float(v) for v in row] for row in la],
                dual_cholesky=[[[exact_float(v) for v in row] for row in np.linalg.cholesky(y)] for y in dual],
                selected_matrix_indices=selected,
                convention='First N matrices use branch 0, next N use branch 1. Physical order x,y,z,X,Y,Z; states x,y,X,Y. Each dual matrix is L L^T exactly.')


def verify(data):
    started = time.monotonic()
    states = [[I(str(v))/I(str(data['state_integer_denominator'])) for v in row] for row in data['state_integers']]
    mean = [[I(v) for v in row] for row in data['mean']]
    la = [[I(v) for v in row] for row in data['acceleration_transform']]
    chosen = data['selected_matrix_indices']
    if len(chosen)!=46 or len(set(chosen))!=46: raise RuntimeError('Need 46 different correction columns')
    exponents = [e for e in monomials(4,4) if e[0]<=1]
    assert len(exponents)==25
    pairs = [(i,j) for i in range(6) for j in range(i,6)]
    total = [I(0) for _ in range(46)]
    total_b = I(0)
    selected = {}; selected_b = {}
    minimum_q = D('Infinity')
    n = len(states)
    if len(data['dual_cholesky'])!=2*n: raise RuntimeError('Incorrect branch count')
    for state_idx,w in enumerate(states):
        x,y,X,Y = w
        q = x*x/2+6*y*y+X*X/2+6*Y*Y
        if q.lo<=0: raise RuntimeError('Zero or uncertified state denominator')
        minimum_q = min(minimum_q,q.lo)
        qgrad = [x,12*y,X,12*Y]
        gradients=[]
        for ex in exponents:
            p = I(1)
            for wi,ei in zip(w,ex): p=p*(wi**ei)
            grad=[]
            for k in range(4):
                dp=I(ex[k])
                for j in range(4): dp=dp*(w[j]**max(0,ex[j]-int(j==k)))
                grad.append(dp/q-p*qgrad[k]/(q*q))
            gradients.append(grad)
        amean = [dot(row,w) for row in mean]
        d = [x,y,amean[0],X,Y,amean[1]]
        ts = [[v,I(0),I(0)] for v in d]
        ts[2][1:] = la[0]; ts[5][1:] = la[1]
        for branch in range(2):
            idx=state_idx+branch*n
            ll=[[I(v) for v in row] for row in data['dual_cholesky'][idx]]
            yy=[[dot(a,b) for b in ll] for a in ll]
            # Congruence T Y T^T, with all trace off-diagonal terms included.
            ty=[[dot(row,[yy[k][j] for k in range(3)]) for j in range(3)] for row in ts]
            cov=[dot(ty[i],ts[j]) for i,j in pairs]
            e_z=dot(yy[0],ts[2]); e_Z=dot(yy[0],ts[5])
            velocity=[y*yy[0][0],e_z,Y*yy[0][0],e_Z]
            flux=[dot(grad,velocity) for grad in gradients]
            column=cov+flux
            total=[a+b for a,b in zip(total,column)]
            b=I(0) if not branch else x*e_z-y*y*yy[0][0]
            total_b=total_b+b
            if idx in chosen: selected[idx]=column; selected_b[idx]=b
    matrix=[[selected[j][i] for j in chosen] for i in range(46)]
    kr,ke=spectral_matrix()
    scales=[1,4,8,1,4,8]
    target=[I(rational(kr[i][j]-ke[i][j]).lo,rational(kr[i][j]+ke[i][j]).hi)/(scales[i]*scales[j]) for i,j in pairs]+[I(0) for _ in range(25)]
    residual=[a-b for a,b in zip(target,total)]
    inv=inverse_decimal(matrix)
    invI=[[I(v) for v in row] for row in inv]
    inverse_residual=[]
    for i in range(46):
        inverse_residual.append([I(int(i==j))-dot(invI[i],[matrix[k][j] for k in range(46)]) for j in range(46)])
    # Use directed summation for the upper row norm, not Decimal default rounding.
    eta=max(sum_up(v.absmax() for v in row) for row in inverse_residual)
    z=[dot(row,residual) for row in invI]
    zmax=max(v.absmax() for v in z)
    if eta>=1: delta=I('Infinity')
    else: delta=I(zmax)/(I(1)-I(eta))
    bnorm=sum_up(selected_b[j].absmax() for j in chosen)
    loss=I(delta.hi)*I(bnorm)
    lower=total_b-I(loss.hi)
    required=rational(Fraction(1,288))
    failures=[]
    if eta>=1: failures.append('Approximate inverse not certified.')
    if delta.hi>=1: failures.append('Corrected positive weights not certified.')
    if lower.lo<=required.hi: failures.append('Whole-family lower bound does not exceed 1/288.')
    named_checks={
        'inverse_residual_lt_1e_minus_70':eta<D('1e-70'),
        'weight_correction_lt_3_over_250':delta.hi<rational(Fraction(3,250)).lo,
        'baseline_objective_gt_459_over_50000':total_b.lo>rational(Fraction(459,50000)).hi,
        'selected_absolute_objective_lt_1_over_100':bnorm<D('.01'),
        'cost_lower_gt_9_over_1000':lower.lo>D('.009'),
    }
    for name,passed in named_checks.items():
        if not passed: failures.append('Failed named bound: '+name)
    return dict(kind='OUTWARD INTERVAL VERIFICATION OF FINITE DUAL',passed=not failures,failures=failures,
                named_bound_checks=named_checks,
                decimal_precision=PRECISION,states=n,dual_matrices=2*n,
                moment_rows=21,essential_flux_rows=25,quartic_remainder_exponents=exponents,
                minimum_q_lower=str(minimum_q),selected_matrix_indices=chosen,
                baseline_moment_intervals=[v.pair() for v in total],target_moment_intervals=[v.pair() for v in target],
                residual_intervals=[v.pair() for v in residual],
                correction_matrix_intervals=[[v.pair() for v in row] for row in matrix],
                approximate_inverse=[[str(v) for v in row] for row in inv],
                inverse_residual_intervals=[[v.pair() for v in row] for row in inverse_residual],
                inverse_residual_infinity_norm_upper=str(eta),preconditioned_residual_intervals=[v.pair() for v in z],
                preconditioned_residual_infinity_norm_upper=str(zmax),
                weight_correction_infinity_norm_bound=delta.pair(),
                baseline_objective_interval=total_b.pair(),selected_objective_intervals=[selected_b[j].pair() for j in chosen],
                selected_objective_absolute_sum_upper=str(bnorm),objective_loss_bound=loss.pair(),
                certified_cost_lower=str(lower.lo),required_threshold=required.pair(),
                elapsed_seconds=time.monotonic()-started)


def sum_up(values):
    result=D(0)
    for value in values: result=UP.add(result,value)
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--regenerate-inputs',action='store_true')
    parser.add_argument('--precision',type=int,default=90)
    args=parser.parse_args()
    global PRECISION,DOWN,UP
    PRECISION=args.precision
    if PRECISION<60: raise ValueError('At least 60 decimal digits required')
    DOWN=Context(prec=PRECISION,rounding=ROUND_FLOOR)
    UP=Context(prec=PRECISION,rounding=ROUND_CEILING)
    ipath=ROOT/'rational_schur_dual_inputs.json'
    if args.regenerate_inputs or not ipath.exists():
        ipath.write_text(json.dumps(make_inputs(),indent=2)+'\n')
    result=verify(json.loads(ipath.read_text()))
    result['input_sha256']=hashlib.sha256(ipath.read_bytes()).hexdigest()
    result['verifier_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    suffix='' if PRECISION==90 else '_precision_'+str(PRECISION)
    path=ROOT/('rational_schur_dual_certificate'+suffix+'.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    keys=['kind','passed','failures','named_bound_checks','states','inverse_residual_infinity_norm_upper',
          'weight_correction_infinity_norm_bound','baseline_objective_interval','certified_cost_lower','required_threshold','elapsed_seconds']
    print(json.dumps({key:result[key] for key in keys},indent=2))
    print('Exact rational inputs:',ipath)
    print('Full certificate:',path)


if __name__=='__main__': main()
