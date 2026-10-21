#!/usr/bin/env python3
"""Independent L061 audit. Only its fixed order and the two saved squares."""
from pathlib import Path
from fractions import Fraction
from math import isqrt
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
CERT = HERE / 'joint-witness-prime-square-certificate.json'
OUT = HERE / 'joint-witness-prime-square-audit-certificate.json'
LEMMA = ROOT / 'lemmas/L061-joint-witness-complete-two-prime-cancellation.md'
K, N = 397573379, 630138897
checks, failures, original_checks = [], [], []


def check(name, actual, required):
    item = dict(name=name, actual=actual, required=required)
    checks.append(item)
    if actual != required:
        failures.append(item)


def original(name, actual, required):
    original_checks.append(dict(name=name, actual=actual, required=required))
    check('independent original: ' + name, actual, required)


def compare(path, actual, required):
    # Complete key sets and every leaf, including all original comparisons.
    if isinstance(required, dict) and isinstance(actual, dict):
        check(path + ': keys', sorted(actual), sorted(required))
        for key in required:
            compare(path + '/' + key, actual.get(key), required[key])
    elif isinstance(required, list) and isinstance(actual, list):
        check(path + ': length', len(actual), len(required))
        for i, value in enumerate(required):
            compare(path + '/' + str(i), actual[i] if i < len(actual) else None, value)
    else:
        check(path, actual, required)


def after(f, g, modulus):
    # f(g(x)) for normalized affine pairs, no denominator coordinate.
    return (f[0] * g[0] % modulus, (f[0] * g[1] + f[1]) % modulus)


def repeat(f, exponent, modulus):
    result = (1, 0)
    while exponent:
        if exponent % 2:
            result = after(f, result, modulus)
        f = after(f, f, modulus)
        exponent //= 2
    return result


def recover(f, length, modulus):
    q = pow(2, length, modulus)
    return [f[0] * q % modulus, f[1] * q % modulus, q]


def log_interval(x):
    z = Fraction(x - 1, x + 1)
    lower = 2 * sum((z**(2*j+1) / (2*j+1) for j in range(64)), Fraction(0))
    return lower, lower + 2*z**129 / (129*(1-z*z))


def main():
    pairs = [(8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
             (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
             (8224,39104),(15494,73672),(29191,138802),(54998,261511),
             (103621,492705),(195229,928293),(367827,1748976),
             (693015,3295208),(1305695,6208431),(2460032,11697176),
             (4634896,22038409),(8732512,41522114),(16452748,78230965),
             (30998279,32670621)]
    inputs = {}
    for ident in ('L055','L056','L057','L060'):
        paths = list((ROOT/'lemmas').glob(ident+'-*.md'))
        original(ident+' unique canonical file', len(paths), 1)
        raw = paths[0].read_bytes()
        inputs[ident] = dict(path=str(paths[0].relative_to(ROOT)), sha256=hashlib.sha256(raw).hexdigest())
        if ident == 'L055':
            source = raw.decode()
    parsed = [list(map(int, line.split('|')[1:-1])) for line in source.splitlines()
              if re.fullmatch(r'\|\d+\|\d+\|\d+\|', line)]
    check('independent transcription of entire allocation', parsed, [[i,*p] for i,p in enumerate(pairs)])
    original('complete input indices', [r[0] for r in parsed], list(range(25)))
    original('canonical tail prescriptions', ['For 0<=i<24 set a_i=2;' in source,
             'set a_24=166504412=' in source], [True,True])
    rows = [dict(i=i,J=j,H=h,a=2 if i<24 else 166504412,
                 k=3*j+h,D=4*j+h+(2 if i<24 else 166504412)) for i,(j,h) in enumerate(pairs)]
    original('positive parameter domain', all(r['J']>=2 and r['H']>=3 and r['a']>=2 for r in rows), True)
    counts = dict(sum_J=sum(r['J'] for r in rows),sum_H=sum(r['H'] for r in rows),
                  sum_a=sum(r['a'] for r in rows),K=sum(r['k'] for r in rows),N=sum(r['D'] for r in rows))
    original('complete allocation counts', list(counts.values()), [66061058,199390205,166504460,K,N])
    order = list(range(25))
    swaps = [[0,8],[7,12]]
    for i,j in swaps:
        order[i],order[j] = order[j],order[i]
    literal_order = [8,1,2,3,4,5,6,12,0,9,10,11,7,13,14,15,16,17,18,19,20,21,22,23,24]
    original('exact two-transposition order', order, literal_order)
    original('intact permutation', sorted(order), list(range(25)))
    original('fixed large-tail final row', [order[-1],rows[order[-1]]['a']], [24,166504412])
    nonzero = dict(delta='Delta>0 by L055: N log(2)-K log(3)>10584/10^14>0; totals unchanged.',
                   numerator='Phi>0 by L056 positive integral offsets and L057 positive chronological weights.',
                   justification='Each J,H>0, 27>16 and 3>2; 11 divides 27^J-16^J. All weights are positive.')
    lo2,hi2 = log_interval(2)
    lo3,hi3 = log_interval(3)
    low, high = N*lo2-K*hi3, N*hi2-K*lo3
    check('positive Lambda lower bound', low > Fraction(10584,10**14), True)
    check('Lambda upper bound', high < Fraction(10585,10**14), True)
    positive_evidence = dict(log2=[str(lo2),str(hi2)],log3=[str(lo3),str(hi3)],
                             Lambda=[str(low),str(high)], required=['10584/100000000000000','10585/100000000000000'])
    text = LEMMA.read_text()
    written = [list(map(int,line.split('|')[1:-1])) for line in text.splitlines()
               if re.fullmatch(r'\|(?:\d+\|){7}',line)]
    check('written table rows', len(written), 50)
    primality, evaluations, normalized, tables, reduced_pair = {}, {}, {}, {}, {}
    for p, expected_phi, expected_delta, expected_sum in ((5,20,5,245),(431,2586,40514,2417479)):
        m = p*p
        trials = [dict(divisor=d,remainder=p%d) for d in range(2,isqrt(p)+1)]
        prime = p>=2 and all(t['remainder']!=0 for t in trials)
        original(f'p={p}: complete trial-divisor primality', prime, True)
        check(f'p={p}: exact square-root guard', isqrt(p)**2<=p<(isqrt(p)+1)**2, True)
        primality[str(p)] = dict(base=p,floor_sqrt=isqrt(p),trials=trials,prime=prime)
        inv = (m+1)//2
        check(f'm={m}: inverse two', 2*inv%m, 1)
        odd, even = (3*inv%m,inv),(inv,0)
        block = (1,0)
        for letter in (odd,odd,even,odd):
            block = after(letter,block,m)
        original(f'm={m}: OOEO block', recover(block,4,m), [27%m,23%m,16%m])
        words, normal_words = [], []
        for r in rows:
            i,j,h,tail = r['i'],r['J'],r['H'],r['a']
            f = after(repeat(even,tail,m),after(repeat(odd,h,m),repeat(block,j,m),m),m)
            normal_words.append(f)
            triple = recover(f,r['D'],m)
            lifted = (pow(27,j,11*m)-pow(16,j,11*m))%(11*m)
            original(f'm={m} row={i}: lifted difference divisible by 11', lifted%11, 0)
            offset = (23*pow(3,h,m)*(lifted//11)+(pow(3,h,m)-pow(2,h,m))*pow(16,j,m))%m
            closed = [pow(3,r['k'],m),offset,pow(2,r['D'],m)]
            original(f'm={m} row={i}: independent word triple', triple, closed)
            words.append(dict(index=i,lifted_modulus=11*m,lifted_difference=lifted,
                              lifted_quotient=lifted//11,closed_triple=closed,composed_triple=triple))
        f, trace, normal_trace, table = (1,0), [], [], []
        for pos,i in enumerate(order):
            t = sum(rows[v]['D'] for v in order[:pos])
            u = sum(rows[v]['k'] for v in order[pos+1:])
            pref_k = sum(rows[v]['k'] for v in order[:pos+1])
            total_d = t+rows[i]['D']
            original(f'm={m} position={pos}: suffix exponent', K-pref_k, u)
            two,three = pow(2,t,m),pow(3,u,m)
            term = recover(normal_words[i],rows[i]['D'],m)[1]*two*three%m
            previous = recover(f,t,m)
            f = after(normal_words[i],f,m)
            state = recover(f,total_d,m)
            trace.append(dict(position=pos,index=i,prefix_N=t,suffix_K=u,prefix_two=two,
                              suffix_three=three,term=term,previous_triple=previous,resulting_triple=state))
            normal_trace.append(list(f))
            table.append([pos,i,words[i]['closed_triple'][1],two,three,term,state[1]])
            original(f'm={m} position={pos}: composed prefix powers', [state[0],state[2]],
                     [pow(3,pref_k,m),pow(2,total_d,m)])
        term_sum = sum(r['term'] for r in trace)
        phi, two_total, three_total = term_sum%m,pow(2,N,m),pow(3,K,m)
        delta = (two_total-three_total)%m
        original(f'm={m}: complete dual-method numerator', state[1], phi)
        original(f'm={m}: final total exponents', [pref_k,total_d], [K,N])
        original(f'm={m}: full composed triple', state, [three_total,phi,two_total])
        original(f'm={m}: inherited common zeros', [phi%p,delta%p], [0,0])
        check(f'm={m}: claimed complete sum/residues', [term_sum,phi,delta], [expected_sum,expected_phi,expected_delta])
        check(f'p={p}: exact integer valuations one', [0<phi<m,0<delta<m,phi%p,delta%p], [True,True,0,0])
        # This conclusion applies to the actual positive integer pair by the
        # prime valuation rule, not by taking gcd of modular representatives.
        reduced_pair[str(p)] = dict(original_numerator_valuation=1,original_denominator_valuation=1,
                                    gcd_valuation=1,reduced_numerator_valuation=0,reduced_denominator_valuation=0)
        evaluations[str(m)] = dict(base=p,modulus=m,words=words,trace=trace,term_sum=term_sum,phi=phi,
                                   two_total=two_total,three_total=three_total,delta=delta,final_triple=state,
                                   numerator_valuation='=1',denominator_valuation='=1',verdict='DENOMINATOR_PRIME_CANCELS')
        start = 0 if p==5 else 25
        compare(f'written m={m}',written[start:start+25],table)
        normalized[str(m)] = dict(words=[list(v) for v in normal_words],prefixes=normal_trace)
        tables[str(m)] = table
    check('written trial divisors at 431', list(map(int,re.search(r'^d: +(.*)$',text,re.M).group(1).split())), list(range(2,21)))
    check('written trial remainders at 431', list(map(int,re.search(r'^r: +(.*)$',text,re.M).group(1).split())), [431%d for d in range(2,21)])
    summary = dict(verdict='NO_STRICT_DENOMINATOR_EXCESS_CERTIFIED',decisive_primes=[],actual_precision=2,
                   required_precision=2,moduli=[25,185761],rows_per_modulus=25,checks=len(original_checks),failures=0,
                   residues={m:{k:v[k] for k in ('phi','two_total','three_total','delta','numerator_valuation','denominator_valuation','verdict')}
                             for m,v in evaluations.items()})
    expected = dict(target="Test L060's fixed two-transposition root modulo 25 and 185761 for a strict numerator/denominator valuation mismatch.",
                    inputs=inputs,parameters=rows,counts=counts,order=order,swaps=swaps,nonzero=nonzero,
                    primality=primality,evaluations=evaluations,checks=original_checks,failures=[],summary=summary)
    compare('complete original certificate',json.loads(CERT.read_text()),expected)
    check('original check count',len(original_checks),223)
    audit_summary = dict(verdict='FAIL' if failures else 'PASS',checks=len(checks),failures=len(failures),
                         original_checks=223,rows_per_modulus=25,moduli=[25,185761],actual_precision=2,required_precision=2,
                         residues=summary['residues'],reduced_pair=reduced_pair,
                         required_test='strict denominator valuation excess',actual_test='equal exact valuations one at both primes')
    OUT.write_text(json.dumps(dict(summary=audit_summary,original_certificate_sha256=hashlib.sha256(CERT.read_bytes()).hexdigest(),
                                   independent_reconstruction=expected,normalized=normalized,written_tables=tables,
                                   positive_evidence=positive_evidence,checks=checks,failures=failures),indent=2)+'\n')
    print(json.dumps(audit_summary,sort_keys=True))
    print('Certificate: '+str(OUT.relative_to(ROOT)))
    if failures:
        print('Failures: '+json.dumps(failures))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
