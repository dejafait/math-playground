"""Bounded fixed-rate diagnostic; finite precision is NOT a certificate.

Run: python3 scripts/paired-subdiagonal/real_scale_1234.py
Full evidence: real-scale-1234.json beside this script.
Only Python's standard library is used. Partial fractions are rational;
exponential evaluation and Hankel elimination use rounded Decimal.
"""
from collections import Counter
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
import random


def partial_fractions(rates):
    counts = Counter(rates)
    result = []
    for q, mu in sorted(counts.items()):
        series = [F(1)] + [F(0)] * (mu - 1)
        for r, nu in sorted(counts.items()):
            if r == q:
                continue
            factor = [F((-1)**j * comb(nu+j-1, j), (r-q)**(nu+j))
                      for j in range(mu)]
            series = [sum((series[k]*factor[j-k] for k in range(j+1)), F(0))
                      for j in range(mu)]
        result.append((q, [series[mu-k-1]/factorial(k) for k in range(mu)]))
    return result


def dec(v):
    return D(v.numerator)/D(v.denominator)


def moments(parts, t, count):
    answer = [D(0)]*count
    for q, poly in parts:
        work = [dec(c) for c in poly]
        exp = (-D(q)*t).exp()
        for v in range(count):
            value = D(0)
            for c in reversed(work):
                value = value*t+c
            answer[v] += exp*value
            work = [-D(q)*c + ((k+1)*work[k+1] if k+1 < len(work) else 0)
                    for k,c in enumerate(work)]
    return answer


def betas(parts, n, t):
    d = n//2
    vals = moments(parts, t, 2*d-1)
    H = [[vals[j+k] for k in range(d)] for j in range(d)]
    pivots = []
    for j in range(d):
        p = H[j][j]
        if (-1)**j*p <= 0:
            raise ArithmeticError(f'nonpositive signed pivot j={j}, t={t}')
        pivots.append(p)
        for k in range(j+1,d):
            fac = H[k][j]/p
            for ell in range(j+1,d):
                H[k][ell] -= fac*H[j][ell]
    return [(-pivots[i]/pivots[i-1]).sqrt() for i in range(1,d)]


def cases():
    data = []
    for n in (4,5,6,8,12,16):
        for a in (1,8,32):
            data.extend([[0]*2+[a]*(n-2), [0]*(n-2)+[a]*2])
    rng = random.Random(1234)
    for n in (6,8,12,16):
        for _ in range(5):
            pairs = [rng.choice([0,1,2,4,8,16,32]) for _ in range(n//2)]
            low = min(pairs)
            data.append(sorted([a-low for a in pairs for _ in range(2)]))
    return sorted(set(tuple(q) for q in data))


def run():
    output = dict(kind='FINITE_PRECISION_DIAGNOSTIC_NOT_PROOF',
                  required='beta_i(t)/beta_i(x)>=1/2 for ALL admissible fixed rates, ranks and 3*x/4<=t<=x; a violation needs rigorous certification.',
                  family='Every listed shifted rate q means the positive rate q+1; paired multisets or one pair plus repeated background. Rates stay fixed as t varies.',
                  formulas='Rational confluent partial fractions for product(s+q)^(-mu), derivative-Hankel signed pivots; common exponential shift and overall rate product cancel from beta.',
                  limitations=['Finite cases and three earlier times only.',
                               'Rounded Decimal values are not interval bounds.',
                               'No uniform monotonicity or half-value proof follows.'],
                  cases=[], failures=[])
    for rates in cases():
        n = len(rates)
        parts = partial_fractions(rates)
        for x in (F(1,10),F(1),F(4)):
            precision = 140+int(n*max(rates)*x/2)
            row = dict(shifted_rates=list(rates), x=str(x), precision=precision)
            try:
                with localcontext() as ctx:
                    ctx.prec = precision
                    end = betas(parts,n,dec(x))
                    values = []
                    for frac in (F(3,4),F(9,10),F(99,100)):
                        early = betas(parts,n,dec(x*frac))
                        for i,(u,v) in enumerate(zip(early,end),1):
                            values.append(dict(i=i, t_over_x=str(frac),
                                               beta_t=format(u,'.69E'),
                                               beta_x=format(v,'.69E'),
                                               ratio=format(u/v,'.69E')))
                    row['values'] = values
            except Exception as exc:
                row['failure'] = str(exc)
                output['failures'].append(dict(shifted_rates=list(rates),x=str(x),error=str(exc)))
            output['cases'].append(row)
    all_values = [(r,v) for r in output['cases'] for v in r.get('values',[])]
    row,value = min(all_values,key=lambda p:D(p[1]['ratio']))
    output['sampled_minimum'] = dict(shifted_rates=row['shifted_rates'],x=row['x'],**value)
    output['sampled_violations'] = [dict(shifted_rates=r['shifted_rates'],x=r['x'],**v)
                                  for r,v in all_values if D(v['ratio']) < D('0.5')]
    output['sampled_increases'] = [dict(shifted_rates=r['shifted_rates'],x=r['x'],**v)
                                 for r,v in all_values if D(v['ratio']) < 1]
    output['checked_ratios'] = len(all_values)
    path = Path(__file__).with_name('real-scale-1234.json')
    path.write_text(json.dumps(output,indent=2)+'\n')
    print('Diagnostic only; full evidence:',path)
    print('Actual sampled minimum ratio:',value['ratio'])
    print('Required universal ratio: >=1/2; monotonicity would require >=1.')
    print('Case:',output['sampled_minimum'])
    print('Checked ratios:',len(all_values),'sampled violations:',len(output['sampled_violations']),
          'sampled increases:',len(output['sampled_increases']))
    print('Failures:',output['failures'])


if __name__ == '__main__':
    run()
