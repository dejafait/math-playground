#!/usr/bin/env python3
"""First frozen-N cell: exact endpoints and reuse of audited L499 envelopes.

No sampling, new transcendental evaluation, mass replay or source-proof audit.
All arithmetic is unrounded Fraction endpoint arithmetic. Analytic transport
is proved separately in C499a; this certificate verifies its scalar interfaces.
"""
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
OUT = HERE / 'first-frozen-cell-certificate.json'
checks = []
report = {
    'scope': 't=.16836, X<=x<4*pi*(691005^2-t/16), N=691004. '
             'L494 saddle and L496 base-phase qualifications retained; '
             'right endpoint, other cells/times and zero time excluded.',
    'method': 'Exact rational endpoint arithmetic; previously audited pi, '
              'L(X) and L499 positive envelopes; log(Y/X)<=Y/X-1.',
}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def encode(a):
    if isinstance(a, F):
        return {'numerator': str(a.numerator), 'denominator': str(a.denominator)}
    if isinstance(a, tuple):
        return {'lower': encode(a[0]), 'upper': encode(a[1])}
    if isinstance(a, list):
        return [encode(v) for v in a]
    if isinstance(a, dict):
        return {k: encode(v) for k, v in a.items()}
    return a


def rat(a):
    if int(a['denominator']) <= 0:
        raise ValueError('nonpositive denominator')
    return F(int(a['numerator']), int(a['denominator']))


def read(a):
    lo, hi = rat(a['lower']), rat(a['upper'])
    if lo > hi:
        raise ValueError('reversed input interval')
    return lo, hi


def pair(a):
    return a if isinstance(a, tuple) else (F(a), F(a))


def add(a, b):
    a, b = pair(a), pair(b)
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    b = pair(b)
    return add(a, (-b[1], -b[0]))


def mul(a, b):
    a, b = pair(a), pair(b)
    v = [x*y for x in a for y in b]
    return min(v), max(v)


def div(a, b):
    b = pair(b)
    if b[0]*b[1] <= 0:
        raise ValueError('zero in divisor')
    return mul(a, (1/b[1], 1/b[0]))


def check(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=encode(actual),
                       required=encode(required)))
    if not passed:
        raise ValueError(name)


def run():
    corner_path = HERE/'fixed-corner-two-charge.json'
    audit_path = HERE/'l499-certificate-audit.json'
    old, audit = [json.loads(p.read_text()) for p in (corner_path, audit_path)]
    report['inputs'] = [dict(path=p.name, sha256=digest(p))
                        for p in (corner_path, audit_path)]
    links = [v['sha256'] for v in audit['inputs'] if v['path'] == corner_path.name]
    check('exact L499 certificate retained by prior audit', links == [digest(corner_path)],
          links, [digest(corner_path)])
    check('prior audit completion record', audit['result'] == 'PASS' and audit['failures'] == [],
          dict(result=audit['result'], failures=audit['failures']), 'PASS; no failures')
    # This is provenance, not a substitute for the accepted L499 proof/audit.
    X, t, N = F('6000284561421.5'), F('.16836'), 691004
    ell0, cap, eps = F('24.18022820120389'), F('.500000000001'), F('.0000006')
    eps1 = (eps+F('.0000013'))*F('8.770232')/F('.14142')
    expected = dict(x=X, t=t, N=N, ell0=ell0, cap=cap, epsilon=eps,
                    epsilon_1=eps1, grid_denominator=str(10**50))
    check('all inherited exact parameters', old['parameters'] == encode(expected),
          old['parameters'], expected)
    pi, LX = [read(old['elementary_inputs'][k]) for k in ('pi', 'L')]
    check('positive inherited elementary intervals', pi[0] > 0 and LX[0] > 0,
          [pi[0], LX[0]], '>0')
    Y = mul(4*((N+1)**2-t/16), pi)
    width = sub(Y, X)
    delta = sub(div(Y, X), 1)
    cutoff_X = add(div(X, mul(4, pi)), t/16)
    saddle_lower_edge = mul(4*N*N, pi)
    # For all x<=Y: L(x)<=L(X)+log(Y/X)<=L(X)+(Y-X)/X.
    LY_upper = LX[1]+delta[1]
    tLY_upper = t*LY_upper
    check('spatial derivative monotonicity range', X >= 2, X, '>=2')
    check('time in L494 and L496 closed domain', F('.16836') <= t <= F('.1718'),
          t, '[.16836,.1718]')
    check('nonempty open cell', width[0] > 0, width, '>0')
    check('anchor cutoff lower bound', N*N <= cutoff_X[0], cutoff_X, '>=691004^2')
    check('anchor cutoff upper bound', cutoff_X[1] < (N+1)**2, cutoff_X, '<691005^2')
    check('fixed support log N below L(X)/2', saddle_lower_edge[1] < X,
          saddle_lower_edge, X)
    check('whole cell in uniform analytic domain', tLY_upper < F('5.17'),
          tLY_upper, '<5.17')
    b = old['bounds']
    R, J, S, K, D, Us, Ur, total = [read(b[k]) for k in
        ('R', 'Jplus', 'log_support', 'Lhat_cap', 'product_derivative_cap',
         'charge_saddle', 'charge_remainder', 'charge_total')]
    for name, a in [('R', R), ('Jplus', J), ('S0', S), ('K0', K), ('D0', D)]:
        check('positive inherited '+name, a[0] > 0, a, '>0')
    Q, C = X*(X*X+5)/(1+X*X)**2, (7*X*X-5)/(1+X*X)**2
    check('exact inherited saddle corrections', rat(b['Qalpha']) == Q
          and rat(b['Calpha']) == C and Q > 0 and C > 0, [Q, C], 'L499 values, both positive')
    Us_direct = div(mul(t*(Q+C), K), ell0)
    Ur_direct = add(mul(R, eps/2), div(mul(2, add(mul(D, eps), mul(R, eps1))), ell0))
    for name, direct, retained in [('saddle charge', Us_direct, Us), ('remainder charge', Ur_direct, Ur)]:
        check('retained enclosure for '+name,
              retained[0] <= direct[0] <= direct[1] <= retained[1], direct, retained)
    combined = add(Us, Ur)
    check('retained total covers both charges', total[0] <= combined[0] <= combined[1] <= total[1],
          combined, total)
    prefix = F('.698591427320603743332620581311')
    complement = F(21688332681815698, 72057594037927936)
    reserve = 1-prefix-complement
    check('exact complete mass reserve', rat(b['reserve_lower']) == reserve,
          reserve, rat(b['reserve_lower']))
    margin = sub(reserve, total)
    check('uniform total charge threshold', total[1] < F('.000020830490'), total, '<.000020830490')
    check('strict uniform reserve comparison', total[1] < reserve, total[1], reserve)
    check('uniform remaining margin threshold', margin[0] > F('.00040166'), margin, '>.00040166')
    report.update(parameters=dict(X=X, t=t, N=N, ell0=ell0, cap=cap, epsilon=eps,
                                   epsilon_1=eps1, Y_definition='4*pi*((N+1)^2-t/16)',
                                   right_endpoint_included=False),
        elementary_inputs=dict(pi=pi, LX=LX),
        domain=dict(Y=Y, width=width, relative_width=delta, cutoff_X=cutoff_X,
                    four_pi_N_squared=saddle_lower_edge, LY_upper=LY_upper,
                    tLY_upper=tLY_upper),
        uniform_envelopes=dict(R0=R, J0=J, S0=S, K0=K, D0=D,
                              Q_at_X=Q, C_at_X=C, charge_saddle=Us,
                              charge_remainder=Ur, charge_total=total,
                              reserve_lower=reserve, remaining_margin=margin))


try:
    run()
except Exception as exc:
    report['exception'] = f'{type(exc).__name__}: {exc}'
    if not checks or checks[-1]['passed']:
        checks.append(dict(name='execution completed', passed=False,
                           actual=report['exception'], required='no exception'))
failures = [r['name'] for r in checks if not r['passed']]
report.update(result='FAIL' if failures else 'PASS', checks=checks, failures=failures,
              script_sha256=digest(Path(__file__)))
OUT.write_text(json.dumps(encode(report), indent=2)+'\n')


def dec(a, upper=True):
    with localcontext() as ctx:
        ctx.prec = 26
        ctx.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        return str(Decimal(a.numerator)/Decimal(a.denominator))


print(f"{report['result']}: {len(checks)} checks; failures={failures}")
if 'domain' in report:
    d, u = report['domain'], report['uniform_envelopes']
    print(f"Y in [{dec(d['Y'][0], False)}, {dec(d['Y'][1])}]; right endpoint excluded")
    print(f"width in [{dec(d['width'][0], False)}, {dec(d['width'][1])}]; required >0")
    print(f"t*L(Y) <= {dec(d['tLY_upper'])}; required <5.17")
    print(f"uniform charge <= {dec(u['charge_total'][1])}; required <{dec(u['reserve_lower'], False)}")
    print(f"remaining margin >= {dec(u['remaining_margin'][0], False)}; required >.00040166")
print(f'certificate={OUT.relative_to(HERE.parent.parent)}')
raise SystemExit(bool(failures))
