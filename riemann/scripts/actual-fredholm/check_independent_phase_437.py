"""Exact-rational checks of ALL saved contour boxes and finite norm data.

This is not an independent audit of the theta evaluator or analytic tails.
It checks complete saved coverage, crossing counts and finite arithmetic.
"""
import json
from decimal import Decimal as D
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
d = json.loads((BASE/'independent-phase-certificate-437.json').read_text())
checks = []


def pair(x):
    a, b = map(F, x)
    assert a <= b
    return a, b


def contains(x, num, den=1, square=False):
    assert den > 0
    a, b = pair(x)
    if square:
        assert a >= 0
        a, b = a*a, b*b
    assert a.numerator*den <= num*a.denominator
    assert num*b.denominator <= b.numerator*den


assert d['failures'] == []
assert d['inherited_failures_435'] == [{'phase':'count','type':'AssertionError','message':''}]
checks.append('original unnecessary root-width assertion failure preserved; wider certified brackets used')
ev = d['evaluation']
assert len(ev['quadrature_cells']) == 128
for k, cell in enumerate(ev['quadrature_cells']):
    assert cell['cell'] == k
    contains(cell['center'], 2*k+1, 128)
    assert len(cell['A_Taylor_coefficients']) == 25
    assert len(cell['moment_integral_error_upper']) == 128
    assert all(F(x) > 0 for x in cell['moment_integral_error_upper'])
checks.append('all 128 quadrature-cell records complete; no independent exp/quadrature replay')

for name in ['inner_contour', 'outer_contour']:
    cc = d[name]
    records = cc['segments']
    count, minimum = 0, None
    for quadrant in range(4):
        parts = [x for x in records if x['quadrant'] == quadrant]
        last = F(0)
        for rec in parts:
            left, right = map(F, rec['t'])
            assert left == last and left < right
            last = right
        assert last == 1
    for k, rec in enumerate(records):
        rr, ii = map(pair, rec['G_box'])
        lower = max(F(0), rr[0], -rr[1], ii[0], -ii[1])
        assert 0 < F(rec['G_lower']) <= lower
        minimum = lower if minimum is None else min(lower, minimum)
        for point in rec['point_enclosures']:
            for bounds, whole in zip(point, [rr, ii]):
                a, b = pair(bounds)
                assert whole[0] <= a <= b <= whole[1]
        assert rec['vertices'][1] == records[(k+1) % len(records)]['vertices'][0]
        for vertex in rec['vertices']:
            assert rr[0] <= F(vertex[0]) <= rr[1]
            assert ii[0] <= F(vertex[1]) <= ii[1]
        (x, y), (xx, yy) = [[F(v) for v in p] for p in rec['vertices']]
        cross = x*yy-y*xx
        assert cross != 0 or not (y <= 0 < yy or yy <= 0 < y)
        count += int(y <= 0 < yy and cross > 0)-int(yy <= 0 < y and cross < 0)
    assert count == cc['count_with_multiplicity'] == 2
    assert 0 < F(cc['G_boundary_lower']) <= minimum
    checks.append(f'{name}: all {len(records)} segments, endpoint inclusions, nonzero boxes and exact winding=2')

n=d['signed']; N,L=n['N'],n['L']; r=3
assert N==512 and L==2048 and N<L-2
ah,dh=list(map(F,n['alpha_hat'])),list(map(F,n['residue_hat']))
sigma,a,rho=F(9,8),F(7,8),F(15,16)
for j,z in enumerate(d['zeros']):
    ends=list(map(pair,z['endpoint_G']))
    assert ends[0][1]<0<ends[1][0] or ends[1][1]<0<ends[0][0]
    assert max(map(abs,pair(z['alpha'])))<a
    for hat,err,enc in [(ah[j],F(n['alpha_error'][j]),z['alpha']),
                        (dh[j],F(n['residue_error'][j]),z['residue'])]:
        lo,hi=pair(enc)
        assert err>=max(hat-lo,hi-hat)
assert pair(d['zeros'][1]['root_w'])[1]<pair(d['zeros'][0]['root_w'])[0]
assert len(n['samples'])==L
for j,s in enumerate(n['samples']):
    assert s['j']==j
    rr,ii=map(pair,s['G'])
    assert rr[0]>0 or rr[1]<0 or ii[0]>0 or ii[1]<0
assert len(n['beta_hat'])==len(n['epsilon'])==len(n['beta_enclosures'])==N
msig=F(d['outer_contour']['G_boundary_lower'])/(sigma+a)**2
assert 0<pair(n['m_sigma'])[0]<=msig
mb=(1+a/sigma)**2/pair(n['m_sigma'])[0]
assert pair(n['M_b'])[1]>=mb
for j,(bh,err,enc,alias) in enumerate(zip(n['beta_hat'],n['epsilon'],n['beta_enclosures'],n['DFT_alias_errors']),1):
    lo,hi=pair(enc)
    assert lo<=F(bh)<=hi and F(err)>=max(F(bh)-lo,hi-F(bh))
    need=pair(n['M_b'])[1]*sigma**(-j-L)/(1-sigma**(-L))
    assert pair(alias)[1]>=need
q=sigma**-2
tn=q**(N+1)*((N+1)-N*q)/(1-q)**2
contains(n['T_N'],tn.numerator,tn.denominator)
hsq=sum(j*F(b)**2 for j,b in enumerate(n['beta_hat'],1))
assert pair(n['h_b'])[1]**2>=hsq
assert pair(n['delta_b'])[1]**2>=sum(j*F(e)**2 for j,e in enumerate(n['epsilon'],1))+pair(n['M_b'])[1]**2*tn
ms=sum(abs(dj)/(rho-a) for dj in dh)
es=sum(F(e)/(rho-a)+abs(dj)*F(ej)/(rho-a)**2 for dj,e,ej in zip(dh,n['residue_error'],n['alpha_error']))
assert pair(n['h_B'])[1]>=ms*rho/(1-rho*rho)
assert pair(n['delta_B'])[1]>=es*rho/(1-rho*rho)
E=pair(n['delta_b'])[1]*pair(n['h_B'])[1]+pair(n['h_b'])[1]*pair(n['delta_B'])[1]+pair(n['delta_b'])[1]*pair(n['delta_B'])[1]
assert pair(n['trace_norm_error'])[1]>=E
checks.append('all root group/error records, all 2048 denominators and 512 coefficient/alias/HS error budgets')

# Complete phase/provenance and DFT checks: exact integer endpoint arithmetic.
# Independent of Decimal's DFT summation and phase-index implementation.
import hashlib
oldpath=BASE/'signed-pair-certificate-435.json'
old=json.loads(oldpath.read_text())
assert hashlib.sha256(oldpath.read_bytes()).hexdigest()==d['reuse_provenance']['input_sha256']
for key in ['evaluation','inner_contour','outer_contour','zeros']:
    assert d[key]==old[key],key
assert n['samples']==old['signed']['samples']
phases=n['independent_phases']
assert len(phases)==L and n['phase_index_rule']=='(-j*n)%2048'
width=F(n['phase_component_width_upper'])
for j,z in enumerate(phases):
    assert z==n['samples'][j]['z']
    for comp in z:
        lo,hi=pair(comp)
        assert hi-lo<=width
assert width<F('1e-70')
assert len(n['DFT_enclosures'])==N
# Both negative modes are excluded for every coefficient (not only -1).
assert all((k-neg)%L!=0 for k in range(1,N+1) for neg in [-2,-1])

def dec_scale(v):
    return max(0,-D(v).as_tuple().exponent)
values=[v for z in phases for comp in z for v in comp]
values += [v for s in n['samples'] for comp in s['b'] for v in comp]
scale=max(map(dec_scale,values)); unit=10**scale

def asint(v):
    t=D(v).as_tuple(); x=int(''.join(map(str,t.digits)))
    return (-x if t.sign else x)*10**(scale+t.exponent)

def ibox(z):
    return [tuple(map(asint,c)) for c in z]

def mul(x,y):
    a=[v*w for v in x for w in y]
    return min(a),max(a)

def cmul(x,y):
    rr,ii=mul(x[0],y[0]),mul(x[1],y[1])
    ri,ir=mul(x[0],y[1]),mul(x[1],y[0])
    return (rr[0]-ii[1],rr[1]-ii[0]),(ri[0]+ir[0],ri[1]+ir[1])
zz=list(map(ibox,phases)); bb=[ibox(s['b']) for s in n['samples']]
den=L*unit**2
# Use reverse-positive indexing from a running EXACT integer accumulator;
# this is modular integer arithmetic only, never complex interval powers.
for k in range(1,N+1):
    sums=[0,0,0,0]; idx=0
    for bval in bb:
        prod=cmul(bval,zz[idx])
        sums=[sums[0]+prod[0][0],sums[1]+prod[0][1],
              sums[2]+prod[1][0],sums[3]+prod[1][1]]
        idx=(idx+L-k)%L
    for comp,start in zip(n['DFT_enclosures'][k-1],[0,2]):
        lo,hi=pair(comp)
        assert lo*den<=sums[start] and hi*den>=sums[start+1],('DFT',k,start)
    real,imag=map(pair,n['DFT_enclosures'][k-1])
    alias=pair(n['DFT_alias_errors'][k-1])[1]
    lo,hi=pair(n['beta_enclosures'][k-1])
    assert lo<=real[0]-alias and hi>=real[1]+alias,('alias transfer',k)
    assert imag[0]-alias<=0<=imag[1]+alias,('imaginary symmetry',k)
checks.append('all inherited inputs unchanged; all 2048 phase widths/provenance and 1048576 modular phase products checked with exact integer endpoints; all 512 complete DFT/imaginary/alias transfers checked')

# Exact integers with a common decimal denominator avoid repeated huge gcds.
def scale_of(x):
    return max(0,-D(x).as_tuple().exponent)

def scaled(x,scale):
    tt=D(x).as_tuple(); digits=int(''.join(map(str,tt.digits)))
    return (-1 if tt.sign else 1)*digits*10**(scale+tt.exponent)

sa=max(map(scale_of,n['alpha_hat'])); sb=max(map(scale_of,n['beta_hat']))
T,B=10**sa,10**sb
aa=[scaled(x,sa) for x in n['alpha_hat']]
bet=[scaled(x,sb) for x in n['beta_hat']]
f=n['finite']; numerators=[]
for i in range(r+1,N+1):
    row=[]
    for j in range(2):
        acc,powden=bet[-1],1
        for l in range(N-1,i-1,-1):
            powden*=T
            acc=acc*aa[j]+bet[l-1]*powden
        contains(f['U_rows'][i-r-1][j],acc,B*T**(N-i))
        row.append(acc)
    numerators.append(row)
gd=B*B*T**(2*(N-r-1))
gu=[[F(sum(row[j]*row[l]*T**(2*k) for k,row in enumerate(numerators)),gd)
     for l in range(2)] for j in range(2)]
gy=[[(ah[j]*ah[l])**r/(1-ah[j]*ah[l]) for l in range(2)] for j in range(2)]
sp=[[F(sum(aa[j]**(i-1)*row[l] for i,row in enumerate(numerators,r+1)),B*T**(N-1))
     for l in range(2)] for j in range(2)]
for saved,exact in [(f['Gram_U'],gu),(f['Gram_Y'],gy),(f['signed_pairing_Ystar_U'],sp)]:
    for j in range(2):
        for l in range(2):
            contains(saved[j][l],exact[j][l].numerator,exact[j][l].denominator)
def det(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]
inter=[[dh[j]*sp[j][l] for l in range(2)] for j in range(2)]
for j in range(2):
    for l in range(2):
        contains(f['signed_interaction_C_Ystar_U'][j][l],inter[j][l].numerator,inter[j][l].denominator)
dd=det([[F(int(j==l))-inter[j][l] for l in range(2)] for j in range(2)])
contains(f['finite_determinant'],dd.numerator,dd.denominator)
tr=sum(dh[j]*dh[l]*gu[j][l]*gy[j][l] for j in range(2) for l in range(2))
prod=det(gu)*det(gy)*(dh[0]*dh[1])**2
assert tr>=0 and prod>=0 and tr*tr>=4*prod
contains(f['singular_square_sum'],tr.numerator,tr.denominator)
contains(f['singular_square_product'],prod.numerator,prod.denominator)
kl,ku=pair(f['finite_norm'])
# λ+ lies above tr/2. Compare (2 x^2-tr)^2 with the discriminant.
dis=tr*tr-4*prod
assert ku*ku>=tr/2 and (2*ku*ku-tr)**2>=dis
assert kl*kl<=tr/2 or (2*kl*kl-tr)**2<=dis
tl,tu=pair(f['finite_trace_norm'])
assert tu*tu>=tr and (tu*tu-tr)**2>=4*prod
assert tl*tl<=tr or (tl*tl-tr)**2<=4*prod
elo,ehi=pair(n['trace_norm_error'])
assert pair(n['actual_trace_norm_upper'])[1]>=tu+ehi
lo,hi=pair(n['original_norm'])
assert lo<=max(F(0),kl-ehi) and hi>=ku+ehi
de=pair(n['determinant_perturbation_error'])[1]
dl,du=pair(f['finite_determinant']); al,au=pair(n['signed_determinant'])
assert al<=dl-de and au>=du+de
checks.append('all 509 U rows, both Gram metrics, signed pairing/determinant and two-sided norm checked with exact integers/rationals')
checks.append('trace-norm product error and triangle enclosures checked; exp perturbation factor relies on documented Decimal contract')
out={'status':'PASS','checks':checks,'failures':[],
     'signed_determinant':n['signed_determinant'],'original_norm':n['original_norm'],
     'required_det_lower':'0','required_norm_lower':'1','decision':n['decision'],
     'limitations':'Complete saved finite/DFT arithmetic check; no independent analytic/evaluator/trig audit or formal verification',
     'input':'scripts/actual-fredholm/independent-phase-certificate-437.json'}
path=BASE/'independent-phase-check-437.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({**out,'certificate':str(path)},indent=2),flush=True)

