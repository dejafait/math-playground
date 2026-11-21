"""One fixed Holland n=0,d=5,D=B_J/2 test; directed intervals throughout.

Reuse L778's audited evaluator and arithmetic. Approximate Newton only
proposes a center; the saved interval Banach certificate is decisive.
"""
import hashlib
import importlib.util
import json
import math
import platform
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
spec = importlib.util.spec_from_file_location('interval431', ROOT/'scripts/actual-fredholm/fixed_pair_431.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
I, D, sym = m.I, m.D, m.sym


def inv(a):
    n = len(a)
    b = [list(row)+[D(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for k in range(n):
        pivot = max(range(k,n), key=lambda i: abs(b[i][k]))
        b[k], b[pivot] = b[pivot], b[k]
        den = b[k][k]
        assert den
        b[k] = [v/den for v in b[k]]
        for i in range(n):
            if i != k:
                c = b[i][k]
                b[i] = [v-c*w for v,w in zip(b[i],b[k])]
    return [row[n:] for row in b]


def system(x, dd, qq):
    a,b,c = x
    out, jac = [], []
    for k in range(3):
        v = (a+k)*(b+k+1)/((a+k+1)*(b+k))*(c+k)*(dd+k+1)/((c+k+1)*(dd+k))
        out.append(v-qq[k])
        jac.append([v/((a+k)*(a+k+1)), -v/((b+k)*(b+k+1)), v/((c+k)*(c+k+1))])
    return out,jac


def peval(co,x):
    r = I(0)
    for c in reversed(co):
        r = r*x+c
    return r


def main():
    source = ROOT/'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    old = json.loads(source.read_text())
    ev = old['evaluation']
    error = I(*ev['uniform_G_error'])
    assert ev['uniform_disk_radius'] == 1600
    aa = [I(*v)+sym(error/(1600**j)) for j,v in enumerate(ev['coefficients'][:5])]
    gamma = [a*(8*4**j*math.factorial(j)) for j,a in enumerate(aa)]
    rr = [g/gamma[0] for g in gamma]
    qq = [rr[k+1].square()/(rr[k]*rr[k+2]) for k in range(3)]
    t = (qq[0]-1)/(qq[1]-1)
    aj = 2*qq[0]/(t-qq[0])
    bjden = qq[0]*(1+1/aj)-1
    bj = 1/bjden
    dd = bj/2
    data = dict(target='fixed n=0,d=5,D=B_J/2',
                runtime=dict(python=platform.python_version(), decimal=m.decimal.__version__,libmpdec=m.decimal.__libmpdec_version__),
                source=str(source.relative_to(ROOT)),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                uniform_G_error=error.pair(),coefficient_error_rule='E_G/1600^j',
                actual_a=[x.pair() for x in aa],gamma=[x.pair() for x in gamma],
                R=[x.pair() for x in rr],q=[x.pair() for x in qq],
                first_stage=dict(T=t.pair(),T_minus_q0=(t-qq[0]).pair(),A_J=aj.pair(),B_J_denominator=bjden.pair(),B_J=bj.pair(),D=dd.pair()),
                attempts=[],failures=[])
    obligatory = dict(q0_minus_1=qq[0]-1,q1_minus_1=qq[1]-1,T_minus_q0=t-qq[0],A_J=aj,B_J=bj,D=dd)
    data['obligatory_bounds'] = {k:v.pair() for k,v in obligatory.items()}
    if any(v.hi < 0 for v in obligatory.values()):
        data['outcome']='STRICT_FIRST_STAGE_OBSTRUCTION'
    elif not all(v.lo>0 for v in obligatory.values()):
        data['outcome']='INCONCLUSIVE_FIRST_STAGE'
    else:
        # One approximate Newton trajectory; no residual is accepted as existence.
        x = [aj.mid(),bj.mid(),dd.mid()]
        converged = False
        for it in range(40):
            f,j = system(x,dd.mid(),[q.mid() for q in qq])
            mm = inv(j)
            delta = [sum(mm[i][k]*f[k] for k in range(3)) for i in range(3)]
            x = [v-h for v,h in zip(x,delta)]
            if max(abs(h) for h in delta)<D('1e-55'):
                converged = True
                break
        data['newton'] = dict(iterations=it+1,converged=converged,center=[str(v) for v in x])
        if not converged or min(x)<=0:
            data['outcome']='INCONCLUSIVE_SOLVER'
        else:
            _,j = system(x,dd.mid(),[q.mid() for q in qq])
            mm = inv(j)  # Decimal numbers now treated as exact rationals.
            data['preconditioner']=[[str(v) for v in row] for row in mm]
            for radius in ('1e-15','1e-18','1e-21'):
                r = D(radius)
                box = [I(v)+sym(I(r)) for v in x]
                f0,_ = system([I(v) for v in x],dd,qq)
                _,jj = system(box,dd,qq)
                residual = [-sum((I(mm[i][k])*f0[k] for k in range(3)),I(0)) for i in range(3)]
                der = [[I(int(i==l))-sum((I(mm[i][k])*jj[k][l] for k in range(3)),I(0)) for l in range(3)] for i in range(3)]
                norms = [sum((I(v.mag()) for v in row),I(0)) for row in der]
                bounds = [I(residual[i].mag())+norms[i]*I(r) for i in range(3)]
                success = all(v.hi<r for v in bounds) and max(v.hi for v in norms)<1 and all(v.lo>0 for v in box)
                rec=dict(radius=radius,box=[v.pair() for v in box],F_center=[v.pair() for v in f0],
                         displacement=[v.pair() for v in residual],derivative=[[v.pair() for v in row] for row in der],
                         row_norms=[v.pair() for v in norms],selfmap_bounds=[v.pair() for v in bounds],required_bound=radius,passed=success)
                data['attempts'].append(rec)
                if success:
                    break
            if not success:
                data['outcome']='INCONCLUSIVE_BOX'
            else:
                a,b,c = box
                co=[I(1)]
                for k in range(5):
                    co.append(-co[-1]*(5-k)/(k+1)*(a+k)*(c+k)*dd/(a*c*(b+k)*(dd+k)))
                data['model_coefficients']=[v.pair() for v in co]
                # Deterministic positive rational grid for disjoint IVT brackets.
                # No candidate parameter changes; endpoint signs use full boxes.
                brackets=[]
                prevx,prev = D(0),peval(co,I(0))
                for n in range(1,10001):
                    xx=D(n)/100
                    val=peval(co,I(xx))
                    if (prev.lo>0 and val.hi<0) or (prev.hi<0 and val.lo>0):
                        brackets.append(dict(interval=[str(prevx),str(xx)],values=[prev.pair(),val.pair()]))
                    if val.lo>0 or val.hi<0:
                        prevx,prev=xx,val
                    if len(brackets)==5:
                        break
                data['root_brackets']=brackets
                data['root_search']=dict(grid='j/100, 0<=j<=10000',last_index=n,required=5,actual=len(brackets))
                data['outcome']='CERTIFIED_MODEL' if len(brackets)==5 else 'INCONCLUSIVE_ROOTS'
    path=BASE/'fixed-model-certificate-476.json'
    path.write_text(json.dumps(data,indent=2)+'\n')
    print('outcome:',data['outcome'])
    for name in ('A_J','B_J','D'):
        print(name,data['first_stage'][name])
    if data['attempts']:
        z=data['attempts'][-1]
        print('Banach:',z['passed'],'row norm upper',max(D(v[1]) for v in z['row_norms']),'required < 1')
        print('selfmap actual',max(D(v[1]) for v in z['selfmap_bounds']),'required <',z['radius'])
    if 'root_search' in data:
        print('root brackets actual/required:',len(data['root_brackets']),'/ 5')
    print('failures:',data['failures'])
    print('certificate:',path.relative_to(ROOT))


if __name__=='__main__':
    main()
