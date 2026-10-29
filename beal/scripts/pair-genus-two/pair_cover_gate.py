"""Bounded raw covering-form construction for the one saved Selmer pair.

Fisher--Yan (2023-09-14), equations (30)--(31), pp.13--14.
No standard covering model or twisted Kummer point is assumed.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import product
from functools import reduce
from math import gcd,lcm
import json
import traceback

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'pair-cover-gate-certificate.json'
D=dict(completed=False,failures=[],bindings={},forms=[],bounds=dict(
    vector_height_cap=2,vector_tests_cap=22344,rational_bits_cap=8192,
    max_rational_bits=0,vector_tests=0),standard_models_certified=False,
    rational_Kummer_point_searched=False,pairing_evaluated=False)


def obs(a):
    if isinstance(a,(list,tuple)):
        for x in a:obs(x)
    elif isinstance(a,(int,Q)):
        a=Q(a);n=max(abs(a.numerator).bit_length(),a.denominator.bit_length())
        D['bounds']['max_rational_bits']=max(D['bounds']['max_rational_bits'],n)
        assert n<=8192
    return a


def read(name):
    raw=(ROOT/name).read_bytes();D['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def invert(m):
    n=len(m);a=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(m)]
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j]);a[j],a[k]=a[k],a[j]
        t=a[j][j];a[j]=[x/t for x in a[j]]
        for k in range(n):
            if j!=k:
                t=a[k][j];a[k]=[x-t*y for x,y in zip(a[k],a[j])]
        obs(a)
    return [row[n:] for row in a]


def det(m):
    a=[list(map(Q,row)) for row in m];s=Q(1)
    for j in range(len(a)):
        k=next((k for k in range(j,len(a)) if a[k][j]),None)
        if k is None:return Q(0)
        if k!=j:a[j],a[k]=a[k],a[j];s=-s
        t=a[j][j];s*=t
        for k in range(j+1,len(a)):
            u=a[k][j]/t;a[k]=[x-u*y for x,y in zip(a[k],a[j])]
        obs(a);obs(s)
    return s


def mul4(a,b):return obs([sum(a[i]*b[j]*TABLE[i][j][k] for i in range(4) for j in range(4)) for k in range(4)])
def mul(a,b):return obs([a[0]*b[0],a[1]*b[1]]+mul4(a[2:],b[2:]))
def mv(m,a):return obs([sum(x*y for x,y in zip(row,a)) for row in m])
def units(n):return [[Q(i==j) for i in range(n)] for j in range(n)]


def bilinear(m,a,b):return sum(a[i]*m[i][j]*b[j] for i in range(6) for j in range(6))


def rank(rows):
    if not rows:return 0
    a=[list(map(Q,row)) for row in rows];r=0
    for j in range(6):
        k=next((k for k in range(r,len(a)) if a[k][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];t=a[r][j];a[r]=[x/t for x in a[r]]
        for k in range(r+1,len(a)):
            t=a[k][j];a[k]=[x-t*y for x,y in zip(a[k],a[r])]
        r+=1
    return r


def main():
    global TABLE
    C=read('odd-membership-35-certificate.json');V=read('odd-membership-35-verification.json')
    model=read('odd-model-support-certificate.json');base=read('quartic-class-certificate.json')
    assert C['completed'] and V['completed'] and not C['failures'] and not V['failures']
    assert V['bindings']['odd-membership-35-certificate.json']==D['bindings']['odd-membership-35-certificate.json']
    TABLE=base['order']['table']
    theta=[Q(2),Q(-2),Q(0),Q(1,25),Q(0),Q(0)]
    powers=[[Q(1),Q(1),Q(1),Q(0),Q(0),Q(0)]]
    for _ in range(5):powers.append(mul(powers[-1],theta))
    change=[[powers[j][i] for j in range(6)] for i in range(6)];inv=invert(change)
    f=model['model']['f'];f6=Q(f[6]);f5=Q(f[5]);dt=det(change)
    assert f6!=0 and dt!=0
    # Candidate class transport normalized at the T=2 branch. See the
    # accompanying draft for the divisor identity and remaining audit gate.
    a,b=C['selected_pair'];xis=[[Q(1),Q(a['rational'])]+list(map(Q,a['quartic_O'])),
                               [Q(1),Q(b['rational'])]+list(map(Q,b['quartic_O']))]
    xis.append(mul(*xis))
    D['transport']=dict(branch_order=['2','-2','quartic alpha/25'],norm_roots=[1,1,1],
                        theta_decomposed=theta,power_to_decomposed=change,
                        decomposed_to_power=inv,curve_f=f,transport_critical_audit_pending=True)
    for label,xi in zip(['epsilon','eta','epsilon_plus_eta'],xis):
        qmat=[[[Q(0) for j in range(6)] for i in range(6)] for k in range(6)]
        for i,ei in enumerate(units(6)):
            for j,ej in enumerate(units(6)):
                coeff=mv(inv,mul(xi,mul(ei,ej)))
                for k in range(6):qmat[k][i][j]=coeff[k]
        G=qmat[5];H=[[qmat[4][i][j]-f5/f6*G[i][j] for j in range(6)] for i in range(6)]
        norm=xi[0]*xi[1]*det([mul4(xi[2:],e) for e in units(4)])
        assert norm==1 and det(G)==-norm/dt**2
        den=lcm(*(x.denominator for row in G for x in row));intG=[[int(x*den) for x in row] for row in G]
        content=reduce(gcd,[abs(x) for row in intG for x in row]);intG=[[x//content for x in row] for row in intG]
        zeros=[];hashes=sha256();tests=0;plane=[]
        for u in product(range(-2,3),repeat=6):
            if reduce(gcd,map(abs,u))!=1:continue
            if next(x for x in u if x)!=abs(next(x for x in u if x)):continue
            value=bilinear(intG,u,u);tests+=1;D['bounds']['vector_tests']+=1
            assert D['bounds']['vector_tests']<=22344
            hashes.update((json.dumps([u,value],separators=(',',':'))+'\n').encode())
            if not value:
                zeros.append(u)
                if all(bilinear(intG,u,v)==0 for v in plane) and rank(plane+[u])>len(plane):plane.append(u)
        D['forms'].append(dict(label=label,xi_decomposed=xi,norm=norm,m=1,
            Q_matrices=qmat,raw_G_matrix=G,raw_H_matrix=H,det_G=det(G),
            normalized_integral_G=intG,tests=tests,test_sha256=hashes.hexdigest(),
            all_small_isotropic_vectors=zeros,greedy_isotropic_subspace=plane,
            actual_subspace_dimension=len(plane),required_subspace_dimension=3))
    D['stopping_gate']='No determinant-compatible standard covering models certified; bounded raw-form plane search only.'
    D['completed']=True


if __name__=='__main__':
    try:main()
    except Exception as e:D['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(D,indent=2,default=str)+'\n')
    print(json.dumps(dict(completed=D['completed'],failures=[e['message'] for e in D['failures']],
        forms=[dict(label=x['label'],tests=x['tests'],isotropic_vectors=len(x['all_small_isotropic_vectors']),
                    subspace_actual=x['actual_subspace_dimension'],subspace_required=3) for x in D['forms']],
        bounds=D['bounds'],stopping_gate=D.get('stopping_gate'),path=str(OUT))))
    raise SystemExit(0 if D['completed'] else 1)
