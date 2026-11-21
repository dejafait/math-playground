"""L922 validity audit: complete unchanged replay, provenance, and conclusions.

No new sign calculation or budget refinement. Analytic review is in L922.
The imported replay uses L037's conditional Decimal/jet primitives.
"""
import contextlib
import hashlib
import importlib.util
import json
import platform
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = Path(__file__).with_suffix('.json')
REPLAY = HERE / 'h2-shared-taylor-audit-replay-215.json'
LOG = HERE / 'h2-shared-taylor-audit-replay-215.log'
SOURCE = HERE / 'h2-shared-taylor-213.json'
PRIOR = HERE / 'h2-shared-taylor-check-213.json'
sys.set_int_max_str_digits(100000)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    report = {'status': 'running', 'checks': {}, 'failures': [],
              'python': platform.python_version(),
              'scope': 'Complete L922 fixed-budget validity audit; Decimal correctness assumed',
              'replay': str(REPLAY.relative_to(ROOT))}
    def check(name, condition):
        report['checks'][name] = bool(condition)
        if not condition:
            raise AssertionError(name)
    try:
        saved = json.loads(SOURCE.read_text())
        old = json.loads(PRIOR.read_text())
        preserved = {str(path.relative_to(ROOT)): sha(path) for path in
                     (SOURCE, PRIOR, HERE / 'h2-shared-taylor-213-first-pass.py',
                      HERE / 'h2-shared-taylor-213-first-pass.json')}
        for owner, data in [('producer', saved), ('prior_replay', old)]:
            for path, expected in data['input_sha256'].items():
                check(owner + ':' + path, sha(ROOT / path) == expected)
        check('fixed_budget', saved['budget'] == {
            'parameter_degree': 2, 'lambda': ['0', '1/5120'],
            'center': '1/10240', 'radius': '1/10240', 'spatial_panels': 64,
            'spatial_cutoff': 2, 'theta_terms': 4, 'spatial_order': 8, 'digits': 100})
        check('source_status', saved['status'] == 'fixed_budget_inconclusive')
        check('prior_status', old['status'] == 'passed')

        spec = importlib.util.spec_from_file_location('check213audit', HERE / 'h2-shared-taylor-check-213.py')
        replay = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(replay)
        replay.OUT = REPLAY
        with LOG.open('w') as log, contextlib.redirect_stdout(log):
            replay.main()
        fresh = json.loads(REPLAY.read_text())
        # This compares all exact tail fractions, 1280 reconstructed records,
        # 20 moment/error sums, 99 exact trace checks, and the final model.
        check('complete_replay_equal_to_prior', fresh == old)
        Q = replay.Q
        trace = saved['trace']
        check('all_trace_nodes_have_three_coefficients',
              all(len(node['coefficients']) == 3 for node in trace))
        check('seven_even_seeds', set(saved['moment_models']) == {str(k) for k in range(0, 14, 2)})
        check('six_log_coefficients', set(saved['S_models']) == {str(k) for k in range(1, 7)})
        check('seven_q_coefficients', len(saved['q_models']) == 7)
        check('three_minors', len(saved['minor_models']) == 3)
        check('q_zero_is_one', trace[saved['q_models'][0]]['op'] == 'constant'
              and trace[saved['q_models'][0]]['label'] == '1')

        def model_range(node_id):
            node = trace[node_id]
            return replay.polynomial_range([Q(c) for c in node['coefficients']]) + Q(node['remainder'])
        summary = saved['summary']
        for index, node_id in enumerate(saved['minor_models']):
            check(f'minor_summary_includes_model_{index + 1}',
                  Q(summary['minor_ranges'][index]).contains(model_range(node_id)))
        for index in (0, 1):
            check(f'minor_{index + 1}_positive', Q(summary['minor_ranges'][index]).a > 0)
        final = trace[saved['minor_models'][2]]
        check('final_polynomial_summary', Q(summary['final_polynomial_range']).contains(
            replay.polynomial_range([Q(c) for c in final['coefficients']])))
        check('final_remainder_summary', summary['final_remainder'] == final['remainder'])
        check('mass_summary', Q(summary['mass_range']).contains(model_range(saved['moment_models']['0'])))
        check('mass_threshold', Q(summary['mass_range']).a > F('.49712'))
        det = Q(summary['determinant'])
        check('saved_final_inclusion', det.contains(model_range(saved['minor_models'][2])))
        check('saved_final_threshold', F('-4.482e-31') < det.a < 0 < det.b < F('1.073e-30'))
        check('saved_final_matches_minor', summary['determinant'] == summary['minor_ranges'][2])
        check('constant_coefficient_contains_zero', Q(final['coefficients'][0]).a < 0 < Q(final['coefficients'][0]).b)
        check('remainder_threshold', Q(final['remainder']).a > F('-4.893e-37')
              and Q(final['remainder']).b < F('4.893e-37'))
        check('spatial_tail_threshold', Q(saved['tails']['spatial']).b < F('5.679e-45'))
        check('total_tail_threshold', Q(saved['tails']['total']).b < F('4.345e-20'))
        for key in ('center', 'right'):
            moments = saved['quadrature'][key]['moments']
            check(key + '_ten_even_moments', set(moments) == {str(k) for k in range(0, 20, 2)})
            check(key + '_all_moments_positive', all(Q(v).a > 0 for v in moments.values()))

        # The fresh replay leaves the actual shared contexts in this module.
        base = sys.modules['certify_hankel']
        from decimal import DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal
        signals = (DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal)
        contexts = {}
        for name in ('DOWN', 'UP', 'NEAR'):
            ctx = getattr(base, name)
            contexts[name] = {'precision': ctx.prec, 'rounding': ctx.rounding,
                              'traps': {s.__name__: ctx.traps[s] for s in signals},
                              'exceptional_flags': {s.__name__: ctx.flags[s] for s in signals}}
        check('fresh_contexts_match_saved', contexts == saved['arithmetic'])
        check('fresh_context_contracts', all(v['precision'] == 100 and all(v['traps'].values())
              and not any(v['exceptional_flags'].values()) for v in contexts.values()))
        check('all_preserved_artifacts_unchanged', all(sha(ROOT / path) == value for path, value in preserved.items()))
        report.update({'status': 'passed', 'fresh_arithmetic': contexts,
                       'preserved_sha256': preserved,
                       'input_sha256': {str(path.relative_to(ROOT)): sha(path) for path in
                          (Path(__file__), SOURCE, PRIOR, HERE / 'h2-shared-taylor-check-213.py')},
                       'replay_sha256': sha(REPLAY),
                       'summary': {'records_replayed': 1280, 'moments_replayed': 20,
                           'trace_nodes_replayed': 99, 'complete_prior_replay_equal': True,
                           'determinant': summary['determinant'],
                           'required': 'strictly positive determinant lower endpoint',
                           'sign_test': 'inconclusive; fixed-budget stop preserved',
                           'validity_failures': [], 'budget_refined': False}})
    except Exception as exc:
        report['status'] = 'failed'
        report['failures'].append(type(exc).__name__ + ': ' + str(exc))
        raise
    finally:
        OUT.write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps({'status': report['status'], 'checks': len(report['checks']),
                          'failures': report['failures'], 'summary': report.get('summary'),
                          'evidence': str(OUT.relative_to(ROOT)),
                          'complete_replay': str(REPLAY.relative_to(ROOT))}, indent=2))


if __name__ == '__main__':
    main()
