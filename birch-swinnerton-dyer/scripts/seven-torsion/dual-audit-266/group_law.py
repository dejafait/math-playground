"""Exact Jacobian chain in Q[X,Y]/(Y^2-c), independent of recurrences."""
from fractions import Fraction
import json

def run(root):
    def trim(p):
        while p and p[-1]==0:p.pop()
        return p
    def add(p,q,s=1):
        r=p.copy()+[0]*max(0,len(q)-len(p))
        for i,v in enumerate(q):r[i]+=s*v
        return trim(r)
    def mul(p,q):
        r=[0]*max(0,len(p)+len(q)-1)
        for i,a in enumerate(p):
            if a:
                for j,b in enumerate(q):
                    if b:r[i+j]+=a*b
        return trim(r)
    cub=[46224,-3024,0,1]
    def plus(p,q,s=1):return (add(p[0],q[0],s),add(p[1],q[1],s))
    def times(p,q):
        return (add(mul(p[0],q[0]),mul(cub,mul(p[1],q[1]))),add(mul(p[0],q[1]),mul(p[1],q[0])))
    def scale(p,c):return (trim([c*v for v in p[0]]),trim([c*v for v in p[1]]))
    def power(p,n):
        r=([1],[])
        for _ in range(n):r=times(r,p)
        return r
    def nonzero(p):return bool(p[0] or p[1])
    checks=[];steps=[]
    def need(ok,label):
        if not ok:raise ValueError(label)
        checks.append(label)
    def double(p,label):
        x,y,z=p
        need(nonzero(y) and nonzero(z),label+'_tangent_denominator_nonzero')
        yy=power(y,2)
        s=scale(times(x,yy),4)
        m=plus(scale(power(x,2),3),scale(power(z,4),-3024))
        xx=plus(power(m,2),scale(s,2),-1)
        yynew=plus(times(m,plus(s,xx,-1)),scale(power(yy,2),8),-1)
        zz=scale(times(y,z),2)
        return (xx,yynew,zz)
    def addition(p,q,label):
        x1,y1,z1=p;x2,y2,z2=q
        u1=times(x1,power(z2,2));u2=times(x2,power(z1,2))
        s1=times(y1,power(z2,3));s2=times(y2,power(z1,3))
        h=plus(u2,u1,-1);r=plus(s2,s1,-1)
        need(nonzero(h) and nonzero(z1) and nonzero(z2),label+'_secant_denominator_nonzero')
        hh=power(h,2);hhh=times(h,hh);v=times(u1,hh)
        xx=plus(plus(power(r,2),hhh,-1),scale(v,2),-1)
        yy=plus(times(r,plus(v,xx,-1)),times(s1,hhh),-1)
        zz=times(h,times(z1,z2))
        steps.append({'operation':label,'H':h,'slope_numerator':r})
        return (xx,yy,zz)
    p=([0,1],[]),([],[1]),([1],[])
    points={1:p}
    points[2]=double(p,'double_1')
    points[3]=addition(points[2],p,'add_2_1')
    points[6]=double(points[3],'double_3')
    points[7]=addition(points[6],p,'add_6_1')
    for n,point in points.items():need(nonzero(point[2]),'nonzero_Z_'+str(n))
    comp=json.loads((root/'replay/dual_after_quotient.json').read_text())
    def entire_D_scalar(name):
        values=[]
        for row in comp[name]:
            f=list(map(Fraction,row))
            need(all(v==0 for v in f[1:]),name+'_all_nonconstant_D_coordinates_zero')
            a=f[0] if f else Fraction(0)
            need(a.denominator==1,name+'_integer_coefficient')
            values.append(a.numerator)
        return (trim(values),[])
    d=entire_D_scalar('composition_denominator_root')
    nx=entire_D_scalar('composition_x_numerator')
    ny=entire_D_scalar('composition_y_multiplier_numerator')
    need(nonzero(d),'composition_denominator_nonzero')
    xx,yy,zz=points[7]
    rx=plus(times(xx,power(d,2)),times(nx,power(zz,2)),-1)
    ry=plus(times(yy,power(d,3)),times(times(([],[1]),ny),power(zz,3)),-1)
    need(not nonzero(rx),'group_law_full_x_composition')
    need(not nonzero(ry),'group_law_full_y_composition')
    result={'passed':True,'failures':[],'checks':checks,'ring':'Q[X,Y]/(Y^2-X^3+3024X-46224), embedded in full D',
            'chain':[1,2,3,6,7],'points':points,'secant_witnesses':steps,
            'composition':{'denominator':d,'x_numerator':nx,'y_multiplier_numerator':ny},
            'residuals':{'x':rx,'y':ry},
            'second_order':'(Phi F)Phi=Phi[7]=[7]Phi; dominant Phi gives Phi F=[7]; direct full-D second replay also retained'}
    (root/'group-law.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
    return {'checks':len(checks),'residuals':{'x':rx,'y':ry},'chain':[1,2,3,6,7]}
