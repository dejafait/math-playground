"""Fixed d=4, (a,b)=(0,1) rank test; no new quadrature or site sweep.

Gautschi Theorem 2.1 supplies the moment coefficient system. Collect
the 4x4 Cramer determinants exactly as polynomials in base mu2,mu4,mu6
before interval evaluation. Dual numbers differentiate every determinant
term, including the denominator. All subsequent enclosures use Fraction
arithmetic with exact outward rounding to a fixed decimal rational grid.
L917/audit197 and L037 supply conditional analytic input containment.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations
from math import isqrt
from pathlib import Path
import json
import platform

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'scripts/heat/low-time-h2-uniform-195.json'
PRIOR = ROOT / 'scripts/heat/low-time-h2-audit-197.json'
OUT = Path(__file__).with_suffix('.json')
GRID = 10**50
TRACE = []
DIVISORS = []


def encode(x):
    return {'lower': str(x[0]), 'upper': str(x[1])}


def box(x):
    lo, hi = F(x['lower']), F(x['upper'])
    assert lo <= hi
    return lo, hi


def outward(x):
    lo, hi = x
    return (F((lo*GRID).__floor__(), GRID),
            F((hi*GRID).__ceil__(), GRID))


class I:
    def __init__(self, pair, operation='constant', inputs=()):
        self.pair = pair
        self.id = len(TRACE)
        TRACE.append({'id': self.id, 'operation': operation,
                      'inputs': list(inputs), 'interval': encode(pair)})

    @staticmethod
    def lift(x):
        return x if isinstance(x, I) else I((F(x), F(x)))

    def __add__(self, other):
        y = I.lift(other)
        return I(outward((self.pair[0]+y.pair[0], self.pair[1]+y.pair[1])),
                 'add', (self.id, y.id))

    __radd__ = __add__

    def __neg__(self):
        return I((-self.pair[1], -self.pair[0]), 'negate', (self.id,))

    def __sub__(self, other):
        return self + (-I.lift(other))

    def __rsub__(self, other):
        return I.lift(other) - self

    def __mul__(self, other):
        y = I.lift(other)
        corners = [a*b for a in self.pair for b in y.pair]
        return I(outward((min(corners), max(corners))), 'multiply', (self.id, y.id))

    __rmul__ = __mul__

    def reciprocal(self):
        lo, hi = self.pair
        DIVISORS.append({'trace_id': self.id, 'interval': encode(self.pair),
                         'excludes_zero': not lo <= 0 <= hi})
        if lo <= 0 <= hi:
            raise ArithmeticError('zero-containing divisor at trace '+str(self.id))
        return I(outward((1/hi, 1/lo)), 'reciprocal', (self.id,))

    def __truediv__(self, other):
        return self * I.lift(other).reciprocal()

    def sqrt(self):
        lo, hi = self.pair
        assert lo >= 0
        lower = isqrt((lo*GRID*GRID).__floor__())
        upper = isqrt((hi*GRID*GRID).__floor__())
        if F(upper*upper, GRID*GRID) < hi:
            upper += 1
        result = F(lower, GRID), F(upper, GRID)
        assert result[0]**2 <= lo <= hi <= result[1]**2
        return I(result, 'sqrt', (self.id,))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = I.lift(1)
        for _ in range(n):
            result = result * self
        return result


# Sparse exact polynomials in u=mu2,v=mu4,w=mu6. Exponents are triples.
class P:
    def __init__(self, terms):
        self.terms = {e: F(c) for e, c in terms.items() if c}

    @staticmethod
    def lift(x):
        return x if isinstance(x, P) else P({(0,0,0): F(x)})

    def __add__(self, other):
        result = self.terms.copy()
        for e, c in P.lift(other).terms.items():
            result[e] = result.get(e, F(0)) + c
        return P(result)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-P.lift(other))

    def __mul__(self, other):
        result = {}
        for e, c in self.terms.items():
            for f, d in P.lift(other).terms.items():
                g = tuple(a+b for a,b in zip(e,f))
                result[g] = result.get(g, F(0)) + c*d
        return P(result)

    __rmul__ = __mul__

    def evaluate(self, variables):
        result = I.lift(0)
        for exponents, coefficient in sorted(self.terms.items()):
            term = I.lift(coefficient)
            for x, n in zip(variables, exponents):
                term = term * (x**n)
            result = result + term
        return result

    def encode(self):
        return [{'exponents': list(e), 'coefficient': str(c)}
                for e,c in sorted(self.terms.items())]


class D:
    """Value and the two partial derivatives; works over P and over I."""
    def __init__(self, value, da, db):
        self.v, self.a, self.b = value, da, db

    def __add__(self, other):
        return D(self.v+other.v, self.a+other.a, self.b+other.b)

    def __neg__(self):
        return D(-self.v, -self.a, -self.b)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return D(self.v*other.v, self.a*other.v+self.v*other.a,
                 self.b*other.v+self.v*other.b)

    def scale(self, scalar):
        return D(self.v*scalar, self.a*scalar, self.b*scalar)

    def __pow__(self, n):
        assert n >= 1
        result = self
        for _ in range(n-1):
            result = result*self
        return result

    def divide(self, other):
        inv = other.v.reciprocal()
        value = self.v*inv
        return D(value, (self.a-value*other.a)*inv,
                 (self.b-value*other.b)*inv)

    def encode(self):
        return {key: {'trace_id': x.id, **encode(x.pair)}
                for key,x in [('value',self.v),('da',self.a),('db',self.b)]}


def determinant(matrix):
    result = D(P.lift(0),P.lift(0),P.lift(0))
    for perm in permutations(range(4)):
        inversions = sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term = D(P.lift(1),P.lift(0),P.lift(0))
        for i,j in enumerate(perm):
            term = term*matrix[i][j]
        result = result+term.scale((-1)**inversions)
    return result


def main():
    source = json.loads(SOURCE.read_bytes())
    prior = json.loads(PRIOR.read_bytes())
    failures = []

    def check(name, condition):
        if not condition:
            failures.append(name)

    prior_hash_checks = {name: sha256((ROOT/name).read_bytes()).hexdigest()==expected
                         for name,expected in prior['input_sha256'].items()}
    check('all accepted audit197 input hashes', all(prior_hash_checks.values()))
    selected = {'lambda':source['panels'][0]['lambda'],
                'moments':{str(k):source['panels'][0]['moments'][str(k)] for k in (0,2,4,6)}}
    check('panel0 includes lambda0 exactly', box(selected['lambda'])==(F(0),F(1,5120)))
    for k,record in selected['moments'].items():
        check('accepted complete input copy M'+k, record==prior['panels'][0]['moments'][k])
    check('accepted audit197 status', prior['status']=='passed')
    check('accepted audit197 failure list', prior['failures']==[])
    if failures:
        raise ArithmeticError(str(failures))

    raw = {k:I(box(record),'input',('/panels/0/moments/'+k,))
           for k,record in selected['moments'].items()}
    check('normalization strictly positive', raw['0'].pair[0]>0)
    variables = [raw[str(k)]/raw['0'] for k in (2,4,6)]
    symbols = [P({e:1}) for e in ((1,0,0),(0,1,0),(0,0,1))]
    base = [P.lift(1),P.lift(0),symbols[0],P.lift(0),symbols[1],
            P.lift(0),symbols[2],P.lift(0)]
    moments = []
    for k in range(8):
        # a^0=b^0=1; at a=0 its derivative is1 only for k=1.
        value = base[k] + (2 if k==0 else 1)
        da = P.lift(1 if k==1 else 0)
        db = P.lift(k)
        moments.append(D(value,da,db))
    gram = [[moments[i+j] for j in range(4)] for i in range(4)]
    rhs = [-moments[i+4] for i in range(4)]
    denominator = determinant(gram)
    numerators = []
    for j in range(4):
        replaced = [row.copy() for row in gram]
        for i in range(4):
            replaced[i][j] = rhs[i]
        numerators.append(determinant(replaced))

    polynomials = {}
    evaluated = {}
    for label, dual in [('gram_det',denominator)]+[('numerator_c'+str(j),x) for j,x in enumerate(numerators)]:
        polynomials[label] = {key:p.encode() for key,p in [('value',dual.v),('da',dual.a),('db',dual.b)]}
        evaluated[label] = D(dual.v.evaluate(variables),dual.a.evaluate(variables),dual.b.evaluate(variables))
    gram_det = evaluated['gram_det']
    check('Gram determinant numerical lower bound positive', gram_det.v.pair[0]>0)
    coeff = [evaluated['numerator_c'+str(j)].divide(gram_det) for j in range(4)]
    c0,c1,c2,c3 = coeff
    # Newton sums and empirical division by4, including their full derivatives.
    p1 = -c3
    p2 = -(c3*p1+c2.scale(2))
    p3 = -(c3*p2+c2*p1+c1.scale(3))
    p4 = -(c3*p3+c2*p2+c1*p1+c0.scale(4))
    r1,r2,r3,r4 = [p.scale(F(1,4)) for p in (p1,p2,p3,p4)]
    variance = r2-r1**2
    third = r3-(r1*r2).scale(3)+(r1**3).scale(2)
    fourth = r4-(r1*r3).scale(4)+(r1**2*r2).scale(6)-(r1**4).scale(3)
    check('empirical variance numerical lower bound positive', variance.v.pair[0]>0)
    A_a = variance.v*third.a-F(3,2)*third.v*variance.a
    A_b = variance.v*third.b-F(3,2)*third.v*variance.b
    B_a = variance.v*fourth.a-2*fourth.v*variance.a
    B_b = variance.v*fourth.b-2*fourth.v*variance.b
    rank_numerator = A_a*B_b-A_b*B_a
    sqrt_v = variance.v.sqrt()
    gden = variance.v**2*sqrt_v
    kden = variance.v**3
    jacobian = [[A_a/gden,A_b/gden],[B_a/kden,B_b/kden]]
    det_den = variance.v**5*sqrt_v
    det_jacobian = rank_numerator/det_den
    direct_det = jacobian[0][0]*jacobian[1][1]-jacobian[0][1]*jacobian[1][0]
    check('two determinant enclosures overlap',
          max(det_jacobian.pair[0],direct_det.pair[0])<=min(det_jacobian.pair[1],direct_det.pair[1]))
    nonzero = not rank_numerator.pair[0]<=0<=rank_numerator.pair[1]
    status = 'nonzero_rank_certified' if nonzero and not failures else 'inconclusive'
    results = {'gram_determinant':gram_det.encode(),
               'coefficients_ascending':[x.encode() for x in coeff],
               'raw_empirical_moments':[x.encode() for x in (r1,r2,r3,r4)],
               'variance':variance.encode(),'third_centered':third.encode(),
               'fourth_centered':fourth.encode(),
               'A_a':{'trace_id':A_a.id,**encode(A_a.pair)},
               'A_b':{'trace_id':A_b.id,**encode(A_b.pair)},
               'B_a':{'trace_id':B_a.id,**encode(B_a.pair)},
               'B_b':{'trace_id':B_b.id,**encode(B_b.pair)},
               'rank_numerator':{'trace_id':rank_numerator.id,**encode(rank_numerator.pair)},
               'jacobian':[[{'trace_id':x.id,**encode(x.pair)} for x in row] for row in jacobian],
               'determinant_denominator':{'trace_id':det_den.id,**encode(det_den.pair)},
               'determinant':{'trace_id':det_jacobian.id,**encode(det_jacobian.pair)},
               'direct_determinant_consistency_only':{'trace_id':direct_det.id,**encode(direct_det.pair)}}
    # Small outward display bounds do not replace the complete rational evidence.
    def display(x, digits=12):
        scale = 10**digits
        lo = (x.pair[0]*scale).__floor__()
        hi = (x.pair[1]*scale).__ceil__()
        return {'lower':format(F(lo,scale).__float__(),'.12g'),
                'upper':format(F(hi,scale).__float__(),'.12g'),
                'exact_lower':str(F(lo,scale)),'exact_upper':str(F(hi,scale))}
    summary = {'status':status,'actual_gram_det':display(gram_det.v),
               'actual_variance':display(variance.v),'actual_rank_numerator':display(rank_numerator),
               'actual_jacobian_determinant':display(det_jacobian),
               'required':'all divisors exclude0; Gram det and V>0; determinant excludes0',
               'nonzero':nonzero,'failures':failures,'certificate':str(OUT.relative_to(ROOT))}
    report = {'status':status,'python':platform.python_version(),
              'qualification':'Conditional L917/audit197 input containment under L037; no independent Decimal verification; finite specialization, no actual-target inclusion or RH claim',
              'fixed_sites':['0','1'],'degree':4,'empirical_divisor':4,
              'source':str(SOURCE.relative_to(ROOT)),
              'input_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in (SOURCE,PRIOR,Path(__file__))},
              'prior_hash_checks':prior_hash_checks,'selected_inputs':selected,
              'base_probability_moments':{'0':{'lower':'1','upper':'1'},
                    **{str(k):encode(x.pair) for k,x in zip((2,4,6),variables)},
                    **{str(k):{'lower':'0','upper':'0'} for k in (1,3,5,7)}},
              'arithmetic':{'type':'exact Fraction with exact outward rational grid rounding','grid_denominator':str(GRID),'no_transcendental_calls':True},
              'polynomials':polynomials,'results':results,'divisors':DIVISORS,
              'trace':TRACE,'required_determinant_excludes_zero':True,
              'rank_certified_subject_to_input_contracts':nonzero and not failures,
              'failures':failures,'summary':summary}
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(summary))


if __name__=='__main__':
    main()
