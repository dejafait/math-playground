"""Audit saved factored evidence; never rerun the original-orbit enumeration.

Integer polynomial products reconstruct all h aggregates with no carry.
No constructor imports, optimizer, enlarged weight support or new search.
"""
import gzip
import hashlib
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from math import comb, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'capacitated-two-distance-critical-audit.json'
report = {'stage': 'in_progress', 'failures': [], 'checks_by_kind': {},
          'pair_checks': []}


def ck(kind, condition, detail=None):
    report['checks_by_kind'][kind] = report['checks_by_kind'].get(kind, 0) + 1
    if not condition:
        report['failures'].append({'kind': kind, 'detail': detail})
        raise AssertionError((kind, detail))


def enc(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def pack(values, indices, bits):
    return sum(v << (bits * k) for v, k in zip(values, indices))


def run():
    raw = gzip.decompress((B / 'capacitated-two-distance-results.json.gz').read_bytes())
    saved = json.loads(raw)
    digest = hashlib.sha256(raw).hexdigest()
    ck('preserved_source_hash', digest ==
       'c26d6d8d9ab453874f0aba97c81cd99049ba5fd8c65b122b2aad032c61b0be44')
    ck('original_bytes', hashlib.sha256((B / 'capacitated-two-distance-results.json').read_bytes()).hexdigest() == digest)
    ck('historical_failure', saved['stage'] == 'obstruction' and saved['failures'] == ['AssertionError()'])
    ck('lossless_storage', len(raw) > saved['caps']['output_bytes'] >
       (B / 'capacitated-two-distance-results.json.gz').stat().st_size)
    for path, sha in saved['input_sha256'].items():
        ck('input_hash', hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == sha, path)
    ck('constructor_hash', hashlib.sha256((B / 'capacitated_two_distance_test.py').read_bytes()).hexdigest() == saved['code_sha256'])
    report['source_sha256'] = digest
    report['input_sha256'] = saved['input_sha256']
    report['historical_failure'] = saved['failures']
    lp = json.loads((B / 'delsarte-lp-results.json').read_text())
    a = [Q(r['numerator'], r['denominator']) for r in lp['exact']['primal']]
    H, N = comb(1024, 68), 65537**28 // 2**128 + 1
    U = Q(comb(1024, 64), comb(68, 64))
    alpha = 2 * (N - 1) / (U - 1)
    g = [1]
    for i in range(68):
        g.append(g[-1] * (68-i) * (956-i) // (i+1)**2)
    ck('canonical_pairs', len(a) == 64 and min(a) > 0 and sum(a) == U-1)
    ck('canonical_pairs', N > 2 and 0 < alpha < 1)
    c = [Q(1)] + [Q(0)]*4 + [Q(N-1)*a[i-5]/((U-1)*g[i]) for i in range(5, 69)]
    q = lcm(*(z.denominator for z in c))
    P = [int(z*q) for z in c]
    for i in range(69):
        ck('shells', g[i] == comb(68, i)*comb(956, i), i)
        ck('pairs', saved['pair_numerators'][i] == P[i], i)
        ck('pair_demand', saved['edge_demands'][i] == (None if i == 0 else enc((N-2)*c[i])), i)
    ck('pair_sums', sum(g) == H and sum(g[i]*c[i] for i in range(69)) == N)
    ck('pair_signs', P[0] == q and P[1:5] == [0]*4 and all(0 < z < q for z in P[5:]))
    for key, val in dict(H=H, N=N, U=enc(U), alpha=enc(alpha), denominator=q, shell_sizes=g).items():
        ck('input_fields', saved[key] == val, key)

    # Every coefficient is nonnegative and <= g_i*g_j <= H^2.
    # Evaluation at 2^bits therefore encodes the exact convolution digits.
    bits = (H*H).bit_length()
    mask = (1 << bits)-1
    ck('no_carry_bound', (1 << bits) > H*H)
    count_bits = 13  # 2^13 > 69^2, hence also bounds count convolutions.
    count_mask = (1 << count_bits)-1
    ck('table_exhaustion', len(saved['coefficient_entries']) == 69**2)
    buckets = {(m,k): [0,0,0] for m in range(4) for k in range(4-m)}
    counts = Counter()
    rows = [[0,0,[]] for _ in range(69)]
    for pos, item in enumerate(saved['coefficient_entries']):
        i, j = divmod(pos, 69)
        ck('table_order', (item['i'], item['j']) == (i,j), pos)
        ts = list(range(max(0,i+j-68), min(i,j)+1))
        ss = list(range(max(0,i+j-956), min(i,j)+1))
        di = [comb(i,t)*comb(68-i,j-t) for t in ts]
        do = [comb(i,s)*comb(956-i,j-s) for s in ss]
        aa = [comb(68,i)*z for z in di]
        bb = [comb(956,i)*z for z in do]
        for key, val in [('t',ts),('s',ss),('D_inside',di),('D_outside',do),
                         ('source_inside',aa),('source_outside',bb)]:
            ck('factor_arrays', item[key] == val, [i,j,key])
        ck('vandermonde', sum(di) == comb(68,j) and sum(do) == comb(956,j), [i,j])
        polynomial = pack(aa,ts,bits)*pack(bb,ss,bits)
        count_poly = pack([1]*len(ts),ts,count_bits)*pack([1]*len(ss),ss,count_bits)
        hs = list(range(i+j-ts[-1]-ss[-1], i+j-ts[0]-ss[0]+1))
        ck('aggregate_exhaustion', [r[0] for r in item['h_records']] == hs, [i,j])
        pair_sum = pair_count = 0
        evidence = []
        for rec, h in zip(item['h_records'], hs):
            exponent = i+j-h
            G = (polynomial >> (bits*exponent)) & mask
            number = (count_poly >> (count_bits*exponent)) & count_mask
            lower, upper = max(ts[0], exponent-ss[-1]), min(ts[-1], exponent-ss[0])
            ck('interval_count', number == max(0,upper-lower+1), [i,j,h])
            cap = min(P[i],P[j],P[h])
            m,k = (i,j,h).count(5),(i,j,h).count(6)
            distinct = min(i,j,h)>0
            expected = [h,number,G,cap,m,k,distinct]
            ck('complete_h_record', rec == expected, [i,j,h])
            evidence.append(expected)
            pair_sum += G
            pair_count += number
            counts['original'] += number
            if any(0 < z < 5 for z in (i,j,h)):
                counts['forbidden'] += number
                ck('null_capacity', cap == 0, [i,j,h])
            rows[i][0] += G
            if distinct:
                counts['distinct'] += number
                rows[i][1] += G
                buckets[m,k][0] += number
                buckets[m,k][1] += G
                buckets[m,k][2] += G*cap
            else:
                counts['repeated'] += number
                ck('repetition_geometry', sorted((i,j,h))[1] == sorted((i,j,h))[2], [i,j,h])
                if i:
                    ck('distinct_endpoint_repetitions', number == 1 and G == g[i], [i,j,h])
                    t = lower
                    rows[i][2].append([j,t,exponent-t,1])
                else:
                    ck('diagonal_objective', number == 1 and G == g[j], j)
        ck('complete_polynomial', pair_sum == g[i]*g[j] and pair_count == len(ts)*len(ss), [i,j])
        ck('no_high_digits', polynomial >> (bits*(ts[-1]+ss[-1]+1)) == 0, [i,j])
        report['pair_checks'].append({'i':i,'j':j,'h_records':len(hs),
            'original_entries':pair_count, 'all_factors_and_coefficients_match':True,
            'reconstructed_h_sha256':hashlib.sha256(json.dumps(evidence,separators=(',',':')).encode()).hexdigest()})
    for i,(full,distinct,rep) in enumerate(rows):
        ck('row_sums', full == g[i]*H and distinct == (g[i]*(H-2) if i else 0), i)
        ck('repeated_terms', rep == ([[0,0,0,1],[i,i,i,1]] if i else []), i)
        ck('saved_rows', saved['rows'][i] == dict(i=i,full_source_sum=full,distinct_source_sum=distinct,repetitions=rep), i)
    for key,val in [('original_entries',counts['original']),('repeated_entries',counts['repeated']),
                    ('forbidden_entries',counts['forbidden']),('distinct_entries',counts['distinct'])]:
        ck('complete_counts', saved[key] == val, key)
    ck('required_counts', counts['original'] == 1500625 and counts['repeated'] == 205 and counts['forbidden'] == 10232)
    ck('presentation_counts', saved['presentation_visits'] == [counts['original']]*6)
    ck('distinct_total', sum(z[1] for z in buckets.values()) == (H-1)*(H-2) == saved['distinct_source_total'])
    audited_buckets = []
    for (m,k),(number,G,K) in sorted(buckets.items()):
        ck('unordered_integrality', H*G % 6 == 0, [m,k])
        audited_buckets.append(dict(m5=m,m6=k,source_entries=number,source_sum=G,
            capacity_weighted_source_sum=K,unordered_triangles=H*G//6))
    ck('all_buckets', saved['buckets'] == audited_buckets)
    ck('all_triangles', sum(z['unordered_triangles'] for z in audited_buckets) == comb(H,3))

    # The complete closed diamond has the following ten break endpoints.
    directions = [(1,0),(0,1),(-1,2),(-1,1),(-2,1),(-1,0),(0,-1),(1,-2),(1,-1),(2,-1)]
    cover = [(0,1),(1,0),(1,1),(1,2),(2,1)]
    from math import gcd
    actual = sorted({(m//gcd(m,k),k//gcd(m,k)) for (m,k),(_,_,K) in buckets.items() if K and m+k})
    ck('break_lines', saved['actual_break_lines'] == [list(z) for z in actual] and set(actual) <= set(cover))
    ck('cover_lines', saved['covering_break_lines'] == [list(z) for z in cover])
    normalized = [(Q(x,abs(x)+abs(y)),Q(y,abs(x)+abs(y))) for x,y in directions]
    pieces = []
    for p,left in enumerate(normalized):
        right = normalized[(p+1)%10]
        ck('diamond_side', all(left[a]*right[a] >= 0 for a in (0,1)))
        signs = []
        for m,k in cover:
            v,w = m*left[0]+k*left[1],m*right[0]+k*right[1]
            ck('whole_segment_sign', v*w >= 0)
            signs.append([m,k,(v>0)-(v<0),(w>0)-(w<0)])
        pieces.append(dict(left=p,right=(p+1)%10,line_endpoint_signs=signs))
    ck('all_segments', saved['pieces'] == pieces)
    demands = [3*(N-2)*g[i]*P[i] for i in (5,6)]
    scale = sum(demands)
    ck('positive_scale', scale>0 and saved['positive_scale'] == scale and saved['demand_coefficients'] == demands)
    evaluations = []
    for (x,y),(xx,yy) in zip(directions,normalized):
        # Reconstruct the saved support as positive and negative half-planes.
        support = sum(K*(m*x+k*y) for (m,k),(_,_,K) in buckets.items() if m*x+k*y > 0)
        required = demands[0]*x+demands[1]*y
        margin = Q(support-required,abs(x)+abs(y))
        evaluations.append(dict(direction=[x,y],normalized=[enc(xx),enc(yy)],
            box_support_numerator=support,demand_pairing_numerator=required,
            normalized_scaled_margin=enc(margin),margin_over_positive_scale=enc(margin/scale),separates=margin<0))
    ck('all_ten_complete_values', saved['evaluations'] == evaluations)
    minimum = min(Q(*z['normalized_scaled_margin']) for z in evaluations)
    ck('minimum', saved['minimum_normalized_scaled_margin'] == enc(minimum) and
       saved['minimum_over_positive_scale'] == enc(minimum/scale))
    ck('strict_verdict', minimum/scale == Q(4,6521) and saved['verdict'] == 'NO_TWO_DISTANCE_SEPARATOR' and
       saved['all_nonzero_strictly_positive'] is True and saved['zero_vector_margin'] == 0)
    report.update(stage='complete',verdict='NO_TWO_DISTANCE_SEPARATOR',H=H,N=N,
        denominator=q,pair_numerators=P,shell_sizes=g,counts=dict(counts),
        buckets=audited_buckets,demand_coefficients=demands,positive_scale=scale,
        actual_break_lines=actual,pieces=pieces,evaluations=evaluations,
        minimum_over_positive_scale=enc(minimum/scale),separator_required='strictly negative',
        zero_vector_margin=0,all_saved_numerical_fields_used_in_proof_checked=True,
        symbolic_obligations='See L109: six atom presentations, multiplicity, box-dual sign, complete diamond coverage.')


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        report['stage'] = 'failed'
        if not report['failures']:
            report['failures'].append(repr(exc))
        raise
    finally:
        OUT.write_text(json.dumps(report,separators=(',',':'))+'\n')
        print('Stage:',report['stage'],'; checks:',sum(report['checks_by_kind'].values()),'; failures:',report['failures'])
        print('Minimum / positive scale:',report.get('minimum_over_positive_scale'),'; separator requires < 0')
        print('Certificate:',OUT)
