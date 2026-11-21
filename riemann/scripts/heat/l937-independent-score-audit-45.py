"""Independent fixed-witness audit. Reads producer evidence, never executes it.

Published weights only; binary outward intervals; finite power expansions;
alternating exponential enclosures; differentiated kernel polynomial sums.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json

SCALE = 2**380
checks = []
divisors = []


def down(x):
    return Q((x*SCALE).numerator // (x*SCALE).denominator, SCALE)


def up(x):
    return -down(-x)


class Box:
    def __init__(self, a=0, b=None):
        if isinstance(a, Box):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = down(Q(a)), up(Q(a if b is None else b))
        assert self.a <= self.b

    def __add__(self, other):
        other = Box(other)
        return Box(self.a+other.a, self.b+other.b)
    __radd__ = __add__

    def __neg__(self):
        return Box(-self.b, -self.a)

    def __sub__(self, other):
        return self + -Box(other)

    def __rsub__(self, other):
        return Box(other) + -self

    def __mul__(self, other):
        other = Box(other)
        vals = [x*y for x in (self.a, self.b) for y in (other.a, other.b)]
        return Box(min(vals), max(vals))
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Box(other)
        assert other.a > 0 or other.b < 0, 'zero-containing divisor'
        divisors.append(min(abs(other.a), abs(other.b)))
        return self * Box(1/other.b, 1/other.a)

    def __rtruediv__(self, other):
        return Box(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        ans = Box(1)
        while n:
            if n % 2:
                ans = ans*self
            self = self*self
            n //= 2
        return ans

    def absolute(self):
        return max(abs(self.a), abs(self.b))

    def data(self):
        return {'lower': str(self.a), 'upper': str(self.b)}


def require(name, condition, evidence=None):
    checks.append({'name': name, 'passed': bool(condition), 'evidence': evidence})


def overlap(name, interval, stored):
    lo, hi = Q(stored['lower']), Q(stored['upper'])
    require(name, max(interval.a, lo) <= min(interval.b, hi),
            {'independent': interval, 'producer': stored})


def contains(name, interval, lo, hi):
    lo, hi = Q(lo), Q(hi)
    require(name, lo <= interval.a <= interval.b <= hi,
            {'independent': interval, 'required': [lo, hi]})


def poly_mul(a, b, degree=6):
    return [sum((a[j]*b[k-j] for j in range(k+1)), Box())
            for k in range(degree+1)]


def evaluate(poly, x):
    ans = Box()
    for c in reversed(poly):
        ans = ans*x+c
    return ans


def exp_minus(x):
    """e^-x, x>=0: 160-term even partial sum, alternating tail, squaring."""
    x = Box(x)
    assert x.a >= 0
    halvings = 0
    while x.b > Q(1, 2):
        x = x/2
        halvings += 1
    term = Box(1)
    total = Box(1)
    for k in range(1, 161):
        term = term*(-x)/k
        total = total+term
    # Even partial sum is an upper bound; first omitted magnitude <= 2^-161/161!.
    total = total + Box(-Q(1, 2**161*factorial(161)), 0)
    assert total.a > 0
    for _ in range(halvings):
        total = total*total
    return total


def atan_pair(q):
    # 100 terms, rather than producer's 96; exact before binary conversion.
    lo = sum((Q((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(100)), Q())
    return Box(lo, lo+Q(1, 201*q**201))


def main():
    base = Path(__file__).parent
    producer_path = base/'l936-score-correction-certificate-43.json'
    prod = json.loads(producer_path.read_text())
    rejected = json.loads((base/'l936-score-correction-certificate-43-first-pass.json').read_text())
    screen = json.loads((base/'l936-score-correction-screen-43-first-pass.json').read_text())
    require('preserved_negative_weight', Q(rejected['weights'][5]) < 0, rejected['weights'][5])
    require('preserved_rejection', rejected['summary']['failures'] == ['weight_positive_5'])
    require('screen_has_no_conclusion', screen['mathematical_conclusion'] == 'none'
            and screen['rigorous'] is False, screen['status'])
    root = Box('0.0000530387415958154365906397391693872935932598188',
               '0.00005303874159581543659063973916938729359325981881')
    raw = [Box(x) for x in ['.497123021571', '.022972233662', '.002962906960',
                           '.000599311666', '.000160971754']]
    raw += [root, Box('.000020475993')]
    # Existing real root from L936; independently check its specified polynomial signs.
    pc = list(map(int, [
        '-62771292108354521989752161390673854977603807286751227007139',
        '2354209566613457384125275894062626786021779646664218000000000000',
        '-22072745990611555673606165989356026991593537500000000000000000000000']))
    a = Q('0.0000530387415958154365906397391693872935932598188')
    b = Q('0.00005303874159581543659063973916938729359325981881')
    endpoint = lambda x: pc[0]+pc[1]*x+pc[2]*x*x
    require('root_opposite_signs', endpoint(a)<0<endpoint(b),
            {'lower_value': endpoint(a), 'upper_value': endpoint(b)})
    require('root_record', Q(prod['response']['root']['lower']) <= a < b
            <= Q(prod['response']['root']['upper']), {'root': root})
    y = [x/raw[0] for x in raw]
    q = [(-1)**j*y[j]/factorial(2*j) for j in range(7)]
    h = q[:]
    h[0] = Box(0)  # exact normalized constant y0=1
    power = [Box(1)]+[Box() for _ in range(6)]
    log = [Box() for _ in range(7)]
    reciprocal = power[:]
    for k in range(1, 7):
        power = poly_mul(power, h)
        log = [x+(-1)**(k+1)*v/k for x, v in zip(log, power)]
        reciprocal = [x+(-1)**k*v for x, v in zip(reciprocal, power)]
    ss = [-j*log[j] for j in range(7)]
    delta = ss[2]*ss[4]-ss[3]*ss[3]
    require('delta_positive', delta.a > 0, delta)
    require('S2_positive', ss[2].a > 0, ss[2])
    # Elimination for D*(p,r)^T=-(S4,S5)^T; no Cramer's formula.
    pivot = ss[4]-ss[3]*ss[3]/ss[2]
    require('elimination_pivot_positive', pivot.a > 0, pivot)
    r = (-ss[5]+ss[3]*ss[4]/ss[2])/pivot
    p = (-ss[4]-ss[3]*r)/ss[2]
    c2sq = 1/(1+p*p+r*r)
    require('normalization_positive', c2sq.a > 0, c2sq)
    vec = [p, r, Box(1)]
    bbar = [sum((vec[i]*vec[j] for i in range(3) for j in range(3)
                 if i+j==n-2), Box()) for n in range(2, 7)]
    # Build each cos(u z)/g(z) coefficient by a polynomial convolution.
    rr = [Box() for _ in range(7)]
    for j in range(7):
        for n in range(2, 7):
            if n >= j:
                rr[j] += -n*bbar[n-2]*reciprocal[n-j]*Q((-1)**j, factorial(2*j))
    require('leading_response', rr[6].a <= -Q(6, factorial(12)) <= rr[6].b
            and rr[6].b-rr[6].a < Q(1,10**100), rr[6])
    for j in range(7):
        overlap('response_coefficient_'+str(j), rr[j], prod['response']['response'][j])
        overlap('log_coefficient_'+str(j), ss[j], prod['response']['S'][j])
        overlap('inverse_coefficient_'+str(j), reciprocal[j], prod['response']['inverse'][j])
    overlap('p_record', p, prod['response']['p'])
    overlap('r_record', r, prod['response']['r'])
    overlap('delta_record', delta, prod['response']['delta'])

    pi = 16*atan_pair(5)-4*atan_pair(239)
    require('pi_domain', 3 < pi.a < pi.b < Q(22,7), pi)
    overlap('pi_record', pi, prod['pi'])
    ta = Q(4*9**4, 2**240)
    tb = Q(156*9**6, 2**240)
    require('tail_constants', ta==Q(prod['tail']['relative_mass'])
            and tb==Q(prod['tail']['absolute_score_numerator']), {'EA': ta, 'EB': tb})
    for m in (4,6):
        require('tail_ratio_'+str(m), Q(10,9)**m/2**57 < Q(1,2), Q(10,9)**m/2**57)
    # Inductive inequalities used in n=9+k geometric estimate.
    require('n_geometric_induction', Q(10,9)*9 == 10 and Q(10,9)>1)
    require('square_induction', 2*9+1 == 19)

    points = list(map(Q, ['0','.19','.195','.38','.385','.57','.575','.775','.78']))
    nums = list(map(int, [
        '342629551549331167928578595198237452234451029',
        '426557058813327609702413571732323783259929594',
        '56912904027720194510092583061216678730988358',
        '122205527368671115281979946784999547871670448',
        '33758257961239763697121188149130759718426132',
        '5573293822800309123450863218672228205428839',
        '12001199277408839756363251855419549979105596',
        '232732544813000000000000000000000000000000',
        '129474634688000000000000000000000000000000']))
    weights = [Q(n, 10**45) for n in nums]
    require('points_match', points==list(map(Q, prod['points'])), points)
    require('weights_match', weights==list(map(Q, prod['weights'])), weights)
    all_rows, offsets, score_records = [], [], []
    for i, (u, w) in enumerate(zip(points, weights)):
        require('weight_positive_'+str(i), w>0, w)
        v = pi/exp_minus(2*u)
        require('v_domain_'+str(i), 3<v.a<=v.b<16, v)
        # K_n/e^(u/2-v), K_n'/e^(u/2-v), summed without individual scores.
        denominator, numerator = Box(), Box()
        terms = []
        factor = 4*v*(2*v-3)
        for n in range(1,9):
            t = exp_minus((n*n-1)*v)
            mass = 4*v*n*n*(2*v*n*n-3)*t
            deriv = (60*v*v*n**4-30*v*n*n-16*v*v*v*n**6)*t
            denominator += mass
            numerator += deriv
            terms.append({'n': n, 'negative_exponential': t,
                          'scaled_mass': mass, 'scaled_derivative': deriv})
            if n>=2:
                overlap('relative_mass_'+str(i)+'_'+str(n), mass/factor,
                        prod['score_records'][i]['terms'][n-2]['relative_mass'])
        head_den, head_num = denominator/factor, numerator/factor
        full_den = head_den+Box(0,ta)
        full_num = head_num+Box(-tb,tb)
        score = full_num/full_den
        require('score_denominator_positive_'+str(i), full_den.a>0, full_den)
        overlap('head_denominator_'+str(i), head_den, prod['score_records'][i]['head_denominator'])
        overlap('head_numerator_'+str(i), head_num, prod['score_records'][i]['head_numerator'])
        overlap('full_score_'+str(i), score, prod['score_records'][i]['full_score'])
        tvar = u*u
        rv = evaluate(rr, tvar)
        urprime = evaluate([2*j*x for j,x in enumerate(rr)], tvar)
        row = [Box((2*j+1)*u**(2*j))+(score+u/Q(5120))*u**(2*j+1)
               for j in range(6)] + [rv, urprime]
        offset = u*score*rv
        for j in range(8):
            overlap('row_'+str(i)+'_'+str(j), row[j], prod['rows'][i][j])
        overlap('offset_'+str(i), offset, prod['offsets'][i])
        all_rows.append(row)
        offsets.append(offset)
        score_records.append({'u':u, 'v':v, 'terms':terms, 'head_denominator':head_den,
                              'head_numerator':head_num, 'full_denominator':full_den,
                              'full_numerator':full_num, 'score':score})
    require('zero_score_enclosed', score_records[0]['score'].a<=0<=score_records[0]['score'].b,
            score_records[0]['score'])
    fsum = sum((w*f for w,f in zip(weights,offsets)), Box())
    columns = [sum((w*row[j] for w,row in zip(weights,all_rows)), Box()) for j in range(8)]
    allowances = [16*col.absolute() for col in columns]
    allowance = sum(allowances, Q())
    upper = fsum.b+allowance
    f_lo, f_hi = '-1.05818188426e-14','-1.05818188425e-14'
    contains('published_offset_bounds', fsum, f_lo, f_hi)
    col_limits = [
        ('1.10905264742e-44','1.10905264743e-44'),
        ('2.03924960631e-45','2.03924960632e-45'),
        ('3.80713857992e-46','3.80713857993e-46'),
        ('4.64782200551e-47','4.64782200552e-47'),
        ('-9.67949205045e-48','-9.67949205044e-48'),
        ('-1.14878796515e-47','-1.14878796514e-47'),
        ('1.35732291792e-18','1.35732291793e-18'),
        ('-1.13668403629e-18','-1.13668403628e-18')]
    for j,col in enumerate(columns):
        contains('published_column_'+str(j), col, *col_limits[j])
        overlap('weighted_column_record_'+str(j), col, prod['separation']['weighted_columns'][j])
    require('published_allowance', allowance <= Q('3.99041112674e-17'), allowance)
    require('published_strict_margin', upper < Q('-1.05419147312e-14'), upper)
    require('required_threshold', upper < -Q(1,10**15), upper)
    overlap('weighted_offset_record', fsum, prod['separation']['weighted_offset'])
    # Independent bounds need not equal producer's expression-dependent endpoints.
    failures = [c['name'] for c in checks if not c['passed']]
    def summary_num(x):
        # Decimal used only for bounded readable summaries.
        from decimal import Decimal, localcontext
        with localcontext() as ctx:
            ctx.prec=16
            return str(Decimal(x.numerator)/Decimal(x.denominator))
    result = {'checks':len(checks), 'failures':failures,
              'weighted_offset_lower':summary_num(fsum.a),
              'weighted_offset_upper':summary_num(fsum.b),
              'all_eight_allowance_upper':summary_num(allowance),
              'whole_box_upper':summary_num(upper), 'required':'strictly < -1e-15',
              'published_required':'strictly < -1.05419147312e-14',
              'minimum_positive_weight':str(min(weights)), 'divisions':len(divisors)}
    evidence = {'summary':result, 'producer_sha256':hashlib.sha256(producer_path.read_bytes()).hexdigest(),
                'arithmetic':'Fraction; outward binary grid 2^-380; 100-term Machin; alternating 160th exponential partial sum',
                'root':root, 'root_endpoint_values':[endpoint(a),endpoint(b)],
                'response':{'raw':raw,'normalized':y,'q':q,'S':ss,'delta':delta,'p':p,'r':r,
                            'c2_squared':c2sq,'reciprocal':reciprocal,'bbar':bbar,'rho':rr},
                'pi':pi, 'tail':{'EA':ta,'EB':tb}, 'points':points,'weights':weights,
                'score_records':score_records,'rows':all_rows,'offsets':offsets,
                'separation':{'weighted_offset':fsum,'columns':columns,'allowances':allowances,
                              'allowance':allowance,'whole_box_upper':upper},
                'divisors':{'count':len(divisors),'minimum':min(divisors)}, 'checks':checks}
    def encode(x):
        if isinstance(x,Box):return x.data()
        if isinstance(x,Q):return str(x)
        raise TypeError(type(x))
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(evidence,default=encode,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('Certificate:',path)
    return bool(failures)


if __name__=='__main__':
    raise SystemExit(main())
