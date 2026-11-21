"""Independent exact replay of certificate1917; no producer import/quadrature.

All saved operands and both endpoints are compared, not merely sign flags.
L917/audit197 supplies analytic containment conditional on L037 contracts.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import platform

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'scripts/heat/low-time-h2-uniform-195.json'
CERT = ROOT / 'scripts/heat/cubic-saved-moment-propagation-1917.json'
PRIOR = ROOT / 'scripts/heat/low-time-h2-audit-197.json'
OUT = Path(__file__).with_suffix('.json')


def box(record):
    assert isinstance(record['lower'], str) and isinstance(record['upper'], str)
    a, b = F(record['lower']), F(record['upper'])
    assert a <= b
    return a, b


def encode(pair):
    return dict(zip(('lower', 'upper'), map(str, pair)))


def mul(x, y):
    corners = [a*b for a in x for b in y]
    return min(corners), max(corners)


def sq(x):
    a, b = x
    return (0 if a <= 0 <= b else min(a*a, b*b)), max(a*a, b*b)


def sub(x, y):
    return x[0]-y[1], x[1]-y[0]


def main():
    producer_bytes = CERT.read_bytes()
    saved = json.loads(producer_bytes)
    source = json.loads(SOURCE.read_bytes())
    prior = json.loads(PRIOR.read_bytes())
    failures = []

    def check(claim, condition):
        if not condition:
            failures.append(claim)

    source_hash = sha256(SOURCE.read_bytes()).hexdigest()
    check('producer source path', saved['source'] == str(SOURCE.relative_to(ROOT)))
    check('producer source hash', saved['source_sha256'] == source_hash)
    check('accepted audit197 input hash', prior['input_sha256'][str(SOURCE.relative_to(ROOT))] == source_hash)
    # Also ensure the accepted replay's own source/code inputs remain unchanged.
    prior_hash_checks = {}
    for name, expected in prior['input_sha256'].items():
        prior_hash_checks[name] = sha256((ROOT/name).read_bytes()).hexdigest() == expected
        check('audit197 hash: ' + name, prior_hash_checks[name])
    selected = {'lambda': source['panels'][0]['lambda'],
                'moments': {str(k): source['panels'][0]['moments'][str(k)] for k in (0, 2, 4, 6)}}
    check('complete selected input copies', selected == saved['selected_inputs'])
    check('audit197 complete panel0 lambda', selected['lambda'] == prior['panels'][0]['lambda'])
    for k, record in selected['moments'].items():
        check('audit197 moment ' + k, record == prior['panels'][0]['moments'][k])
        check('positive actual moment box ' + k, box(record)[0] > 0)
    check('closed parameter endpoints', box(selected['lambda']) == (F(0), F(1,5120)))
    check('parameter exact record', box(saved['parameter_exact']) == box(selected['lambda']))

    # Independently specify the entire expected expression graph, including
    # the secondary consistency expression. Refuse reordered/changed operands.
    plan = []
    def op(name, kind, *args):
        plan.append((name, kind, list(args)))
    for j, (k, factor) in enumerate(zip((0,2,4,6), ('1','1/2','1/12','1/120'))):
        op('M'+str(k), 'input', '/panels/0/moments/'+str(k))
        op('gamma'+str(j), 'scale', 'M'+str(k), factor)
    for args in [
        ('gamma1_squared','square','gamma1'),
        ('gamma0_gamma2','multiply','gamma0','gamma2'),
        ('A','subtract','gamma1_squared','gamma0_gamma2'),
        ('gamma2_squared','square','gamma2'),
        ('gamma1_gamma3','multiply','gamma1','gamma3'),
        ('B','subtract','gamma2_squared','gamma1_gamma3'),
        ('gamma1_gamma2','multiply','gamma1','gamma2'),
        ('gamma0_gamma3','multiply','gamma0','gamma3'),
        ('C','subtract','gamma1_gamma2','gamma0_gamma3'),
        ('AB','multiply','A','B'), ('four_AB','scale','AB','4'),
        ('H','subtract','four_AB','C_squared')]:
        if args[0] == 'H':
            op('C_squared','square','C')
        op(*args)
    for j in (1,2,3):
        op('b'+str(j)+'_reciprocal','reciprocal','gamma0')
        op('b'+str(j),'multiply','gamma'+str(j),'b'+str(j)+'_reciprocal')
    for args in [
        ('b1_squared','square','b1'), ('v','subtract','b1_squared','b2'),
        ('b1_b2','multiply','b1','b2'), ('three_b1_b2','scale','b1_b2','3'),
        ('b1_cubed','multiply','b1_squared','b1'),
        ('two_b1_cubed','scale','b1_cubed','2'),
        ('w_partial','subtract','b3','three_b1_b2'),
        ('twice_w','add','w_partial','two_b1_cubed'), ('w','scale','twice_w','1/2'),
        ('v_squared','square','v'), ('v_cubed','multiply','v_squared','v'),
        ('w_squared','square','w'), ('v_cubed_minus_w_squared','subtract','v_cubed','w_squared'),
        ('four_difference','scale','v_cubed_minus_w_squared','4'),
        ('gamma0_squared','square','gamma0'), ('gamma0_fourth','square','gamma0_squared'),
        ('H_secondary','multiply','gamma0_fourth','four_difference')]:
        op(*args)
    check('complete expression graph', [(r['name'],r['operation'],r['inputs']) for r in saved['trace']] == plan)
    env, replay = {}, []
    for name, kind, operands in plan:
        if kind == 'input':
            result = box(selected['moments'][name[1:]])
        else:
            a = env[operands[0]]
            if kind == 'scale':
                t = F(operands[1]); result = tuple(sorted((t*a[0],t*a[1])))
            elif kind == 'square':
                result = sq(a)
            elif kind == 'reciprocal':
                assert not a[0] <= 0 <= a[1]
                result = (1/a[1],1/a[0])
            else:
                b = env[operands[1]]
                if kind == 'subtract': result = sub(a,b)
                elif kind == 'add': result = (a[0]+b[0],a[1]+b[1])
                elif kind == 'multiply': result = mul(a,b)
                else: raise ValueError(kind)
        env[name] = result
        index = len(replay)
        equal = box(saved['trace'][index]['interval']) == result
        check('exact trace endpoints: ' + name, equal)
        replay.append({'name':name,'operation':kind,'inputs':operands,
                       'interval':encode(result),'saved_endpoints_equal':equal})
    h = env['H']
    # Direct independent primary expression, with a different evaluation order.
    g = [env['gamma'+str(j)] for j in range(4)]
    direct = sub(mul((F(4),F(4)),mul(sub(sq(g[1]),mul(g[0],g[2])),
                   sub(sq(g[2]),mul(g[1],g[3])))),sq(sub(mul(g[1],g[2]),mul(g[0],g[3]))))
    check('independent primary formula', direct == h)
    check('complete primary result copy', box(saved['H']) == h)
    check('complete secondary result copy', box(saved['H_secondary']) == env['H_secondary'])
    rendered = box(saved['H_outward_decimal'])
    denominator = 10**22
    floor_lower = h[0].numerator*denominator//h[0].denominator
    ceil_upper = -((-h[1].numerator*denominator)//h[1].denominator)
    check('exact outward decimal grid', rendered == (F(floor_lower,denominator),F(ceil_upper,denominator)))
    check('outward decimal containment', rendered[0] <= h[0] <= h[1] <= rendered[1])
    check('stated decimal bounds', rendered == (F('7.0891180e-15'),F('7.8529158e-15')))
    check('required exact strict threshold', h[0] > 0)
    secondary = env['H_secondary']
    overlap = max(h[0],secondary[0]) <= min(h[1],secondary[1])
    check('secondary consistency only', overlap and saved['secondary_overlap_only'] is True)
    check('saved failure list', saved['failures'] == [])
    check('saved threshold', F(saved['required_lower_bound']) == 0)
    check('saved status', saved['status'] == 'positive_lower_bound' and saved['strict_positive_certified_subject_to_input_contracts'] is True)
    report = {'status':'passed' if not failures else 'failed','python':platform.python_version(),
        'qualification':'L917/audit197 actual-moment containment under L037; Decimal correctness assumed; no quadrature or library verification',
        'input_sha256':{str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in (SOURCE,CERT,PRIOR,Path(__file__))},
        'prior_hash_checks':prior_hash_checks,'selected_inputs':selected,
        'trace':replay,'H':encode(h),'H_secondary':encode(secondary),'H_outward_decimal':saved['H_outward_decimal'],
        'required_lower_bound':'0','strict_positive':h[0]>0,
        'secondary_used_for_narrowing':False,'producer_preserved':CERT.read_bytes() == producer_bytes,
        'failures':failures,'trace_records_checked':len(replay)}
    OUT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'records':len(replay),'actual_H_outward':saved['H_outward_decimal'],
                      'required':'exact lower(H)>0','strict_positive':h[0]>0,'failures':failures,'certificate':str(OUT.relative_to(ROOT))}))
    assert not failures


if __name__ == '__main__':
    main()
