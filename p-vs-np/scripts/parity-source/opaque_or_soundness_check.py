"""Finite endpoint corroboration for L107; universal proof is in the lemma."""
import hashlib
import itertools
import json
from pathlib import Path

import checker


HERE = Path(__file__).resolve().parent
OUT = HERE / 'output'


def tagged_evaluate(t, sources, opaques):
    if isinstance(t, str):
        if t == 'true':
            return True
        if t == 'false':
            return False
        return sources.get(('source', t), False)
    if t[0] == 'n':
        return not tagged_evaluate(t[1], sources, opaques)
    if isinstance(t[1], tuple) and t[1][0] == 'n':
        return (not tagged_evaluate(t[1][1], sources, opaques)
                or tagged_evaluate(t[2], sources, opaques))
    return opaques.get(('opaque', t), True)


def ordinary(t, env):
    if isinstance(t, str):
        if t in ('true', 'false'):
            return t == 'true'
        return env[t]
    if t[0] == 'n':
        return not ordinary(t[1], env)
    return ordinary(t[1], env) or ordinary(t[2], env)


def conjunction(a, b):
    return ('n', ('o', ('n', a), ('n', b)))


def main():
    report = json.loads((OUT / 'report.json').read_text())
    diagnostic = report['fixtures']['three-row']['endpoint_diagnostic']
    fixture = json.loads((OUT / 'three-row-input.json').read_text())
    expected = diagnostic['exact_formula']
    clauses = [checker.parse(s) for s in
               ['(x|(~y))', '((~x)|y)', '(y|(~z))',
                '((~y)|z)', '(x|z)', '((~x)|(~z))']]
    f = conjunction(conjunction(clauses[0], conjunction(clauses[1], clauses[2])),
                    conjunction(conjunction(clauses[3], clauses[4]), clauses[5]))
    endpoint = ('n', f)
    checks = {
        'fixture_endpoint_matches_saved': checker.fixture_endpoint(fixture) == expected,
        'explicit_six_clause_tree_matches_saved': checker.spell(endpoint) == expected,
        'all_six_tagged_clause_values_true': all(tagged_evaluate(c, {}, {}) for c in clauses),
        'tagged_F_true': tagged_evaluate(f, {}, {}),
        'tagged_exact_endpoint_false': not tagged_evaluate(checker.parse(expected), {}, {}),
    }
    assignments = []
    for bits in itertools.product((False, True), repeat=3):
        env = dict(zip(('x', 'y', 'z'), bits))
        assignments.append({'assignment': env, 'F': ordinary(f, env),
                            'endpoint': ordinary(endpoint, env)})
    checks['ordinary_unsatisfiable_all_eight_assignments'] = all(
        not a['F'] and a['endpoint'] for a in assignments)
    saved_env = diagnostic['decoded_countervaluation']
    reconciled = []
    for source_tree, token in diagnostic['opaque_OR'].items():
        t = checker.parse(source_tree)
        value = tagged_evaluate(t, {}, {})
        reconciled.append({'source_tree': source_tree, 'saved_token': token,
                           'tagged_value': value, 'saved_value': saved_env[token]})
    checks['saved_countervaluation_reconciled'] = (
        all(not saved_env[x] for x in ('x', 'y', 'z'))
        and all(r['tagged_value'] == r['saved_value'] for r in reconciled))
    certificate = {
        'scope': 'Endpoint corroboration only; universal rule proof is L107 sections 1-2.',
        'global_assignment': {'every_nonconstant_source_atom': False,
                              'every_positive_left_OR_tree_atom': True,
                              'namespace': 'disjoint (source,name) and (opaque,tree) pairs'},
        'actual_endpoint': expected,
        'endpoint_sha256': hashlib.sha256(expected.encode()).hexdigest(),
        'fixture': fixture,
        'clause_values': [{'formula': checker.spell(c), 'value': tagged_evaluate(c, {}, {})}
                          for c in clauses],
        'opaque_reconciliation': reconciled,
        'ordinary_eight_assignments': assignments,
        'checks': checks,
        'actual_checks_passed': sum(checks.values()),
        'required_checks_passed': len(checks),
        'failures': [k for k, passed in checks.items() if not passed],
        'universal_rule_soundness_proved_by_script': False,
    }
    path = OUT / 'opaque-or-soundness.json'
    path.write_text(json.dumps(certificate, indent=2) + '\n')
    print('Endpoint checks: %d/%d; exact endpoint value=%d; required=0; failures=%s; certificate=%s'
          % (sum(checks.values()), len(checks), tagged_evaluate(endpoint, {}, {}),
             certificate['failures'], path.relative_to(HERE.parent.parent)))
    if certificate['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
