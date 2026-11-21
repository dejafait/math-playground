"""Exact symbolic collision reduction; no sampled or global root-count claim."""
from fractions import Fraction as F
from pathlib import Path
import json

# Sparse rational polynomials in l,k,t. Use the normalized S=1+l*x+k*x^2.
class P(dict):
    def __init__(self, c=0):
        super().__init__(c if isinstance(c, dict) else ({(0,0,0):F(c)} if c else {}))
    def __add__(self, q):
        q=P(q); z=P(dict(self))
        for m,c in q.items(): z[m]=z.get(m,F(0))+c
        return P({m:c for m,c in z.items() if c})
    __radd__=__add__
    def __neg__(self): return P({m:-c for m,c in self.items()})
    def __sub__(self,q): return self+-P(q)
    def __rsub__(self,q): return P(q)+-self
    def __mul__(self,q):
        q=P(q); z={}
        for m,c in self.items():
            for n,d in q.items():
                a=tuple(i+j for i,j in zip(m,n)); z[a]=z.get(a,F(0))+c*d
        return P({m:c for m,c in z.items() if c})
    __rmul__=__mul__
    def __pow__(self,n):
        z=P(1)
        for _ in range(n): z=z*self
        return z
    def sub(self,values):
        z=P(0)
        for m,c in self.items():
            y=P(c)
            for a,v in zip(m,values): y=y*(P(v)**a)
            z=z+y
        return z
    def encode(self):
        return [{'powers_l_k_t':list(m),'coefficient':str(c)} for m,c in sorted(self.items())]
    def fmt(self):
        terms=[]
        for m,c in sorted(self.items(),reverse=True):
            mon='*'.join(v+(('**'+str(a)) if a>1 else '') for v,a in zip(['l','k','t'],m) if a)
            terms.append(str(c)+('*'+mon if mon else ''))
        return ' + '.join(terms) if terms else '0'

def V(i):
    m=[0,0,0];m[i]=1
    return P({tuple(m):F(1)})
l,k,t=[V(i) for i in range(3)]
r=[P(1),2*l,l*l+2*k,2*l*k,k*k]
a=1+2*t*r[1];b=1+r[1]+2*t*r[2]
c=1+2*r[1]+6*t*r[2];d=r[1]+2*r[2]+6*t*r[3]
f=-2*t;g=-2-6*t*r[1]
det=a*d-b*c;bn=f*d-b*g;cn=a*g-f*c
margin=4*cn*det-bn*bn
# The same sparse arithmetic checks the full input/output identity after
# clearing the determinant, without any division or numerical root finding.
pnum=[P(0) for _ in range(7)]
for i,ri in enumerate(r):
    for j,qj in enumerate([cn,bn,det]): pnum[i+j]=pnum[i+j]+ri*qj
image=[pnum[j]+((j+1)*pnum[j+1] if j<6 else 0)
       +(t*(j+2)*(j+1)*pnum[j+2] if j<5 else 0) for j in range(7)]
residual=[pnum[2]+3*pnum[3]+12*t*pnum[4],
          pnum[3]+4*pnum[4]+20*t*pnum[5],
          pnum[4]+5*pnum[5]+30*t*pnum[6],
          pnum[5]+6*pnum[6],pnum[6]]
square_coefficients=[P(0) for _ in range(5)]
for i,si in enumerate([P(1),l,k]):
    for j,sj in enumerate([P(1),l,k]):
        square_coefficients[i+j]=square_coefficients[i+j]+si*sj
square_completion=-30*(t*l+F(1,5))**2-6*t*t*(l*l-4*k)+2*t-F(4,5)
out={name:v for name,v in {'a':a,'b':b,'c':c,'d':d,'f':f,'g':g,'det':det,'b_numerator':bn,'c_numerator':cn,'positive_pair_numerator':margin,'c_numerator_square_completion':square_completion}.items()}
checks={'cramer_first':a*bn+b*cn==f*det,
        'cramer_second':c*bn+d*cn==g*det,
        'c_numerator_explicit':cn==-36*l*l*t*t-12*l*t+24*k*t*t+2*t-2,
        'c_numerator_square_completion':cn==square_completion,
        'strict_upper_threshold_arithmetic':2*F(5,18)-F(4,5)==-F(11,45),
        'cleared_output_constant_zero':image[0]==P(0),
        'cleared_output_linear_zero':image[1]==P(0),
        'full_cleared_output_identity':image==[P(0),P(0)]+residual,
        'residual_leading_coefficient':residual[4]==det*k*k,
        'r_is_square':square_coefficients==r}
record={'status':'EXACT_REDUCTION_NOT_COUNT_THEOREM','variables':['l','k','t'],
        'normalization':'R=(1+l*x+k*x^2)^2; k!=0 and l^2>4*k; p=R*(x^2+B*x+C). Scaling by k^-2 makes monic.',
        'conditions':'1/4<=t<=5/18; k!=0; l^2>4*k; det<0; positive_pair_numerator>0. These exactly parametrize the admissible two-double-input collisions away from input roots. The input-root case is separately excluded in C020q.',
        'polynomials':{n:v.encode() for n,v in out.items()},
        'formulas':{n:v.fmt() for n,v in out.items()},
        'cleared_input_ascending':[v.encode() for v in pnum],
        'cleared_output_ascending':[v.encode() for v in image],
        'residual_numerator_ascending':[v.encode() for v in residual],
        'actual_bounds':{'c_numerator':'strictly less than -11/45','det_at_admissible_collision':'strictly negative','quartic_real_root_count':'UNRESOLVED'},
        'required_bounds':{'singular_consistency':'c_numerator=0 when det=0','root_count_target':'input two nonreal roots and output four; at a transverse double collision a two-real-root residual can lead to a witness'},
        'checks':checks,'failures':[n for n,v in checks.items() if not v],
        'limitations':['No uniform residual quartic count proved.','No rational witness or whole-class impossibility.','Products of factors and general four-real-root inputs are not covered.','Symbolic checks do not replace the inequality and converse argument in C020q.'],
        'environment_note':'The initial optional SymPy import failed because SymPy is unavailable. This certificate uses only standard-library exact fractions and sparse polynomial arithmetic; no package was installed.'}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(record,indent=2)+'\n')
print('Exact algebra checks:',sum(checks.values()),'/',len(checks))
print('Actual c numerator < -11/45; singular consistency requires zero.')
print('Quartic count unresolved; required full witness counts: (2,4).')
print('Failures:',record['failures']);print('Full evidence:',path)
