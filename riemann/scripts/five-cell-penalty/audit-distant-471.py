"""C744f: complete preserved replay and load-bearing scalar audit.

All pre-existing files are read-only. The accepted Decimal contracts
remain inputs; this does not independently implement transcendentals.
Analytic identities and form-domain reasoning are recorded in C744f.
"""
import contextlib
import hashlib
import json
import runpy
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE/'replay-471'
OUT.mkdir(exist_ok=True)
names = ['certify-455.py', 'certificate-455.json', 'compression-463.json',
         'refined-464.json', 'replay-457/audit.json', 'replay-466/audit.json',
         'distant-469.py', 'distant-469.json', 'distant-trace-469.py',
         'distant-trace-469.json', 'check-distant-469.py', 'distant-checks-469.json']
snap = {n: (HERE/n).read_bytes() for n in names}
sha = lambda x: hashlib.sha256(x).hexdigest()
report = {'status': 'IN_PROGRESS', 'checks': [], 'failures': [],
          'input_sha256': {n: sha(b) for n, b in snap.items()},
          'scope': 'complete C744f two-block certificate; no middle or odd sign',
          'python_version': sys.version}


def save():
    (OUT/'audit.json').write_text(json.dumps(report, indent=2)+'\n')


def check(name, condition):
    report['checks'].append({'name': name, 'passed': bool(condition)})
    if not condition:
        report['failures'].append(name)
        save()
        raise AssertionError(name)


def ns(name):
    return {'__file__': str(HERE/name), '__name__': 'audit_replay', 'AUDIT_OUT': OUT}


try:
    save()
    accepted = json.loads(snap['replay-466/audit.json'])
    oldaudit = json.loads(snap['replay-457/audit.json'])
    for name in ('refined-464.json', 'compression-463.json', 'certificate-455.json',
                 'certify-455.py'):
        check('accepted input unchanged '+name, sha(snap[name]) == accepted['input_sha256'][name])
    check('accepted interval library', sha(snap['certify-455.py']) == oldaudit['source_sha256'])
    core = json.loads(snap['refined-464.json'])
    first = json.loads(snap['distant-469.json'])
    lib = runpy.run_path(str(HERE/'certify-455.py'))
    I, A, PI = (lib[n] for n in ('I', 'A', 'PI'))
    sv = lambda x: I(x['lo'], x['hi'])

    def pw(x, m):
        value = I(1)
        while m:
            if m % 2:
                value *= x
            x = x.sq()
            m //= 2
        return value

    # Only these 64 T values from distant-469 enter the sign proof.
    # Recompute them from the previously accepted inverse-power sums,
    # without using any newly computed distant inverse powers.
    sums = {int(p): sv(v) for p, v in core['inverse_power_sums']['response'].items()}
    evidence = []
    for s in range(64):
        u = (s*PI/A).sq()
        direct = sum((u/((I(4*j+1)/2).sq()+u) for j in range(512)), I(0))
        series = sum((((-1)**m)*pw(u, m+1)*sums[2*m+2] for m in range(32)), I(0))
        ratio = u/(I(2049)/2).sq()
        error = u*pw(ratio, 32)*sums[2]
        value = direct+series+I(error.hi.copy_negate(), error.hi)
        row = {'label': s, 'direct': direct.json(), 'cutoff': 512,
               'ratio': ratio.json(), 'error': error.json(), 'T': value.json()}
        check('all core T fields '+str(s), row == first['T_values'][s])
        check('core expansion ratio '+str(s), ratio.lo >= 0 and ratio.hi < 1)
        evidence.append(row)
    (OUT/'core-T.json').write_text(json.dumps(evidence, indent=2)+'\n')
    save()
    print('All 64 load-bearing core T enclosures reproduced; full trace replay starting.', flush=True)

    # Full source replay includes every phase reset/rotation, every scalar
    # enclosure and combined vector, all prefix columns and the entire tail.
    source = snap['distant-trace-469.py'].decode()
    needle = "OUT=HERE/'distant-trace-469.json'"
    check('unique trace output redirection', source.count(needle) == 1)
    with (OUT/'trace-replay.log').open('w') as log, contextlib.redirect_stdout(log):
        exec(compile(source.replace(needle, "OUT=AUDIT_OUT/'distant-trace-469.json'"),
                     str(HERE/'distant-trace-469.py'), 'exec'), ns('distant-trace-469.py'))
    check('entire trace certificate byte-identical',
          (OUT/'distant-trace-469.json').read_bytes() == snap['distant-trace-469.json'])
    save()
    print('Entire trace certificate reproduced byte for byte; integer replay starting.', flush=True)

    source = snap['check-distant-469.py'].decode()
    needle = "(HERE/'distant-checks-469.json').write_text"
    check('unique checker output redirection', source.count(needle) == 1)
    with (OUT/'integer-replay.log').open('w') as log, contextlib.redirect_stdout(log):
        exec(compile(source.replace(needle, "(AUDIT_OUT/'distant-checks-469.json').write_text"),
                     str(HERE/'check-distant-469.py'), 'exec'), ns('check-distant-469.py'))
    replay = json.loads((OUT/'distant-checks-469.json').read_text())
    check('full integer report byte-identical',
          (OUT/'distant-checks-469.json').read_bytes() == snap['distant-checks-469.json'])
    check('every integer check passes', replay['checks'] == 823342 and
          replay['status'] == 'PASS' and not replay['failures'])
    bound = F(replay['total_trace_upper'])
    eps = F(core['congruence']['norm_upper'])
    check('strict canonical trace bound', bound < F('.289114'))
    check('strict Schur margin', 1-eps-bound > F('.709'))
    check('correct required threshold', F(replay['required_upper']) <= 1-eps)
    report['bounds'] = {key: replay[key] for key in ('prefix_trace', 'entire_tail_trace_upper',
                       'total_trace_upper', 'required_upper')}
    report['bounds']['epsilon_upper'] = str(core['congruence']['norm_upper'])
    report['bounds']['required_trace_upper'] = '.289114'
    report['bounds']['congruence_gap_lower_exact'] = str(1-eps-bound)
    report['bounds']['required_gap_lower'] = '.709'
    report['integer_checks'] = replay['checks']
    report['status'] = 'AUDIT_CHECKS_PASS'
except Exception as exc:
    report['status'] = 'AUDIT_CHECKS_FAILED'
    report['exception'] = repr(exc)
    raise
finally:
    report['old_artifacts_preserved'] = all((HERE/n).read_bytes() == b for n, b in snap.items())
    if not report['old_artifacts_preserved']:
        report['status'] = 'AUDIT_CHECKS_FAILED'
        report['failures'].append('old artifact changed')
    save()
    print('Result:', report['status'], '; audit checks:', len(report['checks']),
          '; integer checks:', report.get('integer_checks'), '; failures:', report['failures'],
          '; old artifacts preserved:', report['old_artifacts_preserved'])
    if 'bounds' in report:
        print('Trace:', report['bounds']['total_trace_upper'], '; required < .289114 and',
              report['bounds']['required_upper'], '; congruence gap > .709')
    print('Full evidence:', OUT/'audit.json')
