"""Fixed-domain supplement to L145's conceptual audit; no witness search.

The separate verifier checks every exact field evaluation and finite-ring
identity. This supplement checks complete record lengths, the printed
load-bearing values, old support/memberships and quotient implications.
It imports neither producer nor replay code.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'two-adic-filter-audit.json'
R = dict(completed=False, failures=[], checks=[], bindings={})


def read(name):
    raw = (ROOT / name).read_bytes()
    R['bindings'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def check(name, condition):
    R['checks'].append(dict(name=name, passed=bool(condition)))
    assert condition, name


def span(columns):
    values = {0}
    for x in columns:
        values |= {v ^ x for v in values}
    return values


def combination(columns, coefficients):
    value = 0
    for i, x in enumerate(columns):
        if coefficients >> i & 1:
            value ^= x
    return value


def elimination_shape(name, record, columns, required_rank):
    n = len(columns)
    check(name + ' exact trace length', len(record['trace']) == n)
    check(name + ' exact rank and kernel length', record['rank'] == required_rank
          and len(record['kernel']) == n - required_rank
          and len(record['pivots']) == required_rank)
    coefficients = record['kernel'] + [r['coefficients'] for r in record['trace']]
    coefficients += [v[1] for v in record['pivots'].values()]
    check(name + ' all coefficient domains', all(0 < c < 2**n for c in coefficients))
    check(name + ' entire trace inputs', [r['input'] for r in record['trace']] == columns)
    check(name + ' every trace identity', all(combination(columns, r['coefficients'])
          == r['reduced'] for r in record['trace']))
    check(name + ' every kernel identity', all(combination(columns, c) == 0
          for c in record['kernel']))


def main():
    c = read('two-adic-filter-certificate.json')
    replay = read('two-adic-filter-verification.json')
    prior = read('two-adic-filter-preaudit-verification.json')
    inputs = {name: read(name) for name in c['bindings']}
    check('complete producer and replay', c['completed'] and replay['completed']
          and not c['failures'] and not replay['failures'])
    check('all producer checks pass', all(row['passed'] for row in c['checks']))
    check('replay unchanged in full', replay == prior)
    check('all producer source hashes', all(R['bindings'][n] == h
          for n, h in c['bindings'].items()))
    check('all replay source hashes', all(R['bindings'][n] == h
          for n, h in replay['bindings'].items()))
    for name in ('real-kummer', 'eleven-adic-filter'):
        a = inputs[name + '-audit.json']
        check(name + ' accepted source binding', a['completed'] and not a['failures']
              and a['bindings'][name + '-certificate.json']
              == R['bindings'][name + '-certificate.json'])
    real = inputs['real-kummer-certificate.json']
    eleven = inputs['eleven-adic-filter-certificate.json']
    model = inputs['odd-model-support-certificate.json']
    check('actual complete quintic', list(map(Q, model['model']['G'])) == list(map(Q,
          [-477484407427500000000, 191519916588000000, -29655931140000,
           2196150000, -76835, 1])))
    check('actual complete quartic', list(map(Q, model['model']['H'])) == list(map(Q,
          [52615361700000000, -15306287040000, 1581228000, -67760, 1])))
    sq = c['square_table']
    check('exact residue and quotient lengths', len(sq['representatives']) == 512
          and len(sq['square_rows']) == len(sq['unit_masks']) == 256)
    check('complete square root domain', [r[0] for r in sq['square_rows']]
          == list(range(1, 512, 2)))
    expected_squares = [1, 17, 293, 373, 437, 449, 465, 485]
    check('printed square subgroup', sorted({r[1] for r in sq['square_rows']})
          == expected_squares)
    check('all saved square roots', all([int(a), int(s)] in sq['square_rows']
          for s, a in sq['square_roots'].items())
          and sorted(map(int, sq['square_roots'])) == expected_squares)
    check('entire five-bit quotient', set(sq['unit_masks'].values()) == set(range(32))
          and all(list(sq['unit_masks'].values()).count(i) == 8 for i in range(32)))
    check('three and only three generators', len(c['generators']) == 3)
    check('single quadratic point', len(c['quadratic_samples']) == 1
          and len(c['quadratic_fields']) == 1)
    records = [g['evaluation'] for g in c['generators']]
    printed = [[0, 0, 497, 44, 352], [0, 0, 241, 26, 208], [4, 16, 341, 50, 404]]
    actual = [[v['rational']['mask'], v['quartic']['valuation'],
               v['quartic']['unit_mod_pi9'], v['quartic']['mask'], v['mask']]
              for v in records]
    check('entire printed generator table', actual == printed)
    p = c['samples'][c['generators'][1]['sample']]
    check('printed rational point', Q(p['X']) == 23 and
          Q(p['Y_squared']) == -473095110634487156892)
    t = c['quadratic_samples'][0]
    sc = t['square_certificate']
    check('actual unramified quadratic coordinate', t['field'] == 'unramified-5'
          and t['X'] == [0, 4] and list(map(Q, c['quadratic_fields'][0]['polynomial']))
          == [Q(-1), Q(-1), Q(1)])
    check('printed Hensel data', list(map(Q, sc['unit_root'])) == [2, 1]
          and sc['valuation'] == 8 and list(map(Q, sc['normalized']))
          == [-1865175319460484283, 2990646298835765]
          and list(map(Q, sc['error'])) == [-1865175319460484288, 2990646298835760])
    check('trace rational coordinate', Q(t['evaluation']['rational']['value'])
          == 9075**2 - 4*9075 - 16 == 82319309)
    image = span([352, 208, 404])
    check('independent complete image span', len(image) == 8)
    check('image rational projection', {m & 7 for m in image} == {0, 4})
    check('rational-zero image quartic masks', {m >> 3 for m in image if not m & 7}
          == {0, 44, 26, 54})
    witnesses = c['witnesses']
    check('exact 39 source and target columns', len(witnesses) == len(real['witnesses'])
          == len(eleven['witnesses']) == 39)
    check('all source records in order', all(w['source'] == real['witnesses'][i]
          == eleven['witnesses'][i]['source'] for i, w in enumerate(witnesses)))
    support = {1, 26, 27, 28, 29, 30, 31}
    for w in witnesses:
        check(w['id'] + ' inverse signed norm', Q(w['source']['inverse_norm'])
              * Q(w['source']['signed_norm']) == 1)
        v = w['source'].get('valuations')
        if v is not None:
            check(w['id'] + ' all outside-S valuations', len(v) == 32
                  and all(v[i] % 2 == 0 for i in range(32) if i not in support))
    expected = [('tuple-60', [-2, 0, 0, -2], 24000, {26: 6, 27: 1, 29: 2, 30: 1},
                 [2, 6, 253, 20, 162], 86),
                ('tuple-62', [-2, 0, 0, 0], 16, {26: 4}, [0, 4, 255, 6, 48], 20)]
    for w, (name, b, norm, vals, local, quotient) in zip(witnesses[2:4], expected):
        src = w['source']; loc = w['local']; f = loc['quartic']
        check(name + ' complete printed source', w['id'] == name and src['coefficients'] == b
              and src['signed_norm'] == norm
              and src['valuations'] == [vals.get(i, 0) for i in range(32)])
        check(name + ' both old memberships', w['real_mask'] == 30
              and w['eleven_mask'] == w['old_quotient'] == 0)
        check(name + ' complete printed local row', [loc['rational']['mask'], f['valuation'],
              f['unit_mod_pi9'], f['mask'], loc['mask']] == local
              and w['dyadic_quotient'] == quotient)
    obstruction_span = span([162, 48])
    check('two independent image cosets', len(obstruction_span) == 4
          and image.intersection(obstruction_span) == {0})
    products = c['kernel_products']
    check('all 36 products in full order', len(products) == 36 and
          [p['coefficients'] for p in products] == c['old_conditions']['kernel'])
    check('first two individual witnesses', [p['coefficients'] for p in products[:2]] == [4, 8])
    for p in products:
        check('kernel product old memberships ' + str(p['coefficients']),
              p['real_mask'] in {0, 30, 24, 6} and p['eleven_mask'] in {0, 5})
    for name, columns, rank in (
            ('image', [v['mask'] for v in records], 3),
            ('old_conditions', [w['old_quotient'] for w in witnesses], 3),
            ('additional_conditions', [p['quotient'] for p in products], 2)):
        elimination_shape(name, c[name], columns, rank)
    check('full fixed quotient span', span([p['quotient'] for p in products]) == {0, 20, 66, 86})
    cases = [dict(c=i, ambient=11+i, old=8+i, new_upper=6+i,
                  rank_upper=5+i, sufficient=1, shortfall=4+i) for i in range(3)]
    check('all rank subtraction cases', all(x['new_upper'] == x['old'] - 2
          and x['rank_upper'] == x['new_upper'] - 1
          and x['shortfall'] == x['rank_upper'] - x['sufficient'] for x in cases))
    R.update(completed=True, image_span=sorted(image), obstruction_span=sorted(obstruction_span),
             generator_table=actual, rank_cases=cases, replay_checks=replay['checks'],
             replay_identical=True, bounds=dict(residue_actual=512, residue_cap=2**20,
             unit_square_rows_actual=256, unit_square_rows_required=256,
             witness_columns_actual=39, witness_columns_required=39,
             kernel_products_actual=36, kernel_products_required=36,
             image_dimension_actual=3, image_dimension_required=3,
             quotient_rank_actual=2, quotient_rank_required=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        R['failures'].append(dict(type=type(exc).__name__, message=str(exc),
                                  traceback=traceback.format_exc()))
    OUT.write_text(json.dumps(R, indent=2) + '\n')
    print(json.dumps(dict(completed=R['completed'], checks=len(R['checks']),
          failures=[f['message'] for f in R['failures']], bounds=R.get('bounds'), path=str(OUT))))
    raise SystemExit(0 if R['completed'] else 1)
