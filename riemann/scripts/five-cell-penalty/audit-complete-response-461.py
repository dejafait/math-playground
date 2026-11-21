"""Audit C744c's fixed scalar without overwriting previous evidence.

Replay the unchanged enclosure source, then check every added projection
using a regrouped 110-digit evaluation with the audited interval library.
Elementary-function contracts are reused, not independently implemented.
Fraction checks cover squares, sums, all rational tail terms and bounds.
The analytic closure/equality audit is canonical in C744c.
"""
import contextlib
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'replay-461'
OUT.mkdir(exist_ok=True)
SOURCE = HERE / 'complete-response-459.py'
CERT = HERE / 'complete-response-459.json'
BASE = HERE / 'certificate-455.json'
LIBRARY = HERE / 'certify-455.py'
CHECK_SOURCE = HERE / 'check-complete-response-459.py'
CHECK_CERT = HERE / 'complete-response-checks-459.json'
OLD_AUDIT = HERE / 'replay-457/audit.json'
preserved_paths = [SOURCE, CERT, BASE, LIBRARY, CHECK_SOURCE, CHECK_CERT, OLD_AUDIT]
snapshots = {p: p.read_bytes() for p in preserved_paths}
checks = []
refined_rows = []
report = {'status': 'IN_PROGRESS', 'checks': checks, 'failures': [],
          'python_version': sys.version,
          'scope': 'Fixed C744c scalar audit; no neutral or all-window sign.'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def check(label, value):
    checks.append({'check': label, 'passed': bool(value)})
    if not value:
        report['failures'].append(label)
        raise AssertionError(label)


def bounds(x):
    return F(x['lo']), F(x['hi'])


def contains(x, pair):
    lo, hi = bounds(x)
    return lo <= pair[0] <= pair[1] <= hi


def square(x):
    lo, hi = bounds(x)
    return (F(0) if lo <= 0 <= hi else min(lo*lo, hi*hi),
            max(lo*lo, hi*hi))


def summed(xs):
    pairs = [bounds(x) for x in xs]
    return sum((x[0] for x in pairs), F(0)), sum((x[1] for x in pairs), F(0))


def walk(x, path=''):
    if isinstance(x, dict):
        if set(x) == {'lo', 'hi'}:
            check('ordered interval ' + path, bounds(x)[0] <= bounds(x)[1])
        else:
            for k, v in x.items():
                walk(v, path + '/' + k)
    elif isinstance(x, list):
        for j, v in enumerate(x):
            walk(v, path + '/' + str(j))


try:
    c = json.loads(snapshots[CERT])
    base = json.loads(snapshots[BASE])
    old_audit = json.loads(snapshots[OLD_AUDIT])
    report['input_sha256'] = {str(p.relative_to(HERE)): sha(b) for p, b in snapshots.items()}
    check('old numerical source matches accepted step457 audit',
          sha(snapshots[LIBRARY]) == old_audit['source_sha256'])
    check('old complete input matches accepted step457 audit',
          sha(snapshots[BASE]) == old_audit['original_sha256'])
    check('step459 records the same old input hashes',
          c['inputs']['certificate_sha256'] == sha(snapshots[BASE]) and
          c['inputs']['interval_source_sha256'] == sha(snapshots[LIBRARY]))

    # Change only the output destination. Keep __file__ at the real
    # source so its reads remain the exact saved old inputs.
    code = snapshots[SOURCE].decode()
    old_output = "out = HERE/'complete-response-459.json'"
    check('one replay output destination', code.count(old_output) == 1)
    ns = {'__file__': str(SOURCE), '__name__': 'c744c_replay', 'AUDIT_OUT': OUT}
    with (OUT / 'replay.log').open('w') as log, contextlib.redirect_stdout(log):
        exec(compile(code.replace(old_output, "out = AUDIT_OUT/'complete-response-459.json'"),
                     str(SOURCE), 'exec'), ns)
    replay_bytes = (OUT / CERT.name).read_bytes()
    replay = json.loads(replay_bytes)
    check('all step459 certificate fields reproduced', replay == c)
    check('step459 certificate byte-identical replay', replay_bytes == snapshots[CERT])
    report['complete_fields_equal'] = list(c)
    report['replay_sha256'] = sha(replay_bytes)

    # Replay the old consistency checker to a new destination too.
    checker = snapshots[CHECK_SOURCE].decode()
    old_check_output = "out = HERE/'complete-response-checks-459.json'"
    check('one consistency output destination', checker.count(old_check_output) == 1)
    with (OUT / 'consistency.log').open('w') as log, contextlib.redirect_stdout(log):
        exec(compile(checker.replace(old_check_output,
                                    "out = AUDIT_OUT/'complete-response-checks-459.json'"),
                     str(CHECK_SOURCE), 'exec'),
             {'__file__': str(CHECK_SOURCE), '__name__': 'c744c_consistency', 'AUDIT_OUT': OUT})
    check('entire previous consistency report reproduced',
          (OUT / CHECK_CERT.name).read_bytes() == snapshots[CHECK_CERT])
    walk(c)
    check('exact unchanged parameters', c['parameters'] == {
        'K': 5, 'penalty': 256, 'unchanged_dyadic_witness': True,
        'old_response_end': 128, 'new_response_end_exclusive': 2048})
    check('unchanged witness and all five contributions',
          c['witness'] == base['witness'] and c['original_terms'] == base['terms'] and
          c['original_energy'] == base['energy'])
    check('all ten physical moment indices preserved by hashed input',
          [(r['cell'], r['sigma']) for r in base['all_physical_moments']] ==
          [(j, s) for j in range(5) for s in (1, -1)])
    check('strict non-neutrality preserved', bounds(base['all_physical_moments'][0]['moment'])[1] < 0)
    check('all nine prime powers and 128 old responses preserved',
          [r['n'] for r in base['prime_terms']] == [2,3,4,5,7,8,9,11,13] and
          [r['j'] for r in base['all_response_projections']] == list(range(128)))
    check('old total encloses every original contribution',
          contains(c['original_energy'], summed(c['original_terms'].values())))

    # Regroup R_j = a^(-1/2)*sqrt(1-exp(-2ac))*
    # [z_0/c + sqrt(2)*c*sum_{q=1}^{63}((-1)^q z_q)/(c^2+k_q^2)].
    # Recompute constants and all operations at 110 digits. The library's
    # directed arithmetic, exp/sqrt contracts and Machin remainder are
    # unchanged. No precision-dependent trigonometric constant is used.
    lib = ns['lib']
    for ctx in ('DOWN', 'UP', 'NEAR'):
        lib[ctx].prec = 110
    I = lib['I']
    pi = 16*lib['atan_inverse'](5)-4*lib['atan_inverse'](239)
    a = 5*I(3).ln()/4
    check('refined pi contained in accepted old enclosure', contains(base['constants']['pi'], bounds(pi.json())))
    check('refined a contained in accepted old enclosure', contains(base['constants']['a'], bounds(a.json())))
    z = [I(n)/c['witness']['denominator'] for n in c['witness']['numerators']]
    k2 = [(q*pi/a).sq() for q in range(64)]
    n0 = 1/a.sqrt()
    sqrt2 = I(2).sqrt()
    signed_z = [z[q]*((-1)**q) for q in range(64)]
    s0 = n0*(z[0]+sqrt2*sum(signed_z[1:], I(0)))
    def mag(x):
        return max(x.lo.copy_abs(), x.hi.copy_abs())
    b1 = n0*sqrt2*sum((I(mag(z[q]))*k2[q] for q in range(1,64)), I(0))
    td = c['tail_proof_data']
    check('S0 contains regrouped 110-digit enclosure', contains(td['S0'], bounds(s0.json())))
    check('saved B1 upper pays refined majorant', F(td['B1']['hi']) >= F(b1.hi))
    rows = c['additional_response_rows']
    check('all and only 1920 new response indices', [r['j'] for r in rows] == list(range(128,2048)))
    for row in rows:
        j = row['j']
        cj = I(4*j+1)/2
        terms = [signed_z[q]/(cj.sq()+k2[q]) for q in range(1,64)]
        # Group signs differently from the original sequential sum.
        positive = sum((t for t in terms if t.lo >= 0), I(0))
        negative = sum((t for t in terms if t.hi < 0), I(0))
        check('all nonzero terms assigned a definite sign j='+str(j),
              all(t.lo >= 0 or t.hi < 0 for t in terms))
        projection = n0*(z[0]/cj+sqrt2*cj*(positive+negative))*(1-(-2*a*cj).exp()).sqrt()
        check('full projection enclosure j='+str(j), contains(row['projection'], bounds(projection.json())))
        check('exact square of saved projection j='+str(j), contains(row['energy'], square(row['projection'])))
        refined_rows.append({'j':j, 'projection':projection.json()})
    check('entire added prefix sum', contains(c['additional_response_prefix'], summed(r['energy'] for r in rows)))

    cn = F(8193,2)
    check('exact first omitted c_N', bounds(td['c_N']) == (cn,cn))
    a0 = F(td['A0_upper'])
    b0 = F(td['B1']['hi'])
    check('A0 bounds full S0 interval', a0 >= max(abs(x) for x in bounds(td['S0'])))
    check('nonnegative tail majorants', a0 >= 0 and bounds(td['B1'])[0] >= 0)
    upper_series = {p:cn**(-p)+cn**(1-p)/(2*(p-1)) for p in (2,4,6)}
    for p, value in upper_series.items():
        check('exact infinite-series upper expression p='+str(p),
              contains(td['series_upper_bounds'][str(p)], (value,value)))
    tail_bound = a0*a0*upper_series[2]+2*a0*b0*upper_series[4]+b0*b0*upper_series[6]
    check('whole omitted response tail paid',
          bounds(c['all_remaining_response_tail'])[0] == 0 and
          bounds(c['all_remaining_response_tail'])[1] >= tail_bound)
    check('restored mass aggregation', contains(c['complete_restored_response_mass'],
          summed([c['additional_response_prefix'], c['all_remaining_response_tail']])))
    check('complete energy aggregation', contains(c['complete_penalized_energy'],
          summed([c['original_energy'], c['complete_restored_response_mass']])))
    table = [
        ('S0', td['S0'], '0.00720056657530500226', '0.00720056657530500228'),
        ('added prefix', c['additional_response_prefix'], '2.2785777575234464e-7', '2.2785777575234465e-7'),
        ('full tail', c['all_remaining_response_tail'], '0', '6.715256029384072e-9'),
        ('restored mass', c['complete_restored_response_mass'], '2.2785777575234464e-7', '2.3457303178172872e-7'),
        ('complete energy', c['complete_penalized_energy'], '2.0418078465924468e-7', '2.1168960422787452e-7')]
    for name, interval, lo, hi in table:
        il, ih = bounds(interval)
        check('outward displayed table '+name, F(lo) <= il <= ih <= F(hi))
    check('displayed B1 strict upper bound', b0 < F('10692.84153364051534'))
    lo, hi = bounds(c['complete_penalized_energy'])
    check('strict claimed scalar bounds', F('2.0418e-7') < lo <= hi < F('2.1169e-7'))
    rl, rh = bounds(c['complete_restored_response_mass'])
    check('strict claimed restored-mass bounds', F('2.2785e-7') < rl <= rh < F('2.3458e-7'))
    report.update(status='PASS', refinement_precision=110,
                  refined_projection_count=len(refined_rows),
                  refined_constants={'pi':pi.json(), 'a':a.json(), 'S0':s0.json(), 'B1_upper':str(b1.hi)},
                  complete_penalized_energy=c['complete_penalized_energy'],
                  complete_restored_response_mass=c['complete_restored_response_mass'],
                  all_remaining_response_tail=c['all_remaining_response_tail'],
                  required_bounds=['2.0418e-7', '2.1169e-7'],
                  rational_tail_bound=str(tail_bound))
except Exception as exc:
    report['status'] = 'FAIL'
    report['exception'] = type(exc).__name__ + ': ' + str(exc)
    raise
finally:
    for p, original in snapshots.items():
        if p.read_bytes() != original:
            report['status'] = 'FAIL'
            report['failures'].append('previous artifact changed: '+str(p))
    report['all_original_artifacts_preserved'] = all(p.read_bytes() == b for p,b in snapshots.items())
    report['check_count'] = len(checks)
    refined_path = OUT / 'refined-projections-110.json'
    refined_path.write_text(json.dumps({'precision':110, 'rows':refined_rows}, indent=2)+'\n')
    report['refined_projection_certificate'] = str(refined_path.relative_to(HERE))
    report['refined_projection_sha256'] = sha(refined_path.read_bytes())
    audit_path = OUT / 'audit.json'
    audit_path.write_text(json.dumps(report, indent=2)+'\n')
    print('Audit:', report['status'], '; checks:', len(checks), '; failures:', report['failures'])
    if 'complete_penalized_energy' in report:
        print('Complete scalar:', report['complete_penalized_energy'], '; required:', report['required_bounds'])
        print('Whole j>=2048 tail:', report['all_remaining_response_tail'])
    print('Original artifacts preserved:', report['all_original_artifacts_preserved'])
    print('Full evidence:', audit_path, '; refined projections:', refined_path)
    if report['status'] == 'FAIL':
        raise SystemExit(1)
