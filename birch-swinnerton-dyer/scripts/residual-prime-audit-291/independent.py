"""Descending-tuple Euclidean arithmetic; no original arithmetic imports."""
import json, signal, subprocess, sys, time
from pathlib import Path
from run_stage import A, ROOT, OLD, read, save, snapshot, prepare

sys.set_int_max_str_digits(0)
START = time.monotonic()
signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('aggregate_180_second_cap')))
signal.alarm(180)
P = 31
REPORT = dict(status='INCOMPLETE', failures=[], checks=0)

def check(ok, label):
    if not ok:
        raise ArithmeticError(label)
    REPORT['checks'] += 1

def norm(a):
    a = tuple(x % P for x in a)
    i = 0
    while i < len(a) and a[i] == 0:
        i += 1
    return a[i:]

def add(a, b):
    n = max(len(a), len(b))
    a = (0,) * (n-len(a)) + a
    b = (0,) * (n-len(b)) + b
    return norm(tuple(x+y for x, y in zip(a, b)))

def scale(a, u):
    return norm(tuple(u*x for x in a))

def mul(a, b):
    if not a or not b:
        return ()
    c = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return norm(c)

def divide(a, b):
    assert b
    r = norm(a)
    q = ()
    while r and len(r) >= len(b):
        shift = len(r)-len(b)
        term = (r[0]*pow(b[0], -1, P) % P,) + (0,)*shift
        q = add(q, term)
        r = add(r, scale(mul(term, b), -1))
    assert add(mul(q, b), r) == norm(a)
    assert not r or len(r) < len(b)
    return q, r

def extended(a, b):
    aa, bb = a, b
    u, v, s, t = (1,), (), (), (1,)
    steps = []
    while b:
        q, r = divide(a, b)
        steps.append(dict(a=a, b=b, quotient=q, remainder=r))
        a, b = b, r
        u, s = s, add(u, scale(mul(q, s), -1))
        v, t = t, add(v, scale(mul(q, t), -1))
    unit = pow(a[0], -1, P)
    g, u, v = scale(a, unit), scale(u, unit), scale(v, unit)
    check(add(mul(u, aa), mul(v, bb)) == g, 'extended_identity')
    return g, u, v, dict(input_a=aa, input_b=bb, steps=steps,
                         normalization=unit, gcd=g, u=u, v=v)

def integer_product(a, b):
    # Descending coefficient convolution, without modular reduction.
    return [sum(a[i]*b[k-i] for i in range(len(a)) if 0 <= k-i < len(b))
            for k in range(len(a)+len(b)-1)]

def main():
    before = read(A / 'original-hashes-before.json')
    check(snapshot() == before, 'original_hashes_before_independent')
    c = read(OLD / 'dedekind.json')
    sel = read(OLD / 'selection.json')
    basis = read(ROOT / 'scripts/seven-torsion/nonmonic-order-283/basis.json')
    check(sel['H'] == basis['H'], 'all_original_H_coefficients')
    H = list(reversed(basis['H']))
    h1 = [x % P for x in reversed(c['H1'])]
    h2 = [x % P for x in reversed(c['H2'])]
    check(len(h1) == 47 and len(h2) == 3 and len(H) == 49, 'specified_degrees')
    check(h1[0] == 1 and h2[0] == H[0] % P == 2, 'unit_top_coefficients')
    check(list(reversed(h1)) != c['H1'] and list(reversed(h2)) != c['H2'], 'both_lifts_changed')
    check(norm(h1) == norm(tuple(reversed(c['H1']))) and norm(h2) == norm(tuple(reversed(c['H2']))), 'admissible_reductions')
    hp = integer_product(h1, h2)
    divisions = [dict(product=hp[i], original=H[i], quotient=(hp[i]-H[i])//P,
                      remainder=(hp[i]-H[i])%P) for i in range(49)]
    check(all(row['remainder'] == 0 for row in divisions), 'all_49_integer_divisions')
    h3 = [row['quotient'] for row in divisions]
    check(h3 != list(reversed(c['H3'])), 'third_lift_changed')
    polys = [norm(h) for h in (h1, h2, h3)]
    d, u, v, chain1 = extended(polys[0], polys[1])
    g, s, t, chain2 = extended(d, polys[2])
    bezout = [mul(s, u), mul(s, v), t]
    quotients = []
    for f in polys:
        q, r = divide(f, g)
        check(not r and mul(q, g) == f, 'full_final_gcd_division')
        quotients.append(q)
    check(add(add(mul(bezout[0], polys[0]), mul(bezout[1], polys[1])), mul(bezout[2], polys[2])) == g, 'three_way_bezout')
    # Compare only after computing the whole gcd with alternative lifts.
    check(g == norm(tuple(reversed(c['G']))) == (1, 0, 24), 'independent_gcd_agreement')
    save(A / 'alternative-lifts.json', dict(coefficient_order='descending', p=P,
         H=H, H1=h1, H2=h2, H3=h3, homogeneous_degrees=[46, 2, 48],
         integer_divisions=divisions, reductions=polys, euclidean_chains=[chain1, chain2],
         G=g, quotients=quotients, bezout=bezout, no_infinity_factor=True))
    REPORT.update(alternative_gcd=list(reversed(g)), homogeneous_degrees=[46,2,48],
                  complete_integer_divisions=49, both_lifts_changed=True,
                  euclidean_steps=[len(chain1['steps']),len(chain2['steps'])])
    tests = [
        ('trial-quotient', 'selection.json', 'exact_search_division'),
        ('factor-multiplicity', 'dedekind.json', 'full_factorization_with_leading_unit'),
        ('frobenius-remainder', 'dedekind.json', 'frobenius_step'),
        ('leading-unit', 'dedekind.json', 'all_integer_lifts'),
        ('H3-coefficient', 'dedekind.json', 'full_integer_H3_identity'),
        ('gcd-quotient', 'dedekind.json', 'gcd_exact_division')]
    results = []
    for name, filename, expected in tests:
        dest = A / ('fixture-' + name)
        prepare(dest)
        obj = read(dest / filename)
        if name == 'trial-quotient':
            obj['trials'][-1]['q'] += 1
        elif name == 'factor-multiplicity':
            obj['factors'][0]['multiplicity'] += 1
        elif name == 'frobenius-remainder':
            obj['factors'][0]['frobenius'][1][0] = (obj['factors'][0]['frobenius'][1][0]+1) % P
        elif name == 'leading-unit':
            obj['H2'][-1] += 1
        elif name == 'H3-coefficient':
            obj['H3'][0] += 1
        elif name == 'gcd-quotient':
            obj['quotients'][0][0] = (obj['quotients'][0][0]+1) % P
        (dest / filename).write_text(json.dumps(obj, separators=(',', ':')))
        # One aggregate alarm/watchdog bounds all six children together.
        result = subprocess.run([sys.executable, '-B', str(dest / 'verify.py')], capture_output=True, text=True,
                                timeout=max(0.1, 179-(time.monotonic()-START)))
        report = read(dest / 'verification-report.json')
        row = dict(fixture=name, expected=expected, actual=report['failures'],
                   checks_before_rejection=report['checks'], returncode=result.returncode,
                   stdout=result.stdout, stderr=result.stderr)
        results.append(row)
        check(result.returncode == 0 and report['status'] == 'FAILED' and
              report['failures'] == ['ArithmeticError: '+expected], 'qualified_rejection_'+name)
    save(A / 'rejections.json', results)
    REPORT['rejections'] = [{k:v for k,v in row.items() if k not in ('stdout','stderr')} for row in results]
    after = snapshot()
    save(A / 'original-hashes-after.json', after)
    check(before == after, 'all_original_bytes_preserved')
    REPORT.update(status='PASS', preserved_original_files=len(before))

try:
    main()
except Exception as e:
    REPORT['status'] = 'FAILED'
    REPORT['failures'].append(type(e).__name__+': '+str(e))
finally:
    signal.alarm(0)
    REPORT['seconds'] = time.monotonic()-START
    save(A / 'independent-report.json', REPORT)
    print(json.dumps(REPORT))
