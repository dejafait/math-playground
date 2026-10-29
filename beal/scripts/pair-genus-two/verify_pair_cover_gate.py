"""Replay every raw coefficient identity and the complete tiny plane-search grid."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from itertools import product,permutations
from functools import reduce
from math import gcd
import json
import traceback

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'pair-cover-gate-verification.json'
R=dict(completed=False,failures=[],checks=0,bindings={})


def ck(b,name):
    R['checks']+=1
    assert b,name


def read(name):
    raw=(ROOT/name).read_bytes();R['bindings'][name]=sha256(raw).hexdigest()
    return json.loads(raw)


def determinant(m):
    z=Q(0);n=len(m)
    for s in permutations(range(n)):
        a=Q((-1)**sum(s[i]>s[j] for i in range(n) for j in range(i+1,n)))
        for i in range(n):a*=Q(m[i][s[i]])
        z+=a
    return z


def main():
    C=read('pair-cover-gate-certificate.json');sources={n:read(n) for n in C['bindings']}
    ck(all(R['bindings'][n]==h for n,h in C['bindings'].items()),'all input hashes')
    T=sources['quartic-class-certificate.json']['order']['table']
    def mul(a,b):return [a[0]*b[0],a[1]*b[1]]+[sum(a[i+2]*b[j+2]*T[i][j][k] for i in range(4) for j in range(4)) for k in range(4)]
    def vec(a):return list(map(Q,a))
    tr=C['transport'];M=[vec(row) for row in tr['power_to_decomposed']];inv=[vec(row) for row in tr['decomposed_to_power']]
    ck([[sum(M[i][k]*inv[k][j] for k in range(6)) for j in range(6)] for i in range(6)]==[[Q(i==j) for j in range(6)] for i in range(6)],'whole inverse')
    theta=vec(tr['theta_decomposed']);power=vec([1,1,1,0,0,0])
    for j in range(6):
        ck([M[i][j] for i in range(6)]==power,'every theta power');power=mul(power,theta)
    pair=sources['odd-membership-35-certificate.json']['selected_pair']
    xis=[[Q(1),Q(a['rational'])]+vec(a['quartic_O']) for a in pair];xis.append(mul(*xis))
    total=0;report=[]
    for F,xi in zip(C['forms'],xis):
        ck(vec(F['xi_decomposed'])==xi,'complete selected xi')
        qmat=[[[Q(x) for x in row] for row in matrix] for matrix in F['Q_matrices']]
        for i in range(6):
            ei=[Q(i==k) for k in range(6)]
            for j in range(6):
                ej=[Q(j==k) for k in range(6)];expected=mul(xi,mul(ei,ej))
                coeff=[qmat[k][i][j] for k in range(6)]
                ck([sum(M[k][l]*coeff[l] for l in range(6)) for k in range(6)]==expected,'all 216 coefficient identities')
        G=[vec(row) for row in F['raw_G_matrix']];H=[vec(row) for row in F['raw_H_matrix']]
        f=tr['curve_f'];ck(G==qmat[5] and H==[[qmat[4][i][j]-Q(f[5],f[6])*G[i][j] for j in range(6)] for i in range(6)],'raw forms')
        ck(determinant(G)==-1/determinant(M)**2==Q(F['det_G']),'full determinant normalization')
        I=F['normalized_integral_G'];factor=next(G[i][j]/I[i][j] for i in range(6) for j in range(6) if I[i][j])
        ck(G==[[factor*x for x in row] for row in I],'integer form proportionality')
        zeros=[];h=sha256();count=0
        for u in product(range(-2,3),repeat=6):
            if reduce(gcd,map(abs,u))!=1:continue
            if next(x for x in u if x)<0:continue
            value=sum(I[i][i]*u[i]**2 for i in range(6))+2*sum(I[i][j]*u[i]*u[j] for i in range(6) for j in range(i+1,6))
            count+=1;h.update((json.dumps([u,value],separators=(',',':'))+'\n').encode())
            if not value:zeros.append(list(u))
        ck(count==F['tests']==7448 and h.hexdigest()==F['test_sha256'],'all bounded search evidence')
        ck(zeros==F['all_small_isotropic_vectors']==[],'complete zero list')
        ck(F['actual_subspace_dimension']==0 and F['required_subspace_dimension']==3,'actual versus required plane dimension')
        total+=count;report.append(dict(label=F['label'],tests=count,isotropic_vectors=len(zeros)))
    ck(total==C['bounds']['vector_tests']==C['bounds']['vector_tests_cap']==22344,'total cap')
    ck(not C['standard_models_certified'] and not C['pairing_evaluated'],'no model or pairing assertion')
    R.update(completed=True,forms=report,tests=total,standard_models_certified=False,pairing_evaluated=False)


if __name__=='__main__':
    try:main()
    except Exception as e:R['failures'].append(dict(message=str(e),traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R,indent=2)+'\n')
    print(json.dumps({**R,'bindings':'saved in certificate','path':str(OUT)}))
    raise SystemExit(0 if R['completed'] else 1)
