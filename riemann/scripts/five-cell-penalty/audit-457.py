"""Replay C744b without overwriting its certificate; check all saved fields.

The numerical enclosure algorithm is certify-455.py, whose code and
mathematical formulas are audited in C744b. This is not an independent
implementation of special functions. Fraction checks independently verify
exact witness transcription, enclosure aggregation, indexing and signs.
Full replay and audit evidence is written under replay-457/.
"""
import ast
import contextlib
import hashlib
import json
import re
import runpy
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'certify-455.py'
ORIGINAL = HERE / 'certificate-455.json'
OUT = HERE / 'replay-457'
OUT.mkdir(exist_ok=True)
checks = []
report = {'status': 'IN_PROGRESS', 'checks': checks, 'failures': []}


def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})
    if not condition:
        report['failures'].append(name)
        raise AssertionError(name)


def bounds(x):
    return F(x['lo']), F(x['hi'])


def contains(x, pair):
    lo, hi = bounds(x)
    return lo <= pair[0] <= pair[1] <= hi


def square(x):
    lo, hi = bounds(x)
    return (F(0) if lo <= 0 <= hi else min(lo*lo, hi*hi),
            max(lo*lo, hi*hi))


def sum_bounds(xs):
    pairs = [bounds(x) for x in xs]
    return sum((p[0] for p in pairs), F(0)), sum((p[1] for p in pairs), F(0))


def walk(x, path=''):
    if isinstance(x, dict):
        if set(x) == {'lo', 'hi'}:
            check('ordered interval ' + path, bounds(x)[0] <= bounds(x)[1])
        else:
            for k, v in x.items():
                walk(v, path + '/' + k)
    elif isinstance(x, list):
        for j, v in enumerate(x):
            walk(v, path + '/' + str(j))


try:
    source_bytes = SOURCE.read_bytes()
    original_bytes = ORIGINAL.read_bytes()
    report['source_sha256'] = hashlib.sha256(source_bytes).hexdigest()
    report['original_sha256'] = hashlib.sha256(original_bytes).hexdigest()
    report['python_version'] = sys.version
    saved = json.loads(original_bytes)
    ns = runpy.run_path(str(SOURCE), run_name='c744b_audit_replay')
    # certify() consults __file__ only to choose its output destination.
    # All mathematical code and parameters are unchanged.
    ns['certify'].__globals__['__file__'] = str(OUT / SOURCE.name)
    with (OUT / 'replay.log').open('w') as log, contextlib.redirect_stdout(log):
        ns['certify']()
    replay_path = OUT / 'certificate-455.json'
    replay_bytes = replay_path.read_bytes()
    replay = json.loads(replay_bytes)
    check('complete replay matches all saved fields', replay == saved)
    check('complete replay is byte-identical', replay_bytes == original_bytes)
    check('original certificate preserved', ORIGINAL.read_bytes() == original_bytes)
    check('source preserved', SOURCE.read_bytes() == source_bytes)
    walk(saved)

    canonical = (ROOT / 'lemmas/C744b-five-cell-128-response-penalty-certificate-obstruction.md').read_text()
    vector_block = re.search(r'```text\n(.*?)\n```', canonical, re.S).group(1)
    canonical_vector = ast.literal_eval('[' + vector_block + ']')
    nums = saved['witness']['numerators']
    den = saved['witness']['denominator']
    check('all 64 canonical, source and certificate coefficients agree',
          len(nums) == 64 and nums == canonical_vector == ns['NUMERATORS'])
    check('denominator is exactly 2^44', den == 2**44 == ns['DENOMINATOR'])
    norm = sum((F(n*n, den*den) for n in nums), F(0))
    check('exact squared norm', norm == F(saved['witness']['norm2_exact'])
          == F(309485009821346058612548645, 309485009821345068724781056))
    check('norm strictly between stated endpoints', F(1) < norm < F('1.000000000000004'))
    check('norm enclosed', contains(saved['witness']['norm2'], (norm, norm)))
    check('parameters unchanged', saved['parameters'] == {
        'K': 5, 'penalty': 256, 'responses': 128,
        'retained_modes_per_parity': 4096, 'covariance_prefix_end': 16384})
    hs = saved['all_h_enclosures']
    check('complete diagonal mode indices', [x['q'] for x in hs] == list(range(64)))
    diag = (sum((F(n*n,den*den)*bounds(x['h'])[0] for n,x in zip(nums,hs)),F(0)),
            sum((F(n*n,den*den)*bounds(x['h'])[1] for n,x in zip(nums,hs)),F(0)))
    check('diagonal encloses exact-weight sum of all h intervals', contains(saved['terms']['diagonal'], diag))

    expected_powers = []
    for n in range(2, 16):
        p = next(d for d in range(2,n+1) if n % d == 0)
        rest = n
        while rest % p == 0:
            rest //= p
        if rest == 1:
            expected_powers.append((n,p))
    prime_terms = saved['prime_terms']
    check('all and only active prime powers, with base primes',
          [(x['n'],x['base_prime']) for x in prime_terms] == expected_powers)
    check('prime total encloses every signed term',
          contains(saved['terms']['prime'], sum_bounds([x['energy'] for x in prime_terms])))
    responses = saved['all_response_projections']
    check('all 128 response indices', [x['j'] for x in responses] == list(range(128)))
    for x in responses:
        check('response square ' + str(x['j']), contains(x['energy'], square(x['projection'])))
    check('response sum', contains(saved['terms']['responses'], sum_bounds([x['energy'] for x in responses])))
    moments = saved['all_physical_moments']
    check('all ten physical moment indices',
          [(x['cell'],x['sigma']) for x in moments] == [(j,s) for j in range(5) for s in (1,-1)])
    for x in moments:
        sq = square(x['moment'])
        check('physical penalty square ' + str((x['cell'],x['sigma'])),
              contains(x['penalty'], (256*sq[0], 256*sq[1])))
    check('penalty sum', contains(saved['terms']['penalty'], sum_bounds([x['penalty'] for x in moments])))
    check('witness is not exactly neutral', bounds(moments[0]['moment'])[1] < 0)
    check('total encloses sum of all five contributions',
          contains(saved['energy'], sum_bounds(list(saved['terms'].values()))))
    elo,ehi = bounds(saved['energy'])
    check('strict stated energy bounds', F('-2.368e-8') < elo <= ehi < F('-2.288e-8'))
    check('strong negative acceptance bound', ehi < F('-2e-8'))
    floors = saved['complement_floors']
    check('both complement parities', [x['parity'] for x in floors] == [1,-1])
    for x, threshold in zip(floors, ['1.76988','0.82159']):
        dl,dh = bounds(x['d4096']); rl,rh = bounds(x['rho'])
        check('complement subtraction ' + str(x['parity']), contains(x['floor'], (dl-rh,dh-rl)))
        check('strict complement lower bound ' + str(x['parity']), bounds(x['floor'])[0] > F(threshold))
    report.update(status='PASS', energy=saved['energy'],
                  required_negative_upper_bound='-2e-8',
                  norm2_exact=str(norm), complement_floors=floors,
                  replay_sha256=hashlib.sha256(replay_bytes).hexdigest(),
                  complete_fields_equal=list(saved),
                  scope='Audit of fixed lower comparison only; no complete-energy sign.')
except Exception as exc:
    report['status'] = 'FAIL'
    report['exception'] = type(exc).__name__ + ': ' + str(exc)
    raise
finally:
    audit_path = OUT / 'audit.json'
    audit_path.write_text(json.dumps(report,indent=2)+'\n')
    print('Audit:', report['status'], '; checks:', len(checks), '; failures:', report['failures'])
    if 'energy' in report:
        print('Energy:', report['energy'], '; required upper < -2e-8')
        for x in report['complement_floors']:
            print('Parity:', x['parity'], '; complement floor:', x['floor'], '; required > 0')
    print('Full evidence:', audit_path)
