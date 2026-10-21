#!/usr/bin/env python3
"""Independent L060 audit: consume the recorded prefix; never extend its search."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations, chain, product
from math import comb
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = ROOT/'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
LEMMA = ROOT/'lemmas/L060-two-transposition-joint-prime-nonvanishing-stop.md'
CERT = HERE/'joint-prime-two-transposition-certificate.json'
WRITTEN = HERE/'joint-prime-written-table-check.json'
OUT = HERE/'joint-prime-witness-audit-certificate.json'
K, N = 397573379, 630138897
checks, failures = [], []


def check(name, actual, required):
    item = dict(name=name, actual=actual, required=required)
    checks.append(item)
    if actual != required:
        failures.append(item)


def after(f, g, m):
    # Normalized maps: f(g(x)), with no denominator coordinate.
    return (f[0]*g[0] % m, (f[0]*g[1]+f[1]) % m)


def repeat(f, n, m):
    value = (1, 0)
    while n:
        if n & 1:
            value = after(f, value, m)
        f = after(f, f, m)
        n >>= 1
    return value


def recover(f, length, m):
    q = pow(2, length, m)
    return [f[0]*q % m, f[1]*q % m, q]


def log_interval(x):
    z = Fraction(x-1, x+1)
    lo = 2*sum((z**(2*j+1)/(2*j+1) for j in range(64)), Fraction(0))
    return lo, lo+2*z**129/(129*(1-z*z))


def main():
    source = SOURCE.read_text()
    pairs = [(8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
             (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
             (8224,39104),(15494,73672),(29191,138802),(54998,261511),
             (103621,492705),(195229,928293),(367827,1748976),
             (693015,3295208),(1305695,6208431),(2460032,11697176),
             (4634896,22038409),(8732512,41522114),(16452748,78230965),
             (30998279,32670621)]
    parsed = [list(map(int, s.split('|')[1:-1])) for s in source.splitlines()
              if re.fullmatch(r'\|\d+\|\d+\|\d+\|', s)]
    check('all canonical input rows', parsed, [[i,*p] for i,p in enumerate(pairs)])
    rows = [dict(i=i,J=j,H=h,a=2 if i<24 else 166504412,
                 k=3*j+h,D=4*j+h+(2 if i<24 else 166504412))
            for i,(j,h) in enumerate(pairs)]
    expected_checks = []

    def original(name, actual, required):
        expected_checks.append(dict(name=name,actual=actual,required=required))
        check('independent original check: '+name, actual, required)

    original('literal indices', [r[0] for r in parsed], list(range(25)))
    original('tail prescriptions', ['For 0<=i<24 set a_i=2;' in source,
             'set a_24=166504412=' in source], [True,True])
    original('allocation sums', [sum(r[f] for r in rows) for f in ['J','H','a']],
             [66061058,199390205,166504460])
    original('total exponents', [sum(r[f] for r in rows) for f in ['k','D']], [K,N])
    words, normal, denominator = {}, {}, {}
    for m in (5,431):
        inv = (m+1)//2
        check(f'm={m}: inverse two', 2*inv % m, 1)
        odd, even = (3*inv % m,inv), (inv,0)
        block = after(odd,after(even,after(odd,odd,m),m),m)
        original(f'm={m}: OOEO', recover(block,4,m), [27%m,23%m,16%m])
        words[str(m)], normal[m] = [], []
        for r in rows:
            i,j,h,a = (r[f] for f in ['i','J','H','a'])
            f = after(repeat(even,a,m),after(repeat(odd,h,m),repeat(block,j,m),m),m)
            triple = recover(f,r['D'],m)
            lift = (pow(27,j,11*m)-pow(16,j,11*m)) % (11*m)
            original(f'm={m} row={i}: lifted quotient', lift%11, 0)
            c = (23*pow(3,h,m)*(lift//11)+(pow(3,h,m)-pow(2,h,m))*pow(16,j,m)) % m
            closed = [pow(3,r['k'],m),c,pow(2,r['D'],m)]
            original(f'm={m} row={i}: two evaluations', triple, closed)
            words[str(m)].append(dict(index=i,lifted_difference=lift,lifted_quotient=lift//11,
                                     closed_triple=closed,composed_triple=triple))
            normal[m].append(f)
        two,three = pow(2,N,m),pow(3,K,m)
        denominator[str(m)] = dict(two_total=two,three_total=three,delta=(two-three)%m)
        original(f'm={m}: denominator zero', (two-three)%m, 0)

    def evaluate(order,m):
        f = (1,0)
        for i in order:
            f = after(normal[m][i],f,m)
        t,used_k,total = 0,0,0
        for i in order:
            r = rows[i]
            used_k += r['k']
            c = words[str(m)][i]['closed_triple'][1]
            total += c*pow(2,t,m)*pow(3,K-used_k,m)
            t += r['D']
        return recover(f,N,m), total%m

    identity = list(range(25))
    for name,order,wanted in [('literal',identity,[4,240]),
            ('L057 swap',[6,1,2,3,4,5,0]+list(range(7,25)),[0,240])]:
        original(f'{name}: known residues', [evaluate(order,m)[0][1] for m in (5,431)],wanted)
    # Independently reconstruct exactly the reported sequence prefix. This is
    # bookkeeping validation, with no candidate after the reported stop tested.
    saved = json.loads(CERT.read_text())
    swaps = list(combinations(range(24),2))
    sequences = chain([()], ((s,) for s in swaps), product(swaps,repeat=2))
    records, comparisons, seen, duplicate = [], [], set(), 0
    for ordinal,sequence in enumerate(sequences,1):
        order = identity[:]
        for a,b in sequence:
            order[a],order[b] = order[b],order[a]
        key = tuple(order)
        if key in seen:
            duplicate += 1
        else:
            seen.add(key)
            residues = []
            for m in (5,431):
                state,weighted = evaluate(order,m)
                required = [denominator[str(m)]['three_total'],weighted,denominator[str(m)]['two_total']]
                item = dict(sequence_number=ordinal,modulus=m,actual=state,required=required)
                comparisons.append(item)
                if state != required:
                    failures.append(dict(name='recorded-order comparison',**item))
                residues.append(state[1])
            records.append(dict(sequence=[list(s) for s in sequence],order=order,residues=residues))
        if ordinal == 2354:
            break
    check('all 4580 recorded-order comparisons', sum(x['actual']==x['required'] for x in comparisons),4580)
    check('no earlier common zero in recorded prefix',
          [i for i,r in enumerate(records) if r['residues']==[0,0]],[2289])
    witness = records[-1]
    order = [8,1,2,3,4,5,6,12,0,9,10,11,7,13,14,15,16,17,18,19,20,21,22,23,24]
    check('specified witness membership',witness,dict(sequence=[[0,8],[7,12]],order=order,residues=[0,0]))
    original('witness intact multiplicities',sorted(order),identity)
    original('witness final index',order[-1],24)
    original('witness closing tail',rows[order[-1]]['a'],166504412)
    traces, normalized_traces = {}, {}
    for m in (5,431):
        f,t,used_k,term_sum = (1,0),0,0,0
        trace, normalized_trace = [], []
        for p,i in enumerate(order):
            r = rows[i]
            u = K-used_k-r['k']
            check(f'm={m} position={p}: exponents',[t,u],
                  [sum(rows[v]['D'] for v in order[:p]),sum(rows[v]['k'] for v in order[p+1:])])
            two,three = pow(2,t,m),pow(3,u,m)
            term = words[str(m)][i]['closed_triple'][1]*two*three%m
            previous = recover(f,t,m)
            f = after(normal[m][i],f,m)
            result = recover(f,t+r['D'],m)
            trace.append(dict(position=p,index=i,prefix_N=t,suffix_K=u,
                **{k:v for k,v in words[str(m)][i].items() if k!='index'},
                prefix_two=two,suffix_three=three,term=term,previous_triple=previous,resulting_triple=result))
            normalized_trace.append(dict(index=i,word=list(normal[m][i]),prefix=list(f)))
            t += r['D']
            used_k += r['k']
            term_sum += term
            original(f'm={m} position={p}: partial powers',[result[0],result[2]],
                     [pow(3,used_k,m),pow(2,t,m)])
        original(f'm={m}: witness independent weighted zero',[term_sum%m,result[1]],[0,0])
        traces[str(m)] = dict(trace=trace,term_sum=term_sum,final_triple=result,**denominator[str(m)])
        normalized_traces[str(m)] = normalized_trace
        check(f'm={m}: totals and sums',[t,used_k,term_sum,result],
              [N,K,45 if m==5 else 6034,[2,0,2] if m==5 else [108,0,108]])
    summary = dict(verdict='COMMON_ZERO_STOP',moduli=[5,431],sequences_actual=2354,
        sequences_required=1+276+276**2,unique_orders_actual=len(seen),
        unique_orders_required_for_exhaustion=1+comb(24,2)+2*comb(24,3)+3*comb(24,4),
        duplicate_sequences=duplicate,evaluations=len(comparisons),per_order_comparison_failures=0,
        checks=len(expected_checks),failures=0,exhaustive=False)
    expected = dict(target="Test joint modulo-5 and modulo-431 nonvanishing for all orders obtained from L055's literal order by at most two transpositions among indices 0 through 23.",
        source=str(SOURCE.relative_to(ROOT)),source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        parameters=rows,counts=dict(K=K,N=N),word_evidence=words,denominator=denominator,
        summary=summary,witness=witness,witness_evidence=traces,search_records=records,
        checks=expected_checks,failures=[])
    for key in expected:
        check('complete original field /'+key,saved.get(key),expected[key])
    check('original complete key set',sorted(saved),sorted(expected))
    # Rebuild the entire ten-comparison transcription certificate from the
    # independently computed traces and the complete two written tables.
    transcription = []
    lemma = LEMMA.read_text()
    for m,wanted_sum in ((5,45),(431,6034)):
        part = lemma.split(f'Modulo {m}:\n',1)[1]
        part = part.split('Modulo 431:',1)[0] if m==5 else part.split('The contribution sums',1)[0]
        written = [list(map(int,s.split('|')[1:-1])) for s in part.splitlines()
                   if re.fullmatch(r'\|(?:\d+\|){7}',s)]
        ev = traces[str(m)]
        required = [[r['position'],r['index'],r['closed_triple'][1],r['prefix_two'],
                     r['suffix_three'],r['term'],r['resulting_triple'][1]] for r in ev['trace']]
        for name,actual,wanted in [
            (f'm={m}: all written entries',written,required),
            (f'm={m}: table size',len(written),25),
            (f'm={m}: intact multiplicities',sorted(r[1] for r in written),identity),
            (f'm={m}: term sums',[sum(r[5] for r in written),ev['term_sum']],[wanted_sum]*2),
            (f'm={m}: common zeros',[sum(r[5] for r in written)%m,written[-1][6],ev['delta']],[0,0,0])]:
            transcription.append(dict(name=name,actual=actual,required=wanted))
            check('independent transcription: '+name,actual,wanted)
    check('complete original transcription certificate',json.loads(WRITTEN.read_text()),
          dict(checks=transcription,failures=[]))
    l2,l3 = log_interval(2),log_interval(3)
    lo,hi = N*l2[0]-K*l3[1],N*l2[1]-K*l3[0]
    check('positive Delta input: lower Lambda',lo>Fraction(10584,10**14),True)
    check('positive Delta input: upper Lambda',hi<Fraction(10585,10**14),True)
    files = [SOURCE,LEMMA,CERT,WRITTEN,HERE/'test_joint_prime_two_transpositions.py',
             HERE/'check_joint_prime_written_tables.py']
    result = dict(target="Critically audit L060's two-transposition common-zero witness and the stop of the joint modulo-5/modulo-431 nonvanishing diagnostic.",
        method='Independent normalized affine pairs, right-to-left powers, separately transcribed allocation; full original evidence comparison',
        input_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
        normalized_traces=normalized_traces,complete_witness=traces,
        recorded_order_comparisons=comparisons,
        lambda_bounds=dict(lower=str(lo),upper=str(hi),terms=64,
                           required_lower='10584/100000000000000',required_upper='10585/100000000000000'),
        checks=checks,failures=failures,
        summary=dict(verdict='FAIL' if failures else 'AUDIT_PASS',checks=len(checks),failures=len(failures),
                     original_checks=len(expected_checks),transcription_checks=len(transcription),
                     witness_rows=50,recorded_orders=len(records),per_order_comparisons=len(comparisons),
                     sequences=2354,duplicates=duplicate,exhaustive=False,
                     residues=[traces[str(m)]['final_triple'] for m in (5,431)],
                     term_sums=[traces[str(m)]['term_sum'] for m in (5,431)]))
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summary'],sort_keys=True))
    print('Required: 50 witness rows, 165 original checks, 10 transcription checks, 4580 recorded-order comparisons; zero mismatches.')
    print('Actual/required sums: 45/45 and 6034/6034; common-zero triples: (2,0,2) and (108,0,108).')
    print('Required strict Lambda interval: (10584/10^14,10585/10^14); actual exact bounds saved; checks:',lo>Fraction(10584,10**14),hi<Fraction(10585,10**14))
    print('Partial sequence coverage: 2354/76453; distinct orders: 2290/36203; no exhaustion claimed.')
    print('Failures:',[r['name'] for r in failures])
    print('Certificate:',OUT.relative_to(ROOT))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
