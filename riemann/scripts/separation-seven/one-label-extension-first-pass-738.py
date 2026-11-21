#!/usr/bin/env python3
"""Bounded one-label test: first-block finite evidence, then paid-work preflight.

No inverse or NNLS. Exact scalar sign constraints use the certified736 box.
Decimal residual validation retains the inherited directed-arithmetic contract.
The full prescribed30-update continuation is stopped on a strict work LOWER
bound, before new moment generation or remaining-block numerical work.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from decimal import Decimal as D, localcontext, Context, ROUND_FLOOR, ROUND_CEILING
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve()
OUT = HERE.with_suffix('.json')
INPUT = HERE.with_name('fixed-support-gram-weights-736.json')
ANCHOR = HERE.with_name('fixed-support-shared-734.json')
INTERP = HERE.with_name('fixed-support-componentwise-735.json')
IP_REPLAY = HERE.with_name('fixed-support-componentwise-replay-735.json')
SEPARATOR = HERE.with_name('fixed-support-separator-replay-736.json')
files = [INPUT, ANCHOR, INTERP, IP_REPLAY, SEPARATOR]
data, anchor, interp, replay, separator = [json.loads(p.read_text()) for p in files]
PREC, N, ITER, WORK_CAP = 256, 35, 30, 10**8
down = Context(prec=PREC, rounding=ROUND_FLOOR)
up = Context(prec=PREC, rounding=ROUND_CEILING)
labels = anchor['parameters']['labels']
block = data['blocks'][0]
J = 2048
indices = [J+i*(J-1)//128 for i in labels]
nodes = [F(4*j+1, 2*J)-3 for j in indices]
wlo = [F(x)-F(r) for x,r in zip(block['weights'],block['box_radii'])]
whi = [F(x)+F(r) for x,r in zip(block['weights'],block['box_radii'])]
RA = [[D(x) for x in row] for row in anchor['anchor']['interpolation_preconditioner']]
checks = {
    'inputs_have_no_integrity_failure': data['failed_integrity_checks']==[] and interp['failed_checks']==[] and replay['failed_checks']==[] and separator['failed_checks']==[],
    'input_script_binding': data['script_sha256']==sha256(INPUT.with_suffix('.py').read_bytes()).hexdigest(),
    'anchor_binding': data['input_hashes'][ANCHOR.name]==sha256(ANCHOR.read_bytes()).hexdigest(),
    'common_radius_binding': data['input_hashes'][INTERP.name]==sha256(INTERP.read_bytes()).hexdigest() and data['input_hashes'][IP_REPLAY.name]==sha256(IP_REPLAY.read_bytes()).hexdigest(),
    'separator_binding':separator['input_sha256']==sha256(INPUT.read_bytes()).hexdigest(),
    'same35_labels_and_k11_indices': labels==data['parameters']['labels']==interp['parameters']['labels'] and indices==block['indices'] and block['k']==11,
    'certified_particular_solution_box': block['checks']['strict_residual_centered_inclusion'] and min(F(r) for r in block['box_radii'])>0,
    'retained_original_gram_contraction': block['gram']['contraction_pass'] and F(block['gram']['norm_upper'])<1,
}
assert all(checks.values())


def cheb(t):
    values = [F(1), t]
    for _ in range(2, N):
        values.append(2*t*values[-1]-values[-2])
    return values


def q(v):
    return down.divide(D(v.numerator),D(v.denominator)), up.divide(D(v.numerator),D(v.denominator))


def add(a,b):
    return down.add(a[0],b[0]),up.add(a[1],b[1])


def scale(a,c):
    if c>=0:
        return down.multiply(a[0],c),up.multiply(a[1],c)
    return down.multiply(a[1],c),up.multiply(a[0],c)


def interval_dot(row,x):
    total = (D(0),D(0))
    for a,c in zip(row,x):
        total = add(total,scale(a,c))
    return total


def dot(row,x):
    total = D(0)
    for i in range(N):
        total += row[i]*x[i]
    return total


columns = [cheb(t) for t in nodes]
trials = []
selected = None
with localcontext() as ctx:
    ctx.prec = PREC
    for label in [i for i in range(129) if i not in labels]:
        jnew = J+label*(J-1)//128
        tnew = F(4*jnew+1,2*J)-3
        v = []
        for i,ji in enumerate(indices):
            value = F(1)
            for h,jh in enumerate(indices):
                if h!=i:
                    value *= F(jnew-jh,ji-jh)
            v.append(value)
        extra = cheb(tnew)
        identity = [sum((columns[i][a]*v[i] for i in range(N)),F(0))==extra[a] for a in range(N)]
        assert all(identity)
        # Inner interval guarantees signs for EVERY w in the736 solution box.
        # Outer interval contains every scalar that could work for exact w.
        il, ol, iu, ou = F(0),F(0),None,None
        inner_zero_ok, outer_zero_ok = True,True
        for i,vi in enumerate(v):
            if vi>0:
                a,b = wlo[i]/vi,whi[i]/vi
                iu = a if iu is None else min(iu,a)
                ou = b if ou is None else min(ou,b)
            elif vi<0:
                il,ol = max(il,wlo[i]/vi),max(ol,whi[i]/vi)
            else:
                inner_zero_ok &= wlo[i]>=0
                outer_zero_ok &= whi[i]>=0
        assert iu is not None and ou is not None
        trial = {'label':label,'k':11,'original_index':jnew,
            'cardinal_values_exact':list(map(str,v)),
            'extra_column_identities':identity,
            'inner_interval':list(map(str,[il,iu])),
            'outer_interval':list(map(str,[ol,ou])),
            'zero_constraints_inner':inner_zero_ok,'zero_constraints_outer':outer_zero_ok}
        trials.append(trial)
        if not outer_zero_ok or ol>ou:
            trial['decision']='EXACT_MATCHING_INFEASIBLE_ONLY'
            continue
        if not inner_zero_ok or il>=iu:
            trial['decision']='INCONCLUSIVE_CERTIFICATE_STOP'
            break
        scalar = (D(((il+iu)/2).numerator)/D(((il+iu)/2).denominator))
        sf = F(scalar)
        assert il<=sf<=iu
        exact_lower = [wlo[i]-sf*v[i] for i in range(N)]
        exact_upper = [whi[i]-sf*v[i] for i in range(N)]
        assert min(exact_lower)>0 and sf>0
        # A separate rounded candidate:30 fixed updates, all original moments.
        af = [[columns[i][a] for i in range(N)] for a in range(N)]
        ai = [[q(z) for z in row] for row in af]
        am = [[D(z.numerator)/D(z.denominator) for z in row] for row in af]
        moments = [(D(a),D(b)) for a,b in block['original_moments'][:N]]
        bm = [(a+b)/2 for a,b in moments]
        x = [D(0)]*N
        for _ in range(ITER):
            rr = [bm[a]-dot(am[a],x) for a in range(N)]
            x = [x[i]+dot(RA[i],rr) for i in range(N)]
        # Round each exact x_i-s*v_i once to the fixed precision.
        xf = [F(z)-sf*v[i] for i,z in enumerate(x)]
        weights = [D(z.numerator)/D(z.denominator) for z in xf]+[scalar]
        all_nodes = nodes+[tnew]
        all_columns = columns+[extra]
        residual = []
        for a in range(N):
            row = [q(col[a]) for col in all_columns]
            approx = interval_dot(row,weights)
            residual.append((down.subtract(approx[0],moments[a][1]),up.subtract(approx[1],moments[a][0])))
        rmax = max(max(a.copy_abs(),b.copy_abs()) for a,b in residual)
        K = D(block['gram_inverse_norm_upper'])
        eps2 = up.multiply(D(N),up.multiply(up.multiply(rmax,rmax),K))
        trial.update({'decision':'FIRST_BLOCK_FEASIBLE_THEN_WORK_PREFLIGHT',
            'scalar_decimal':str(scalar),
            'exact_solution_weight_lower':list(map(str,exact_lower+[sf])),
            'exact_solution_weight_upper':list(map(str,exact_upper+[sf])),
            'particular30_decimal':list(map(str,x)),
            'rounded36_weights_decimal':list(map(str,weights)),
            'original_residual_intervals':[[str(a),str(b)] for a,b in residual],
            'original_gram_inverse_norm_upper':str(K),
            'epsilon_squared_upper':str(eps2),
            'all_rounded_weights_positive':min(weights)>0,
            'rounded_original_residual_pass':F(eps2)<=F(5,10**19)**2})
        selected = trial
        break

# Full-production preflight, not an executed-work or general complexity claim.
# Each count is tied to source loops explained in C998w section8.
pricing = {
    'retained735_constructor_lower':32505725,
    'retained735_exact_replay_product_sum_loop_lower':61*N**3*4,
    'three731_gram_inverse_update_lower':3*N*(34*35*36//3)*4,
    'new61_gram_certificate_lower':61*N**3*12,
    'new61_fixed30_candidate_dot_lower':61*ITER*2*N*N*5,
}
total = sum(pricing.values())
checks.update({
    'one_label_tested_before_work_stop':len(trials)<=94,
    'all_extra_column_identities':all(all(t['extra_column_identities']) for t in trials),
    'first_block_exact_rule_strictly_positive':selected is not None and min(map(F,selected['exact_solution_weight_lower']))>0,
    'first_block_rounded_rule_positive':selected is not None and selected['all_rounded_weights_positive'],
    'first_block_original_residual_pass':selected is not None and selected['rounded_original_residual_pass'],
    'full_prescription_lower_exceeds_cap':total>WORK_CAP,
    'zero_new_inverses_and_nnls':True,
})
report = {
    'script_sha256':sha256(HERE.read_bytes()).hexdigest(),
    'input_hashes':{p.name:sha256(p.read_bytes()).hexdigest() for p in files},
    'parameters':{'labels':labels,'precision':PREC,'candidate_updates':ITER,
        'required_k':list(range(11,72)),'max_labels':94,'label_order':'increasing',
        'work_cap':WORK_CAP,'epsilon_limit':'5e-19','new_inverses':0,'new_nnls':0},
    'trials':trials,
    'pricing_lower_subtotals':pricing,'full_prescription_work_lower':total,
    'complete_work_upper':None,'peak_bytes_upper':None,
    'unexecuted_blocks':list(range(12,72)),
    'status':'STOP_FIXED30_FULL_PRODUCTION_COST',
    'qualification':'k11 finite feasibility only; no61-block rule or global error claim; cost stop is source-specific',
    'checks':checks,'failed_checks':[k for k,v in checks.items() if not v],
}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print('Labels tested:',[t['label'] for t in trials],'; selected first-block label:',None if selected is None else selected['label'])
if selected:
    print('k11:36 rounded weights positive:',selected['all_rounded_weights_positive'],
          '; original epsilon^2 upper:',format(D(selected['epsilon_squared_upper']),'.7g'),'; required<=2.5e-37')
print('Full fixed30 production mandatory lower:',total,'; required complete upper<=',WORK_CAP,'; STOP')
print('Checks:',sum(checks.values()),'/',len(checks),'; failures:',report['failed_checks'])
print('Certificate:',OUT.relative_to(HERE.parents[2]),'; observed bytes:',OUT.stat().st_size,'; peak bytes upper unproved')
if report['failed_checks']:
    raise SystemExit(1)
