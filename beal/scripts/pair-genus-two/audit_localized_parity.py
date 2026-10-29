"""L137 saved-instance audit supplement; no search or producer import.

The reviewed verifier checks complete linear algebra. This supplement binds
the audited upstream objects and tests the seven printed identities in every
coordinate using integer addition, rather than bit-mask elimination.
"""
import json
import re
from fractions import Fraction
from hashlib import sha256
from localized_parity_budget import ROOT, Budget

OUT = ROOT / 'localized-parity-audit.json'
RESULT = dict(completed=False, failures=[], checks=[], input_sha256={})
EXPECTED = {
    'quartic-order-certificate.json': '4531a1f5ed1b9291da37fe111651bb72ee488cfaeadefb7679dd255fb473680e',
    'quartic-class-certificate.json': 'c5363d1b846188e37fc53590b61de34923bb981da25ddd895cd82e14dda9b73b',
    'quartic-parity-certificate.json': 'fdb376f96717188690de8c849197d8b64834afdcdc56d789f427f2cf186c5501',
    'localized-parity-certificate.json': 'eb7e393e385bf994d7398ed8162d307b3f2ff2d9f593b0133cf024684ea5e76f'}


def reject_number(token):
    raise ValueError('Nonexact JSON number: ' + token)


def read(name):
    raw = (ROOT / name).read_bytes()
    RESULT['input_sha256'][name] = sha256(raw).hexdigest()
    return json.loads(raw, parse_float=reject_number, parse_constant=reject_number)


def check(name, actual, required):
    passed = actual == required
    RESULT['checks'].append(dict(name=name, actual=actual, required=required, passed=passed))
    if not passed:
        raise AssertionError(name)


def exact_tree(value, key=''):
    if type(value) is bool:
        return key in ('completed', 'included')
    if isinstance(value, dict):
        return all(exact_tree(v, k) for k, v in value.items())
    if isinstance(value, list):
        return all(exact_tree(v) for v in value)
    return value is None or type(value) in (int, str)


def main():
    order, base, parity, cert = [read(name) for name in EXPECTED]
    field = read('quartic-field-certificate.json')
    replay = read('localized-parity-verification.json')
    prior = read('localized-parity-preaudit-verification.json')
    old_replay = read('quartic-parity-verification.json')
    audits = [read('quartic-' + name + '-audit.json') for name in ('order', 'class', 'parity')]
    for name, digest in EXPECTED.items():
        check('canonical hash ' + name, RESULT['input_sha256'][name], digest)
    for name in ('localized_parity.py', 'verify_localized_parity.py',
                 'localized_parity_budget.py', 'audit_localized_parity.py'):
        RESULT['input_sha256'][name] = sha256((ROOT / name).read_bytes()).hexdigest()
    check('localized certificate exact numbers and boolean positions', exact_tree(cert), True)
    for audit, name, status in zip(audits, ('order', 'class', 'parity'), ('passed', 'completed', 'completed')):
        check(name + ' audit status and failures', [audit[status], audit['failures']], [True, []])
        filename = 'quartic-' + name + '-certificate.json'
        check(name + ' audit binding', audit['input_sha256'][filename], EXPECTED[filename])
        check(name + ' every saved audit comparison',
              all(c['passed'] is True and c['actual'] == c['required'] for c in audit['checks']), True)
    # These comparisons bind full objects. Upstream primality/maximality proofs
    # are reused from the canonical audits, not inferred from matching flags.
    g = [-109375, -32500, 150, 64, 1]
    check('L133 integral polynomial', [int(x) for x in field['integral_absolute_polynomial']], g)
    check('L133 branch polynomial', field['input_q4'], [7, 52, -6, -64, -25])
    check('L133 scaling coefficient identity', [g[i] * 25**i for i in range(5)],
          [-25**3 * x for x in field['input_q4']])
    check('L133 field maps', [field['field_maps']['alpha_to_theta'], field['field_maps']['theta_to_alpha']],
          [[0, 25], ['0', '1/25']])
    check('L134 exact polynomial', order['polynomial'], g)
    final = order['orders'][order['final_order_id']]
    basis = [[Fraction(x) for x in row] for row in final['basis']]
    expected_basis = [[1, 0, Fraction(25, 50), Fraction(19375, 18750)],
                      [0, 1, Fraction(14, 50), Fraction(4475, 18750)],
                      [0, 0, Fraction(1, 50), Fraction(239, 18750)],
                      [0, 0, 0, Fraction(1, 18750)]]
    check('entire displayed integral basis', [[str(x) for x in row] for row in basis],
          [[str(Fraction(x)) for x in row] for row in expected_basis])
    check('index and discriminant', [order['total_index'], final['discriminant']], [937500, 2874960])
    check('full class input order', base['order'], final)
    check('class input order hash', base['input_sha256'], EXPECTED['quartic-order-certificate.json'])
    check('parity full multiplication table', parity['table'], final['table'])
    check('parity factor base hash', parity['input_sha256'], EXPECTED['quartic-class-certificate.json'])
    check('all ordered factor-base records', parity['primes'], base['generators'])
    check('factor-base length', len(base['generators']), 32)
    check('entire exceptional characteristic domain', [e['p'] for e in base['exceptional']], [2, 3, 5])
    check('all exceptional maximal space IDs', [e['maximal_ideals'] for e in base['exceptional']],
          [[58], [185, 208], [990, 997, 1066]])
    check('exact support indices', [i for i, p in enumerate(base['generators']) if 330 % p['p'] == 0],
          [1, 26, 27, 28, 29, 30, 31])
    check('entire localized selected lattices', cert['selected_primes'],
          [base['generators'][i] for i in cert['selected_indices']])
    check('11 prime-to-index hypothesis', order['total_index'] % 11 != 0, True)
    check('11 full polynomial reduction', [x % 11 for x in g], [9, 5, 7, 9, 1])
    check('11 factorization', cert['regular11']['factors'], [[5, 1]] * 4)
    check('exactly one regular 11 record', len([e for e in base['regular'] if e['p'] == 11]), 1)
    # Complete new replay, not just success flags, must match the preserved run.
    check('replay key set', sorted(replay), sorted(prior))
    for key in replay:
        if key != 'budget':
            check('unchanged replay field ' + key, replay[key], prior[key])
    check('replay input hashes', replay['input_hashes'],
          [EXPECTED[n] for n in ('quartic-class-certificate.json', 'quartic-parity-certificate.json',
                                'localized-parity-certificate.json')])
    check('complete replay result', [replay['completed'], replay['failures'], replay['checks'],
          replay['rank'], replay['required_rank'], replay['upper_bound']], [True, [], 6739, 30, 32, 2])
    check('L136 audit binds its complete replay', audits[2]['input_sha256']['quartic-parity-verification.json'],
          RESULT['input_sha256']['quartic-parity-verification.json'])
    accepted = [e for e in parity['elements'] if e['decision'] == 'accepted']
    old_accepted = [e for e in old_replay['elements'] if e['decision'] == 'accepted']
    check('all accepted IDs in three inputs',
          [cert['accepted_ids'], [e['tuple_id'] for e in old_accepted]],
          [[e['tuple_id'] for e in accepted]] * 2)
    check('all 182 full valuation vectors', cert['accepted_valuations'], [e['valuations'] for e in accepted])
    check('all 182 audited replay vectors', cert['accepted_valuations'], [e['valuations'] for e in old_accepted])
    check('fixed row dimensions', [len(cert['accepted_valuations']), sorted({len(v) for v in cert['accepted_valuations']})],
          [182, [32]])
    lemma = (ROOT.parent.parent / 'lemmas/L137-pair-quartic-localized-parity-bound.md').read_text()
    printed = [dict(coordinate=int(i), relation_indices=[int(k.strip()) for k in ks.split(',')])
               for i, ks in re.findall(r'^\| e_(\d+) \| ([0-9, ]+) \|$', lemma, re.M)]
    check('all printed witnesses equal full replay witnesses', printed, replay['selected_original_span_witnesses'])
    check('seven distinct required coordinates', [w['coordinate'] for w in printed], [1, 26, 27, 28, 29, 30, 31])
    RESULT['coordinate_witnesses'] = []
    contributions = 0
    for witness in printed:
        indices = witness['relation_indices']
        check('original-row domain ' + str(witness['coordinate']),
              len(indices) <= 10 and all(0 <= k < 182 for k in indices) and len(set(indices)) == len(indices), True)
        totals = [0] * 32
        for k in indices:
            for j in range(32):
                totals[j] += cert['accepted_valuations'][k][j]
                contributions += 1
        actual = [x % 2 for x in totals]
        required = [int(j == witness['coordinate']) for j in range(32)]
        check('all 32 coordinates for e_' + str(witness['coordinate']), actual, required)
        RESULT['coordinate_witnesses'].append(dict(witness, integer_totals=totals, parity=actual))
    check('coordinate-contribution finite bound', contributions <= 7 * 10 * 32, True)
    RESULT['fixed_domain'] = dict(rows=182, columns=32, witnesses=7,
                                contributions=contributions, contribution_cap=2240)
    RESULT['completed'] = True


if __name__ == '__main__':
    budget = Budget()
    try:
        main()
    except Exception as exc:
        RESULT['failures'].append(repr(exc))
        budget.fail(exc)
        raise
    finally:
        budget.save()
        RESULT['budget'] = budget.data
        OUT.write_text(json.dumps(RESULT, indent=2) + '\n')
        print(json.dumps(dict(completed=RESULT['completed'], checks=len(RESULT['checks']),
            failures=RESULT['failures'], rank=30 if RESULT['completed'] else None,
            required_rank=32, fixed_domain=RESULT.get('fixed_domain'),
            cumulative_xor_bounds=budget.data, certificate=str(OUT))))
