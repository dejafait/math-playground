#!/usr/bin/env python3
"""Exact outward fixed-point certificate for the finite-lattice contour bound.

No floating-point value is a premise. Every elementary operation rounds
outward on 2^-72 intervals; square roots use integer isqrt; logarithms,
pi and trigonometric values use series with explicit remainder bounds.
The JSON contains all terminal derivative boxes and angular rate rows.
"""
import argparse
import json
import math
from pathlib import Path

S = 1 << 72

def ceildiv(a, b):
    return -((-a) // b)

class I:
    __slots__ = ('lo', 'hi')
    def __init__(self, lo, hi=None):
        self.lo, self.hi = lo, lo if hi is None else hi
        assert self.lo <= self.hi
    def __add__(a, b):
        if isinstance(b, int): b = rat(b)
        return I(a.lo + b.lo, a.hi + b.hi)
    __radd__ = __add__
    def __neg__(a): return I(-a.hi, -a.lo)
    def __sub__(a, b): return a + (-b if isinstance(b, I) else -rat(b))
    def __rsub__(a, b): return rat(b) - a
    def __mul__(a, b):
        if isinstance(b, int): b = rat(b)
        vals = (a.lo*b.lo, a.lo*b.hi, a.hi*b.lo, a.hi*b.hi)
        return I(min(vals)//S, ceildiv(max(vals), S))
    __rmul__ = __mul__
    def __truediv__(a, b):
        if isinstance(b, int): b = rat(b)
        assert b.lo > 0 or b.hi < 0, (b.lo, b.hi)
        if b.hi < 0: return (-a)/(-b)
        nums = (a.lo*S, a.hi*S)
        ds = (b.lo, b.hi)
        return I(min(v//d for v in nums for d in ds),
                 max(ceildiv(v, d) for v in nums for d in ds))
    def sq(a):
        if a.lo >= 0: return I(a.lo*a.lo//S, ceildiv(a.hi*a.hi,S))
        if a.hi <= 0: return (-a).sq()
        return I(0, ceildiv(max(a.lo*a.lo,a.hi*a.hi),S))
    def sqrt(a):
        assert a.lo >= 0
        lo, hi = math.isqrt(a.lo*S), math.isqrt(a.hi*S)
        return I(lo, hi + (hi*hi < a.hi*S))
    def dump(a): return [str(a.lo), str(a.hi)]

def rat(a, b=1):
    return I((a*S)//b, ceildiv(a*S,b))

def hull(a,b): return I(min(a.lo,b.lo),max(a.hi,b.hi))

def artanh_series(z, count=24):
    assert 0 <= z.lo <= z.hi < S
    z2=z.sq(); term=z; total=rat(0)
    for k in range(count):
        total=total+term/(2*k+1)
        term=term*z2
    tail=term/((2*count+1)*(1-z2))
    return I(total.lo, (total+tail).hi)*2

LN2=artanh_series(rat(1,3))

def log_point(v):
    assert v > 0
    k=v.bit_length()-S.bit_length()
    den=S*(1<<k) if k>=0 else S//(1<<(-k))
    assert den <= v < 2*den
    z=rat(v-den,v+den)
    return artanh_series(z)+LN2*k

def log_hi(v): return log_point(v.hi).hi

def atan_recip(d, count):
    z=rat(1,d); z2=z.sq(); term=z; total=rat(0)
    for k in range(count):
        total=total+(term/(2*k+1) if k%2==0 else -term/(2*k+1))
        term=term*z2
    err=term/(2*count+1)
    return I(total.lo-err.hi,total.hi+err.hi)

PI=16*atan_recip(5,32)-4*atan_recip(239,12)
TRIG={}

def trig(j,n):
    # Exact angle j*pi/n, 0<=j<=n, using reflection about pi/2.
    key=(j,n)
    if key in TRIG: return TRIG[key]
    if 2*j>n:
        c,s=trig(n-j,n); ans=(-c,s)
    else:
        z=PI*rat(j,n); z2=z.sq()
        ct=rat(1); st=z; c=ct; s=st
        for k in range(1,20):
            ct=-(ct*z2)/((2*k-1)*(2*k))
            st=-(st*z2)/((2*k)*(2*k+1))
            c=c+ct; s=s+st
        # For |z|<=pi/2, both omitted Taylor remainders are <10^-35.
        eps=rat(1,10**35).hi
        ans=(I(c.lo-eps,c.hi+eps),I(s.lo-eps,s.hi+eps))
    TRIG[key]=ans
    return ans

def trig_box(j,k,n):
    ca,sa=trig(j,n); cb,sb=trig(k,n)
    c=I(cb.lo,ca.hi)
    s=hull(sa,sb)
    if 2*j<=n<=2*k: s=I(s.lo,S)
    return c,s

D=rat(5,4); R=rat(11,8); U=R.sq(); Y=rat(9,20)
E0=rat(117,100); LAMBDA=PI*rat(20,27)

def derivative_integral(e,c,s,y,nt):
    total=rat(0)
    for j in range(nt):
        t=hull(rat(j,nt),rat(j+1,nt))
        a=e+t*c; b=y-t*s
        cc=U*c+e*t; dd=U*s-t*y
        g= -a/(a.sq()+b.sq()) + t*cc/(cc.sq()+dd.sq())
        total=total+g
    return total/nt

def certify_derivatives():
    leaves=[]; failures=[]
    for region,el,er,threshold in [('top',D,R,rat(-3,10)),
                                  ('bottom',E0,D,rat(-9,4))]:
        for sign in [-1,1]:
            # Dyadic coordinates for e and theta. Refine only unproved boxes.
            stack=[(j,j+1,16,k,k+1,128,256,0)
                   for j in range(16) for k in range(128)]
            while stack:
                j,jj,ne,k,kk,na,nt,depth=stack.pop()
                e=hull(el+(er-el)*rat(j,ne),el+(er-el)*rat(jj,ne))
                c,s=trig_box(k,kk,na)
                val=derivative_integral(e,c,s,sign*Y,nt)
                ok=(val.hi<=threshold.lo if region=='top'
                    else val.lo>=threshold.hi)
                if ok:
                    leaves.append({'region':region,'sign':sign,
                         'e_cell':[j,jj,ne],'theta_cell':[k,kk,na],
                         't_cells':nt,'integral_interval':val.dump()})
                elif depth>=9:
                    failures.append({'region':region,'sign':sign,
                         'e_cell':[j,jj,ne],'theta_cell':[k,kk,na],
                         't_cells':nt,'integral_interval':val.dump()})
                elif depth%3==2:
                    stack.append((j,jj,ne,k,kk,na,nt*2,depth+1))
                elif depth%3==0:
                    stack.extend([(j,jj,ne,2*k,k+kk,2*na,nt,depth+1),
                                  (j,jj,ne,k+kk,2*kk,2*na,nt,depth+1)])
                else:
                    stack.extend([(2*j,j+jj,2*ne,k,kk,na,nt,depth+1),
                                  (j+jj,2*jj,2*ne,k,kk,na,nt,depth+1)])
    return leaves,failures

def anchor_ratio(t,c):
    n=D.sq()+t.sq()+2*D*t*c
    den=U.sq()+D.sq()*t.sq()+2*U*D*t*c
    return n/den

def horizontal_bottom(t,c,s):
    e=E0
    disc=(2*e*t+(U+t.sq())*c).sq()+(U-t.sq()).sq()*s.sq()
    amp=anchor_ratio(t,c).sqrt()*(disc.sqrt()+U-t.sq())/(2*(e+t*c))
    return log_hi(amp)

def endpoint(t,c,s,y):
    den=D.sq()+y.sq()+t.sq()+2*D*t*c-2*y*t*s
    num=U.sq()+t.sq()*(D.sq()+y.sq())+2*U*D*t*c-2*U*t*y*s
    return ceildiv(log_hi(anchor_ratio(t,c)*num/den),2)

def certify_angular_rates(na=512,nt=128):
    # A lower bound -70 for each second t derivative makes trapezoids
    # upper bounds with error 70/(12 nt^2), even for a factorwise maximum.
    et=rat(70,12*nt*nt).hi
    beta=ceildiv(log_hi((U+Y.sq())/U),6)
    rows=[]
    for k in range(na+1):
        c,s=trig(k,na); sums=[0,0,0,0]
        for j in range(nt+1):
            t=rat(j,nt); weight=1 if j in (0,nt) else 2
            vals=[ceildiv(log_hi(U*anchor_ratio(t,c)),2),
                  horizontal_bottom(t,c,s),endpoint(t,c,s,Y),
                  endpoint(t,c,s,-Y)]
            sums=[a+weight*b for a,b in zip(sums,vals)]
        bounds=[ceildiv(z,2*nt)+et for z in sums]
        bounds[0]+=beta
        bounds[1]-=(LAMBDA*rat(2,25)).lo
        rows.append({'angle':[k,na], 'rate_uppers':list(map(str,bounds)),
                     'maximum_upper':str(max(bounds))})
    trapezoid=ceildiv(sum((1 if k in (0,na) else 2)*
                           int(row['maximum_upper']) for k,row in enumerate(rows)),2*na)
    ea=(100*PI.sq()/rat(12*na*na)).hi
    return rows,{'t_error_upper':str(et),'angular_error_upper':str(ea),
                 'top_spatial_cost_upper':str(beta),
                 'mean_upper':str(trapezoid+ea),
                 'required_upper':str(rat(-33,1000).lo)}

def global_bounds():
    # A=29/20 strictly bounds every |a| in the rectangle.
    A=rat(29,20)
    b1=rat(1)/(D-1)
    b1=b1+rat(1)/(E0-1)+A/(U-A)+D/(U-D)
    bt2=rat(1)/(D-1).sq()+rat(1)/(E0-1).sq()+A.sq()/(U-A).sq()+D.sq()/(U-D).sq()
    ba2=D/(D-1).sq()+A/(E0-1).sq()+U*A/(U-A).sq()+U*D/(U-D).sq()
    checks={
      'rectangle_radius':(U+Y.sq()).hi<A.sq().lo,
      'first_t_derivative_16':b1.hi<rat(16).lo,
      'second_t_derivative_70':bt2.hi<rat(70).lo,
      'second_angle_derivative_100':ba2.hi<rat(100).lo,
      'lambda_above_9_4':LAMBDA.lo>rat(9,4).hi,
      'top_spatial_derivative_below_3_10':rat(4,15).hi<rat(3,10).lo,
      'kernel_for_n_ge_5':(LAMBDA*5*rat(2,25)).lo>LN2.hi,
      'admissible_radius':(D.sq()+Y.sq()).hi<rat(273,200).sq().lo,
      'pi_trig_remainder':PI.hi<rat(22,7).lo,
    }
    # (pi/2)^40/40! < (11/7)^40/40! < 10^-35, with exact integers.
    checks['trig_remainder_exact']=(11**40*10**35 < 7**40*math.factorial(40))
    return {'checks':checks,'first_t_bound':b1.dump(),
            'second_t_bound':bt2.dump(),'second_angle_bound':ba2.dump(),
            'pi_interval':PI.dump(),'log2_interval':LN2.dump(),
            'lambda_interval':LAMBDA.dump()}

def inspect_certificate(path):
    """Inspect every stored terminal value and the complete domain cover.

    This validates the certificate's aggregation/coverage, not an
    independent replay of each interval operation in its producer.
    """
    from fractions import Fraction
    o=json.loads(path.read_text()); failures=[]; extrema={}
    def check(ok,label):
        if not ok: failures.append(label)
    check(o['status']=='PASS','producer_status')
    check(int(o['scale'])==S,'scale')
    check(o['global_bounds']==global_bounds(),'global_arithmetic_replay')
    check(not o['failures'] and not o['derivative_failures'],'producer_failures')
    expected={(j,k) for j in range(16) for k in range(128)}
    for region in ['top','bottom']:
        for sign in [-1,1]:
            leaves=[v for v in o['derivative_leaves'] if v['region']==region and v['sign']==sign]
            cells=[]; vals=[]
            for v in leaves:
                j,jj,ne=v['e_cell'];k,kk,na=v['theta_cell']
                check((jj,ne,kk,na,v['t_cells'])==(j+1,16,k+1,128,256),
                      f'noncanonical_leaf_{region}_{sign}_{j}_{k}')
                lo,hi=map(int,v['integral_interval']);vals.append((lo,hi));cells.append((j,k))
                check(lo<=hi,'interval_order')
                check(10*hi<=-3*S if region=='top' else 4*lo>=-9*S,
                      f'derivative_threshold_{region}_{sign}_{j}_{k}')
            check(len(cells)==len(expected) and set(cells)==expected,
                  f'full_disjoint_cover_{region}_{sign}')
            extrema[f'{region}_{sign}']=[str(min(v[0] for v in vals)),str(max(v[1] for v in vals))]
    rows=o['angular_rows'];check(len(rows)==513,'angular_count')
    weighted=0
    for k,row in enumerate(rows):
        check(row['angle']==[k,512],'angular_grid')
        vals=list(map(int,row['rate_uppers']));check(len(vals)==4,'four_edges')
        check(int(row['maximum_upper'])==max(vals),'maximum_retains_every_edge')
        weighted+=(1 if k in (0,512) else 2)*max(vals)
    cp=o['comparison']
    check(int(cp['t_error_upper'])==rat(70,12*128*128).hi,'t_error')
    check(int(cp['angular_error_upper'])==(100*PI.sq()/rat(12*512*512)).hi,'angle_error')
    total=ceildiv(weighted,1024)+int(cp['angular_error_upper'])
    check(total==int(cp['mean_upper']),'full_mean_aggregation')
    check(1000*total<=-33*S,'mean_rate_threshold')
    audit={'status':'PASS' if not failures else 'FAIL','scale':str(S),
           'derivative_values_inspected':len(o['derivative_leaves']),
           'angular_rows_inspected':len(rows),'derivative_extrema':extrema,
           'comparison':cp,'failures':failures,
           'scope':'All terminal values, complete disjoint grid covers and exact aggregation; no independent analytic audit or interval-operation replay.'}
    dest=path.with_name('full-circle-root-compensation-inspection.json')
    dest.write_text(json.dumps(audit,indent=2)+'\n')
    print('Full certificate inspection:',audit['status'],len(o['derivative_leaves']),'derivative boxes;',len(rows),'angular rows')
    print('Actual mean upper:',str(Fraction(total,S)),'required <= -33/1000')
    print('Failures:',failures,'; inspection:',dest)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--derivatives-only',action='store_true')
    ap.add_argument('--inspect-certificate',action='store_true')
    args=ap.parse_args()
    path=Path(__file__).with_name('full-circle-root-compensation-certificate.json')
    if args.inspect_certificate:
        inspect_certificate(path)
        return
    out={'schema':'fixed_point_contour_v1','scale':str(S),
         'status':'INCOMPLETE','global_bounds':global_bounds()}
    path.write_text(json.dumps(out,indent=2)+'\n')
    leaves,failures=certify_derivatives()
    out['derivative_leaves']=leaves;out['derivative_failures']=failures
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('Derivative boxes:',len(leaves),'failures:',len(failures),flush=True)
    if not args.derivatives_only:
        rows,comparison=certify_angular_rates()
        out['angular_rows']=rows;out['comparison']=comparison
        out['failures']=[k for k,v in out['global_bounds']['checks'].items() if not v]
        out['failures']+=['derivative_bound'] if failures else []
        if int(comparison['mean_upper'])>int(comparison['required_upper']):
            out['failures'].append('mean_rate')
        out['status']='PASS' if not out['failures'] else 'FAIL'
        print('Mean upper:',int(comparison['mean_upper'])/S,
              'required <=',int(comparison['required_upper'])/S,flush=True)
        print('Failures:',out['failures'],flush=True)
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('Full certificate:',path,flush=True)

if __name__=='__main__': main()
