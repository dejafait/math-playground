"""Floating nomination only; the JSON is not a sign certificate."""
from decimal import Decimal as D, localcontext
from math import factorial, exp
from pathlib import Path
import json


def response():
    with localcontext() as ctx:
        ctx.prec = 85
        # Diagnostic midpoint only. Certification must retain the whole bracket.
        root = (D('0.0000530387415958154365906397391693872935932598188')
                + D('0.00005303874159581543659063973916938729359325981881'))/2
        raw = list(map(D, ['0.497123021571', '0.022972233662',
            '0.002962906960', '0.000599311666', '0.000160971754',
            str(root), '0.000020475993']))
        q = [(-1)**j*x/raw[0]/D(factorial(2*j)) for j,x in enumerate(raw)]
        s = [D(0)]
        for n in range(1,7):
            s.append(-n*q[n]-sum((s[k]*q[n-k] for k in range(1,n)), D(0)))
        delta = s[2]*s[4]-s[3]**2
        p = (s[3]*s[5]-s[4]**2)/delta
        r = (s[3]*s[4]-s[2]*s[5])/delta
        v = [p,r,D(1)]
        b = {n:sum((v[i]*v[j] for i in range(3) for j in range(3)
                    if i+j==n-2),D(0)) for n in range(2,7)}
        inv=[D(1)]
        for n in range(1,7):
            inv.append(-sum((q[j]*inv[n-j] for j in range(1,n+1)),D(0)))
        R=[-sum((n*b[n]*inv[n-j]*(-1)**j/D(factorial(2*j))
                 for n in range(max(2,j),7)),D(0)) for j in range(7)]
        return dict(root=str(root),p=str(p),r=str(r),R=list(map(str,R)))


class LP:
    """Small dense simplex: max c*x, A*x<=b, x>=0. Float diagnostic."""
    EPS=1e-11
    def __init__(self,A,b,c):
        self.m,self.n=len(b),len(c)
        m,n=self.m,self.n
        self.B=[n+i for i in range(m)]
        self.N=list(range(n))+[-1]
        self.T=[[0.]*(n+2) for _ in range(m+2)]
        for i in range(m):
            self.T[i][:n]=A[i][:]
            self.T[i][n]=-1.
            self.T[i][n+1]=b[i]
        for j in range(n):self.T[m][j]=-c[j]
        self.T[m+1][n]=1.
    def pivot(self,r,s):
        T,m,n=self.T,self.m,self.n
        z=1./T[r][s]
        for i in range(m+2):
            if i==r:continue
            for j in range(n+2):
                if j!=s:T[i][j]-=T[r][j]*T[i][s]*z
        for j in range(n+2):
            if j!=s:T[r][j]*=z
        for i in range(m+2):
            if i!=r:T[i][s]*=-z
        T[r][s]=z
        self.B[r],self.N[s]=self.N[s],self.B[r]
    def phase(self,k):
        T,m,n=self.T,self.m,self.n
        row=m+1 if k==1 else m
        for _ in range(20000):
            allowed=[j for j in range(n+1) if not(k==2 and self.N[j]==-1)]
            improving=[j for j in allowed if T[row][j]<-self.EPS]
            if not improving:return True
            s=min(improving,key=lambda j:self.N[j])
            allowed=[i for i in range(m) if T[i][s]>self.EPS]
            if not allowed:return False
            least=min(T[i][n+1]/T[i][s] for i in allowed)
            r=min((i for i in allowed if T[i][n+1]/T[i][s]<=least+self.EPS),
                  key=lambda i:self.B[i])
            self.pivot(r,s)
        raise RuntimeError('Diagnostic simplex iteration budget')
    def solve(self):
        T,m,n=self.T,self.m,self.n
        r=min(range(m),key=lambda i:T[i][n+1])
        if T[r][n+1]<-self.EPS:
            self.pivot(r,n)
            if not self.phase(1) or T[m+1][n+1]<-self.EPS:
                return 'infeasible',None,None
            if abs(T[m+1][n+1])>self.EPS:return 'infeasible',None,None
            if -1 in self.B:
                r=self.B.index(-1)
                s=min(range(n+1),key=lambda j:(T[r][j],self.N[j]))
                self.pivot(r,s)
        if not self.phase(2):return 'unbounded',None,None
        x=[0.]*n
        for i in range(m):
            if self.B[i]<n:x[self.B[i]]=T[i][n+1]
        return 'optimal',T[m][n+1],x


def score(u):
    v=3.141592653589793*exp(2*u)
    # Factored first term; finite terms are diagnostic, never a full-score bound.
    a=b=0.
    for n in range(1,8):
        z=v*n*n
        w=z*(2*z-3)*exp(-(n*n-1)*v)
        a+=w
        b+=w*(4.5+6/(2*z-3)-2*z)
    return b/a


def main():
    data=response()
    R=list(map(float,data['R']))
    points=[i/200 for i in range(401)]
    columns=[];f=[]
    for u in points:
        h=score(u)
        rv=sum(R[j]*u**(2*j) for j in range(7))
        dr=sum(2*j*R[j]*u**(2*j) for j in range(1,7))
        row=[(2*j+1)*u**(2*j)+(u/5120+h)*u**(2*j+1)
             for j in range(6)]+[1e8*rv,1e8*dr]
        norm=max(1.,max(map(abs,row)))
        columns.append([x/norm for x in row])
        f.append(1e8*u*h*rv/norm)
    # Nonnegative point masses annihilating all eight correction columns.
    A=[];b=[]
    for j in range(8):
        row=[x[j] for x in columns]
        A.extend([row,[-t for t in row]]);b.extend([1e-10,1e-10])
    A.append([1.]*len(points));b.append(1.)
    status,opt,w=LP(A,b,[-t for t in f]).solve()
    support=[]
    if w:
        support=[dict(u=points[i],weight=t) for i,t in enumerate(w) if t>1e-9]
    out=dict(scope='FLOAT DIAGNOSTIC ONLY: fixed approved witness/lambda/class',
             response=data,status=status,objective=opt,support=support,
             maximum_column_residual=max(abs(sum(wi*col[j] for wi,col in zip(w,columns)))
                                          for j in range(8)) if w else None,
             rigorous=False)
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status=status,objective=opt,support_count=len(support),
                         required='positive objective plus rigorous coefficient separation',
                         residual=out['maximum_column_residual'],certificate=False,
                         path=str(path)),indent=2))


if __name__=='__main__':main()
