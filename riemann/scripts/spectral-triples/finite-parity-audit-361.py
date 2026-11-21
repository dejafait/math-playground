"""Audit L759 at its original cell; preserve every original artifact.

Reproduce the entire generator in memory with a redirected __file__ in a
temporary directory, and compare every certificate field except elapsed time.
Independent inertia uses integer fixed-point intervals and the dot-product
LDL recurrence, importing neither Decimal arithmetic nor the generator's I.
"""
import ast
from fractions import Fraction
import hashlib
import json
from math import comb, isqrt
from pathlib import Path
import platform
import shutil
import tempfile
import time

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'finite-parity-359.py'
INPUT = SOURCE.with_suffix('.json')
OUTPUT = HERE / 'finite-parity-audit-361.json'
REPLAY = HERE / 'finite-parity-replay-361.json'
SCALE = 10**220
started = time.monotonic()
result = {'kind': 'independent fixed-cell certificate audit', 'failures': [],
          'input_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
          'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
          'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'python': platform.python_version(), 'scale_digits': 220,
          'checks': {}, 'inertia': [], 'outcome': 'IN_PROGRESS'}


def save():
    result['elapsed_seconds'] = time.monotonic()-started
    OUTPUT.write_text(json.dumps(result, indent=2)+'\n')


def require(ok, message):
    if not ok:
        result['failures'].append(message)
        save()
        raise ArithmeticError(message)


def lower(q):
    return q.numerator*SCALE//q.denominator


def upper(q):
    return -((-q.numerator*SCALE)//q.denominator)


def from_pair(pair):
    a, b = map(Fraction, pair)
    require(a <= b, 'unordered input interval')
    return lower(a), upper(b)


def point(value):
    q = Fraction(value)
    return lower(q), upper(q)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[1], a[1]-b[0]


def mul(a, b):
    terms = [x*y for x in a for y in b]
    return min(terms)//SCALE, -((-max(terms))//SCALE)


def div(a, b):
    require(not b[0] <= 0 <= b[1], 'fixed-point divisor contains zero')
    lows, highs = [], []
    for x in a:
        for y in b:
            numerator, denominator = x*SCALE, y
            if denominator < 0:
                numerator, denominator = -numerator, -denominator
            lows.append(numerator//denominator)
            highs.append(-((-numerator)//denominator))
    return min(lows), max(highs)


def store_pair(a):
    # Scientific-notation decimal strings represent the exact grid endpoints.
    return [str(v)+'e-220' for v in a]


def inside(a, b):
    return b[0] <= a[0] and a[1] <= b[1]


try:
    old = json.loads(INPUT.read_text())
    require(result['source_sha256'] == old['script_sha256'], 'generator hash mismatch')
    require(old['parameters'] == dict(N=120, K=512, R=160, EM=80, precision=170),
            'unexpected cell or precision')
    require(old['failures'] == [], 'original certificate has failures')
    result['checks']['original_hash_and_parameters'] = True
    save()

    # Execute an identical copy: no mutation of the original output or script.
    with tempfile.TemporaryDirectory(prefix='riemann-parity-361-') as folder:
        copied = Path(folder)/SOURCE.name
        shutil.copyfile(SOURCE, copied)
        namespace = {'__file__': str(copied), '__name__': '__main__'}
        exec(compile(copied.read_bytes(), str(copied), 'exec'), namespace)
        shutil.copyfile(copied.with_suffix('.json'), REPLAY)
    replay = json.loads(REPLAY.read_text())
    matched = []
    require(set(old) == set(replay), 'replay field set mismatch')
    for key in old:
        if key == 'elapsed_seconds':
            continue
        require(old[key] == replay[key], 'replay mismatch: '+key)
        matched.append(key)
    result['checks']['complete_replay_matched_fields'] = matched
    result['replay_sha256'] = hashlib.sha256(REPLAY.read_bytes()).hexdigest()
    result['checks']['decimal_contexts'] = {
        name: {'precision': namespace[name].prec,
               'Emin': namespace[name].Emin, 'Emax': namespace[name].Emax,
               'flags': {signal.__name__: value for signal, value in namespace[name].flags.items()}}
        for name in ('LO', 'HI')}
    for name in ('LO', 'HI'):
        for signal, flag in namespace[name].flags.items():
            if signal.__name__ not in ('Rounded', 'Inexact'):
                require(not flag, name+' exception flag: '+signal.__name__)

    # Verify even Bernoulli numbers by their defining recurrence, rather
    # than the generator's triangular algorithm (whose B_1 convention differs).
    bern = [Fraction(1)]
    for n in range(1, 161):
        bern.append(-sum(Fraction(comb(n+1, k))*bern[k] for k in range(n))/Fraction(n+1))
    require(all(bern[2*r] == namespace['BB'][2*r] for r in range(81)),
            'Bernoulli recurrence mismatch')
    result['checks']['all_even_bernoulli_numbers_through_160'] = True
    ast_floats = [node.value for node in ast.walk(ast.parse(SOURCE.read_text()))
                  if isinstance(node, ast.Constant) and isinstance(node.value, float)]
    require(not ast_floats, 'binary floating literal in generator')
    result['checks']['no_binary_float_literals'] = True

    # Complete rational parsing/ordering, symmetry, and parity compatibility.
    matrices = {}
    stats = {}
    for key, dimension in [('full_matrix', 241), ('even_matrix', 121), ('odd_matrix', 120)]:
        raw = old[key]
        require(len(raw) == dimension and all(len(row) == dimension for row in raw),
                key+' wrong dimension')
        mat = [[from_pair(entry) for entry in row] for row in raw]
        for i in range(dimension):
            for j in range(dimension):
                require(max(mat[i][j][0], mat[j][i][0]) <= min(mat[i][j][1], mat[j][i][1]),
                        key+' symmetric interval intersection failure')
                if key == 'full_matrix':
                    require(max(mat[i][j][0], mat[-i-1][-j-1][0]) <=
                            min(mat[i][j][1], mat[-i-1][-j-1][1]),
                            'full matrix parity intersection failure')
        matrices[key] = mat
        stats[key] = {'dimension': dimension, 'ordered_entries_checked': dimension**2,
                      'max_width': str(max(x[1]-x[0] for row in mat for x in row))+'e-220',
                      'symmetric_interval_intersections': True}
    result['checks']['complete_matrix_checks'] = stats
    full = matrices['full_matrix']
    rt = isqrt(2*SCALE*SCALE)
    rt2 = (rt, rt+1)
    require(rt*rt <= 2*SCALE*SCALE < (rt+1)*(rt+1), 'integer sqrt failed')
    require(inside(full[120][120], matrices['even_matrix'][0][0]), 'even central entry')
    for j in range(1, 121):
        cross = div(add(full[120][120+j], full[120][120-j]), rt2)
        require(inside(cross, matrices['even_matrix'][0][j]), 'even central cross entry')
        for k in range(1, 121):
            p, q = full[120+j][120+k], full[120+j][120-k]
            r, s = full[120-j][120+k], full[120-j][120-k]
            even = div(add(add(add(p, q), r), s), point(2))
            odd = div(add(sub(sub(p, q), r), s), point(2))
            require(inside(even, matrices['even_matrix'][j][k]), 'even basis enclosure')
            require(inside(odd, matrices['odd_matrix'][j-1][k-1]), 'odd basis enclosure')
    result['checks']['all_parity_basis_enclosures'] = True

    # The scalar/T_s fields are all read and checked, not sampled.
    for key in ('constants', 'inverse_power_tails'):
        for pair in old[key].values():
            from_pair(pair)
    for row in old['frequencies']:
        for pair in row:
            from_pair(pair)
    require(set(old['inverse_power_tails']) == {str(s) for s in range(2, 324)}, 'missing T_s')
    require(len(old['frequencies']) == 121, 'missing scalar frequencies')
    result['checks']['complete_scalar_fields_ordered_and_replayed'] = True
    result['checks']['original_inertia'] = []
    required = [('even', '1e-55', 121, 1), ('odd', '1e-55', 120, 0), ('even', '5e-56', 121, 1)]
    require(len(old['inertia']) == 3, 'unexpected original inertia count')
    for record, (block, shift, dimension, expected) in zip(old['inertia'], required):
        require((record['block'], record['shift'], record['success'], record['negative']) ==
                (block, shift, True, expected), 'original inertia metadata failure')
        piv = [from_pair(p) for p in record['pivots']]
        require(len(piv) == dimension and all(not a <= 0 <= b for a, b in piv),
                'original pivot zero overlap or dimension failure')
        require(sum(b < 0 for a, b in piv) == expected, 'original pivot sign count failure')
        distances = [min(abs(a), abs(b)) for a, b in piv]
        relative_widths = [Fraction(b-a, d) for (a,b), d in zip(piv, distances)]
        require(min(distances) > lower(Fraction('3.7e-11')), 'original pivot margin failure')
        require(max(relative_widths) < Fraction('2e-36'), 'original relative width failure')
        result['checks']['original_inertia'].append({
            'block': block, 'shift': shift, 'pivots_checked': dimension,
            'negative': expected, 'min_distance': str(min(distances))+'e-220',
            'relative_width_lt_2e-36': True})
    save()
    print('Full original replay, scalar fields, parity bases and all 362 saved pivots checked.', flush=True)

    # Independent LDL: a_ij = sum_{r<j} l_ir d_r l_jr + l_ij d_j;
    # dot products against the unchanged original matrix, no Schur updates.
    for block, shift, dimension, expected in required:
        mat = matrices[block+'_matrix']
        factors = [[point(0) for j in range(dimension)] for i in range(dimension)]
        pivots = []
        for j in range(dimension):
            diagonal = sub(mat[j][j], point(shift))
            for r in range(j):
                diagonal = sub(diagonal, mul(mul(factors[j][r], factors[j][r]), pivots[r]))
            require(not diagonal[0] <= 0 <= diagonal[1],
                    f'independent {block} {shift} zero pivot at {j}')
            pivots.append(diagonal)
            factors[j][j] = point(1)
            for i in range(j+1, dimension):
                numerator = mat[i][j]
                for r in range(j):
                    numerator = sub(numerator, mul(mul(factors[i][r], factors[j][r]), pivots[r]))
                factors[i][j] = div(numerator, diagonal)
        negative = sum(p[1] < 0 for p in pivots)
        require(negative == expected, 'independent inertia count differs')
        distances = [min(abs(a), abs(b)) for a,b in pivots]
        result['inertia'].append({'block': block, 'shift': shift, 'negative': negative,
                                  'dimension': dimension, 'pivots': list(map(store_pair, pivots)),
                                  'min_distance': str(min(distances))+'e-220',
                                  'factor_intervals': [[store_pair(x) for x in row[:i+1]]
                                                       for i, row in enumerate(factors)]})
        save()
        print('Independent integer LDL:', block, shift, 'negative', negative,
              'required', expected, 'nonzero pivots', len(pivots), flush=True)
    result['gap_lower'] = '5e-56'
    result['required_gap'] = '>0'
    result['outcome'] = 'AUDIT_PASSED'
    save()
    print('RESULT', result['outcome'], 'strict gap >', result['gap_lower'], 'required >0', flush=True)
    print('failures', result['failures'], 'certificate', OUTPUT, 'replay', REPLAY, flush=True)
except Exception as error:
    result['outcome'] = 'AUDIT_INCOMPLETE_OR_FAILED'
    if str(error) not in result['failures']:
        result['failures'].append(type(error).__name__+': '+str(error))
    save()
    print('RESULT', result['outcome'], 'failures', result['failures'], 'certificate', OUTPUT, flush=True)
    raise
