#!/usr/bin/env python3
"""Independent complete L057 audit using permutations of F_5, not triples."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'fixed-allocation-permutation-audit-certificate.json'
K, N = 397573379, 630138897
IDENTITY = list(range(5))
O = [(3*x+1)*3 % 5 for x in IDENTITY]  # 3 = inverse of 2 modulo 5
E = [x*3 % 5 for x in IDENTITY]


def followed_by(first, second):
    return [second[first[x]] for x in IDENTITY]


def power_by_cycles(mapping, exponent):
    assert sorted(mapping) == IDENTITY and exponent >= 0
    result = []
    for x in IDENTITY:
        cycle = [x]
        y = mapping[x]
        while y != x:
            assert y not in cycle
            cycle.append(y)
            y = mapping[y]
        result.append(cycle[exponent % len(cycle)])
    return result


def recover(mapping, length):
    q = [1, 2, 4, 3][length % 4]
    a, c = q*(mapping[1]-mapping[0]) % 5, q*mapping[0] % 5
    assert all(q*mapping[x] % 5 == (a*x+c) % 5 for x in IDENTITY)
    return [a, c, q]


def main():
    source = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
    raw = source.read_bytes()
    text = raw.decode()
    allocation = []
    for line in text.splitlines():
        cells = line.strip('|').split('|')
        if len(cells) == 3 and all(c.isdigit() for c in cells):
            allocation.append(tuple(map(int, cells)))
    assert [r[0] for r in allocation] == list(range(25))
    assert 'For 0<=i<24 set a_i=2; set a_24=166504412=' in text
    # Independent literal transcription of the canonical allocation.
    literal_pairs = [(8,40),(15,72),(28,134),(52,249),(98,467),
        (184,877),(347,1650),(653,3106),(1230,5849),(2317,11018),
        (4365,20756),(8224,39104),(15494,73672),(29191,138802),
        (54998,261511),(103621,492705),(195229,928293),
        (367827,1748976),(693015,3295208),(1305695,6208431),
        (2460032,11697176),(4634896,22038409),(8732512,41522114),
        (16452748,78230965),(30998279,32670621)]
    assert [(j,h) for _,j,h in allocation] == literal_pairs
    checks, failures, reconstructed_checks = [], [], []

    def check(name, actual, required):
        record = dict(name=name, actual=actual, required=required)
        checks.append(record)
        if actual != required:
            failures.append(record)

    def original_check(name, actual, required):
        record = dict(name=name, actual=actual, required=required)
        reconstructed_checks.append(record)
        check('independent '+name, actual, required)

    original_check('indices', [r[0] for r in allocation], list(range(25)))
    original_check('short-tail source statement', True, True)
    original_check('large-tail source statement', True, True)
    block = IDENTITY
    for letter in [O, O, E, O]:
        block = followed_by(block, letter)
    check('OOEO recovered from individual letters', recover(block, 4), [2,3,1])
    rows, maps = [], []
    for i, j, h in allocation:
        a = 2 if i < 24 else 166504412
        k, length = 3*j+h, 4*j+h+a
        f = followed_by(followed_by(power_by_cycles(block, j),
             power_by_cycles(O, h)), power_by_cycles(E, a))
        triple = recover(f, length)
        p2, p3 = [1,2,4,3], [1,3,4,2]
        c = (3*p3[h % 4]*(p2[j % 4]-1)+p3[h % 4]-p2[h % 4]) % 5
        direct = [p3[k % 4], c, p2[length % 4]]
        original_check(f'word {i}: compressed / closed formula', triple, direct)
        rows.append(dict(i=i,J=j,H=h,a=a,k=k,length=length,
                         A=triple[0],C=triple[1],Q=triple[2]))
        maps.append(f)
    original_check('total odd count', sum(r['k'] for r in rows), K)
    original_check('total length', sum(r['length'] for r in rows), N)
    denominator = (p2[N % 4]-p3[K % 4]) % 5
    original_check('denominator residue', denominator, 0)

    def evaluate(order):
        original_check('intact-index multiplicities', sorted(order), list(range(25)))
        f, trace = IDENTITY, []
        for pos, i in enumerate(order):
            t = sum(rows[b]['length'] for b in order[:pos])
            v = sum(rows[b]['k'] for b in order[:pos])
            u = sum(rows[b]['k'] for b in order[pos+1:])
            previous = recover(f, t)
            f = followed_by(f, maps[i])
            current = recover(f, t+rows[i]['length'])
            two, three = p2[t % 4], p3[u % 4]
            term = rows[i]['C']*two*three % 5
            trace.append(dict(position=pos,index=i,prefix_N=t,prefix_K=v,
                suffix_K=u,prefix_two=two,suffix_three=three,contribution=term,
                previous_triple=previous,resulting_triple=current))
        total_k = sum(rows[i]['k'] for i in order)
        total_n = sum(rows[i]['length'] for i in order)
        result = recover(f, total_n)
        term_sum = sum(r['contribution'] for r in trace)
        original_check('order totals', [total_k,total_n], [K,N])
        original_check('two whole-numerator evaluations', result[1], term_sum % 5)
        original_check('whole slope and denominator power', [result[0],result[2]],
                       [p3[K % 4],p2[N % 4]])
        return dict(order=order,numerator=result[1],weighted_sum=term_sum % 5,
                    contribution_sum=term_sum,total_triple=result,trace=trace)

    literal = evaluate(list(range(25)))
    original_check('literal numerator matches L056', literal['numerator'], 4)
    swaps, evaluations = [], []
    for j in range(1,7):  # Exactly the six recorded tests; no new diagnostic.
        order = list(range(25))
        order[0], order[j] = order[j], order[0]
        result = evaluate(order)
        swaps.append(dict(swap=[0,j],numerator=result['numerator']))
        evaluations.append(result)
    witness = dict(evaluations[-1], swap=[0,6])
    check('first zero is the sixth tested swap',
          [r['numerator'] == 0 for r in swaps], [False]*5+[True])
    summary = dict(verdict='UNIFORM_PRIME_FIVE_EXCLUSION_FAILS',modulus=5,
        maximum_swaps=300,swaps_tested=6,checks=len(reconstructed_checks),failures=0,
        denominator=denominator,witness_numerator=witness['numerator'],witness_swap=[0,6])
    expected = dict(target="Decide whether modulo 5 excludes every permutation of L055's 25 fixed word triples.",
        source='lemmas/'+source.name, source_sha256=hashlib.sha256(raw).hexdigest(),
        counts=dict(K=K,N=N),parameters=rows,literal=literal,tested_swaps=swaps,
        witness=witness,summary=summary,checks=reconstructed_checks,failures=[])
    original = json.loads((HERE/'fixed-allocation-permutation-mod-five-certificate.json').read_text())
    check('main certificate complete key set', sorted(original), sorted(expected))
    for key in expected:
        check('main certificate complete /'+key, original.get(key), expected[key])

    proof = (ROOT/'lemmas/L057-fixed-allocation-permutation-prime-five-stop.md').read_text()
    printed = [list(map(int, m)) for m in re.findall(
        r'^\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|$', proof, re.M)]
    table = [[r['position'],r['index'],rows[r['index']]['A'],rows[r['index']]['C'],
        rows[r['index']]['Q'],r['prefix_two'],r['suffix_three'],r['contribution']]
        for r in witness['trace']]
    check('all 25 printed rows', printed, table)
    transcription = dict(checks=[
        dict(name='complete written table',actual=printed,required=table),
        dict(name='term sum',actual=sum(r[-1] for r in printed),required=45),
        dict(name='exact 25 index multiplicities',actual=sorted(r[1] for r in printed),
             required=list(range(25)))],failures=[])
    saved = json.loads((HERE/'fixed-allocation-permutation-written-table-check.json').read_text())
    check('complete transcription certificate', saved, transcription)
    check('j=1 exact exponents', [witness['trace'][1]['prefix_N'],
                                witness['trace'][1]['suffix_K']], [3040,397570571])
    check('j=6 exact exponents', [witness['trace'][6]['prefix_N'],
                                witness['trace'][6]['suffix_K']], [6357,397567694])
    # Accumulated numerators differ; only exponents and weighted terms agree.
    suffix_fields = ['position','index','prefix_N','prefix_K','suffix_K',
                     'prefix_two','suffix_three','contribution']
    check('unchanged suffix exponents and contributions j>=7',
        [[r[k] for k in suffix_fields] for r in witness['trace'][7:]],
        [[r[k] for k in suffix_fields] for r in literal['trace'][7:]])
    OUT.write_text(json.dumps(dict(method='F5 permutation cycles, complete certificate comparison',
        branch_maps=dict(O=O,E=E,OOEO=block),word_maps=maps,
        reconstructed=expected,all_six_swap_evaluations=evaluations,
        written_table=table,checks=checks,failures=failures,
        summary=dict(checks=len(checks),failures=len(failures),numerator=witness['numerator'],
            denominator=denominator,contribution_sum=witness['contribution_sum'])),indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks),failures=len(failures),
        actual=[witness['numerator'],denominator,witness['contribution_sum']],
        required=[0,0,45])))
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        print('Failed checks: '+', '.join(r['name'] for r in failures))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
