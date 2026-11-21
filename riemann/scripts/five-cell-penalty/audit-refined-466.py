"""C744e audit: preserved replay, independent centered moments, exact residual.

No point eigenvalue is trusted. All pre-existing artifacts are preserved.
Analytic enclosure/domain justification is canonical in C744e.
"""
import contextlib
import hashlib
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'replay-466'
OUT.mkdir(exist_ok=True)
sys.set_int_max_str_digits(0)
names = ['refined-464.py', 'sign-464.py', 'check-refined-464.py',
         'refined-464.json', 'refined-checks-464.json', 'compression-463.py',
         'compression-463.json', 'certify-455.py', 'certificate-455.json',
         'complete-response-459.json', 'replay-457/audit.json']
snapshots = {name: (HERE/name).read_bytes() for name in names}
sha = lambda b: hashlib.sha256(b).hexdigest()
report = {'status': 'IN_PROGRESS', 'checks': [], 'failures': [],
          'input_sha256': {name: sha(data) for name, data in snapshots.items()},
          'scope': 'C744e fixed complete even64 compression only',
          'python_version': sys.version}


def check(name, truth):
    report['checks'].append({'name': name, 'passed': bool(truth)})
    if not truth:
        report['failures'].append(name)
        raise AssertionError(name)


def pair(x):
    return F(x['lo']), F(x['hi'])


def contains(x, value):
    lo, hi = pair(x)
    return lo <= value <= hi


def namespace(name):
    return {'__file__': str(HERE/name), '__name__': 'audit_replay',
            'AUDIT_OUT': OUT}


try:
    saved = json.loads(snapshots['refined-464.json'])
    old = json.loads(snapshots['compression-463.json'])
    accepted = json.loads(snapshots['replay-457/audit.json'])
    check('accepted interval library unchanged',
          sha(snapshots['certify-455.py']) == accepted['source_sha256'])
    check('accepted scalar inputs unchanged',
          sha(snapshots['certificate-455.json']) == accepted['original_sha256'])

    # Recompute every inherited cross entry, without doing the unused
    # coarse response/LDL calculation or overwriting its certificate.
    source = snapshots['compression-463.py'].decode()
    cut = '\nresponses, response_gram = [], zeros()'
    check('one inherited-assembly boundary', source.count(cut) == 1)
    ns = namespace('compression-463.py')
    with (OUT/'inherited-replay.log').open('w') as log, contextlib.redirect_stdout(log):
        exec(compile(source.split(cut)[0], str(HERE/'compression-463.py'), 'exec'), ns)
    I, A = ns['I'], ns['A']
    check('all nine prime components replay exactly', ns['prime_components'] == old['prime_components'])
    check('all ten physical moment rows replay exactly', ns['moments'] == old['all_ten_moment_rows'])
    for key, variable in [('prime_matrix', 'prime'), ('penalty_matrix', 'penalty')]:
        check(key+' replays exactly', ns['jmatrix'](ns[variable]) == old[key])
    # Algebraically simplified pole projection: integrate 2 cosh(x/2).
    # Use the original operation order additionally to test exact saved data.
    c = I(1)/2
    row = [ns['norm'][q]*((-1)**q)*c/(c.sq()+ns['k2'][q])*
           (1-(-2*A*c).exp()).sqrt() for q in range(64)]
    pole = [x*(A/2).exp()*(1-(-A).exp()).sqrt() for x in row]
    check('every pole row replays exactly', [x.json() for x in pole] == old['pole_row'])
    check('every pole cross entry replays exactly',
          [[(x*y).json() for y in pole] for x in pole] == old['pole_matrix'])

    # Replay every refined enclosure. Only the output path is changed;
    # __file__ and all read paths remain original, including source hashes.
    source = snapshots['refined-464.py'].decode()
    needle = "path=HERE/'refined-464.json'"
    check('one matrix replay output', source.count(needle) == 1)
    with (OUT/'matrix-replay.log').open('w') as log, contextlib.redirect_stdout(log):
        exec(compile(source.replace(needle, "path=AUDIT_OUT/'refined-464.json'"),
                     str(HERE/'refined-464.py'), 'exec'), namespace('refined-464.py'))
    replay = json.loads((OUT/'refined-464.json').read_text())
    for key, value in replay.items():
        if key != 'status':
            check('complete matrix replay field '+key, value == saved[key])
    check('only sign fields were subsequently added',
          set(saved)-set(replay) == {'congruence', 'sign_source_sha256'})

    check('all fixed expansion parameters', saved['parameters']['rational_prefix'] == 512
          and saved['parameters']['geometric_terms'] == 32
          and saved['parameters']['block_degree'] == 144
          and saved['parameters']['final_index'] == 2**180)
    check('171 consecutive blocks', [b['J'] for b in saved['blocks']] ==
          [2**j for j in range(9, 180)])
    check('complete response/integer power ranges',
          set(saved['inverse_power_sums']['response']) == {str(p) for p in range(2,67)}
          and set(saved['inverse_power_sums']['integer']) == {str(p) for p in range(2,34)})

    # Independent positive recurrence: W_(2J)=(W_J-J) union (W_J+J).
    # Start by direct finite sums, then double, instead of solving (4).
    moments = [2*sum(w**l for w in range(1,512,2)) for l in range(0,145,2)]
    moment_evidence = []
    for block in saved['blocks']:
        J = block['J']
        check('centered zeroth moment '+str(J), moments[0] == J)
        for l in range(2,145,2):
            check('independent centered telescoping '+str(J)+','+str(l),
                  (l+1)*moments[l//2]+sum(math.comb(l+1,i)*moments[(l+1-i)//2]
                  for i in range(3,l+2,2)) == J**(l+1))
        moment_evidence.append({'J': J, 'even_moments_degree_0_through_144': moments})
        for kind, C, D, powers in [('response', F(6*J-1,2), F(6*J-1,2), range(2,67)),
                                    ('integer', F(3*J-1,2), F(3*J-1), range(2,34))]:
            rho = F(J-1)/D
            check('strict displacement domain '+kind+','+str(J), 0 < rho < F(1,3))
            for p in powers:
                q = rho*F(p+145,146)
                check('strict geometric ratio '+kind+','+str(J)+','+str(p), 0 < q < 1)
                error = J*C**(-p)*math.comb(p+144,145)*rho**145/(1-q)
                check('exact block error '+kind+','+str(J)+','+str(p),
                      contains(block[kind][str(p)]['error'], error))
        moments = [2*sum(math.comb(l,t)*J**(l-t)*moments[t//2]
                         for t in range(0,l+1,2)) for l in range(0,145,2)]
    (OUT/'centered-moments.json').write_text(json.dumps(moment_evidence)+'\n')
    for kind, x, spacing, powers in [('response', F(4*2**180+1,2), 2, range(2,67)),
                                     ('integer', F(2**180), 1, range(2,34))]:
        for p in powers:
            exact = x**(-p)+x**(1-p)/(spacing*(p-1))
            check('exact final tail '+kind+','+str(p),
                  contains(saved['final_positive_tails'][kind][str(p)], exact))

    # The independent exact integer congruence verifier reads the original
    # complete saved matrices; redirect only its report destination.
    source = snapshots['check-refined-464.py'].decode()
    needle = "(HERE/'refined-checks-464.json').write_text"
    check('one exact verifier output', source.count(needle) == 1)
    with (OUT/'exact-replay.log').open('w') as log, contextlib.redirect_stdout(log):
        exec(compile(source.replace(needle, "(AUDIT_OUT/'refined-checks-464.json').write_text"),
                     str(HERE/'check-refined-464.py'), 'exec'), namespace('check-refined-464.py'))
    exact = json.loads((OUT/'refined-checks-464.json').read_text())
    check('all 6538 exact checks pass', len(exact['checks']) == 6538 and
          all(c['passed'] for c in exact['checks']) and not exact['failures'])
    check('full exact report byte-identical',
          (OUT/'refined-checks-464.json').read_bytes() == snapshots['refined-checks-464.json'])
    bound, lower = F(exact['exact_residual_norm_upper']), F(exact['uniform_eigenvalue_lower_bound'])
    check('claimed saved norm valid and below threshold', bound <= F(saved['congruence']['norm_upper']) < F('1.774e-14') < 1)
    check('strict finite margin', lower > F('1e-43'))
    check('complete entry width', F(saved['max_entry_width']) < F('5.850e-55'))
    check('gamma logarithmic remainder', F(saved['gamma_log_series_error']['hi']) < F('1.965e-90'))
    check('rational Gram remainder', F(saved['gram_geometric_error_before_normalization']['hi']) < F('5.142e-57'))
    report['bounds'] = {key: exact[key] for key in
                       ['exact_residual_norm_upper', 'B_frobenius_squared', 'uniform_eigenvalue_lower_bound']}
    report['bounds']['required_norm_upper'] = '1'
    report['bounds']['required_margin_lower'] = '1e-43'
    report['status'] = 'AUDIT_CHECKS_PASS'
except Exception as exc:
    report['status'] = 'AUDIT_CHECKS_FAILED'
    report['exception'] = repr(exc)
    raise
finally:
    preserved = all((HERE/name).read_bytes() == data for name, data in snapshots.items())
    report['old_artifacts_preserved'] = preserved
    if not preserved:
        report['status'] = 'AUDIT_CHECKS_FAILED'
        report['failures'].append('old artifact changed')
    (OUT/'audit.json').write_text(json.dumps(report, indent=2)+'\n')
    print('Result:', report['status'], '; checks:', len(report['checks']),
          '; failures:', report['failures'], '; old artifacts preserved:', preserved)
    if 'bounds' in report:
        print('Residual <1.774e-14; required <1. Margin >1e-43; required >1e-43.')
    print('Full evidence:', OUT/'audit.json', '; moments:', OUT/'centered-moments.json')
