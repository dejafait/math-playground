"""Audit complete coverage, rational budgets and final signed enclosures.

Root/heat/weak entry bounds and tensor propagation rely on the generator's
interval induction and stated IEEE error model, not independent recomputation.
"""
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

import numpy as np
from check_continuum_pure_sectors import operators
from check_continuum_tensor import product_terms

ROOT = Path(__file__).parent
PATH = ROOT/'signed-retained-enclosure-certificate.json'


def up(a, b):
    return -((-a)//b)


def nested(x):
    return tuple(nested(y) for y in x) if isinstance(x, list) else x


def fraction(row):
    return F(int(row['num']), int(row['den']))


def main():
    data = json.loads(PATH.read_text())
    S = int(data['scale'])
    assert S == 10**80 and data['cutoff'] == 112 and data['degree'] == 12
    assert hashlib.sha256((ROOT/'stored-fourier-enclosure-certificate.json').read_bytes()).hexdigest() == data['input_sha256']
    source = ROOT/'full-time-sensitivity-enclosure-certificate.json'
    assert hashlib.sha256(source.read_bytes()).hexdigest() == data['sensitivity_input_sha256']
    sensitivity = json.loads(source.read_text())
    assert sensitivity['passed'] and not sensitivity['failures']
    algebra = [operators(pair) for pair in ((0, 2), (1, 3))]
    ops = {(a, i, c): product_terms(algebra[a][0][i], algebra[a][1], c)
           for a in range(2) for i in range(2) for c in range(4)}
    expected = {(a, c, j, key[j]) for (a, i, c), op in ops.items() for key in op for j in range(4)}
    saved = [(r['alpha'], r['component'], r['axis'], nested(r['key'])) for r in data['feature_coverage']]
    assert len(set(saved)) == len(saved) and set(saved) == expected
    baseline = {(r['alpha'], r['component'], r['axis'], nested(r['key'])): int(r['baseline_upper'])
                for r in sensitivity['feature_tables']}
    assert set(baseline) == expected
    initial = [0, 0]
    for (a, i, c), op in ops.items():
        for key, v in op.items():
            raw = 1
            for j in range(4):
                raw *= baseline[a, c, j, key[j]]
            initial[i] += up(up(raw, S**3)*abs(v.numerator), v.denominator)
    assert initial == [int(x) for x in data['absolute_initial_upper']]
    absolute = [F(x, S)*8*F(64, 27)**3 for x in initial]
    assert absolute == [fraction(x) for x in data['absolute_full_upper']]
    m = 12
    C = F(factorial(m)**4, (2*m+1)*factorial(2*m)**3)
    tail = 1/sum((F(108)**j/F(factorial(j)) for j in range(161)), F(0))
    A = C*(1+2*m+22*(2*factorial(2*m+2)+2*m*factorial(2*m+1)))+109*tail
    B = C*(1+22*factorial(2*m+1))+tail
    assert fraction(data['inverse_weight_errors']['A']) == A
    assert fraction(data['inverse_weight_errors']['B']) == B
    assert F(50176, 4*2**14) < 1 and F(27, 64)*256 == 108
    assert len(data['roots']) == 12 and len(data['mapped_rule']) == 276
    assert {(r['panel'], r['node']) for r in data['mapped_rule']} == {(p, j) for p in range(23) for j in range(12)}
    assert len(data['heat_enclosures']) == 276
    for row in data['heat_enclosures']:
        assert len(row) == 113
        assert all(0 <= int(x['lo']) <= int(x['hi']) <= S for x in row)
    gamma = F(554, 2**53-554)
    G = float.fromhex(data['arithmetic_model']['dot_gamma_upper'])
    assert F(G) > gamma and F(float(1-G)) < 1-gamma
    assert F(1, 2**53-1) < F(float(1e-15))
    assert F(float.fromhex(data['arithmetic_model']['additive_error_per_operation'])) > 1000*F(2)**(-1022)
    files = {}
    entries_checked = 0
    for entry in data['feature_evidence']:
        path = ROOT/entry['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256']
        files[entry['path']] = np.load(path)
    assert len(files) == 8
    for row in data['feature_coverage']:
        archive = files[f"signed-retained-tables-{row['alpha']}-{row['component']}.npz"]
        name = f"axis{row['axis']}_feature{row['index']}"
        center, radius = archive[name+'_center'], archive[name+'_radius']
        assert center.shape == radius.shape == (276, 276)
        assert np.all(np.isfinite(center)) and np.all(np.isfinite(radius)) and np.all(radius >= 0)
        entries_checked += center.size
    for file in files.values():
        file.close()
    assert {(r['alpha'], (3, 6).index(r['probe']), r['component']) for r in data['collected_groups']} == set(ops)
    assert all(r['terms'] == len(ops[r['alpha'], (3, 6).index(r['probe']), r['component']]) for r in data['collected_groups'])
    for i, row in enumerate(data['final']):
        c = F(float.fromhex(row['reported_value_hex']))
        radius = F(float.fromhex(row['arithmetic_radius_hex']))
        E = radius+absolute[i]*(A+B+A*B)
        coeff = F(int(sensitivity['full_time_sensitivity_upper'][i]), S)
        tail_i = [F('1.37381915696e-11'), F('5.49527662781e-11')][i]
        lo, hi = c-E-coeff-tail_i, c+E+coeff+tail_i
        assert fraction(row['exact_I_lower']) == lo and fraction(row['exact_I_upper']) == hi
        assert E < [100, 1000][i] and lo > 0
        assert lo > [F('452.8'), F('3351.60')][i]
        assert hi < [F('453.35'), F('3353.59')][i]
        assert row['budget_pass'] and row['sign_certified']
        assert c > 0 and radius >= 0
        assert absolute[i]*(A+B+A*B) < [F(1, 5), F(18, 25)][i]
    assert data['status'] == 'PASS' and not data['failures']
    result = dict(status='PASS', features_checked=len(saved), coordinate_entries_checked=entries_checked,
                  collected_terms_checked=sum(len(op) for op in ops.values()),
                  actual_bounds=[dict(probe=r['probe'], E_upper=r['retained_error_upper'],
                                      total_error_upper=r['total_error_upper'],
                                      I_lower=r['exact_I_lower_float'], I_upper=r['exact_I_upper_float'])
                                 for r in data['final']], required_E=[100, 1000], failures=[],
                  certificate_sha256=hashlib.sha256(PATH.read_bytes()).hexdigest(),
                  qualification='Coverage, every saved coordinate enclosure shape/finiteness, and exact rational aggregate budgets audited. Root/heat/weak and tensor enclosure correctness relies on generator induction and its stated IEEE model.')
    output = ROOT/'signed-retained-enclosure-audit.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', features=len(saved), coordinate_entries_checked=entries_checked,
                          actual=result['actual_bounds'], required=[100, 1000], failures=[], path=str(output))))


if __name__ == '__main__':
    main()
