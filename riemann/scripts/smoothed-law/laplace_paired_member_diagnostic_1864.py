"""Exploratory floating-point pair test; NOT a rigorous certificate.

Uses integration by parts on the original complete even member:
D_j = int h'(x) 4j/[x(x*x+j)] dx, E_j = int h'''(x) same dx.
Both boundary terms vanish; this is only a stable quadrature diagnostic.
"""
import cmath
import itertools
import json
import math
from pathlib import Path


def values(gamma, delta, sigma):
    z = complex(gamma, -delta)
    norm = 1 / math.sqrt(4 * math.pi * sigma)

    def jet(v):
        g = norm * cmath.exp(-v*v/(4*sigma))
        return (-v/(2*sigma)*g,
                (3*v/(4*sigma*sigma)-v**3/(8*sigma**3))*g)

    g0 = norm * cmath.exp(-z*z/(4*sigma))
    h2 = ((z*z/(4*sigma*sigma)-1/(2*sigma))*g0).real
    h4 = ((z**4/(16*sigma**4)-3*z*z/(4*sigma**3)
           +3/(4*sigma*sigma))*g0).real

    def f(x):
        if x == 0:
            return [4*h2, 4*h2, 4*h4, 4*h4]
        a, b = jet(x-z), jet(x+z)
        hp = ((a[0]+b[0])/2).real
        hppp = ((a[1]+b[1])/2).real
        q = [4*j/(x*(x*x+j)) for j in (1, 2)]
        return [hp*q[0], hp*q[1], hppp*q[0], hppp*q[1]]

    def integral(n):
        cuts = sorted(set([0, 1, max(1, gamma-20), max(1, gamma-8),
                           gamma, gamma+8, gamma+20]))
        out = [0.0]*4
        for a, b in zip(cuts, cuts[1:]):
            dx = (b-a)/n
            terms = [[] for _ in range(4)]
            for k in range(n+1):
                wt = 1 if k in (0,n) else (4 if k % 2 else 2)
                for i, value in enumerate(f(a+k*dx)):
                    terms[i].append(wt*value)
            for i in range(4):
                out[i] += math.fsum(terms[i])*dx/3
        return out

    lo, hi = integral(256), integral(512)
    return {'gamma': gamma, 'delta': delta, 'sigma': sigma,
            'D1_D2_E1_E2': hi, 'refinement_difference':
            [abs(a-b) for a,b in zip(lo,hi)]}


def main():
    members = [(14.0001,0), (15,0), (20,0), (40,0), (100,0),
               (100.001,0.499), (150,0.499), (1000,0), (1000,0.499)]
    all_rows = []
    pairs = []
    for sigma in (1, 1.5, 2):
        rows = [values(g,d,sigma) for g,d in members]
        all_rows.extend(rows)
        for i,j in itertools.combinations_with_replacement(range(len(rows)),2):
            a,b,c,d = rows[i]['D1_D2_E1_E2']
            e,f,g,h = rows[j]['D1_D2_E1_E2']
            pair = (a*h+e*d-b*g-f*c)/2
            pairs.append({'sigma':sigma, 'members':[members[i],members[j]],
                          'P':pair, 'P_times_gamma6_gamma6':pair*members[i][0]**6*members[j][0]**6})
    result = {'rigorous':False, 'purpose':'exploratory only; refinement is not error certification',
              'members':all_rows, 'pairs':pairs,
              'summary':{'pair_count':len(pairs), 'positive_samples':sum(p['P']>0 for p in pairs),
                         'scaled_min':min(p['P_times_gamma6_gamma6'] for p in pairs),
                         'scaled_max':max(p['P_times_gamma6_gamma6'] for p in pairs),
                         'required_bound':'P <= 0 for every admissible pair; samples do not establish it'}}
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summary']))
    print('NOT CERTIFIED; full exploratory record:',path)


if __name__ == '__main__':
    main()
