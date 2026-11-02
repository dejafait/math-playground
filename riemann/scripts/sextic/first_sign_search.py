"""Exploration only: no floating-point sample certifies a sign."""
import json, math
from pathlib import Path
n=8192
h=3/n
us=[i*h for i in range(n+1)]
bs=[0.25,0.5,1,2,4,8,12,16]
rows=[]
for b in bs:
    ws=[(1 if i in (0,n) else 4 if i%2 else 2)*math.exp(-u**6-b*u*u)*2*h/3 for i,u in enumerate(us)]
    for x in range(2,65,2):
        f=math.fsum(w*math.cos(x*u) for w,u in zip(ws,us))
        fp=-math.fsum(w*u*math.sin(x*u) for w,u in zip(ws,us))
        fpp=-math.fsum(w*u*u*math.cos(x*u) for w,u in zip(ws,us))
        d=fp*fp-f*fpp
        rows.append(dict(b=b,x=x,F=f,Fp=fp,Fpp=fpp,D=d))
cert=dict(kind='UNCERTIFIED_EXPLORATION',rectangle={'b':[0,16],'x':[-64,64]},method='composite Simpson, [0,3], N=8192; no error certification',evaluations=len(rows),cap=256,rows=rows)
p=Path('scripts/sextic/first-sign-exploration.json')
p.write_text(json.dumps(cert,indent=2)+'\n')
negative=sorted([r for r in rows if r['D']<0],key=lambda r:r['D'])
print(json.dumps(dict(evaluations=len(rows),cap=256,negative_samples=len(negative),most_negative=negative[:5],path=str(p)),indent=2))
