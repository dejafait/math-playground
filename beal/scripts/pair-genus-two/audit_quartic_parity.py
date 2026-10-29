"""L136 audit supplement; full arithmetic is checked by the reviewed replay.

Bind accepted inputs, inspect all exact data and compare complete replay
outputs, including exceptions, sign pairs and units. No new relation search.
"""
import json
from pathlib import Path
from hashlib import sha256
from quartic_parity_budget import run

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'quartic-parity-audit.json'
RESULT = dict(completed=False, failures=[], checks=[], input_sha256={})


def reject_float(token):
    raise ValueError('Nonexact JSON number: ' + token)


def read(name):
    raw = (ROOT / name).read_bytes()
    RESULT['input_sha256'][name] = sha256(raw).hexdigest()
    return json.loads(raw, parse_float=reject_float, parse_constant=reject_float)


def check(name, actual, required):
    passed = actual == required
    RESULT['checks'].append(dict(name=name, actual=actual, required=required, passed=passed))
    if not passed:
        raise AssertionError(name)


def exact_tree(x, key=''):
    if type(x) is bool:
        return key in ('completed', 'member', 'identity')
    if isinstance(x, dict):
        return all(exact_tree(v, k) for k, v in x.items())
    if isinstance(x, list):
        return all(exact_tree(v) for v in x)
    return x is None or type(x) in (int, str)


def save():
    RESULT['budget'] = b.summary()
    OUT.write_text(json.dumps(RESULT, indent=2) + '\n')


def main():
    data = read('quartic-parity-certificate.json')
    replay = read('quartic-parity-verification.json')
    prior = read('quartic-parity-preaudit-verification.json')
    base = read('quartic-class-certificate.json')
    base_audit = read('quartic-class-audit.json')
    order = read('quartic-order-certificate.json')
    order_audit = read('quartic-order-audit.json')
    for name in ('quartic_parity_generate.py', 'quartic_parity_replay.py',
                 'quartic_parity_budget.py', 'audit_quartic_parity.py'):
        RESULT['input_sha256'][name] = sha256((ROOT / name).read_bytes()).hexdigest()
    check('exact certificate numbers and boolean positions', exact_tree(data), True)
    expected = {
        'quartic-parity-certificate.json': 'fdb376f96717188690de8c849197d8b64834afdcdc56d789f427f2cf186c5501',
        'quartic-class-certificate.json': 'c5363d1b846188e37fc53590b61de34923bb981da25ddd895cd82e14dda9b73b',
        'quartic-order-certificate.json': '4531a1f5ed1b9291da37fe111651bb72ee488cfaeadefb7679dd255fb473680e'}
    for name, digest in expected.items():
        check('canonical input hash ' + name, RESULT['input_sha256'][name], digest)
    check('L134 audit binds actual order', order_audit['input_sha256']['quartic-order-certificate.json'], expected['quartic-order-certificate.json'])
    check('L135 audit binds actual factor base', base_audit['input_sha256']['quartic-class-certificate.json'], expected['quartic-class-certificate.json'])
    check('L135 input binds actual order', base['input_sha256'], expected['quartic-order-certificate.json'])
    check('entire final maximal order', base['order'], order['orders'][order['final_order_id']])
    check('entire ordered prime lattices', data['primes'], base['generators'])
    check('entire multiplication table', data['table'], base['order']['table'])
    for label, audit, field in (('order', order_audit, 'passed'), ('class', base_audit, 'completed')):
        check(label + ' audit complete', audit[field], True)
        check(label + ' audit failures', audit['failures'], [])
    for key, value in replay.items():
        if key != 'budget':
            check('unchanged full replay field ' + key, value, prior[key])
    check('replay binds exact producer', replay['certificate_sha256'], expected['quartic-parity-certificate.json'])
    check('replay checks', replay['checks'], 316162)
    check('replay completed without failure', [replay['completed'], replay['failures']], [True, []])
    check('all 354 lattices replayed', len(replay['lattices']), 354)
    check('all 624 elements replayed', len(replay['elements']), 624)
    check('printed counts', replay['counts'], dict(accepted=182, rational_cofactor=438, omitted_prime=4))
    check('rank, threshold and upper bound', [replay['rank'], replay['required_rank'], replay['class_two_rank_upper_bound']], [30, 32, 2])
    check('printed forward pivots', replay['producer_pivots'],
          [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,25,26,27,28,29,30,31])
    summaries, exceptions, units, rational_rejects = [], [], [], []
    by_id = {e['tuple_id']: e for e in data['elements']}
    memberships = 0
    for entry in data['elements']:
        t = entry['tuple_id']
        opposite = by_id[624 - t]
        check('opposite coefficients ' + str(t), opposite['coefficients'], [-a for a in entry['coefficients']])
        keys = ['norm', 'decision', 'residual']
        if 'valuations' in entry:
            keys.extend(['valuations', 'supported_norm'])
            memberships = memberships + sum(len(tests) for tests in entry['membership'])
        check('complete sign symmetry ' + str(t), [opposite[k] for k in keys], [entry[k] for k in keys])
        summary = {k: entry[k] for k in ('tuple_id', 'norm', 'decision')}
        if 'valuations' in entry:
            summary.update(valuations=entry['valuations'], supported_norm=entry['supported_norm'])
        summaries.append(summary)
        if entry['decision'] == 'rational_cofactor':
            rational_rejects.append(dict(tuple_id=t, norm=entry['norm'], residual=entry['residual'], divisions=entry['smooth_divisions']))
        if entry['decision'] == 'omitted_prime':
            exceptions.append(dict(summary, coefficients=entry['coefficients'], omitted_norm=entry['norm'] // entry['supported_norm']))
        if entry['norm'] == 1:
            check('unit retained with zero valuations ' + str(t), [entry['decision'], entry['valuations']], ['accepted', [0] * 32])
            units.append(dict(summary, coefficients=entry['coefficients']))
    check('every complete replay element summary', replay['elements'], summaries)
    check('all successful and first-failed memberships', memberships, 7008)
    check('all rational rejections', len(rational_rejects), 438)
    check('all omitted-ideal rejections', len(exceptions), 4)
    check('both signs of every accepted element retained',
          sorted(624 - t for t in replay['accepted_ids']), replay['accepted_ids'])
    for i, (lattice, summary) in enumerate(zip(data['lattices'], replay['lattices'])):
        origin = lattice['origin']
        if 'identity' in origin:
            vector = [0] * 32
        elif 'prime' in origin:
            vector = [int(j == origin['prime']) for j in range(32)]
        else:
            left, right = origin['product']
            vector = [x + y for x, y in zip(replay['lattices'][left]['exponents'], replay['lattices'][right]['exponents'])]
        check('entire replay lattice summary ' + str(i), summary, dict(id=i, norm=lattice['norm'], exponents=vector))
    RESULT.update(rational_rejections=rational_rejects, omitted_ideal_rejections=exceptions,
                  units=units, completed=True)
    save()
    print(json.dumps(dict(completed=True, checks=len(RESULT['checks']), failures=RESULT['failures'],
                          rank=replay['rank'], required_rank=32, units=len(units),
                          budget=b.summary(), certificate=str(OUT))))


if __name__ == '__main__':
    if not globals().get('__instrumented__'):
        run(__file__)
    else:
        try:
            main()
        except Exception as exc:
            RESULT['failures'].append(repr(exc))
            save()
            raise
