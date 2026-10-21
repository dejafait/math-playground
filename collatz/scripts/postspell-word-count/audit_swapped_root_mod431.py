#!/usr/bin/env python3
"""Independent L059 audit; no original evaluator imported or certificates overwritten."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
M, LIFT, K, N = 431, 4741, 397573379, 630138897
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
LEMMA = ROOT / 'lemmas/L059-swapped-root-mod431-nonintegrality.md'
OUT = HERE / 'swapped-root-mod431-audit-certificate.json'
checks, failures = [], []


def check(name, actual, required):
    row = dict(name=name, actual=actual, required=required)
    checks.append(row)
    if actual != required:
        failures.append(row)


def compose(f, g):
    """f after g; normalized affine pairs modulo 4741."""
    return (f[0]*g[0] % LIFT, (f[0]*g[1]+f[1]) % LIFT)


def power(f, n):
    """Right-to-left; acc composed with base**remaining stays f**original."""
    acc = (1, 0)
    while n:
        if n % 2:
            acc = compose(acc, f)
        f = compose(f, f)
        n //= 2
    return acc


def recover(f, length):
    q = pow(2, length, LIFT)
    return [f[0]*q % M, f[1]*q % M, q % M]


def log_bounds(x):
    # log(x)=2 sum z^(2j+1)/(2j+1), z=(x-1)/(x+1).
    z = F(x-1, x+1)
    lo = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(64)), F(0))
    error = 2*z**129/(129*(1-z*z))
    return lo, lo+error


def main():
    raw = SOURCE.read_bytes()
    text = raw.decode()
    # Independently transcribed entire canonical input, then compared to disk.
    pairs = [(8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
             (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
             (8224,39104),(15494,73672),(29191,138802),(54998,261511),
             (103621,492705),(195229,928293),(367827,1748976),
             (693015,3295208),(1305695,6208431),(2460032,11697176),
             (4634896,22038409),(8732512,41522114),(16452748,78230965),
             (30998279,32670621)]
    parsed = [list(map(int, s.split('|')[1:-1])) for s in text.splitlines()
              if re.fullmatch(r'\|\d+\|\d+\|\d+\|', s)]
    check('canonical input', parsed, [[i,j,h] for i,(j,h) in enumerate(pairs)])
    rows = [dict(i=i,J=j,H=h,a=2 if i<24 else 166504412,
                 k=3*j+h,D=4*j+h+(2 if i<24 else 166504412))
            for i,(j,h) in enumerate(pairs)]
    order = [6,1,2,3,4,5,0,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    expected_checks = []

    def original(name, actual, required):
        expected_checks.append(dict(name=name, actual=actual, required=required))
        check('recompute: '+name, actual, required)

    original('indices', [x[0] for x in parsed], list(range(25)))
    original('tail prescription', ['For 0<=i<24 set a_i=2;' in text,
             'set a_24=166504412=' in text], [True,True])
    original('allocation sums', [sum(r[f] for r in rows) for f in ['J','H','a']],
             [66061058,199390205,166504460])
    original('counts', [sum(r[f] for r in rows) for f in ['k','D']], [K,N])
    original('intact multiplicities', sorted(order), list(range(25)))
    original('closing tail', rows[order[-1]]['a'], 166504412)
    check('inverse two identity', 2*2371 % LIFT, 1)
    odd, even = (3*2371 % LIFT,2371), (2371,0)
    block = compose(odd,compose(even,compose(odd,odd)))
    original('OOEO', recover(block,4), [27,23,16])
    state = (1,0)
    pn = pk = term_sum = 0
    trace, independent = [], []
    for pos,i in enumerate(order):
        r = rows[i]
        j,h,tail = r['J'],r['H'],r['a']
        word = compose(power(even,tail),compose(power(odd,h),power(block,j)))
        triple = recover(word,r['D'])
        lift = (pow(27,j,LIFT)-pow(16,j,LIFT)) % LIFT
        original(f'row {i}: lifted exact division', lift % 11, 0)
        c = (23*pow(3,h,M)*(lift//11)+(pow(3,h,M)-pow(2,h,M))*pow(16,j,M)) % M
        closed = [pow(3,r['k'],M),c,pow(2,r['D'],M)]
        original(f'row {i}: closed versus division-free', closed, triple)
        t = sum(rows[x]['D'] for x in order[:pos])
        u = sum(rows[x]['k'] for x in order[pos+1:])
        original(f'position {pos}: exponents', [pn,K-pk-r['k']], [t,u])
        two,three = pow(2,t,M),pow(3,u,M)
        term = triple[1]*two*three % M
        term_sum += term
        previous = recover(state,pn)
        state = compose(word,state)
        pn += r['D']
        pk += r['k']
        result = recover(state,pn)
        original(f'position {pos}: partial powers', [result[0],result[2]],
                 [pow(3,pk,M),pow(2,pn,M)])
        trace.append(dict(position=pos,index=i,prefix_N=t,suffix_K=u,
            lifted_difference=lift,lifted_quotient=lift//11,closed_triple=closed,
            composed_triple=triple,prefix_two=two,suffix_three=three,term=term,
            previous_triple=previous,resulting_triple=result))
        independent.append(dict(index=i,normalized_word=list(word),
                                normalized_prefix=list(state)))
    two,three = pow(2,N,M),pow(3,K,M)
    delta,phi = (two-three)%M, term_sum%M
    original('total exponents', [pk,pn], [K,N])
    original('weighted versus chronological numerator', phi, recover(state,N)[1])
    original('denominator reproduced', delta, 0)
    expected_summary = dict(modulus=M,numerator=phi,denominator=delta,two_total=two,
        three_total=three,term_sum=term_sum,checks=len(expected_checks),failures=0,
        verdict='NONINTEGRAL')
    expected = dict(target="Test whether modulo 431 excludes integer realization of L057's fixed swapped-order root.",
        source='lemmas/'+SOURCE.name,source_sha256=hashlib.sha256(raw).hexdigest(),
        counts=dict(K=K,N=N),order=order,parameters=rows,trace=trace,
        summary=expected_summary,checks=expected_checks,failures=[])
    original_file = HERE/'swapped-root-mod431-certificate.json'
    saved = json.loads(original_file.read_text())
    # Whole-object equality includes every leaf, key, order and failure array.
    for key in expected:
        check('original certificate /'+key, saved.get(key), expected[key])
    check('original certificate key set', sorted(saved), sorted(expected))
    table = [[x['position'],x['index'],x['prefix_N'],x['suffix_K'],
              *x['composed_triple'],x['prefix_two'],x['suffix_three'],
              x['term'],x['resulting_triple'][1]] for x in trace]
    written = [list(map(int,line.split('|')[1:-1])) for line in LEMMA.read_text().splitlines()
               if re.fullmatch(r'\|(?:\d+\|){11}',line)]
    check('entire written table', written, table)
    expected_written = dict(checks=[dict(name='complete written table',actual=written,required=table),
        dict(name='term sum',actual=term_sum,required=5412),
        dict(name='all rows',actual=len(table),required=25)],
        failures=[],summary=dict(checks=3,failures=0))
    written_file = HERE/'swapped-root-mod431-written-table-check.json'
    check('complete transcription certificate', json.loads(written_file.read_text()), expected_written)
    a,b = log_bounds(2),log_bounds(3)
    lo,hi = N*a[0]-K*b[1],N*a[1]-K*b[0]
    check('strict positive Lambda lower bound', lo>F(10584,10**14), True)
    check('Lambda upper bound', hi<F(10585,10**14), True)
    check('required integer contradiction', [phi,delta,two,three,term_sum], [240,0,108,108,5412])
    files = [SOURCE,LEMMA,HERE/'test_swapped_root_mod431.py',original_file,written_file]
    out = dict(target="Critically audit L059's modulo-431 exclusion and complete exact certificate.",
        method='Normalized affine pairs modulo 4741, right-to-left powers, independent input transcription',
        input_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
        allocation=rows,order=order,independent=independent,trace=trace,
        lambda_bounds=dict(lower=str(lo),upper=str(hi),required_lower='10584/100000000000000',
                           required_upper='10585/100000000000000',terms=64),
        checks=checks,failures=failures,
        summary=dict(checks=len(checks),failures=len(failures),original_checks=len(expected_checks),
            transcription_checks=3,rows=len(trace),numerator=phi,denominator=delta,
            two_total=two,three_total=three,term_sum=term_sum,
            verdict='FAIL' if failures else 'AUDIT_PASS'))
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out['summary'],sort_keys=True))
    print('Required: 25 intact rows; numerator 240 != 0; denominator 0; 0 mismatches.')
    print('Required positive Lambda interval: (10584/10^14,10585/10^14); both strict checks passed:',
          lo>F(10584,10**14) and hi<F(10585,10**14))
    print('Certificate:', OUT.relative_to(ROOT))
    if failures:
        print('Failures:', [r['name'] for r in failures])
        raise SystemExit(1)


if __name__ == '__main__':
    main()
