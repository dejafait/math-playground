#!/usr/bin/env python3
"""Independent all-entry dyadic audit; never execute600/635 or resume the point.

The gzip certificate contains exact dyadic shifts and margins for EVERY
entry. Arithmetic uses common-denominator integers; storage removes only
powers of two, and checks every inverse conversion. No tolerances.
"""
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

P = Path(__file__).resolve().parent
ROOT = P.parent.parent
OUT = P / 'exact-recentering-audit-637'
TARGET = ("Audit whether 635's failed saved-Y recentering comparison is a "
          "mathematical input failure or a verifier overestimate, without "
          "modifying or resuming the parked point prescription.")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


checks = []
report = dict(target=TARGET, checks=checks, failures=[], result='INCONCLUSIVE')


def ck(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        raise AssertionError(label)


def up(x):
    return np.nextafter(x, np.inf)


def exact_record(n, q, pos):
    f = Fraction(n, 1 << q)
    return dict(numerator=str(f.numerator), denominator=str(f.denominator),
                position=pos, approximate=float(f))


try:
    c635 = json.loads((P / 'common-residual-center-repair-635.json').read_text())
    c600 = json.loads((P / 'joint-entrywise-600.json').read_text())
    pins = dict(c635['input_hashes'])
    pins['common-residual-center-repair-635.npz'] = c635['archive']['sha256']
    pins['common-residual-center-repair-executed-635.py'] = c635['script_sha256']
    pins['common-residual-center-repair-635.py'] = c635['current_source_sha256']
    pins['joint-entrywise-600.json'] = sha(P / 'joint-entrywise-600.json')
    pins['common-residual-center-repair-635.json'] = sha(P / 'common-residual-center-repair-635.json')
    report['input_hashes'] = pins
    for name, expected in pins.items():
        ck(sha(P / name) == expected, 'pin ' + name)
    ck(c635['executed_source']['sha256'] == c635['script_sha256'], 'executed635 identity')
    ck(c635['input_hashes']['joint-entrywise-600.py'] == c600['script_sha256'], '600 script identity')
    ck(c635['input_hashes']['joint-entrywise-600.npz'] == c600['archive']['sha256'], '600 archive identity')
    ck(c635['failures'] == ['saved exact-Y boxes contain all recentered solutions'], '635 sole failure')
    ck(c600['failures'] == [], '600 recorded arithmetic checks')
    failed = [v['label'] for v in c635['checks'] if not v['passed']]
    ck(len(c635['checks']) == 1050 and len(failed) == 1 and failed == c635['failures'],
       'all1050 recorded635 checks inspected')
    ck(all(set(v) == {'lo', 'hi'} and Fraction(v['lo']) <= Fraction(v['hi'])
           for v in c635['directed_ratio_intervals'])
       and len(c635['directed_ratio_intervals']) == 1022, 'complete635 ratio metadata inspected')

    shape = (1022, 2044)
    with np.load(P / 'common-residual-center-repair-635.npz', allow_pickle=False) as archive:
        stopped = {k: archive[k] for k in archive.files}
    ck(set(stopped) == set(c635['complete_array_check_summary']), 'exact four stopped arrays')
    summaries = {}
    for name, a in stopped.items():
        expected_shape = (1022, 1022) if name == 'K_reenclosure_margin' else shape
        ck(a.shape == expected_shape and a.dtype == np.float64 and np.isfinite(a).all(),
           'all stopped entries finite/dimensioned ' + name)
        s = dict(shape=list(a.shape), count=a.size, minimum=float(a.min()),
                 maximum=float(a.max()), negative_count=int(np.count_nonzero(a < 0)),
                 zero_count=int(np.count_nonzero(a == 0)))
        ck(all(v == c635['complete_array_check_summary'][name][k] for k, v in s.items()),
           'complete recorded summary matches ' + name)
        summaries[name] = s
    report['stopped_arrays'] = summaries

    names = ['galerkin_proposal', 'galerkin_z_center', 'galerkin_solution_center',
             'galerkin_inclusion_image_radius', 'galerkin_solution_radius']
    with np.load(P / 'joint-entrywise-600.npz', allow_pickle=False) as archive:
        a = [archive[k] for k in names]
    for name, v in zip(names, a):
        ck(v.shape == shape and v.dtype == np.float64 and np.isfinite(v).all(),
           'all saved entries finite/dimensioned ' + name)
    p, z, c, image, radius = a
    ck(np.all(image >= 0) and np.all(radius >= 0), 'all saved radii nonnegative')

    # Literal600 Ball(proposal)+Ball(z_center,image_radius), no matrix algebra.
    er = up((np.abs(p)+np.abs(z))*1e-15+1e-280)
    ck(np.array_equal((p+z).view(np.uint64), c.view(np.uint64)), '600 all center bits reproduced')
    assembled = up(up(image)+er)
    ck(np.array_equal(assembled.view(np.uint64), radius.view(np.uint64)), '600 all radius bits reproduced')

    # Literal635 extra Ball operations; only verify their saved stopped output.
    c1 = p+z
    r1 = up(up(np.zeros(shape))+er)
    c2 = c1-c
    r2 = up(up(r1)+up((np.abs(c1)+np.abs(c))*1e-15+1e-280))
    shift_upper = up(np.abs(c2)+r2)
    replay635 = np.nextafter(radius-up(image+shift_upper), -np.inf)
    ck(np.array_equal(replay635.view(np.uint64), stopped['Y_recenter_margin'].view(np.uint64)),
       '635 every stopped recentering bit reproduced')

    # A safe common denominator; each individual conversion independently checks it.
    audit_values = a + [er, shift_upper, stopped['Y_recenter_margin']]
    q = max(0, max(53-int(np.frexp(np.min(np.abs(v[v != 0])))[1])
                   for v in audit_values if np.any(v != 0)))

    def integers(row):
        out = []
        for v in row:
            n, d = float(v).as_integer_ratio()
            k = d.bit_length()-1
            if d != 1 << k or k > q:
                raise ArithmeticError('invalid common denominator')
            out.append(n << (q-k))
        return out

    fields = ['exact_shift', 'exact_margin', 'addition_error_slack',
              'radius_assembly_slack', 'verifier_shift_excess', 'margin_minus635']

    def encoded(n):
        if n == 0:
            return ['0', 0]
        shift = (abs(n) & -abs(n)).bit_length()-1
        mantissa, exponent = n >> shift, q-shift
        if (mantissa << shift) != n:
            raise ArithmeticError('storage roundtrip failed')
        return [str(mantissa), exponent]

    stats = {k: dict(negative_count=0, zero_count=0, minimum=None) for k in fields[1:]}
    evidence = OUT.with_suffix('.jsonl.gz')
    failure_entries = []
    with gzip.open(evidence, 'wt', encoding='utf-8') as out:
        out.write(json.dumps(dict(shape=shape, arithmetic_denominator_power=q, fields=fields,
                                  encoding='each pair [signed_integer, denominator_power] means signed_integer/2**denominator_power',
                                  formula='r-i-abs(p+z-c)', required_minimum=0))+'\n')
        for row in range(shape[0]):
            ip, iz, ic, ii, ir, ie, isu, iy = [integers(v[row]) for v in audit_values]
            values = [[] for _ in fields]
            for col, v in enumerate(zip(ip, iz, ic, ii, ir, ie, isu, iy)):
                pp, zz, cc, im, rr, ee, su, yy = v
                shift = pp+zz-cc
                margin = rr-im-abs(shift)
                line = [shift, margin, ee-abs(shift), rr-im-ee,
                        su-abs(shift), margin-yy]
                for k, n, dest in zip(fields, line, values):
                    dest.append(encoded(n))
                    if k != 'exact_shift':
                        s = stats[k]
                        s['negative_count'] += int(n < 0)
                        s['zero_count'] += int(n == 0)
                        if s['minimum'] is None or n < s['minimum']:
                            s['minimum'], s['position'] = n, [row, col]
                if min(line[1:]) < 0:
                    failure_entries.append(dict(position=[row, col], numerators=[str(x) for x in line]))
            out.write(json.dumps(dict(row=row, numerators=values), separators=(',', ':'))+'\n')
            if row % 256 == 0:
                print('exact rows checked', row+1, 'of', shape[0], flush=True)
    report['common_denominator_power'] = q
    report['entry_count'] = shape[0]*shape[1]
    report['exact_statistics'] = {k: dict(negative_count=s['negative_count'], zero_count=s['zero_count'],
                                        minimum=exact_record(s['minimum'], q, s['position']),
                                        required_minimum=0) for k, s in stats.items()}
    report['failure_entries'] = failure_entries
    report['exact_evidence'] = dict(path=str(evidence.relative_to(ROOT)), sha256=sha(evidence))
    ck(not failure_entries, 'all exact margins/slacks nonnegative at every entry')
    ck(all(sha(P / name) == expected for name, expected in pins.items()), 'all inputs unchanged')
    report['result'] = 'SAVED_IMAGE_CONTAINED_VERIFIER_EXCESS'
    report['qualifications'] = ['Original solve inclusion, arithmetic and analytic hypotheses retained',
                                'No resumed635, JY/head repair, scalar objective, floor or RH result']
except Exception as exc:
    report['failures'].append(type(exc).__name__+': '+str(exc))

report['script_sha256'] = sha(Path(__file__))
OUT.with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
print('result', report['result'], 'entries', report.get('entry_count'), 'failures', report['failures'])
for name, stat in report.get('exact_statistics', {}).items():
    print(name, 'actual min', stat['minimum'], 'required>=0', 'negative', stat['negative_count'])
print('certificate', OUT.with_suffix('.json').relative_to(ROOT),
      'full exact evidence', report.get('exact_evidence', {}).get('path'))
