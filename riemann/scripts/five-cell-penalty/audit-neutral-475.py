"""C744g conceptual audit support: exact replay and independent scalar form.

The frozen witness and all parameters are unchanged. Original artifacts
are read-only. Full evidence is saved; stdout contains only the verdict.
The scalar path uses centered-cell moments and signed response sums,
not the saved graph difference matrix or its point LDL proposal.
"""
import contextlib
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'replay-475'
OUT.mkdir(exist_ok=True)
names = ['certify-455.py', 'neutral-certificate-473.py',
         'check-neutral-473.py', 'neutral-certificate-473.json',
         'neutral-checks-473.json', 'refined-464.json',
         'compression-463.json', 'replay-466/audit.json']
snapshots = {n: (HERE/n).read_bytes() for n in names}
sha = lambda b: hashlib.sha256(b).hexdigest()
report = {'status': 'IN_PROGRESS', 'checks': [], 'failures': [],
          'input_sha256': {n: sha(b) for n, b in snapshots.items()},
          'python_version': sys.version,
          'scope': 'Fixed64+20, original ten moments, minimum-L2, complete half-energy difference.'}


def check(name, truth):
    report['checks'].append({'name': name, 'passed': bool(truth)})
    if not truth:
        report['failures'].append(name)
        raise AssertionError(name)


try:
    saved = json.loads(snapshots['neutral-certificate-473.json'])
    core = json.loads(snapshots['refined-464.json'])
    accepted = json.loads(snapshots['replay-466/audit.json'])
    check('accepted core audit passes', accepted['status'] == 'AUDIT_CHECKS_PASS'
          and not accepted['failures'] and accepted['old_artifacts_preserved'])
    for n in ('certify-455.py', 'refined-464.json', 'compression-463.json'):
        check('unchanged accepted input '+n, sha(snapshots[n]) == accepted['input_sha256'][n])

    # Re-run every Fraction check with only its output destination changed.
    source = snapshots['check-neutral-473.py'].decode()
    needle = "dest=HERE/'neutral-checks-473.json'"
    check('one checker output destination', source.count(needle) == 1)
    ns = {'__file__': str(HERE/'check-neutral-473.py'),
          '__name__': 'audit_replay', 'AUDIT_OUT': OUT}
    with (OUT/'exact-replay.log').open('w') as log, contextlib.redirect_stdout(log):
        exec(compile(source.replace(needle, "dest=AUDIT_OUT/'neutral-checks-473.json'"),
                     str(HERE/'check-neutral-473.py'), 'exec'), ns)
    exact = json.loads((OUT/'neutral-checks-473.json').read_text())
    check('all3695 exact checks pass', len(exact['checks']) == 3695
          and all(x['passed'] for x in exact['checks']) and not exact['failures'])
    check('exact report byte identical', (OUT/'neutral-checks-473.json').read_bytes()
          == snapshots['neutral-checks-473.json'])
    lemma = (HERE.parent.parent/'lemmas/C744g-five-cell-minimum-L2-neutral-graph-half-energy-stop.md').read_text()
    block = lemma.split('```text\n', 1)[1].split('```', 1)[0].split()
    frozen = saved['direction']['exact_decimal_coefficients']
    check('all canonical witness coefficients match', len(block) == 48 and
          [F(x) for x in block]+[F(0)]*16 == [F(x) for x in frozen])
    for j, threshold in enumerate(['0.0003483', '2.1740e-8', '0.0003371', '1.4041e-8', '1.9314e-9']):
        check('claimed pivot bound '+str(j), F(saved['range']['positive_pivots'][j]['lo']) > F(threshold))

    # The same audited directed elementary contracts, with explicit tighter
    # Machin/Taylor remainders. Do not compute the unused old gamma estimate.
    source = snapshots['certify-455.py'].decode().split('\nGAMMA=gamma_interval()')[0]
    edits = [('PREC = 70', 'PREC = 110'), ('range(100)', 'range(160)'),
             ('201*n**201', '321*n**321'),
             ('I(4**100)/math.factorial(100)', 'I(4**180)/math.factorial(180)'),
             ('range(1,50)', 'range(1,90)')]
    for before, after in edits:
        check('one refined library substitution '+before, source.count(before) == 1)
        source = source.replace(before, after)
    lib = {'__file__': str(HERE/'certify-455.py'), '__name__': 'refined_elementary_audit'}
    exec(compile(source, str(OUT/'refined-elementary-memory'), 'exec'), lib)
    I, PI, a, ell, sc = (lib[n] for n in ('I', 'PI', 'A', 'ELL', 'sincos'))
    iv = lambda x: I(x['lo'], x['hi'])
    mag = lambda x: max(x.lo.copy_abs(), x.hi.copy_abs())
    sym = lambda x: I(x.hi.copy_negate(), x.hi)
    def power(x, n):
        y = I(1)
        while n:
            if n % 2:
                y *= x
            x = x.sq()
            n //= 2
        return y
    def contained(x, box):
        return F(box['lo']) <= F(x.lo) <= F(x.hi) <= F(box['hi'])
    def overlaps(x, box):
        return max(F(x.lo), F(box['lo'])) <= min(F(x.hi), F(box['hi']))

    check('refined half width inside accepted enclosure', contained(a, core['parameters']['a']))
    k = [q*PI/a for q in range(84)]
    u = [x.sq() for x in k]
    nrm = [(1/a).sqrt()] + [(2/a).sqrt()]*83
    full = [x/I(2).sqrt() for x in nrm]
    C = []
    for cell in range(5):
        for sigma in (1, -1):
            beta = I(sigma)/2
            ep, em = (sigma*ell/4).exp(), (-sigma*ell/4).exp()
            sh, ch = (ep-em)/2, (ep+em)/2
            row = []
            for q in range(84):
                sk, ck = sc(q*PI/5)
                st, ct = sc(2*q*(cell-2)*PI/5)
                even = 2*(beta*sh*ck+k[q]*ch*sk)/(beta.sq()+u[q])
                odd = 2*(beta*ch*sk-k[q]*sh*ck)/(beta.sq()+u[q])
                value = full[q]*(ct*even-st*odd)
                row.append(value)
                check('centered moment inside saved row '+str((cell, sigma, q)),
                      contained(value, saved['range']['all_ten_rows'][2*cell+(sigma == -1)][q]))
            C.append(row)
    z = [I(x) for x in frozen]
    A = [row[64:] for row in C[:5]]
    b = [sum((C[j][q]*z[q] for q in range(64)), I(0)) for j in range(5)]
    G = [[sum((A[r][t]*A[s][t] for t in range(20)), I(0)) for s in range(5)] for r in range(5)]
    L = [[I(int(r == s)) for s in range(5)] for r in range(5)]
    piv = []
    for j in range(5):
        p = G[j][j]-sum((L[j][t].sq()*piv[t] for t in range(j)), I(0))
        check('independent reduced Gram positive pivot '+str(j), p.lo > 0)
        piv.append(p)
        for r in range(j+1, 5):
            L[r][j] = (G[r][j]-sum((L[r][t]*L[j][t]*piv[t] for t in range(j)), I(0)))/p
    sol = []
    for j in range(5):
        sol.append(b[j]-sum((L[j][t]*sol[t] for t in range(j)), I(0)))
    sol = [sol[j]/piv[j] for j in range(5)]
    for j in range(4, -1, -1):
        sol[j] -= sum((L[t][j]*sol[t] for t in range(j+1, 5)), I(0))
    y = [-sum((A[j][t]*sol[j] for j in range(5)), I(0)) for t in range(20)]
    for t in range(20):
        check('independent correction inside exact rational map contraction '+str(t),
              ns['y'][t].lo <= F(y[t].lo) <= F(y[t].hi) <= ns['y'][t].hi)
    v = z+y

    S = {int(p): iv(x) for p, x in core['inverse_power_sums']['response'].items()}
    cN = I(2049)/2
    ratio = u[83]/cN.sq()
    check('full response ratio below0.03435', ratio.hi < I('0.03435').lo)
    gerr = S[2]*33*power(ratio, 32)/(1-ratio).sq()
    eerr = (-2*a*cN).exp()*S[2]
    check('response rational remainder below2.440e-49', gerr.hi < I('2.440e-49').lo)
    h0 = -iv(core['gamma'])-PI/2-3*I(2).ln()-PI.ln()
    powers = [[power(x, m) for m in range(33)] for x in u]
    h, herr = [], []
    for q in range(84):
        value = h0
        for j in range(512):
            c = I(4*j+1)/2
            value += 2*u[q]/(c*(c.sq()+u[q]))
        value += sum((2*(-1)**m*powers[q][m+1]*S[2*m+3] for m in range(32)), I(0))
        error = 2*u[q]*power(u[q]/cN.sq(), 32)*S[3]
        h.append(value+sym(error)); herr.append(error)
        check('independent diagonal overlaps saved '+str(q), overlaps(h[-1], saved['energy']['h'][q]))
    check('largest digamma remainder below2.429e-49', herr[83].hi < I('2.429e-49').lo)

    prime_data = []
    for n, p, _ in lib['PRIMES']:
        delay = I(n).ln(); half = a-delay/2
        sins, cosines = [], []
        for t in range(167):
            freq = t*PI/a
            sins.append(half if t == 0 else sc(freq*half)[0]/freq)
            cosines.append(sc(freq*delay/2)[1])
        prime_data.append((n, p, -2*I(p).ln()/I(n).sqrt(), sins, cosines))

    def scalar_form(coeff, tag):
        d = [coeff[q]*nrm[q]*(-1)**q for q in range(84)]
        diag = sum((coeff[q].sq()*h[q] for q in range(84)), I(0))
        primes = []
        for n, p, weight, sins, cosines in prime_data:
            corr = I(0)
            for r in range(84):
                for s in range(r, 84):
                    entry = sins[abs(r-s)]*cosines[r+s]+sins[r+s]*cosines[abs(r-s)]
                    corr += (1 if r == s else 2)*coeff[r]*coeff[s]*full[r]*full[s]*entry
            primes.append({'n': n, 'base_prime': p, 'correlation': corr.json(),
                           'energy': (weight*corr).json()})
        arithmetic = sum((iv(x['energy']) for x in primes), I(0))
        # Signed projection first; square only after the full mode sum.
        projections, squares = [], []
        for j in range(512):
            c = I(4*j+1)/2
            projection = sum((d[q]*c/(c.sq()+u[q]) for q in range(84)), I(0))
            square = (1-(-2*a*c).exp())*projection.sq()
            projections.append(projection.json()); squares.append(square.json())
        prefix = sum((iv(x) for x in squares), I(0))
        moments = [sum((d[q]*powers[q][m] for q in range(84)), I(0)) for m in range(32)]
        tail = sum(((-1)**m*S[2*m+2]*sum((moments[t]*moments[m-t] for t in range(m+1)), I(0))
                    for m in range(32)), I(0))
        l1 = sum((I(mag(x)) for x in d), I(0))
        error = l1.sq()*(gerr+eerr)
        tail += sym(error)
        response = prefix+tail
        # Direct integral against p_+=2cosh(x/2), no square-root factors.
        pole_projection = (a/2).exp()*(1-(-a).exp())*sum((d[q]*I('0.5')/(I('0.25')+u[q]) for q in range(84)), I(0))
        pole = pole_projection.sq()
        total = diag+arithmetic+response+pole
        result = {'diagonal': diag.json(), 'prime_components': primes,
                  'arithmetic': arithmetic.json(), 'signed_response_projections': projections,
                  'response_squares': squares, 'response_prefix': prefix.json(),
                  'tail_signed_power_moments': [x.json() for x in moments],
                  'tail_absolute_remainder': error.json(), 'complete_tail': tail.json(),
                  'complete_response': response.json(), 'pole_projection': pole_projection.json(),
                  'pole': pole.json(), 'complete_energy': total.json()}
        (OUT/(tag+'-scalar.json')).write_text(json.dumps(result, indent=2)+'\n')
        return total

    ecore = scalar_form(z+[I(0)]*20, 'core')
    egraph = scalar_form(v, 'graph')
    cm = [sum((C[j][q]*z[q] for q in range(64)), I(0)) for j in range(10)]
    penalty = 256*sum((x.sq() for x in cm), I(0))
    H = ecore+penalty
    difference = egraph-H/2
    ynorm = sum((x.sq() for x in y), I(0))
    check('independent scalar graph energy positive', egraph.lo > 0)
    check('independent scalar core energy positive', H.lo > 0)
    check('independent complete difference upper below zero', difference.hi < 0)
    check('independent complete difference in canonical displayed bounds',
          F('-1.135514938e-37') <= F(difference.lo) <= F(difference.hi) <= F('-1.135514937e-37'))
    for name, value in [('core_penalized_energy', H), ('corrected_complete_energy', egraph),
                        ('independent_complete_difference', difference), ('correction_norm_squared', ynorm)]:
        check('independent scalar and exact matrix enclosures overlap '+name, overlaps(value, exact[name]))
    report['independent'] = {'precision': 110, 'a': a.json(), 'ratio': ratio.json(),
        'all_ten_centered_moment_rows': [[x.json() for x in row] for row in C],
        'gram': [[x.json() for x in row] for row in G], 'pivots': [x.json() for x in piv],
        'correction': [x.json() for x in y], 'h': [x.json() for x in h],
        'h_errors': [x.json() for x in herr], 'core_penalty': penalty.json(),
        'core_penalized_energy': H.json(), 'corrected_complete_energy': egraph.json(),
        'difference': difference.json(), 'correction_norm_squared': ynorm.json(),
        'response_rational_error': gerr.json(), 'response_exponential_error': eerr.json(),
        'required_difference_upper': '0'}
    report['status'] = 'AUDIT_CHECKS_PASS'
except Exception as exc:
    report['status'] = 'AUDIT_CHECKS_FAILED'
    report['exception'] = repr(exc)
    raise
finally:
    preserved = all((HERE/n).read_bytes() == b for n, b in snapshots.items())
    report['old_artifacts_preserved'] = preserved
    if not preserved:
        report['status'] = 'AUDIT_CHECKS_FAILED'
        report['failures'].append('old artifact changed')
    (OUT/'audit.json').write_text(json.dumps(report, indent=2)+'\n')
    print('Result:', report['status'], '; checks:', len(report['checks']),
          '; failures:', report['failures'], '; old artifacts preserved:', preserved)
    if 'independent' in report:
        print('Complete difference:', report['independent']['difference'], '; required upper <0')
        print('Core and graph energy:', report['independent']['core_penalized_energy'],
              report['independent']['corrected_complete_energy'])
    print('Full evidence:', OUT/'audit.json', OUT/'core-scalar.json', OUT/'graph-scalar.json')
