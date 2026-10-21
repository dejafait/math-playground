#!/usr/bin/env python3
"""Independent full L080 audit; only t=0,1 and modulus 25.

No constructor import/execution. Generic matrices and explicitly checked
periods replace its binary triple powers. Original artifacts are read-only.
"""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'redistributed-h-survivors-mod25-audit-certificate.json'
SOURCE = HERE / 'redistributed-h-survivors-mod25-certificate.json'
TABLE = [
    (8,40), (15,72), (28,134), (52,249), (98,467), (184,877),
    (347,1650), (653,3106), (1230,5849), (2317,11018),
    (4365,20756), (8224,39104), (15494,73672), (29191,138802),
    (54998,261511), (103621,492705), (195229,928293),
    (367827,1748976), (693015,3295208), (1305695,6208431),
    (2460032,11697176), (4634896,22038409), (8732512,41522114),
    (16452748,78230965), (30998279,32670621)]
IDENTITY = [[1,0],[0,1]]
ODD, EVEN = [[3,1],[0,2]], [[1,0],[0,2]]
checks, failures = [], []


def check(name, actual, required):
    record = dict(name=name, actual=actual, required=required)
    checks.append(record)
    if actual != required:
        failures.append(record)


def multiply(left, right):
    return [[sum(left[i][k]*right[k][j] for k in range(2)) % 25
             for j in range(2)] for i in range(2)]


def triple(matrix):
    return [matrix[0][0], matrix[0][1], matrix[1][1]]


def scalar_powers(base):
    sequence = [1]
    for _ in range(20):
        sequence.append(sequence[-1]*base % 25)
    check(f'scalar {base} period', sequence[-1], 1)
    return sequence


def matrix_powers(base, name):
    sequence = [IDENTITY]
    for _ in range(20):
        sequence.append(multiply(base, sequence[-1]))
    check(f'matrix {name} period', sequence[-1], IDENTITY)
    return sequence


def main():
    raw = SOURCE.read_bytes()
    old = json.loads(raw)
    l055 = (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
    l080 = (ROOT / 'lemmas/L080-redistributed-h-survivors-prime-five-nonintegrality.md').read_text()
    parsed = [list(map(int, row)) for row in
              re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', l055, re.M)]
    check('all source pairs', parsed, [[i,j,h] for i,(j,h) in enumerate(TABLE)])
    for path, digest in old['sources'].items():
        check('source hash '+path, hashlib.sha256((ROOT/path).read_bytes()).hexdigest(), digest)
    check('saved failure list', old['failures'], [])
    check('saved check count', len(old['checks']), 65)
    for c in old['checks']:
        check('saved equality '+c['name'], c['actual'], c['required'])
    check('cases exactly 0 and 1', [c['t'] for c in old['cases']], [0,1])
    two, three = scalar_powers(2), scalar_powers(3)
    block = IDENTITY
    for letter in [ODD, ODD, EVEN, ODD]:
        block = multiply(letter, block)
    check('block matrix', block, [[2,23],[0,16]])
    powers = {name: matrix_powers(base, name) for name,base in
              [('O',ODD),('E',EVEN),('B',block)]}
    check('11 unit', 11*16 % 25, 1)
    printed = re.findall(r'^\|(\d+)\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|$', l080, re.M)
    check('printed residue rows', len(printed), 25)
    cases = []
    for t in (0,1):
        rows = []
        for i,(j,old_h) in enumerate(TABLE):
            h = old_h + (-1 if i == 0 else 1 if i == 24 else 0)
            beta = t if i == 23 else 9250245-t if i == 24 else 0
            a = 2+18*beta
            rows.append(dict(i=i,J=j,H=h,beta=beta,a=a,k=3*j+h,d=4*j+h+a))
        totals = [sum(r[key] for r in rows) for key in ['J','H','beta','a','k','d']]
        check(f'{t} totals', totals, [66061058,199390205,9250245,166504460,397573379,630138897])
        check(f'{t} row hypotheses', all(r['J']>=2 and r['H']>=3 and r['beta']>=0 and r['a']%18==2 for r in rows), True)
        check(f'{t} strict J order', all(rows[i]['J']<rows[i+1]['J'] for i in range(24)), True)
        k_total, n_total = totals[-2:]
        check(f'{t} stored counts', old['counts'], dict(K=k_total,N=n_total))
        state, trace, matrices = IDENTITY, [], []
        for i,row in enumerate(rows):
            j,h,a,k,d = [row[key] for key in ['J','H','a','k','d']]
            # Later maps multiply on the left. No binary-power routine.
            matrix = multiply(powers['E'][a%20], multiply(powers['O'][h%20], powers['B'][j%20]))
            prefix = sum(r['d'] for r in rows[:i])
            suffix = sum(r['k'] for r in rows[i+1:])
            # Coordinate form of F, independently expanded from 3^k eta.
            offset = (23*three[k%20] - 12*three[h%20]*two[(4*j)%20]
                      - 11*two[(h+4*j)%20])*16 % 25
            closed = [three[k%20], offset, two[d%20]]
            check(f'{t}/{i} matrix vs coordinate offset', triple(matrix), closed)
            before = state
            state = multiply(matrix, state)
            term = offset*two[prefix%20]*three[suffix%20] % 25
            record = dict(**row,prefix_N=prefix,suffix_K=suffix,offset=offset,
                          prefix_two=two[prefix%20],suffix_three=three[suffix%20],
                          contribution=term,closed_triple=closed,composed_triple=triple(matrix),
                          before_triple=triple(before),after_triple=triple(state))
            stored = old['cases'][t]['trace'][i]
            check(f'{t}/{i} exact field set', sorted(stored), sorted(record))
            for key,value in record.items():
                check(f'{t}/{i} {key}', stored[key], value)
            if len(printed)==25:
                actual = [int(cell.split('/')[t if '/' in cell else 0].strip()) for cell in printed[i]]
                check(f'{t}/{i} printed table', actual, [i,offset,two[prefix%20],three[suffix%20],term])
            trace.append(record)
            matrices.append(matrix)
        check(f'{t} full trace length', len(old['cases'][t]['trace']), 25)
        representative_sum = sum(r['contribution'] for r in trace)
        phi = representative_sum % 25
        p2,p3 = two[n_total%20],three[k_total%20]
        delta = (p2-p3)%25
        check(f'{t} full sum and composition', triple(state), [p3,phi,p2])
        check(f'{t} denominator powers', [n_total%20,k_total%20,p2,p3,delta], [17,19,22,17,5])
        check(f'{t} claimed Phi', phi, [16,7][t])
        check(f'{t} claimed representative sum', representative_sum, [341,332][t])
        check(f'{t} valuation premises', [phi%5 != 0,delta%5==0,delta!=0], [True,True,True])
        summary = dict(t=t,modulus=25,required_modulus=25,numerator=phi,
                       denominator=delta,numerator_valuation=0,numerator_valuation_lower_bound=0,
                       denominator_valuation=1,verdict='FIVE_SURVIVES_REDUCED_DENOMINATOR',
                       contribution_sum=representative_sum,total_triple=triple(state))
        check(f'{t} complete summary', old['cases'][t]['summary'], summary)
        tail_row = re.search(r'^\|'+str(t)+r'\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|$',l080,re.M)
        actual_tail = list(map(int,tail_row.groups())) if tail_row else None
        check(f'{t} printed tail lengths', actual_tail,
              [rows[23]['a'],rows[24]['a'],rows[23]['d'],rows[24]['d'],trace[24]['prefix_N']])
        cases.append(dict(t=t,trace=trace,matrices=matrices,summary=summary))
    certificate = dict(source_sha256=hashlib.sha256(raw).hexdigest(),
                       method='generic matrices, explicit period-20 cycles, coordinate-form offset',
                       scalar_cycles=dict(two=two,three=three),matrix_cycles=powers,
                       cases=cases,checks=checks,failures=failures,
                       summary=dict(checks=len(checks),failures=len(failures),rows=50,
                                    compositions=2,actual_modulus=25,required_modulus=25,
                                    pairs=[[c['summary']['numerator'],c['summary']['denominator']] for c in cases]))
    OUT.write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps(certificate['summary'],sort_keys=True))
    print('Required: every saved row field, printed table, composition and valuation premise agrees.')
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        print('Failure details are in certificate /failures.')
        raise SystemExit(1)


if __name__ == '__main__':
    main()
