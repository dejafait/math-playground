"""L116 audit: full reviewed replay plus independent Newton-trace checks.

Preserves the producer and original replay. The theorem-level audit is in L116.
No number-field backend, producer imports, or floating-point arithmetic.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import re
import runpy
import traceback

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'marked-octic-maximal-order-certificate.json'
REPLAY = HERE / 'marked-octic-maximal-order-audit-replay.json'
OUTPUT = HERE / 'marked-octic-maximal-order-audit-certificate.json'
LEMMA = HERE.parent.parent / 'lemmas/L116-marked-octic-maximal-order.md'
checks = []


def check(name, actual, required):
    checks.append(dict(name=name, actual=actual, required=required,
                       passed=actual == required))
    assert actual == required, name


def encode(x):
    if isinstance(x, Q):
        return int(x) if x.denominator == 1 else str(x)
    if isinstance(x, list):
        return [encode(v) for v in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    return x


def main():
    raw = SOURCE.read_bytes()
    c = json.loads(raw)
    failures, ledger, newton_grams = [], [], []
    try:
        replay = runpy.run_path(str(HERE / 'replay_marked_octic_maximal_order.py'))
        replay['main'].__globals__['OUTPUT'] = REPLAY
        replay['main']()
        r = json.loads(REPLAY.read_text())
        check('replay binds complete source bytes', r['producer_sha256'], sha256(raw).hexdigest())
        check('full replay passed', r['passed'], True)
        check('full replay failures', r['failures'], [])
        check('all replay comparisons inspected', all(x['actual'] == x['required'] and x['passed']
                                                     for x in r['checks']), True)
        check('replay comparison count', len(r['checks']), 1331)

        # Newton identities from F/275, independent of any order product table.
        f = [Q(x, 275) for x in [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]]
        traces = [Q(8)]
        for k in range(1, 15):
            if k <= 8:
                value = -sum(f[8-j]*traces[k-j] for j in range(1, k)) - k*f[8-k]
            else:
                value = -sum(f[8-j]*traces[k-j] for j in range(1, 9))
            traces.append(value)
        for i, o in enumerate(c['orders']):
            b = [[Q(x) for x in row] for row in o['basis']]
            gram = [[sum(b[k][a]*b[l][d]*traces[k+l]
                         for k in range(8) for l in range(8))
                     for d in range(8)] for a in range(8)]
            check(f'order {i} Newton trace Gram', gram, o['gram'])
            newton_grams.append(gram)

        matrices = re.findall(r'```text\n(.*?)\n```', LEMMA.read_text(), re.S)
        parsed = [[[Q(x) for x in row.split()] for row in block.splitlines()]
                  for block in matrices]
        final = c['orders'][c['final_order_id']]
        check('two canonical displayed matrices', len(parsed), 2)
        check('complete printed basis', parsed[0], [[Q(x) for x in row] for row in final['basis']])
        check('complete printed Gram matrix', parsed[1], final['gram'])

        for group in ['steps', 'final_checks']:
            for i, s in enumerate(c[group]):
                # Full replay proves each equality. Retain the complete kernel
                # vectors and ranks together to make their distinct roles clear.
                item = dict(group=group, record=i, prime=s['prime'], order=s['order_id'],
                            exponent=s['frobenius_exponent'], index=s['index'],
                            nilpotent_rank=s['nilpotent_kernel']['rank'],
                            nilpotent_vectors=s['nilpotent_kernel']['vectors'],
                            multiplier_rank=s['multiplier_kernel']['rank'],
                            multiplier_vectors=s['multiplier_kernel']['vectors'])
                ledger.append(item)
                if group == 'final_checks':
                    target = [[int(i == j) for j in range(8)] for i in range(64)]
                    check(f'final {s["prime"]} full reduced joint matrix',
                          s['multiplier_kernel']['rref'], target)
        check('complete radical/multiplier record count', len(ledger), 23)
        check('signed final discriminant', final['discriminant'], 2**8*3**7*5**4*11**7)
        check('total starting-order index', c['total_index'], 2**32*3**10*5**2)
        for p, expected in [(2, [2,4,8,16,32,64,128,4,4]),
                            (3, [3,9,27,81]), (5, [5,5]), (11, [])]:
            check(f'complete strict index sequence at {p}',
                  [s['index'] for s in c['steps'] if s['prime'] == p and not s['terminal']], expected)
    except Exception:
        failures.append(traceback.format_exc())
    result = dict(producer_sha256=sha256(raw).hexdigest(),
                  replay_path=REPLAY.name, checks=checks, complete_kernel_ledger=ledger,
                  newton_grams=newton_grams, failures=failures, passed=not failures)
    OUTPUT.write_text(json.dumps(encode(result), indent=2)+'\n')
    print('audit passed', result['passed'], 'checks', len(checks), 'failures', len(failures))
    print('complete kernel pairs', len(ledger), 'required', 23,
          'final ranks required', [8,8,8,8])
    print('certificate', OUTPUT)
    if failures:
        print(failures[0])
        raise SystemExit(1)


if __name__ == '__main__':
    main()
