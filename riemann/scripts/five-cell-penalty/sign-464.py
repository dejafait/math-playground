"""Untrusted Decimal congruence proposal, followed by a directed check."""
import hashlib
import json
import runpy
from decimal import Decimal, localcontext
from pathlib import Path
HERE=Path(__file__).resolve().parent
path=HERE/'refined-464.json'
out=json.loads(path.read_text())
lib=runpy.run_path(str(HERE/'certify-455.py'))
I,UP=(lib[k] for k in ('I','UP'))
D=64
M=[[I(x['lo'],x['hi']) for x in row] for row in out['complete_matrix']]
with localcontext() as ctx:
    ctx.prec=100
    C=[[(x.lo+x.hi)/2 for x in row] for row in M]
    L=[[Decimal(0) for _ in range(D)] for _ in range(D)]
    for j in range(D):
        p=C[j][j]-sum(L[j][k]**2 for k in range(j))
        if p<=0:
            out['status']='INCONCLUSIVE'
            out['failures']=['point Cholesky proposal failed at '+str(j)]
            path.write_text(json.dumps(out,indent=2)+'\n')
            print(out['status'],out['failures'])
            raise SystemExit(0)
        L[j][j]=p.sqrt()
        for i in range(j+1,D):
            L[i][j]=(C[i][j]-sum(L[i][k]*L[j][k] for k in range(j)))/L[j][j]
    B=[[Decimal(0) for _ in range(D)] for _ in range(D)]
    for i in range(D):
        B[i][i]=1/L[i][i]
        for j in range(i):
            B[i][j]=-sum(L[i][k]*B[k][j] for k in range(j,i))/L[i][i]
    B=[[I(format(x,'.64E')) if s<=r else I(0) for s,x in enumerate(row)] for r,row in enumerate(B)]
print('Untrusted congruence proposed. Checking every residual entry.',flush=True)
BM=[[sum((B[r][k]*M[k][s] for k in range(r+1)),I(0)) for s in range(D)] for r in range(D)]
residual=[[I(0) for _ in range(D)] for _ in range(D)]
for r in range(D):
    for s in range(r,D):
        x=sum((BM[r][k]*B[s][k] for k in range(s+1)),I(0))-(1 if r==s else 0)
        residual[r][s]=x
        residual[s][r]=x
rows=[sum((I(max(x.lo.copy_abs(),x.hi.copy_abs())) for x in row),I(0)) for row in residual]
bound=max(x.hi for x in rows)
assert all(B[r][r].lo>0 for r in range(D))
jm=lambda m:[[x.json() for x in row] for row in m]
out['congruence']={'B':jm(B),'residual':jm(residual),'row_bounds':[x.json() for x in rows],
                   'norm_upper':str(bound),'required':'strictly below 1; B triangular with nonzero diagonal'}
out['status']='CERTIFIED_POSITIVE_COMPLETE_COMPRESSION' if bound<1 else 'INCONCLUSIVE'
out['failures']=[] if bound<1 else ['congruence residual norm bound >= 1']
out['sign_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
path.write_text(json.dumps(out,indent=2)+'\n')
print('Result:',out['status'],'; residual norm upper',bound,'; required < 1')
print('Failures:',out['failures'],'; full certificate:',path)
