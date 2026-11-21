"""Second finite observable evaluation: directed Decimal, exponential sinh.

Only the reviewed Ball class is extracted from the earlier independent
L761 audit; no upstream audit or generator is run or overwritten.
"""
import ast
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
OUT = Path(__file__).with_suffix('.json')
down = Context(prec=260, rounding=ROUND_FLOOR)
up = Context(prec=260, rounding=ROUND_CEILING)
source = HERE/'ccm-trial-audit-371.py'
tree = ast.parse(source.read_text())
node = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'Ball')
exec(compile(ast.Module(body=[node], type_ignores=[]), str(source), 'exec'))
report = dict(outcome='IN_PROGRESS', failures=[], checks={}, directions={}, hashes={})


def require(ok, name):
    report['checks'][name] = bool(ok)
    if not ok:
        raise ArithmeticError(name)


def load(name):
    p = HERE/name
    report['hashes'][name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return json.loads(p.read_text())


def read(x):
    return Ball(*x)


def exp(x):
    return Ball(down.next_minus(down.exp(x.a)), up.next_plus(up.exp(x.b)))


def csave(x):
    return dict(real=x[0].pair(), imag=x[1].pair())


def overlap(x, saved, name):
    y = read(saved)
    require(max(x.a, y.a) <= min(x.b, y.b), name)


try:
    report['hashes'][source.name] = hashlib.sha256(source.read_bytes()).hexdigest()
    report['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    primary = load('ccm-boundary-observable-373.json')
    trial = load('ccm-trial-certificate-369.json')
    ground = load('commutator-certificate-364.json')
    require(primary['outcome'] == 'CERTIFIED_OBSERVABLE_MISS' and not primary['failures'],
            'primary_completed')
    L, pi = read(trial['constants']['L']), read(trial['constants']['pi'])
    rootL = L.sqrt()
    a = L/8
    prefactor = (exp(a)-exp(-a))/rootL
    report['prefactor'] = prefactor.pair()
    overlap(prefactor, primary['constants']['prefactor'], 'independent_prefactor')
    br, bi, er, ei = Ball(), Ball(), Ball(), Ball()
    for j in range(-120, 121):
        v = trial['projection']['exact_trial_coefficients'][str(j)]
        re, im = read(v['real']), read(v['imag'])
        nu, t = 2*pi*j/L, Ball(1)/4
        den = nu.sq()+t.sq()
        rr, ri = prefactor*t/den, -prefactor*nu/den
        bv = re/rootL, im/rootL
        ev = rr*re-ri*im, rr*im+ri*re
        br, bi, er, ei = br+bv[0], bi+bv[1], er+ev[0], ei+ev[1]
        for key, val in [('fourier_row', (rr, ri)),
                         ('boundary_contribution', bv), ('observable_contribution', ev)]:
            for component, x in zip(('real', 'imag'), val):
                overlap(x, primary['directions'][str(j)][key][component],
                        f'{j}_{key}_{component}')
        report['directions'][str(j)] = dict(fourier_row=csave((rr, ri)),
                                            boundary_contribution=csave(bv),
                                            observable_contribution=csave(ev))
    b2 = br.sq()+bi.sq()
    babs = b2.sqrt()
    require(babs.a > 0, 'nonzero_before_division')
    rr, ri = (er*br+ei*bi)/b2, (ei*br-er*bi)/b2
    g = read(ground['row']['fourier_at_boundary_normalized_ground'])
    require(g.a > 1, 'ground_absolute_value_above_1')
    d = ((rr-g).sq()+ri.sq()).sqrt()/g
    for key, vals in [('boundary', (br, bi)), ('trial_observable', (er, ei)),
                      ('normalized_trial_observable', (rr, ri))]:
        report[key] = csave(vals)
        for component, x in zip(('real', 'imag'), vals):
            overlap(x, primary[key][component], key+'_'+component)
    overlap(babs, primary['boundary_modulus'], 'boundary_modulus_overlap')
    overlap(d, primary['discrepancy'], 'discrepancy_overlap')
    require(D('4.72968e-29') < babs.a <= babs.b < D('4.72969e-29'), 'boundary_bracket')
    require(D('0.48616229937498') < d.a <= d.b < D('0.48616229937499'), 'discrepancy_bracket')
    require(d.a > D('0.1'), 'threshold_miss')
    report['boundary_modulus'], report['discrepancy'] = babs.pair(), d.pair()
    forbidden = {'Underflow', 'Overflow', 'InvalidOperation', 'DivisionByZero', 'Subnormal', 'Clamped'}
    report['flags'] = {name: [k.__name__ for k, v in ctx.flags.items() if v]
                       for name, ctx in [('down', down), ('up', up)]}
    require(not any(forbidden.intersection(v) for v in report['flags'].values()), 'arithmetic_flags')
    report['outcome'] = 'INDEPENDENT_OBSERVABLE_MISS_CONFIRMED'
except Exception as exc:
    report['outcome'] = 'FAILED'
    report['failures'].append(repr(exc))
finally:
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('RESULT', report['outcome'], 'failures:', report['failures'])
    print('required discrepancy <=1/10; certified bracket (0.48616229937498, 0.48616229937499)'
          if report['outcome'] != 'FAILED' else 'No confirmation')
    print('Full certificate:', OUT.relative_to(HERE.parent.parent))
    if report['outcome'] == 'FAILED':
        raise SystemExit(1)
