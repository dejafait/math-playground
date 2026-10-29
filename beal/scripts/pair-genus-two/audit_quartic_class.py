"""L135 audit supplement: bind accepted inputs and every printed generator.

The separately reviewed complete replay checks arithmetic and exhaustion.
This supplement checks the statement/output bridge, not a new factor base.
Uses the unchanged cumulative class budget; no producer mathematics imports.
"""
import json
from pathlib import Path
from hashlib import sha256
from quartic_class_budget import run

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'quartic-class-audit.json'
RESULT = dict(completed=False, failures=[], checks=[], input_sha256={})


def reject_float(token):
    raise ValueError('Nonexact JSON number: ' + token)


def read(name):
    payload = (ROOT / name).read_bytes()
    RESULT['input_sha256'][name] = sha256(payload).hexdigest()
    return json.loads(payload, parse_float=reject_float, parse_constant=reject_float)


def check(name, actual, required):
    ok = actual == required
    RESULT['checks'].append(dict(name=name, actual=actual, required=required, passed=ok))
    if not ok:
        raise AssertionError(name)


def integral_tree(value):
    if isinstance(value, list):
        return all(integral_tree(v) for v in value)
    return type(value) is int


def save():
    RESULT['budget'] = b.summary()
    OUT.write_text(json.dumps(RESULT, indent=2) + '\n')


def main():
    data = read('quartic-class-certificate.json')
    replay = read('quartic-class-verification.json')
    order = read('quartic-order-certificate.json')
    order_audit = read('quartic-order-audit.json')
    for name in ('quartic_class_generate.py', 'quartic_class_replay.py',
                 'quartic_class_budget.py', 'audit_quartic_class.py'):
        RESULT['input_sha256'][name] = sha256((ROOT / name).read_bytes()).hexdigest()
    accepted = '4531a1f5ed1b9291da37fe111651bb72ee488cfaeadefb7679dd255fb473680e'
    check('actual order hash equals L134 audited input',
          RESULT['input_sha256']['quartic-order-certificate.json'], accepted)
    check('order audit binds same input', order_audit['input_sha256']['quartic-order-certificate.json'], accepted)
    check('class input binds accepted order', data['input_sha256'], accepted)
    check('entire final order', data['order'], order['orders'][order['final_order_id']])
    check('replay binds actual class certificate', replay['certificate_sha256'],
          RESULT['input_sha256']['quartic-class-certificate.json'])
    check('replay complete', replay['completed'], True)
    check('replay failures', replay['failures'], [])
    check('replay full check count', replay['checks'], 1409026)
    check('cutoff matches printed 159', data['bound']['U'], 159)
    check('positive square-root upper bound', data['bound']['sqrt_upper'], 1696)
    check('printed prime domain', data['primes'],
          [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,
           67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157])
    regular_expected = [(7,0),(11,5),(13,7),(17,3),(17,15),(29,15),
                        (31,17),(43,41),(47,8),(71,41),(71,44),(73,53),
                        (79,1),(79,77),(97,7),(97,56),(101,66),(113,37),
                        (127,56),(131,80),(137,119),(149,45),(151,14),
                        (151,53),(157,10),(157,86)]
    exceptional_expected = [
        (2, [[1,0,0,1],[0,1,0,1],[0,0,1,1],[0,0,0,2]]),
        (3, [[1,0,0,1],[0,1,0,1],[0,0,1,2],[0,0,0,3]]),
        (3, [[1,1,0,0],[0,0,1,0],[0,0,0,1],[0,3,0,0]]),
        (5, [[1,0,0,1],[0,1,0,0],[0,0,1,2],[0,0,0,5]]),
        (5, [[1,0,0,1],[0,1,0,1],[0,0,1,4],[0,0,0,5]]),
        (5, [[1,0,0,4],[0,1,0,0],[0,0,1,3],[0,0,0,5]])]
    generators = data['generators']
    check('exact generator count', len(generators), 32)
    for i, (p, c) in enumerate(regular_expected):
        I = generators[i]
        check('printed regular ideal ' + str(i), [I['p'], I['factor'], I['lattice']['norm']], [p,[c,1],p])
    for j, (p, columns) in enumerate(exceptional_expected):
        I = generators[26 + j]
        check('printed exceptional ideal ' + str(j),
              [I['p'], I['lattice']['columns'], I['lattice']['norm']], [p,columns,p])
    regular_summary = []
    exceptional_summary = []
    excluded = []
    for r in data['regular']:
        regular_summary.append(dict(p=r['p'], factors=r['factors'],
                                    norms=[I['lattice']['norm'] for I in r['ideals']]))
        for I in r['ideals']:
            check('integral factor at ' + str(r['p']), integral_tree(I['factor']), True)
            if not I['included']:
                excluded.append(dict(p=r['p'], factor=I['factor'], norm=I['lattice']['norm']))
                check('excluded norm exceeds cutoff at ' + str(r['p']), I['lattice']['norm'] > 159, True)
    check('complete replay regular summary', replay['regular'], regular_summary)
    for r, size, proper, count in zip(data['exceptional'], [67,212,1120], [4,7,11], [1,2,3]):
        check('exceptional domain counts at ' + str(r['p']),
              [len(r['spaces']),len(r['proper_ideals']),len(r['maximal_ideals'])], [size,proper,count])
        exceptional_summary.append(dict(p=r['p'],subspaces=size,proper_ideals=proper,
                                        maximal_ideals=r['maximal_ideals'],norms=[r['p']] * count))
    check('complete replay exceptional summary', replay['exceptional'], exceptional_summary)
    for r in data['regular'] + data['exceptional']:
        for I in r['ideals']:
            for k in ('columns','p_coordinates','closure_actions'):
                check('integral lattice data at ' + str(r['p']) + ': ' + k,
                      integral_tree(I['lattice'][k]), True)
    check('generator norm summary', replay['generator_norms'], [I['lattice']['norm'] for I in generators])
    check('all generator norms at most 157', max(replay['generator_norms']) <= 157, True)
    RESULT['excluded_regular_ideals'] = excluded
    RESULT['scope'] = 'L135 statement/output binding; full arithmetic and domain exhaustion checked by separately reviewed and executed replay'
    RESULT['completed'] = True
    save()
    print(json.dumps(dict(completed=True,checks=len(RESULT['checks']),
                          failures=RESULT['failures'],budget=b.summary(),certificate=str(OUT))))


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
