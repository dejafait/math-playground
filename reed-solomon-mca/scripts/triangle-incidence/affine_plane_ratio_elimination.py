"""Exact seed-free necessary minors for L077's V0 equations (F_97)."""
import json
from itertools import combinations, permutations
from pathlib import Path
P=97
N=4
ZERO={}
def const(n): return {(0,)*N:n%P} if n%P else {}
def var(i): return {tuple(int(j==i) for j in range(N)):1}
def add(a,b):
 c=a.copy()
 for m,v in b.items():
  c[m]=(c.get(m,0)+v)%P
  if not c[m]: del c[m]
 return c
def neg(a):return {m:-v%P for m,v in a.items()}
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 c={}
 for m,u in a.items():
  for n,v in b.items():
   k=tuple(x+y for x,y in zip(m,n));c[k]=(c.get(k,0)+u*v)%P
 return {k:v for k,v in c.items() if v}
def prod(*xs):
 out=const(1)
 for x in xs:out=mul(out,x)
 return out
def det(rows):
 out={};n=len(rows)
 for perm in permutations(range(n)):
  parity=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))%2
  term=prod(*(rows[i][perm[i]] for i in range(n)))
  out=add(out,neg(term) if parity else term)
 return out
def evaluate(poly,point):
 return sum(v*__import__('functools').reduce(lambda x,y:x*y%P,
              (pow(x,d,P) for x,d in zip(point,m)),1) for m,v in poly.items())%P
A,B,C,D=(var(i) for i in range(4));one=const(1)
M=[
 [prod(A,B),neg(prod(B,D)),prod(sub(one,D),sub(one,B),C),neg(sub(one,D))],
 [prod(sub(one,C),A),prod(C,B,D),neg(prod(C,sub(D,one))),const(-1)],
 [A,prod(D,sub(one,A),B),neg(prod(A,sub(one,D),C)),neg(D)],
 [sub(prod(A,A,sub(one,C)),prod(A,C,sub(B,one))),ZERO,
  prod(C,sub(prod(B,sub(A,one)),prod(C,sub(one,B)))),sub(C,A)],
 [ZERO,sub(prod(B,B,sub(one,A)),prod(A,B,sub(C,one))),
  sub(prod(B,C,sub(A,one)),prod(C,C,sub(one,B))),sub(C,B)],
]
minors=[(list(ix),det([M[i] for i in ix])) for ix in combinations(range(5),4)]
U=sub(sub(add(A,B),prod(A,B)),prod(A,C))
V=sub(add(A,C),add(prod(A,C),prod(B,C)))
R=add(prod(sub(U,prod(D,V)),sub(U,prod(D,V))),
      prod(const(4),B,C,D,sub(one,A),sub(one,B)))
factors=[prod(A,B,C,D),prod(A,B,C),prod(A,B,C,sub(one,B)),
         prod(A,B,C,sub(one,A)),prod(A,B,C,sub(one,C))]
identities=[{'rows':ix,'difference':encode_diff}
            for (ix,p),f in zip(minors,factors)
            for encode_diff in [sub(p,prod(f,R))]]
failures=[f'nonzero identity difference for rows {i["rows"]}'
          for i in identities if i['difference']]
encode=lambda p:[{'powers':list(m),'coefficient':v} for m,v in sorted(p.items())]
def rank(matrix):
    matrix=[r.copy() for r in matrix];n=0
    for c in range(len(matrix[0])):
        pivot=next((r for r in range(n,len(matrix)) if matrix[r][c]%P),None)
        if pivot is None: continue
        matrix[n],matrix[pivot]=matrix[pivot],matrix[n]
        matrix[n]=[x*pow(matrix[n][c],-1,P)%P for x in matrix[n]]
        for r in range(len(matrix)):
            if r!=n:
                scale=matrix[r][c]
                matrix[r]=[(x-scale*y)%P for x,y in zip(matrix[r],matrix[n])]
        n+=1
        if n==len(matrix):break
    return n
# One explicit obstruction regression, not a labeling census or a sampling bound.
H=sorted(x for x in range(1,P) if pow(x,16,P)==1)
names=['a','b','y_1','y_2','c','d_1','d_2','d_3',
       'z_1','d_4','d_5','w_1','z_2','d_6','w_2','d_7']
labeling=dict(zip(names,H))
tuples=[['y_1','z_2','w_1','d_1'],['y_2','c','d_6','d_5'],
        ['b','z_1','d_2','d_7'],['a','d_4','d_3','w_2']]
def chi(names):
    a,b,c,d=[labeling[x] for x in names]
    return (c-a)*(d-b)*pow((d-a)*(c-b)%P,-1,P)%P
ratios=[chi(t) for t in tuples]
numeric_matrix=[[evaluate(p,ratios) for p in row] for row in M]
regression={'labeling':labeling,'ratio_tuples':tuples,'ratios':ratios,
            'R':evaluate(R,ratios),'augmented_matrix':numeric_matrix,
            'augmented_rank':rank(numeric_matrix)}
if regression['R']==0 or regression['augmented_rank']!=4:
    failures.append('explicit obstruction regression')
cert={'scope':'Necessary seed-free V0 cross-ratio conditions only; no H-labeling census',
      'variables':['A','B','C','D'],'matrix':[[encode(p) for p in row] for row in M],
      'minors':[{'rows':ix,'polynomial':encode(p),'degree_D':max((m[3] for m in p),default=-1)} for ix,p in minors],
      'R':encode(R),
      'identities':[{'rows':i['rows'],'factor':encode(f),
                     'difference':encode(i['difference'])}
                    for i,f in zip(identities,factors)],
      'explicit_obstruction':regression,
      'actual':{'exact_polynomial_identities':sum(not i['difference'] for i in identities),
                'explicit_obstruction_rank':regression['augmented_rank']},
      'required':{'exact_polynomial_identities':5,'explicit_obstruction_rank':4},
      'failures':failures}
path=Path(__file__).with_name('affine-plane-ratio-minors.json')
path.write_text(json.dumps(cert,indent=2)+'\n')
print(f'{"FAIL" if failures else "PASS"}: exact polynomial identities '
      f'{cert["actual"]["exact_polynomial_identities"]}/5; '
      f'one explicit obstruction rank {regression["augmented_rank"]}/4; '
      f'R={regression["R"]}, ratios={ratios}. No uniform labeling decision.')
print('Certificate:',path,'failures:',failures)
raise SystemExit(bool(failures))
