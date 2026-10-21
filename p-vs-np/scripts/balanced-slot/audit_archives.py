"""Recheck complete saved component archives without regenerating or replacing them."""
import argparse
import hashlib
import json
from pathlib import Path
import checker

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output'

def fixed_goals():
    # Independent literal definitions, no compiler or planner import.
    def n(a): return '(~' + a + ')'
    def i(a, b): return '(' + a + '>' + b + ')'
    def x(a, b): return i(i(a, b), n(i(b, a)))
    def e(a, b): return n(x(a, b))
    a, b, c = 'A', 'B', 'C'
    z = n(i('q', 'q'))
    return dict(assoc=e(x(x(a,b),c),x(a,x(b,c))), comm=e(x(a,b),x(b,a)),
                cancel=e(x(a,a),z), zero_slots=e(z,x(z,z)),
                trans=i(e(a,b),i(e(b,c),e(a,c))), symm=i(e(a,b),e(b,a)),
                congL=i(e(a,b),e(x(a,c),x(b,c))),
                congR=i(e(a,b),e(x(c,a),x(c,b))), refl=e(a,a),
                imp_bridge=e(i(a,b),i(n(n(a)),b)), double_neg_bridge=e(a,n(n(a))))

def image(s):
    def walk(t):
        if isinstance(t, str): return t
        if t[0] == 'not': return ('not', walk(t[1]))
        return ('or', ('not', walk(t[1])), walk(t[2]))
    return checker.serialize(walk(checker.parse(s, 'native')[0]))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('group', choices=['library', 'cancel', 'exchange'])
    args = parser.parse_args()
    result = {'group': args.group, 'checks': [], 'failures': []}
    saved = json.loads((OUT/'certificate.json').read_text())
    lib = json.loads((OUT/'fixed-library-checks.json').read_text())
    tasks = []
    if args.group == 'library':
        for name, goal in fixed_goals().items():
            for mode in ('native', 'not-or'):
                tasks.append((name, mode, goal if mode == 'native' else image(goal),
                              lib['checks'][name][mode], None))
    else:
        name = 'm4-root-cancel' if args.group == 'cancel' else 'm8-root-exchange'
        case = next(c for c in saved['cases'] if c['name'] == name)
        trace = json.loads((OUT/(name+'.trace.json')).read_text())
        for mode in ('native', 'not-or'):
            goal = checker.slot_goal(trace['input_terms'], case['pair'], case['action'], mode)
            tasks.append((name, mode, goal, case['proofs'][mode]['measurement'],
                          case['proofs'][mode]['bounds']))
    dest = OUT/('audit-170-'+args.group+'.json')
    def save(): dest.write_text(json.dumps(result, indent=2)+'\n')
    save()
    for name, mode, goal, old, bounds in tasks:
        measured = checker.check(OUT/(name+'.'+mode+'.jsonl.gz'), goal)
        equal = measured == old
        checks = {} if bounds is None else {
            key: {'actual': measured[field], 'required': bounds[bound],
                  'pass': measured[field] <= bounds[bound]}
            for key, field, bound in [
                ('lines','lines','required_lines_max'),
                ('depth','max_line_depth','required_depth_max'),
                ('record_nodes','max_record_nodes','required_record_nodes_max'),
                ('bytes','bytes','required_bytes_max')]}
        result['checks'].append({'name': name, 'mode': mode, 'expected_goal': goal,
                                 'measurement': measured, 'matches_saved': equal, 'bounds': checks})
        if not equal or not all(v['pass'] for v in checks.values()):
            result['failures'].append(name+'.'+mode)
        save()
        print(name, mode, 'complete archive accepted; matches saved', equal,
              'actual/required', checks, 'certificate', dest.relative_to(HERE.parent.parent), flush=True)
    if args.group == 'library':
        measured_constants = {'L': max(x['measurement']['lines'] for x in result['checks'])}
        for mode in ('native', 'not-or'):
            rows = [x['measurement'] for x in result['checks'] if x['mode'] == mode]
            measured_constants[mode] = {'D': max(x['max_line_depth'] for x in rows),
                                        'S': max(x['max_record_nodes'] for x in rows)}
        result['constants'] = measured_constants
        if measured_constants != lib['constants']: result['failures'].append('library constants')
        result['corruptions'] = []
        for mode in ('native','not-or'):
            goal = checker.slot_goal(['p0','p1'], 0, 'exchange', mode)
            for corrupt in saved['corruptions'][mode]:
                try:
                    checker.check(HERE/corrupt['path'], goal)
                except checker.Invalid as err:
                    result['corruptions'].append({'path': corrupt['path'], 'rejected': True, 'reason': str(err)})
                else:
                    result['failures'].append(corrupt['path'])
        result['source_hashes'] = []
        prov = json.loads((HERE/'sources/provenance.json').read_text())
        for source in [dict(path=prov['extract'], sha256=prov['sha256'])]+prov['retrieval_snapshots']:
            actual = hashlib.sha256((HERE/'sources'/source['path']).read_bytes()).hexdigest()
            result['source_hashes'].append({'path': source['path'], 'actual': actual,
                                            'required': source['sha256'], 'pass': actual == source['sha256']})
            if actual != source['sha256']: result['failures'].append(source['path'])
    result['complete'] = True
    save()
    print('failures', result['failures'], 'certificate', dest.relative_to(HERE.parent.parent), flush=True)
    if result['failures']: raise SystemExit(1)

if __name__ == '__main__': main()
