#!/usr/bin/env python3
"""Consume complete block/divisor evidence and report exact rational bounds.

This checks evidence completeness and arithmetic totals, not an independent
critical audit of the full proof or the 25,983,188-divisor moment producer.
"""
from fractions import Fraction as F
from pathlib import Path
import csv
import hashlib
import json
import struct

ROOT = Path(__file__).resolve().parent
NAME = 'complementary-mass'
Q = 1 << 56


def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def pair(a):
    a = list(map(int, a))
    assert a[0] <= a[1]
    return a


def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v)//Q, -((-max(v))//Q)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[1], a[1]-b[0]


def outward_decimal(q, upper, places=20):
    z = q*10**places
    v = -((-z.numerator)//z.denominator) if upper else z.numerator//z.denominator
    return f'{v//10**places}.{v%10**places:0{places}d}'


def main():
    seed = json.loads((ROOT/(NAME+'-seeds.json')).read_text())
    moments = json.loads((ROOT/(NAME+'-moments.json')).read_text())
    result = json.loads((ROOT/(NAME+'-result.json')).read_text())
    assert not seed['failures'] and not moments['failures'] and not result['failures']
    assert seed['Q'] == int(moments['Q']) == int(result['Q']) == Q
    N, H, T = seed['N'], seed['H'], seed['exp_floor']
    assert N == 691004 and H == 110560640 and T == 31720474772
    assert moments['N'] == N and moments['H'] == H and moments['T_floor'] == T
    for field in ('seeds', 'config'):
        assert sha(ROOT/seed[field]['path']) == seed[field]['sha256']
    assert (ROOT/seed['seeds']['path']).stat().st_size == 32*N
    assert sha(ROOT/seed['source_ledger']['path']) == seed['source_ledger']['sha256']
    assert seed['source_ledger']['rows'] == N
    q30 = 10**30
    exp_interval = pair(seed['exp_ell_grid30'])
    assert exp_interval[0]//q30 == exp_interval[1]//q30 == T > H
    ell = F('24.18022820120389')
    fac = pair(seed['two_over_ell_grid56'])
    assert F(fac[0], Q) <= 2/ell <= F(fac[1], Q)
    # Recompute every prefix moment from all input rows.
    A = B = (0, 0)
    seed_primes = {}
    with (ROOT/(NAME+'-seeds.bin')).open('rb') as f:
        for n in range(1, N+1):
            al, ah, ll, lh = struct.unpack('<qqqq', f.read(32))
            assert 0 <= al <= ah and 0 <= ll <= lh
            A = add(A, (al, ah))
            B = add(B, mul((al, ah), (ll, lh)))
            if n <= 307:
                seed_primes[n] = (al, ah, ll, lh)
        assert not f.read(1)
    assert A == tuple(pair(moments['A_N'])) and B == tuple(pair(moments['B_N']))
    config = (ROOT/(NAME+'-config.txt')).read_text().splitlines()
    assert list(map(int,config[0].split())) == [Q,N,H,T,*fac]
    primes = []
    for line in config[1:]:
        p, al, ah, ll, lh = map(int,line.split())
        assert seed_primes[p] == (al, ah, ll, lh)
        primes.append((p,(al, ah),(ll, lh)))
    expected_primes = [p for p in range(2,308) if all(p%d for d in range(2, int(p**.5)+1))]
    assert [p for p,_,_ in primes] == expected_primes
    # Recompute all Euler moments using the exact interval recurrence.
    R, RL = (Q,Q),(0,0)
    for p,r,lp in primes:
        RL = add(mul(RL,add((Q,Q),r)),mul(R,mul(r,lp)))
        R = mul(R,add((Q,Q),r))
    assert R == tuple(pair(moments['R'])) and RL == tuple(pair(moments['Rlog']))
    rres = sub(R,pair(moments['enumerated_R']))
    lres = sub(RL,pair(moments['enumerated_Rlog']))
    rres = max(0,rres[0]),rres[1]
    lres = max(0,lres[0]),lres[1]
    assert rres == tuple(pair(moments['residual_R']))
    assert lres == tuple(pair(moments['residual_Rlog']))
    far = sub(mul(fac,add(mul(A,lres),mul(B,rres))),mul(A,rres))
    far = max(0,far[0]),far[1]
    assert far == tuple(pair(moments['far_tail']))
    tail = add(pair(moments['clipped_tail']),far)
    assert tail == tuple(pair(moments['positive_tail'])) == tuple(pair(result['positive_tail']))
    # Replay the entire edge divisor stream with an independent recursion
    # pruned at H rather than T. Every stored product and radius is checked.
    depthcounts = [0]*64
    divisor_rows = expected_updates = 0
    with (ROOT/(NAME+'-divisors.bin')).open('rb') as f:
        def visit(start, d, r, sign, depth):
            nonlocal divisor_rows, expected_updates
            row = f.read(32)
            assert len(row) == 32
            assert struct.unpack('<qqqq',row) == (d,*r,sign)
            divisor_rows += 1
            depthcounts[depth] += 1
            expected_updates += max(0,min(N,H//d)-N//d)
            for j in range(start,len(primes)):
                p,rp,_ = primes[j]
                if d > H//p:
                    break
                visit(j+1,d*p,mul(r,rp),-sign,depth+1)
        visit(0,1,(Q,Q),1,0)
        assert not f.read(1)
    assert divisor_rows == moments['divisors_le_H']
    assert sum(moments['depth_counts']) == moments['divisors_le_T']
    assert all(a<=b for a,b in zip(depthcounts,moments['depth_counts']))
    edge = (0,0)
    first, updates, positive, negative, straddling, width, blocks = N+1,0,0,0,0,0,0
    with (ROOT/(NAME+'-blocks.tsv')).open() as f:
        for row in csv.DictReader(f,delimiter='\t'):
            row = {k:int(v) for k,v in row.items()}
            assert row['first'] == first and first<=row['last']<=H
            assert row['last'] == min(H,first+1000000-1)
            assert row['positive']+row['negative']+row['straddling'] == row['last']-first+1
            assert 0<=row['lower']<=row['upper'] and row['max_width']>=0
            edge = add(edge,(row['lower'],row['upper']))
            updates += row['updates']
            positive += row['positive']; negative += row['negative'];straddling += row['straddling']
            width = max(width,row['max_width']); blocks += 1
            first = row['last']+1
    assert first == H+1 and blocks == 110
    assert edge == tuple(pair(result['edge']))
    assert updates == expected_updates == result['channel_updates']
    assert result['rows'] == H-N == positive+negative+straddling
    assert [positive,negative,straddling,width] == [result[k] if k!='max_coefficient_width' else int(result[k])
                                                  for k in ('positive','negative','straddling','max_coefficient_width')]
    complement = add(edge,tail)
    assert complement == tuple(pair(result['complement_majorant']))
    threshold = F('.301408572679396256667379418689')
    assert int(result['threshold_floor_grid']) == (threshold*Q).__floor__()
    passed = F(complement[1],Q) < threshold
    assert result['provisional_pass'] == (complement[1] < (threshold*Q).__floor__())
    prefix = json.loads((ROOT/'finite-prefix-certificate.json').read_text())
    assert F(prefix['inputs']['t']) == F('.16836')
    assert F(prefix['inputs']['x']) == F('6000284561421.5')
    assert F(prefix['inputs']['ell0']) == ell and prefix['inputs']['prime_limit'] == 307
    prefix_hi = F(int(prefix['result']['prefix_interval_grid'][1]),10**30)
    assert 1-prefix_hi == threshold
    assert prefix_hi+F(complement[1],Q) < F('.999577507')
    assert threshold-F(complement[1],Q) > F('.00042249')
    report = dict(scope='Complete fixed-corner majorant, known-method reproduction; not charges or RH',
        Q=str(Q), target_threshold=str(threshold),
        actual_complement_upper=str(F(complement[1],Q)), strict_pass=passed,
        margin_lower=str(threshold-F(complement[1],Q)),
        combined_prefix_upper=str(prefix_hi+F(complement[1],Q)),
        combined_coarse_upper='.999577507', combined_margin_strict_lower='.00042249',
        edge_decimal=[outward_decimal(F(edge[0],Q),False),outward_decimal(F(edge[1],Q),True)],
        tail_decimal=[outward_decimal(F(tail[0],Q),False),outward_decimal(F(tail[1],Q),True)],
        majorant_decimal=[outward_decimal(F(complement[0],Q),False),outward_decimal(F(complement[1],Q),True)],
        enclosure_width=str(F(complement[1]-complement[0],Q)),
        complete_evidence=dict(seed_rows=N, edge_rows=H-N,blocks=blocks,
                               edge_divisors=divisor_rows,moment_divisors=moments['divisors_le_T'],
                               channel_updates=updates,edge_depth_counts=depthcounts),
        qualifications=['L497 proof/code critical audit pending','Full moment enumeration not independently replayed',
                        'Producer proof/code and binary format require separate critical audit',
                        'Majorant enclosure lower endpoint is not a lower bound for C_N',
                        'Base-phase/saddle imports retain their qualifications; strict charges and uniform transport open'],
        evidence=[dict(path=p.name,sha256=sha(p)) for p in (
            ROOT/(NAME+'-seeds.py'),ROOT/(NAME+'.cpp'),Path(__file__),
            ROOT/(NAME+'-seeds.json'),ROOT/(NAME+'-seeds.bin'),ROOT/(NAME+'-config.txt'),
            ROOT/(NAME+'-divisors.bin'),ROOT/(NAME+'-blocks.tsv'),
            ROOT/(NAME+'-moments.json'),ROOT/(NAME+'-result.json'))], failures=[])
    out = ROOT/(NAME+'-verification.json')
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(f'Complete edge: {report["edge_decimal"]}; full positive tail: {report["tail_decimal"]}')
    print(f'Majorant <= {report["majorant_decimal"][1]}; required < {threshold}; pass={passed}; failures=0')
    print(f'Width={report["enclosure_width"]}; margin >= {report["margin_lower"]}; all {H-N} edge rows, {divisor_rows} edge divisors checked')
    print(f'Full certificate: {out.relative_to(ROOT.parent.parent)}; mathematical critical audit remains pending')


if __name__ == '__main__':
    main()
