"""Audit L055's displayed certificate and normalization, without solver code.

The preceding independent beta reconstruction checks the source formulas.
Here the manuscript itself supplies the weights. Every contribution to
each dual column is saved, including zero-weight modes. Symbolic averaging
and the implication to arbitrary assignments are reviewed in L055.
"""
import hashlib
import json
import re
from fractions import Fraction as Q
from math import comb
from pathlib import Path

ROOT = Path(__file__).parent
LEMMA = ROOT.parent.parent / 'lemmas/L055-free-triple-five-shell-fixed-pair-exclusion.md'
OUT = ROOT / 'free-triple-five-shell-critical-audit-results.json'


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def encode(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def eigen(n, a, r):
    return sum((-1)**h*c(a, h)*c(5-a, r-h)*c(n-5-a, r-h)
               for h in range(r+1))


def main():
    checks, failures, hashes = [], [], {}

    def check(name, truth, data=None):
        record = {'name': name, 'passed': bool(truth), 'data': data}
        checks.append(record)
        if not truth:
            failures.append(record)

    def read(name):
        raw = (ROOT/name).read_bytes()
        hashes[name] = hashlib.sha256(raw).hexdigest()
        return json.loads(raw)

    saved = read('free-triple-five-shell-results.json')
    audit = read('free-triple-five-shell-audit-results.json')
    pair = read('selected-triple-sdp-results.json')
    manuscript = LEMMA.read_text()
    weight_rows = re.findall(r'^\| \((\d),(\d)\) \| (\d+)/(\d+) \|$', manuscript, re.M)
    weights = {(int(a), int(b)): Q(int(p), int(q)) for a, b, p, q in weight_rows}
    modes = [(a, b) for a in range(6) for b in range(6)]
    check('eleven_distinct_displayed_weights', len(weight_rows) == len(weights) == 11)
    check('reconstruction_complete', audit['verified'] and audit['failures'] == []
          and audit['checks'] == 1318 and audit['source_sha256'] == hashes['free-triple-five-shell-results.json'])
    p5 = Q(*pair['p'][5])
    rho = (Q(c(1024, 64), c(68, 64))+1)/(2*c(1024, 68))
    S = c(68, 5)*c(956, 5)
    check('positive_normalizations', rho > 0 and p5 > 0)
    check('fixed_p5_identity', p5 == Q(*saved['parameters']['p'][5])
          and p5 == Q(4982733184, 5*S))
    check('shell_size', S == saved['parameters']['shell_size'] == 68643272053310642688)
    relations, region_records = [], []
    for r in range(6):
        for q in range(6):
            # Ordered regions: A-only, AC-only, AB-only, ABC,
            # BC-only, B-only, C-only, outside all three.
            regions = [5-r, r, r, 63-r, 5-q, q, q, 951-q]
            check('actual_region_sizes', min(regions) >= 0 and sum(regions) == 1024, [r, q])
            diagonal = (r, q) == (0, 0)
            forbidden = 1 <= r+q <= 4
            incidence = regions[3] == 61 and [regions[i] for i in (1, 2, 4)] == [2]*3 and [regions[i] for i in (0, 5, 6)] == [3]*3
            check('unique_incidence_relation', incidence == ((r, q) == (2, 3)), [r, q])
            kind = 'diagonal' if diagonal else 'zero' if forbidden or incidence else 'free'
            if kind == 'free':
                relations.append((r, q))
            region_records.append({'relation': [r, q], 'regions': regions, 'kind': kind})
    check('all_relations_partition', len(region_records) == 36 and len(relations) == 20
          and sum(row['kind'] == 'zero' for row in region_records) == 15
          and list(map(list, relations)) == saved['parameters']['relations'])
    factors = {n: [[eigen(n, a, r) for r in range(6)] for a in range(6)] for n in (68, 956)}
    for n in factors:
        for a in range(6):
            for r in range(6):
                check('full_beta_reconstruction_agreement', encode(factors[n][a][r]) == audit['factors'][str(n)][a][r], [n, a, r])
    mode_records = []
    for a, b in modes:
        multiplicity = (c(68, a)-c(68, a-1))*(c(956, b)-c(956, b-1))
        check('positive_mode_dimension', multiplicity > 0, [a, b])
        mode_records.append({'mode': [a, b], 'multiplicity': multiplicity})
        if a or b:
            index = saved['parameters']['modes'].index([a, b])
            weight = weights.get((a, b), Q(0))
            check('displayed_or_zero_dual_weight', weight >= 0 and weight == Q(*saved['exact']['dual'][index]), [a, b])
    check('complete_product_dimension', sum(row['multiplicity'] for row in mode_records) == S)
    columns = []
    for r, q in relations:
        valency = factors[68][0][r]*factors[956][0][q]
        check('positive_valency', valency > 0, [r, q])
        terms = []
        for a, b in modes[1:]:
            coefficient = -Q(factors[68][a][r]*factors[956][b][q], valency)
            weight = weights.get((a, b), Q(0))
            i = saved['parameters']['modes'].index([a, b])
            j = saved['parameters']['relations'].index([r, q])
            check('every_saved_coefficient', coefficient == Q(*saved['matrix'][i][j]), [a, b, r, q])
            terms.append({'mode': [a, b], 'coefficient': encode(coefficient),
                          'weight': encode(weight), 'contribution': encode(weight*coefficient)})
        total = sum(Q(*row['contribution']) for row in terms)
        check('exact_dual_column_identity', total == 1, [r, q])
        columns.append({'relation': [r, q], 'valency': valency, 'terms': terms, 'total': encode(total)})
    upper = 1+sum(weights.values())
    required = S*p5
    check('displayed_weight_sum', sum(weights.values()) == Q(1143872637, 5))
    check('displayed_upper_and_Schur_requirement', upper == Q(1143872642, 5) and required == Q(4982733184, 5))
    check('strict_gap', required-upper == Q(3838860542, 5) > 0)
    check('independent_report_bounds', encode(upper) == audit['row_sum_upper'] and encode(required) == audit['required_row_sum'])
    anchor = frozenset(range(68))
    neighbor = (anchor-frozenset(range(5))) | frozenset(range(68, 73))
    indices = [frozenset([anchor]), frozenset([anchor, neighbor])]
    def fixed_union_moment(family):
        if len(family) == 1:
            return rho
        left, right = tuple(family)
        return rho*Q(*pair['p'][len(left-right)])
    normalized = [[fixed_union_moment(I | J)/rho for J in indices] for I in indices]
    check('Boolean_diagonal_and_anchor', normalized == [[1, p5], [p5, p5]])
    report = {'input_sha256': hashes, 'checks': checks, 'check_count': len(checks),
              'failures': failures, 'verified': not failures,
              'displayed_weights': [{'mode': list(mode), 'weight': encode(w)} for mode, w in weights.items()],
              'rho': encode(rho), 'p5': encode(p5), 'shell_size': S,
              'relation_dictionary': region_records, 'modes': mode_records,
              'dual_columns': columns, 'row_sum_upper': encode(upper),
              'required_row_sum': encode(required), 'strict_gap': encode(required-upper)}
    OUT.write_text(json.dumps(report, separators=(',', ':'))+'\n')
    print('Manuscript audit checks:', len(checks), '; failures:', len(failures))
    print('Relations/free columns/modes: 36/20/36; required: 36/20/36')
    print('Exact row sum upper/required:', upper, '/', required, '; gap:', required-upper)
    print('Certificate:', OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
