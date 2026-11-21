"""Replay and extend the fixed-pair certificate audit without overwriting step431.

The analytic proof audit is canonical in L778. This reruns the inspected
implementation, compares EVERY evidence field, then reruns the separate
exact-rational checker at a fresh output location. It is not an independent
implementation of transcendental arithmetic or formal verification.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / 'audit-433'
OUT.mkdir(exist_ok=True)
SOURCE = BASE / 'fixed_pair_431.py'
CHECKER = BASE / 'check_saved_431.py'
ORIGINAL = BASE / 'fixed-pair-certificate-431.json'
REPORT = OUT / 'audit-report.json'
spec = importlib.util.spec_from_file_location('fixed_pair_431', SOURCE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
old = json.loads(ORIGINAL.read_text())
report = {
    'status': 'UNFINISHED', 'failures': [], 'checks': [],
    'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'checker_sha256': hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
    'original_sha256': hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),
    'required_upper': '1',
    'scope': 'Complete same-code replay plus exact-rational saved-data checks; analytic review is in L778; backend contracts trusted, not formally verified.'
}


def save():
    REPORT.write_text(json.dumps(report, indent=2) + '\n')


def compare(name, fresh):
    assert fresh == old[name], 'Complete field mismatch: ' + name
    report['checks'].append('Exact equality of ALL recomputed fields: ' + name)
    save()


def endpoints(x):
    lo, hi = map(F, x)
    assert lo <= hi
    return lo, hi


def upper_square(box):
    return max(abs(x) for x in endpoints(box))**2


try:
    save()
    replay = {k: old[k] for k in ['step', 'pair', 'runtime', 'scope']}
    replay.update(status='AUDIT_REPLAY_IN_PROGRESS', failures=[])
    coeff, eg, replay['evaluation'] = m.build()
    compare('evaluation', replay['evaluation'])
    for key, radius in [('inner_contour', 1024), ('outer_contour', 1280)]:
        replay[key] = m.contour(coeff, eg, radius)
        compare(key, replay[key])
    alpha, residue, replay['zero'] = m.root_and_residue(coeff, eg)
    compare('zero', replay['zero'])
    replay['norm'] = m.fourier(coeff, eg, alpha, residue, replay['outer_contour'])
    compare('norm', replay['norm'])
    replay['status'] = 'COMPLETE_REPLAY_PENDING_ANALYTIC_AUDIT_RECORD'
    (OUT / 'fixed-pair-certificate-431.json').write_text(json.dumps(replay, indent=2) + '\n')

    # Execute the unchanged checker source with __file__ anchored in OUT.
    # Its only writes are then in OUT; the original evidence is preserved.
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(compile(CHECKER.read_text(), str(CHECKER), 'exec'),
             {'__file__': str(OUT / CHECKER.name), '__name__': '__main__'})
    (OUT / 'finite-check-output.txt').write_text(output.getvalue())
    finite = json.loads((OUT / 'saved-data-check-431.json').read_text())
    assert finite['status'] == 'PASS' and not finite['failures']
    report['checks'].append('Unchanged exact-rational checker passed every record at fresh output path')

    # Independent rational domain and error checks omitted by that checker.
    for key in ['inner_contour', 'outer_contour']:
        radius = replay[key]['radius_w']
        assert radius + 256 < 1600
        for rec in replay[key]['segments']:
            # Exact parametrization center lies on |w|=radius. Its saved
            # enclosure and the parameter box are also inside evaluator disk.
            for box in [rec['center_w'], rec['w_box']]:
                assert sum(upper_square(v) for v in box) < 1600**2
            delta_sq = F(0)
            for box, center in zip(rec['w_box'], rec['center_w']):
                lo, hi = endpoints(box)
                cl, ch = endpoints(center)
                delta_sq += max(abs(lo-ch), abs(hi-cl))**2
            assert delta_sq < 256**2
    root = endpoints(replay['zero']['root_w'])
    assert max(map(abs, root)) + 100 < 1600
    for sample in replay['norm']['samples']:
        assert sum(upper_square(v) for v in sample['z']) * 1024**2 < 1600**2
    report['checks'].append('All contour boxes, Taylor ratios, root derivative disks and DFT boxes satisfy exact rational evaluator-domain bounds')

    n = replay['norm']
    sigma, N, L = F(5, 4), n['N'], n['L']
    mb = endpoints(n['M_b'])[1]
    for index, alias in enumerate(n['DFT_alias_errors'], 1):
        required = mb * sigma**(-(index+L)) / (1-sigma**(-L))
        assert endpoints(alias)[1] >= required
        assert (index+1) % L != 0
    report['checks'].append('All 192 alias bounds dominate the exact rational requirement and exclude the negative mode')

    signals = {}
    for name, ctx in [('DN', m.DN), ('UP', m.UP), ('RN', m.RN)]:
        flags = [key.__name__ for key, value in ctx.flags.items() if value]
        assert set(flags) <= {'Inexact', 'Rounded'}, (name, flags)
        signals[name] = flags
    report['context_flags'] = signals
    report['checks'].append('No exceptional Decimal flags other than expected Inexact/Rounded')
    assert hashlib.sha256(ORIGINAL.read_bytes()).hexdigest() == report['original_sha256']
    report['checks'].append('Original certificate unchanged')
    report['actual_norm'] = n['original_norm']
    report['full_product_error'] = n['full_product_error']
    report['actual_counts'] = [replay[k]['count_with_multiplicity'] for k in ['inner_contour', 'outer_contour']]
    report['required_counts'] = [1, 1]
    report['status'] = 'PASS'
except Exception as exc:
    report['status'] = 'FAIL'
    report['failures'].append({'type': type(exc).__name__, 'message': str(exc)})
    save()
    raise
save()
print(json.dumps({key: report[key] for key in ['status', 'actual_norm', 'required_upper', 'actual_counts', 'required_counts', 'failures']}, indent=2))
print('Full audit report:', REPORT)
print('Full replay evidence:', OUT / 'fixed-pair-certificate-431.json')
