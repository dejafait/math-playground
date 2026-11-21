#!/usr/bin/env python3
"""Independent audit of the unchanged L936 witness, using exact remainders.

Does not import/run the producer. Uses polynomial extended Euclid for
inverses, cofactor determinants and Gaussian solves, rather than the
producer's quadratic conjugate inverses, permutation determinants and
Cramer's rule. All evidence and comparisons are written to disk.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from math import factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'scripts/heat/low-time-h2-uniform-195.json'
ORIGINAL = ROOT / 'scripts/heat/contact-s7-root-slice-39.json'
PRODUCER = ROOT / 'scripts/heat/contact-s7-root-slice-39.py'
OUTPUT = ROOT / 'scripts/heat/contact-s7-independent-audit-41.json'
checks, comparisons, divisions = {}, {}, []


def require(name, value):
    checks[name] = bool(value)
    if not value:
        save('FAILED', {'first_failure': name})
        raise AssertionError(name)


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p or [F(0)]


def add(p, q):
    return trim([(p[i] if i < len(p) else F(0))
                 + (q[i] if i < len(q) else F(0))
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    return trim([c*x for x in p])


def mul(p, q):
    out = [F(0)] * (len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, z in enumerate(q):
            out[i+j] += x*z
    return trim(out)


def divide(p, q):
    p, q = trim(p), trim(q)
    if q == [0]:
        raise ZeroDivisionError('polynomial division by zero')
    quot = [F(0)] * max(1, len(p)-len(q)+1)
    while p != [0] and len(p) >= len(q):
        k, c = len(p)-len(q), p[-1]/q[-1]
        quot[k] += c
        p = add(p, [F(0)]*k+scale(q, -c))
    return trim(quot), p


def evaluate(p, x):
    return sum((a*x**j for j, a in enumerate(p)), F(0))


def formal_log(q):
    """Explicit truncated log(1+h); coefficients are raw-X polynomials."""
    n = len(q)-1
    h = [[F(0)]] + q[1:]
    power = [[F(1)]] + [[F(0)] for _ in range(n)]
    log = [[F(0)] for _ in range(n+1)]
    for k in range(1, n+1):
        power = [sum_poly([mul(power[j], h[i-j]) for j in range(i+1)])
                 for i in range(n+1)]
        log = [add(z, scale(w, F((-1)**(k+1), k)))
               for z, w in zip(log, power)]
    return [scale(p, -j) for j, p in enumerate(log)]


def sum_poly(items):
    out = [F(0)]
    for p in items:
        out = add(out, p)
    return out


def encode(obj):
    if 'R' in globals() and isinstance(obj, R):
        return {'a': str(obj.p[0]), 'b': str(obj.p[1] if len(obj.p)>1 else F(0))}
    if isinstance(obj, F):
        return str(obj)
    if isinstance(obj, dict):
        return {str(k): encode(v) for k, v in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [encode(v) for v in obj]
    return obj


def save(result, data):
    cert = dict(result=result, checks=checks, comparisons=comparisons,
                failures=[k for k,v in checks.items() if not v],
                divisions=divisions, evidence=data)
    OUTPUT.write_text(json.dumps(encode(cert), indent=2)+'\n')


source_bytes, original_bytes = SOURCE.read_bytes(), ORIGINAL.read_bytes()
old = json.loads(original_bytes)
panel = json.loads(source_bytes)['panels'][0]
boxes = [(F(panel['moments'][str(2*j)]['lower']),
          F(panel['moments'][str(2*j)]['upper'])) for j in range(7)]
source_hash = sha256(source_bytes).hexdigest()
require('source_identity', source_hash == old['source']['sha256']
        == 'f0afdc26fd2463272ee7918073b5abed7e3170a64cbf8226bf16291820acc792')
require('complete_endpoint_strings_identical',
        panel['moments'] == old['source']['complete_moment_intervals'])
require('panel_lambda', F(panel['lambda']['lower']) == 0
        and F(panel['lambda']['upper']) == F(1,5120)
        and panel['lambda'] == old['source']['lambda_interval'])
fixed = [F(x) for x in ['0.497123021571', '0.022972233662',
         '0.002962906960', '0.000599311666', '0.000160971754',
         '0.000053040634', '0.000020475993']]
for j, (a,b) in enumerate(boxes):
    rounded = ((a+b)/2*10**12+F(1,2))//1
    require(f'fixed_rounding_{j}', fixed[j] == F(rounded,10**12))
require('positive_common_mass', fixed[0] > 0)
qformal = [[F((-1)**j, factorial(2*j))*fixed[j]/fixed[0]]
           if j != 5 else [F(0), -F(1,factorial(10))/fixed[0]]
           for j in range(7)]
sformal = formal_log(qformal)
delta_poly = add(mul(sformal[2],sformal[4]),scale(mul(sformal[3],sformal[3]),-1))
P = sum_poly([mul(delta_poly,sformal[6]),
              scale(mul(mul(sformal[4],sformal[4]),sformal[4]),-1),
              scale(mul(mul(sformal[3],sformal[4]),sformal[5]),2),
              scale(mul(sformal[2],mul(sformal[5],sformal[5])),-1)])
expected_integer = [-62771292108354521989752161390673854977603807286751227007139,
 2354209566613457384125275894062626786021779646664218000000000000,
 -22072745990611555673606165989356026991593537500000000000000000000000]
require('original_quadratic', len(P)==3 and P==list(map(F,old['root']['polynomial_low_to_high'])))
positive_scale = F(old['root']['positive_integer_polynomial_scale'])
require('integer_coefficients_positive_scaling', positive_scale>0
        and scale(P,positive_scale)==expected_integer
        and old['root']['integer_polynomial_low_to_high']==expected_integer)
lo = F('0.0000530387415958154365906397391693872935932598188')
hi = F('0.00005303874159581543659063973916938729359325981881')
require('unchanged_bracket', [lo,hi] == list(map(F,old['root']['final_bracket'])))
require('bracket_inside_complete_box', boxes[5][0] < lo < hi < boxes[5][1])
final_signs = [evaluate(P,lo),evaluate(P,hi)]
initial_signs = [evaluate(P,x) for x in boxes[5]]
require('strict_IVT_signs', final_signs[0]<0<final_signs[1])
require('initial_opposite_signs', initial_signs[0]<0<initial_signs[1])
require('exact_root_values', final_signs==list(map(F,old['root']['final_values']))
        and initial_signs==list(map(F,old['root']['initial_values'])))
require('original_initial_bracket', list(map(F,old['root']['initial_bracket']))==list(boxes[5]))
# Verify the original refinement record as well, without writing it back.
left,right=boxes[5]
for _ in range(old['root']['bisections']):
    mid=(left+right)/2
    z=evaluate(P,mid)
    if not z:
        left=right=mid
        break
    if z*evaluate(P,left)>0:
        left=mid
    else:
        right=mid
require('bisection_record', [left,right]==list(map(F,old['root']['bisected_bracket']))
        and lo<=left<=right<=hi and old['root']['bisections']==160)


class R:
    """Polynomial residue class; no irreducibility or field assumption."""
    def __init__(self, value=0):
        if isinstance(value,R):
            self.p=value.p
        else:
            self.p=divide(list(map(F,value)) if isinstance(value,list) else [F(value)],P)[1]
    def __add__(self, other): return R(add(self.p,R(other).p))
    __radd__=__add__
    def __neg__(self): return R(scale(self.p,-1))
    def __sub__(self, other): return self+-R(other)
    def __rsub__(self, other): return R(other)+-self
    def __mul__(self, other): return R(mul(self.p,R(other).p))
    __rmul__=__mul__
    def __eq__(self, other): return self.p==R(other).p
    def inverse(self):
        # Extended Euclid: a*P+b*self = gcd. Accept only constant nonzero gcd.
        a,b=P,self.p
        u,v=[F(0)],[F(1)]
        while b!=[0]:
            quotient,remainder=divide(a,b)
            a,b=b,remainder
            u,v=v,add(u,scale(mul(quotient,v),-1))
        if len(a)!=1 or not a[0]:
            raise ZeroDivisionError('nonunit residue')
        answer=R(scale(u,1/a[0]))
        assert self*answer==1
        bounds=self.bounds()
        assert bounds[0]>0 or bounds[1]<0
        divisions.append(dict(denominator=self,inverse=answer,gcd=a[0],bounds=bounds,
                              product_residual=self*answer-1))
        return answer
    def __truediv__(self, other): return self*R(other).inverse()
    def bounds(self):
        a=self.p[0]
        b=self.p[1] if len(self.p)>1 else F(0)
        return [min(a+b*lo,a+b*hi),max(a+b*lo,a+b*hi)]


def readR(obj): return R([F(obj['a']),F(obj['b'])])


def compare(name, fresh, stored):
    def equal(a,b):
        if isinstance(a,R): return a==readR(b)
        if isinstance(a,F): return a==F(b)
        if isinstance(a,list): return len(a)==len(b) and all(equal(x,z) for x,z in zip(a,b))
        if isinstance(a,dict):
            normalized={str(k):v for k,v in a.items()}
            return normalized.keys()==b.keys() and all(equal(normalized[k],b[k]) for k in normalized)
        return a==b
    comparisons[name]=equal(fresh,stored)
    require('comparison_'+name, comparisons[name])


def determinant(a):
    if len(a)==1: return a[0][0]
    return sum(((-1)**j*a[0][j]*determinant([row[:j]+row[j+1:] for row in a[1:]])
                for j in range(len(a))),R(0))


def solve(a,b):
    a=[row.copy()+[z] for row,z in zip(a,b)]
    for i in range(len(a)):
        inverse=a[i][i].inverse()
        a[i]=[x*inverse for x in a[i]]
        for j in range(len(a)):
            if j!=i:
                factor=a[j][i]
                a[j]=[x-factor*y for x,y in zip(a[j],a[i])]
    return [row[-1] for row in a]


def dot(a,b): return sum((x*z for x,z in zip(a,b)),R(0))
def matvec(a,b): return [dot(row,b) for row in a]


def all_minors(a):
    return {','.join(map(str,ids)):determinant([[a[i][j] for j in ids] for i in ids])
            for k in range(1,len(a)+1) for ids in combinations(range(len(a)),k)}


def log_values(y):
    q=[(-1)**j*z/R(factorial(2*j)) for j,z in enumerate(y)]
    # Explicit formal logarithm, with ring-valued coefficients lifted to polynomials.
    s=[R(p) for p in formal_log([x.p for x in q])]
    return q,s


alpha=R([0,1])
require('quadratic_relation', R(P)==0)
compare('relation_A',-P[0]/P[2],old['root']['relation_A'])
compare('relation_B',-P[1]/P[2],old['root']['relation_B'])
compare('fixed_rounded_midpoints',fixed,old['construction']['fixed_rounded_midpoints'])
compare('formal_q',qformal,old['root']['formal_q0_through_q6'])
compare('formal_S',sformal[1:],old['root']['formal_S1_through_S6'])
m=[R(z) if j!=5 else alpha for j,z in enumerate(fixed)]
y=[z/R(fixed[0]) for z in m]
q,s=log_values(y)
delta=s[2]*s[4]-s[3]*s[3]
D=[[s[2],s[3]],[s[3],s[4]]]
pr=solve(D,[-s[4],-s[5]])
vector=pr+[R(1)]
require('original_p_r_formulas', pr[0]==(s[3]*s[5]-s[4]*s[4])/delta
        and pr[1]==(s[3]*s[4]-s[2]*s[5])/delta)
membership={}
for j,(z,(lower,upper)) in enumerate(zip(m,boxes)):
    require(f'box_{j}_both_sides',(z-lower).bounds()[0]>0 and (upper-z).bounds()[0]>0)
    require(f'common_mass_{j}',R(fixed[0])*y[j]==z)
    membership[str(j)]=dict(m=z,enclosure=z.bounds(),lower_slack=z-lower,
                           upper_slack=upper-z,relative_box_position=(z-lower)/R(upper-lower))
require('normalized_y0',y[0]==1)
W=[[y[i+j+1] for j in range(3)] for i in range(3)]
v=y[4:7]
av=solve(W,v)
require('W_solve_residuals',matvec(W,av)==v)
y.append(dot(v,av))
q,s=log_values(y)
log_residuals=[s[n]+n*q[n]+sum((s[k]*q[n-k] for k in range(1,n)),R(0))
               for n in range(8)]
require('finite_log_recurrence_all_coefficients',all(z==0 for z in log_residuals))
M3=[[y[i+j] for j in range(4)] for i in range(4)]
N3=[[y[i+j+1] for j in range(4)] for i in range(4)]
H2=[[s[i+j+2] for j in range(3)] for i in range(3)]
matrices=dict(W=W,M3=M3,N3=N3,H2=H2)
minors={name:all_minors(a) for name,a in matrices.items()}
for name in ['W','M3','N3','H2']:
    for ids,z in minors[name].items():
        require(name+'_minor_'+ids,z.bounds()[0]>0 if name in ['W','M3'] else z.bounds()[0]>=0)
null_rows=matvec(H2,vector)
require('all_three_exact_null_rows',all(z==0 for z in null_rows))
# Check the proof's full H2 factorization and the actual zero Schur complement.
U=[[R(1),R(0)],[R(0),R(1)],[-pr[0],-pr[1]]]
hfactor=[[sum((U[i][k]*D[k][l]*U[j][l] for k in range(2) for l in range(2)),R(0))
          for j in range(3)] for i in range(3)]
require('H2_factorization',hfactor==H2)
schur=y[7]-dot(v,av)
require('exact_N3_schur_and_determinants',schur==0
        and determinant(N3)==0 and determinant(H2)==0)
norm=dot(vector,vector)
require('positive_normalizing_square',norm.bounds()[0]>0)
products=[[a*b/norm for b in vector] for a in vector]
require('real_unit_c_nonzero_last_coordinate',sum((products[j][j] for j in range(3)),R(0))==1
        and products[2][2].bounds()[0]>0)
b={n:sum((products[i][j] for i in range(3) for j in range(3) if i+j==n-2),R(0))
   for n in range(2,7)}
B=-2*sum((n*(2*n+1)*b[n]*s[n+1] for n in range(2,6)),R(0))
B+=4*sum((n*b[n]*sum((s[k]*s[n+1-k] for k in range(2,n)),R(0)) for n in range(2,7)),R(0))
phi=-156*products[2][2]*s[7]+B
ds={n:-2*n*(2*n+1)*s[n+1]+4*n*sum((s[a]*s[n+1-a] for a in range(1,n+1)),R(0))
    for n in range(2,7)}
full_flux=sum((products[i][j]*ds[i+j+2] for i in range(3) for j in range(3)),R(0))
endpoint=sum((n*b[n]*s[n] for n in range(2,7)),R(0))
require('full_flux_equals_L874_functional',full_flux==phi and endpoint==0)
require('strict_H1_S2',s[2].bounds()[0]>F('3.714e-5'))
require('strict_H1_delta',F('9.7e-16')<delta.bounds()[0]<=delta.bounds()[1]<F('7.026e-15'))
require('claimed_strict_flux_interval',F('5.339503291e-15')<=phi.bounds()[0]
        <=phi.bounds()[1]<=F('5.339503292e-15'))
construction=dict(m0_through_m6=m,y0_through_y7=y,q0_through_q7=q,S1_through_S7=s[1:],
                  contact_vector_unnormalized=vector,norm_squared=norm,
                  normalized_pair_products=products,raw_v=v,raw_W_inverse_v=av)
for key,value in construction.items(): compare(key,value,old['construction'][key])
compare('membership',membership,old['membership'])
compare('matrices',matrices,old['matrices'])
compare('W_all_minors',minors['W'],old['W_principal_minors'])
compare('all_other_minors',{k:v for k,v in minors.items() if k!='W'},old['principal_minors'])
compare('null_rows',null_rows,old['null_rows_unnormalized'])
compare('log_residuals',log_residuals,old['independent_finite_log_residuals'])
compare('flux',dict(b2_through_b6=b,B=B,Phi=phi,full_heat_flux=full_flux),old['flux'])
compare('principal_minor_enclosures',{k:{ids:z.bounds() for ids,z in v.items()}
        for k,v in minors.items() if k!='W'},old['principal_minor_enclosures'])
inverse_evidence=[]
for j,rec in enumerate(old['inverse_records']):
    denominator,inverse=readR(rec['denominator']),readR(rec['inverse'])
    aa=denominator.p[0]
    bb=denominator.p[1] if len(denominator.p)>1 else F(0)
    conjugate=R([aa+bb*(-P[1]/P[2]),-bb])
    norm_value=denominator*conjugate
    require(f'original_inverse_{j}',norm_value==F(rec['conjugate_product'])
            and norm_value!=0 and denominator*inverse==1
            and denominator.inverse()==inverse)
    compare(f'inverse_enclosure_{j}',denominator.bounds(),rec['enclosure'])
    inverse_evidence.append(dict(denominator=denominator,inverse=inverse,
                                norm=norm_value,bounds=denominator.bounds(),residual=denominator*inverse-1))


def contains(label, interval, bounds):
    require('outward_'+label,F(interval['lower'])<=bounds[0]<=bounds[1]<=F(interval['upper']))


signs=old['complete_outward_sign_evidence']
for name,values in [('initial_P',initial_signs),('final_P',final_signs)]:
    for j,z in enumerate(values): contains(name+str(j),signs[name][j],[z,z])
for j,values in membership.items():
    for k in ['lower_slack','upper_slack']:
        contains('membership_'+j+k,signs['membership_slacks'][j][k],values[k].bounds())
for name,data in minors.items():
    stored=signs['W_principal_minors'] if name=='W' else signs['principal_minors'][name]
    for ids,z in data.items(): contains(name+ids,stored[ids],z.bounds())
for j,rec in enumerate(inverse_evidence):
    contains('inverse_'+str(j),signs['inverse_denominators'][j],rec['bounds'])
contains('norm',signs['norm_squared'],norm.bounds())
quantities=dict(m5=m[5],m6=m[6],m5_box_position=membership['5']['relative_box_position'],
                S2=s[2],delta=delta,c2_squared=products[2][2],Phi=phi,y7=y[7])
for name,z in quantities.items():
    contains('quantity_'+name,signs['quantities'][name],z.bounds())
    contains('compact_'+name,old['compact_rational_enclosures'][name],z.bounds())
require('complete_original_inverse_record_count',len(inverse_evidence)==12)
require('all_original_checks_true',len(old['checks'])==114 and all(old['checks'].values())
        and old['failures']==[] and old['result']=='CERTIFIED_VIOLATING_FINITE_TUPLE')
evidence=dict(source_sha256=source_hash,producer_sha256=sha256(PRODUCER.read_bytes()).hexdigest(),
              original_certificate_sha256=sha256(original_bytes).hexdigest(),
              polynomial=P,positive_scale=positive_scale,root_bracket=[lo,hi],
              root_values=final_signs,complete_moment_intervals=panel['moments'],
              construction=construction,membership=membership,matrices=matrices,
              principal_minors=minors,principal_minor_bounds={k:{ids:z.bounds() for ids,z in v.items()}
              for k,v in minors.items()},H2_factorization_residuals=[[hfactor[i][j]-H2[i][j]
              for j in range(3)] for i in range(3)],N3_schur_residual=schur,
              null_rows=null_rows,log_residuals=log_residuals,original_inverse_evidence=inverse_evidence,
              flux=dict(B=B,Phi=phi,full=full_flux,endpoint_cancellation=endpoint),
              strict_bounds={k:z.bounds() for k,z in quantities.items()},
              outward_sign_evidence=signs,
              required=dict(S2_lower='3.714e-5',delta_lower='9.7e-16',delta_upper='7.026e-15',
                            Phi_lower='5.339503291e-15',Phi_upper='5.339503292e-15'),
              scope='Unchanged finite-class witness only; no actual realization or RH sign.')
save('AUDIT_PASSED_UNCHANGED_FINITE_WITNESS',evidence)
print('AUDIT_PASSED_UNCHANGED_FINITE_WITNESS')
print('Phi: [5.339503291e-15, 5.339503292e-15]; required > 0')
print('S2 > 3.714e-5; 9.7e-16 < Delta < 7.026e-15; all two-sided boxes pass')
print('M3/W PD; N3/H2 PSD with exact zero determinants; all contact/log/flux residuals zero')
print('Checks:',len(checks),'comparisons:',len(comparisons),'original inverses:',len(inverse_evidence),
      'replay divisions:',len(divisions),'failures:',[])
print('Certificate:',OUTPUT.relative_to(ROOT))
