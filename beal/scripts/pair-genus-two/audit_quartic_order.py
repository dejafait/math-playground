"""Bounded supplement to L134's critical audit; accounting-only shared import.

Checks L132's complete relevant irreducibility evidence, L133's field scaling,
the final displayed basis, and every actual/required entry of the replay.
The order replay itself must first be executed and its algorithms audited.
This supplement does not substitute boolean summaries for that replay.
"""
import json
from hashlib import sha256
from pathlib import Path
import traceback
from quartic_order_budget import Budget

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / 'quartic-order-audit.json'
budget = Budget()
checks, divisions, failures = [], [], []


def check(name, actual, required):
    passed = budget.cmp('==', actual, required)
    checks.append(dict(name=name, actual=actual, required=required, passed=passed))
    if not passed:
        raise AssertionError(name)


def remainder(coefficients, divisor, p):
    r = list(coefficients)
    while budget.cmp('>=', len(r), len(divisor)):
        offset = budget.op('-', len(r), len(divisor))
        leading = r[-1]  # every divisor is monic
        for j, value in enumerate(divisor):
            index = offset + j  # container index bookkeeping
            r[index] = budget.op('%', budget.op('-', r[index],
                                  budget.op('*', leading, value)), p)
        while r and budget.cmp('==', r[-1], 0):
            r.pop()
    return r or [0]


def main():
    budget.phase('critical audit: complete irreducibility, scaling and replay payload')
    paths = ['degree-three-branch-certificate.json', 'quartic-order-certificate.json',
             'quartic-order-verification.json']
    raw = {name: (ROOT / name).read_bytes() for name in paths}
    hashes = {name: sha256(value).hexdigest() for name, value in raw.items()}
    try:
        branch, cert, replay = [json.loads(raw[name]) for name in paths]
        rec = branch['primes'][6]
        check('irreducibility prime', rec['prime'], 19)
        for d in (2, 3, 4):
            budget.charge('factor_trials')
            check('19 primality divisor ' + str(d),
                  budget.cmp('!=', budget.op('%', 19, d), 0), True)
        quartic = [7, 52, -6, -64, -25]
        reduced = [budget.op('%', a, 19) for a in quartic]
        check('degree-preserving quartic reduction', reduced, [7, 14, 13, 12, 13])
        check('saved quartic reduction', rec['quartic'], reduced)
        expected = [(a, 1) for a in range(19)]
        expected += [(a, b, 1) for a in range(19) for b in range(19)]
        saved = {tuple(row['divisor']): row['remainder'] for row in rec['divisor_trials']}
        check('complete distinct divisor domain', sorted(saved), sorted(expected))
        check('no duplicate divisor rows', len(rec['divisor_trials']), 380)
        for divisor in expected:
            budget.charge('factor_trials')
            rem = remainder(reduced, divisor, 19)
            divisions.append(dict(divisor=list(divisor), remainder=rem))
            check('saved remainder ' + str(divisor), rem, saved[divisor])
            check('nonzero remainder ' + str(divisor), any(rem), True)
        g = [-109375, -32500, 150, 64, 1]
        scaled_g = [budget.op('*', a, budget.op('**', 25, i))
                    for i, a in enumerate(g)]
        scaled_q = [budget.op('*', -15625, a) for a in quartic]
        check('g(25T) = -25^3 Q4(T)', scaled_g, scaled_q)
        check('order certificate polynomial', cert['polynomial'], g)
        final = cert['orders'][cert['final_order_id']]
        expected_basis = [[1, 0, '1/2', '31/30'], [0, 1, '7/25', '179/750'],
                          [0, 0, '1/50', '239/18750'], [0, 0, 0, '1/18750']]
        check('L134 displayed basis', final['basis'], expected_basis)
        check('replay binds unchanged producer', replay['producer_sha256'],
              hashes['quartic-order-certificate.json'])
        check('producer failure list', cert['failures'], [])
        check('replay failure list', replay['failures'], [])
        check('complete replay check count', len(replay['checks']), 967)
        for row in replay['checks']:
            check('replay actual/required: ' + row['name'], row['actual'], row['required'])
            check('replay passed flag: ' + row['name'], row['passed'], True)
        check('replay final decision', replay['passed'], True)
    except Exception:
        detail = traceback.format_exc()
        failures.append(detail)
        budget.failure(detail)
    out = dict(input_sha256=hashes, checks=checks, irreducibility_divisions=divisions,
               failures=failures, passed=not failures,
               scope='L134 audit supplement; order arithmetic checked by separately reviewed replay',
               budget=budget.summary())
    OUTPUT.write_text(json.dumps(out, indent=2) + '\n')
    budget.save()
    print('passed', out['passed'], 'checks', len(checks),
          'irreducibility_divisions', len(divisions), 'required', 380,
          'failures', len(failures))
    print(json.dumps(budget.summary(), sort_keys=True))
    print('certificate', OUTPUT)
    if failures:
        print(failures[0])
        raise SystemExit(1)


if __name__ == '__main__':
    main()
