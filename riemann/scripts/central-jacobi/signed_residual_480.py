"""One approved n=0,d=5 signed-coefficient test; exact rational intervals.

Reuses L791's full box and L778's audited analytic evaluator. No model
search, degree change, transcendental recomputation or source-certificate
mutation. Fractions are rounded outward to the audit's 10^-100 grid.
"""
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
spec = importlib.util.spec_from_file_location('rational478', BASE/'audit_478.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
Q = audit.Q


def power(x, n):
    ans = Q(1)
    for _ in range(n):
        ans = ans*x
    return ans


def peval(co, x):
    ans = Q(0)
    for c in reversed(co):
        ans = ans*x+c
    return ans


def sign(v):
    return 1 if v.lo > 0 else -1 if v.hi < 0 else 0


def decimal_bound(x, upper=False, places=30):
    scale = 10**places
    n = (x*scale).__ceil__() if upper else (x*scale).__floor__()
    prefix = '-' if n < 0 else ''
    n = abs(n)
    return f'{prefix}{n//scale}.{n%scale:0{places}d}'


def shown(x):
    return [decimal_bound(x.lo), decimal_bound(x.hi, True)]


def main():
    paths = [ROOT/'scripts/actual-fredholm/fixed-pair-certificate-431.json',
             BASE/'fixed-model-certificate-476.json']
    hashes = {str(p.relative_to(ROOT)): audit.digest(p) for p in paths}
    inherited = json.loads(paths[0].read_text())
    model = json.loads(paths[1].read_text())
    checks, failures = [], []
    data = dict(target='fixed n=0,d=5,D=B_J/2; signed index5 residual',
                input_hashes=hashes, rational_grid='1/10^100',
                program_sha256=audit.digest(Path(__file__)),
                checks=checks, failures=failures)

    def check(name, ok):
        checks.append(dict(name=name, passed=bool(ok)))
        if not ok:
            failures.append(name)

    def require(name, ok):
        check(name, ok)
        if not ok:
            raise ValueError(name)

    try:
        require('source hash matches audited model', hashes[str(paths[0].relative_to(ROOT))] == model['source_sha256'])
        require('certified unchanged model', model['outcome'] == 'CERTIFIED_MODEL' and len(model['attempts']) == 1)
        ev = inherited['evaluation']
        require('analytic Cauchy disk radius', ev['uniform_disk_radius'] == 1600)
        eg = Q(*ev['uniform_G_error'])
        require('positive inherited analytic error', 0 < eg.lo <= eg.hi < F('3.141e-48'))
        # Analytic error is ADDED to the complete quadrature widths.
        aa = []
        for j in range(6):
            err = eg.hi/F(1600**j)
            aa.append(Q(*ev['coefficients'][j])+Q(-err, err))
        gg = [v*(8*4**j*math.factorial(j)) for j,v in enumerate(aa)]
        require('all six actual gammas positive', all(v.lo > 0 for v in gg))
        rr = [v/gg[0] for v in gg]
        # The existing full parameter box is retained; no contraction/refinement.
        box = [Q(*v) for v in model['attempts'][0]['box']]
        a,b,c = box
        dd = Q(*model['first_stage']['D'])
        require('full original positive box', all(v.lo > 0 for v in box+[dd]))
        ss = b*rr[1]
        ta = rr[5]/power(ss, 5)
        co = [Q(1)]
        for k in range(5):
            co.append(-co[-1]*(5-k)/(k+1)*(a+k)*(c+k)*dd/(a*c*(b+k)*(dd+k)))
        tm = -co[5]
        require('positive actual and model magnitudes', ta.lo > 0 and tm.lo > 0)
        # Q(x)=x^5 p(1/x)=f(x)-t. Leading coefficient is exactly one.
        fco = [Q(0)]+list(reversed(co[:5]))
        derivative = [fco[j]*j for j in range(1,6)]
        require('monic reversal and derivative factor five', fco[5].lo == fco[5].hi == 1 and derivative[4].lo == derivative[4].hi == 5)
        require('alternating fixed coefficients', all(sign(co[j]) == (-1)**j for j in range(5)))
        data.update(actual_a=[v.pair() for v in aa], gamma=[v.pair() for v in gg],
                    R=[v.pair() for v in rr], box=[v.pair() for v in box],
                    D=dd.pair(), S=ss.pair(), model_coefficients=[v.pair() for v in co],
                    f_coefficients=[v.pair() for v in fco], derivative_coefficients=[v.pair() for v in derivative],
                    actual_magnitude=ta.pair(), model_magnitude=tm.pair(),
                    actual_coefficient=(-ta).pair(), model_coefficient=co[5].pair(),
                    signed_coefficient_residual=(tm-ta).pair())
        # Fixed rational grid proposes brackets; every sign uses the full box.
        brackets = []
        left, vl = F(0), peval(derivative, Q(0))
        for n in range(1,201):
            right = F(n,1000)
            vr = peval(derivative, Q(right))
            if sign(vl)*sign(vr) == -1:
                brackets.append((left,right))
            if sign(vr):
                left,vl = right,vr
        require('four disjoint positive critical brackets', len(brackets) == 4 and all(0 < lo < hi for lo,hi in brackets) and all(brackets[j][1] < brackets[j+1][0] for j in range(3)))
        records, values = [], []
        for i,(lo,hi) in enumerate(brackets):
            initial = [str(lo),str(hi)]
            sl = sign(peval(derivative,Q(lo)))
            sr = sign(peval(derivative,Q(hi)))
            require(f'critical orientation {i+1}', (sl,sr) == ((1,-1) if i%2 == 0 else (-1,1)))
            # Width below 1e-12 is ample relative to the coefficient uncertainty.
            while hi-lo > F('1e-12'):
                mid = (lo+hi)/2
                sm = sign(peval(derivative,Q(mid)))
                require(f'refinement sign excludes zero {i+1} at {mid}', sm != 0)
                if sm == sl:
                    lo = mid
                else:
                    hi = mid
            x = Q(lo,hi)
            val = peval(fco,x)
            values.append(val)
            records.append(dict(initial=initial, interval=x.pair(),
                                derivative_endpoints=[peval(derivative,Q(lo)).pair(), peval(derivative,Q(hi)).pair()],
                                f_at_critical=val.pair()))
        # Enclose exact max/min even without presupposing the active extremum.
        lower = Q(max(values[j].lo for j in (1,3)), max(values[j].hi for j in (1,3)))
        upper = Q(min(values[j].lo for j in (0,2)), min(values[j].hi for j in (0,2)))
        positive_lower = Q(max(F(0),lower.lo), max(F(0),lower.hi))
        dl,du = ta-lower,upper-ta
        ml,mu = tm-lower,upper-tm
        residual_lower, residual_upper = tm-upper, tm-lower
        data.update(critical_points=records, collision_lower=lower.pair(), collision_upper=upper.pair(),
                    coefficient_interval=dict(lower=(-upper).pair(),upper=(-lower).pair()),
                    residual_interval=dict(lower=residual_lower.pair(),upper=residual_upper.pair()),
                    positive_magnitude_lower=positive_lower.pair(),
                    actual_collision_distances=dict(lower=dl.pair(),upper=du.pair()),
                    model_collision_distances=dict(lower=ml.pair(),upper=mu.pair()),
                    degree_drop_distance=ta.pair(),
                    critical_selection=dict(lower_x2=values[1].lo > values[3].hi,
                                            upper_x1=values[0].hi < values[2].lo))
        check('positive lower finite collision boundary', lower.lo > 0)
        check('strict model interior', ml.lo > 0 and mu.lo > 0)
        check('strict actual interior', dl.lo > 0 and du.lo > 0)
        # The diagnostic asks for the actual sign, not a prescribed direction.
        check('signed coefficient residual excludes zero', sign(tm-ta) != 0)
        for p in paths:
            check('source preserved '+str(p.relative_to(ROOT)), audit.digest(p) == hashes[str(p.relative_to(ROOT))])
        data['outcome'] = ('CERTIFIED_STRICT_INTERIOR' if not failures else
                           'STRICT_INTERVAL_VIOLATION' if dl.hi < 0 or du.hi < 0 else 'INCONCLUSIVE')
        data['summary'] = dict(gamma5=shown(gg[5]), S=shown(ss),
            actual_magnitude=shown(ta), model_magnitude=shown(tm),
            signed_coefficient_residual=shown(tm-ta),
            permitted_signed_residual_interval=dict(lower=shown(residual_lower),upper=shown(residual_upper)),
            critical_points=[dict(x=shown(Q(*v['interval'])), f=shown(values[j])) for j,v in enumerate(records)],
            collision_interval=dict(lower=shown(lower), upper=shown(upper)),
            actual_collision_distances=dict(lower=shown(dl), upper=shown(du)),
            model_collision_distances=dict(lower=shown(ml), upper=shown(mu)),
            required='both collision distances > 0 and actual magnitude > 0')
    except Exception as exc:
        failures.append(type(exc).__name__+': '+str(exc))
        data['outcome'] = 'INCONCLUSIVE'
    path = BASE/'signed-residual-certificate-480.json'
    path.write_text(json.dumps(data,indent=2)+'\n')
    print('outcome:',data['outcome'],'checks:',len(checks),'failures:',failures)
    for key,value in data.get('summary',{}).items():
        print(key+':',value)
    print('certificate:',path.relative_to(ROOT))
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
