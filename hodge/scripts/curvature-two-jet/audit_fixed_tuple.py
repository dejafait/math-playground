"""Independent exact audit of the saved L144 witness; does not import its solver.

Quaternion multiplication constructs the frames. Python object integers avoid
fixed-width overflow. The rank computation uses reverse-column rational pivots.
All affine columns are substituted into the original tensor equations.
"""
import hashlib
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import numpy as np

ROOT = Path(__file__).parent
source = ROOT / 'fixed_tuple_certificate.json'
saved = json.loads(source.read_text())
checks = {}
residuals = {}

def check(name, condition):
    checks[name] = bool(condition)

def zero(name, a):
    a = np.asarray(a, dtype=object)
    bad = np.argwhere(a != 0)
    residuals[name] = {'scalar_count': a.size, 'nonzero_count': len(bad),
                     'max_absolute_residual': int(max(map(abs, a.flat), default=0)),
                     'nonzero_entries': [[list(map(int, idx)), str(a[tuple(idx)])]
                                         for idx in bad]}
    check(name, not len(bad))

def qmul(i, j):
    if i == 0: return 1, j
    if j == 0: return 1, i
    if i == j: return -1, 0
    if (i, j) in [(1, 2), (2, 3), (3, 1)]: return 1, 6-i-j
    return -1, 6-i-j

left, right = [], []
for k in range(1, 4):
    l, r = np.zeros((4, 4), dtype=object), np.zeros((4, 4), dtype=object)
    for a in range(4):
        sign, out = qmul(k, a); l[out, a] = sign
        sign, out = qmul(a, k); r[out, a] = sign
    left.append(l); right.append(-r)
M = np.array(right, dtype=object)
T = np.array(left, dtype=object)  # faithful real su(2), -trace/4 pairing
B = np.zeros((10, 8, 8), dtype=object)
for t in range(3):
    B[t, :4, :4] = M[t]
    B[3+t, 4:, 4:] = M[t]
for t, m in enumerate([np.eye(4, dtype=object), *M]):
    B[6+t, :4, 4:] = m
    B[6+t, 4:, :4] = -m.T
L = np.zeros((3, 8, 8), dtype=object)
L[:, :4, :4] = T; L[:, 4:, 4:] = T
check('saved_basis_matches_quaternion_construction', B.tolist() == saved['curvature_basis'])
zero('basis_skew', B + B.transpose(0, 2, 1))
zero('basis_invariance', [l.T @ b @ l-b for l in L for b in B])
zero('su2_normalization', [T[i] @ T[j]-T[j] @ T[i]-2*T[k]
                          for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]])
zero('basis_gram', np.tensordot(B, B, axes=((1,2),(1,2))) -
     np.diag([4]*6+[8]*4))
# ASD: star exchanges (01,23), (02,31), (03,12), with positive signs.
zero('asd_orientation', [[m[0,1]+m[2,3], m[0,2]+m[3,1], m[0,3]+m[1,2]] for m in M])
H = np.zeros((5,3,3), dtype=object)
H[0] = np.diag([1,-1,0]); H[1] = np.diag([0,1,-1])
for n,(i,j) in enumerate([(0,1),(0,2),(1,2)],2): H[n,i,j]=H[n,j,i]=1
check('saved_base_basis_matches', H.tolist() == saved['base_operator_basis'])
G = np.zeros((10,8,8,8,8), dtype=object)
for factor in range(2):
    sl = slice(4*factor,4*factor+4)
    for h in range(5):
        G[5*factor+h,sl,sl,sl,sl] = sum(
            (H[h,k,l]*np.multiply.outer(M[k], M[l]) for k,l in product(range(3),repeat=2)),
            np.zeros((4,4,4,4), dtype=object))
zero('base_skew_input', G+G.transpose(0,2,1,3,4))
zero('base_skew_output', G+G.transpose(0,1,2,4,3))
zero('base_pair_symmetry', G-G.transpose(0,4,3,2,1))
zero('base_first_bianchi', G+G.transpose(0,4,1,3,2)+G.transpose(0,2,4,3,1))
zero('base_ricci', [[sum(G[h,i,j,i,a] for i in range(8)) for j,a in product(range(8),repeat=2)] for h in range(10)])
zero('base_quaternion_commutators', [G[h,i,j]@l-l@G[h,i,j] for h,i,j in product(range(10),range(8),range(8)) for l in L])
R = np.zeros((8,8,3), dtype=object)
R[:,:,0] = B[6]; R[:,:,1] = B[7]; R[:,:,2] = 2*B[0]+B[3]
check('saved_tuple_matches', np.tensordot(B,np.array(saved['su2_coefficients'],dtype=object),axes=(0,0)).tolist() == R.tolist())
Rmat = np.tensordot(R,T,axes=(2,0))
# W is computed directly by matrix commutator and full two-form matrix action.
W = np.zeros((8,8,8,8,3,11), dtype=object)
for i,j,a,b in product(range(8),repeat=4):
    comm = Rmat[i,j]@Rmat[a,b]-Rmat[a,b]@Rmat[i,j]
    for c in range(3):
        numerator = -np.trace(comm@T[c])
        assert numerator % 4 == 0
        W[i,j,a,b,c,0] = numerator//4
for h,i,j,c in product(range(10),range(8),range(8),range(3)):
    W[i,j,:,:,c,h+1] = -(G[h,i,j].T@R[:,:,c]+R[:,:,c]@G[h,i,j])
order = [(i,j,t) for i in range(8) for j in range(i,8) for t in range(10)]
check('unknown_order', [list(x) for x in order] == saved['unknown_order'])
check('parameter_order', saved['parameter_order'] == ['constant']+[f'base{b+1}_H{h+1}' for b in range(2) for h in range(5)])
X = np.array([[Fraction(x) for x in row] for row in saved['solution']],dtype=object).reshape(360,3,11)
check('dense_shape', X.shape == (360,3,11))
check('integral_witness', all(x.denominator == 1 for x in X.flat))
X = np.array([int(x) for x in X.flat],dtype=object).reshape(X.shape)
S = np.zeros(X.shape,dtype=object)
for key,row in saved['solution_sparse'].items():
    n=order.index(tuple(map(int,key.split(','))))
    for column,value in row.items():
        c,h=map(int,column.split(',')); S[n,c,h]=Fraction(value)
zero('dense_sparse_agreement', X-S)
V = np.zeros(W.shape,dtype=object)
for n,(i,j,t) in enumerate(order):
    V[i,j] += np.multiply.outer(B[t],X[n])
for i in range(8):
    for j in range(i): V[i,j] = V[j,i]+W[i,j]
zero('W_skew_derivative', W+W.transpose(1,0,2,3,4,5))
zero('V_curvature_skew', V+V.transpose(0,1,3,2,4,5))
zero('full_ricci_identity', V-V.transpose(1,0,2,3,4,5)-W)
zero('full_differentiated_bianchi', V+V.transpose(0,3,1,2,4,5)+V.transpose(0,2,3,1,4,5))
zero('full_V_type', [l.T@V[i,j,:,:,c,h]@l-V[i,j,:,:,c,h]
                      for l in L for i,j,c,h in product(range(8),range(8),range(3),range(11))])
zero('full_differentiated_divergence', [sum(V[i,j,j,b] for j in range(8)) for i,b in product(range(8),repeat=2)])
traceV = sum(V[i,i] for i in range(8))
contract = np.array([[-sum(W[i,a,b,i]+W[i,b,i,a] for i in range(8)) for b in range(8)] for a in range(8)],dtype=object)
zero('full_contracted_identity', traceV-contract)
required = np.zeros((4,4,3,11),dtype=object); required[:,:,:,0] = -4*R[:4,4:]
zero('mixed_L143_equation', traceV[:4,4:]-required)
check('V_nonzero', bool(np.any(V)))
energy=int(np.sum(traceV[:4,4:,:,0]*R[:4,4:])); norm=int(np.sum(R[:4,4:]**2))
check('energy_and_norm', (energy,norm)==(-32,8))
check('saved_contractions', all(
    [str(x) for x in traceV[a,b].flat] == row['actual'] == row['required']
    for row in saved['mixed_contracted_equation'] for a,b in [row['indices']]))
# Independent reverse-column sparse rational elimination; only homogeneous
# coefficients are needed for rank. Augmented columns verify zero residuals.
lookup={v:n for n,v in enumerate(order)}
rows=[]
for i in range(8):
    for j,a,b in combinations(range(8),3):
        row={}; rhs=np.zeros((3,11),dtype=object)
        for d,x,y in [(j,a,b),(a,b,j),(b,j,a)]:
            for t in range(10):
                n=lookup[min(i,d),max(i,d),t]
                row[n]=row.get(n,0)+B[t,x,y]
            if i>d: rhs-=W[i,d,x,y]
        row={n:Fraction(v) for n,v in row.items() if v}
        zero(f'linear_row_{len(rows)}', sum((v*X[n] for n,v in row.items()),np.zeros((3,11),dtype=object))-rhs)
        rows.append((row,[Fraction(v) for v in rhs.flat]))
pivots={}; pivot_log=[]; inconsistent=[]
for row_number,(orig,rhs_orig) in enumerate(reversed(rows)):
    row=dict(orig); rhs=list(rhs_orig)
    while row:
        p=max(row); f=row[p]
        if p not in pivots:
            row={n:v/f for n,v in row.items()}; rhs=[v/f for v in rhs]
            pivots[p]=(row,rhs); pivot_log.append([447-row_number,p,str(f)]); break
        base,brhs=pivots[p]
        for n,v in base.items():
            row[n]=row.get(n,0)-f*v
            if not row[n]: del row[n]
        rhs=[a-f*b for a,b in zip(rhs,brhs)]
    else:
        if any(rhs): inconsistent.append([447-row_number,list(map(str,rhs))])
check('rank_and_nullity', len(pivots)==saved['rank']==255 and 360-len(pivots)==saved['free_dimension_per_su_coordinate']==105)
check('all_affine_rhs_consistent', not inconsistent and saved['nonzero_residual_conditions']==[])
check('witness_statistics', int(np.count_nonzero(X))==218 and int(np.count_nonzero(np.any(X!=0,axis=(1,2))))==136 and max(map(abs,X.flat))==8)
failures=[k for k,v in checks.items() if not v]
out={'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'method':'Independent quaternion multiplication; full saved witness; Python object integers; reverse-row reverse-column Fraction elimination',
     'checks':checks,'failures':failures,'residuals':residuals,
     'rank':len(pivots),'required_rank':255,'nullity':360-len(pivots),'required_nullity':105,
     'reverse_pivot_log':pivot_log,'inconsistent_rows':inconsistent,
     'retained_base_parameters':10,'affine_columns':33,
     'witness_nonzero_scalars':int(np.count_nonzero(X)),
     'witness_max_abs':int(max(map(abs,X.flat))),
     'V_max_abs_by_affine_column':[int(max(map(abs,V[:,:,:,:,c,h].flat))) for c in range(3) for h in range(11)],
     'energy':energy,'required_energy':-32,'mixed_norm_squared':norm,'required_mixed_norm_squared':8,
     'verdict':'VERIFIED necessary uniform compatibility' if not failures else 'FAILED audit',
     'limitations':'No SU(2) jet sufficiency, connection, global F, cycle or transport.'}
path=ROOT/'fixed_tuple_audit_certificate.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(f'Checks {sum(checks.values())}/{len(checks)}; failures {failures}')
print(f'Rank {len(pivots)}/255 required; nullity {360-len(pivots)}/105 required; inconsistent rows {len(inconsistent)}')
print(f'Base parameters 10/10; affine columns 33/33; energy {energy}/-32; norm {norm}/8')
print(f'Certificate: {path}')
raise SystemExit(bool(failures))
