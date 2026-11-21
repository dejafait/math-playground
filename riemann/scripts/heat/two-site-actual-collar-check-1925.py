"""Independent arithmetic replay and full symbolic determinant comparison."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CERT = HERE / 'two-site-actual-collar-1925.json'
OUT = Path(__file__).with_suffix('.json')
spec = importlib.util.spec_from_file_location('replay1921', HERE/'two-site-theta-jacobian-check-1921.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


def main():
    saved = json.loads(CERT.read_bytes())
    failures = []
    checks = 0

    def check(name, condition):
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(name)

    check('unchanged complete inputs', all(sha256((ROOT/name).read_bytes()).hexdigest() == digest
          for name, digest in saved['input_sha256'].items()))
    check('accepted audit input hashes', all(saved['accepted_audit_hash_checks'].values()))
    source = json.loads((HERE/'low-time-h2-uniform-195.json').read_bytes())
    check('complete five selected raw inputs', saved['selected_inputs'] == {
        str(k): source['panels'][0]['moments'][str(k)] for k in (0, 2, 4, 6, 8)})
    values = []
    divisor_records = []
    box_inputs = {'a': (F(-1, 4), F(1, 4)), 'b': (F(3, 4), F(5, 4))}
    for n, row in enumerate(saved['trace']):
        check('sequential id '+str(n), row['id'] == n)
        op, ids = row['operation'], row['inputs']
        if op == 'constant':
            expected = p.interval(row['interval'])
            check('point constant '+str(n), expected[0] == expected[1] and not ids)
        elif op == 'input':
            expected = p.interval(source['panels'][0]['moments'][ids[0].split('/')[-1]])
        elif op == 'box_input':
            expected = box_inputs[ids[0]]
        else:
            operand_ids = ids[:1] if op == 'integer_power' else ids
            check('backward operands '+str(n), all(0 <= j < n for j in operand_ids))
            x = values[ids[0]]
            if op == 'add':
                expected = p.add(x, values[ids[1]])
            elif op == 'negate':
                expected = p.neg(x)
            elif op == 'multiply':
                expected = p.mul(x, values[ids[1]])
            elif op == 'reciprocal':
                expected = p.reciprocal(x)
                divisor_records.append({'trace_id': ids[0], 'interval': p.enc(x), 'excludes_zero': True})
            elif op == 'integer_power':
                k = ids[1]
                endpoints = [x[0]**k, x[1]**k]
                if k and not k % 2 and x[0] <= 0 <= x[1]:
                    endpoints.append(F(0))
                expected = p.rounded((min(endpoints), max(endpoints)))
            elif op == 'sqrt':
                expected = p.interval(row['interval'])
                check('complete squared inequalities '+str(n),
                      expected[0] >= 0 and expected[0]**2 <= x[0] <= x[1] <= expected[1]**2)
            else:
                raise ValueError(op)
        check('complete endpoints '+str(n), expected == p.interval(row['interval']))
        values.append(expected)
    check('complete division record', saved['divisors'] == divisor_records)

    def copies(obj):
        if isinstance(obj, dict):
            if 'trace_id' in obj:
                check('saved result '+str(obj['trace_id']), p.interval(obj) == values[obj['trace_id']])
            else:
                for value in obj.values():
                    copies(value)
        elif isinstance(obj, list):
            for value in obj:
                copies(value)
    for key in ('actual', 'point', 'collar', 'orientations'):
        copies(saved[key])

    # Independent dual permutation expansion versus producer's Laplace
    # expansion followed by monomial differentiation. All five variables.
    zero = p.constant(0)
    one = p.constant(1)

    def add(x, y):
        return tuple(p.padd(a, b) for a, b in zip(x, y))

    def multiply(x, y):
        return (p.pmul(x[0], y[0]),
                p.padd(p.pmul(x[1], y[0]), p.pmul(x[0], y[1])),
                p.padd(p.pmul(x[2], y[0]), p.pmul(x[0], y[2])))

    def negate(x):
        return tuple(p.pneg(a) for a in x)

    def determinant(matrix):
        result = (zero, zero, zero)
        for perm in permutations(range(4)):
            term = (one, zero, zero)
            for i, j in enumerate(perm):
                term = multiply(term, matrix[i][j])
            odd = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4)) % 2
            result = add(result, negate(term) if odd else term)
        return result

    moments = []
    for k in range(8):
        value = p.constant(1) if k == 0 else {}
        if k in (2, 4, 6):
            e = [0]*5
            e[k//2-1] = 1
            value = {tuple(e): F(1)}
        derivatives = []
        for site in (3, 4):
            e = [0]*5
            e[site] = k
            value = p.padd(value, {tuple(e): F(1)})
            e[site] = max(0, k-1)
            derivatives.append({tuple(e): F(k)} if k else {})
        moments.append((value, *derivatives))
    gram = [[moments[i+j] for j in range(4)] for i in range(4)]
    polynomials = {'gram_det': determinant(gram)}
    for j in range(4):
        matrix = [row.copy() for row in gram]
        for i in range(4):
            matrix[i][j] = negate(moments[i+4])
        polynomials['numerator_c'+str(j)] = determinant(matrix)
    for name, triple in polynomials.items():
        for key, expected in zip(('value', 'da', 'db'), triple):
            actual = {tuple(x['exponents']): F(x['coefficient']) for x in saved['polynomials'][name][key]}
            check('complete polynomial '+name+'/'+key, actual == expected)

    # Exact midpoint inverse, both affine orientations.
    J = [[p.interval(x) for x in row] for row in saved['point']['jacobian']]
    midpoint = [[sum(x)/2 for x in row] for row in J]
    for sign in (1, -1):
        R = [[F(x) for x in row] for row in saved['orientations'][str(sign)]['R']]
        oriented = [[sign*x for x in midpoint[0]], midpoint[1]]
        check('exact midpoint inverse '+str(sign),
              all(sum(R[i][l]*oriented[l][j] for l in range(2)) == int(i == j)
                  for i in range(2) for j in range(2)))
    failed = p.interval(saved['collar']['blocked_divisor'])
    gamma = p.interval(saved['actual']['gamma'])
    kurtosis = p.interval(saved['actual']['k'])
    check('quoted actual gamma bound', F(-744, 1000) < gamma[0] <= gamma[1] < F(-725, 1000))
    check('quoted actual fourth invariant bound', F(1963, 1000) < kurtosis[0] <= kurtosis[1] < F(2010, 1000))
    check('unpaid full collar divisor', failed[0] < 0 < failed[1])
    check('strict outward failed bound', F(-4383, 10**6) < failed[0] < 0 < failed[1] < F(6650, 10**6))
    check('no inclusion or exclusion claimed', all(
        x['status'] == 'inconclusive_unpaid_collar_divisor' and
        not x['krawczyk_evaluated'] and not x['range_exclusion_evaluated']
        for x in saved['orientations'].values()))
    report = {'status': 'passed' if not failures else 'failed', 'checks': checks,
              'trace_nodes': len(values), 'full_symbolic_components': 15,
              'failed_divisor': p.enc(failed), 'failures': failures,
              'input_sha256': {str(path.relative_to(ROOT)): sha256(path.read_bytes()).hexdigest()
                               for path in (CERT, Path(__file__), HERE/'two-site-theta-jacobian-check-1921.py')},
              'qualification': 'Finite arithmetic/symbolic replay, not independent Decimal verification or nonlinear inclusion'}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({**report, 'input_sha256': 'saved in certificate',
                      'certificate': str(OUT.relative_to(ROOT))}))
    assert not failures


if __name__ == '__main__':
    main()
