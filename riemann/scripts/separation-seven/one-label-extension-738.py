#!/usr/bin/env python3
"""Bounded one-label test: all94 supports fail the original residual tolerance.

No inverse or NNLS. Exact scalar sign constraints use the certified736 box.
Decimal residual validation retains the inherited directed-arithmetic contract.
The exact dual validation is independent of the Decimal starting box.
The unused prescribed30-update continuation also has a work LOWER bound
above the cap; no remaining-block numerical work is run.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from decimal import Decimal as D, localcontext, Context, ROUND_FLOOR, ROUND_CEILING
from math import lcm
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

# Exact original-atom validation of the dual consequences. This stage does
# not use Decimal arithmetic, interval moments, RA, or the736 box as premises.
# The box selects witnesses; the following integer sums validate them anew.
assert selected is None and len(trials)==94
mass_denominator = lcm(*((4*j+1)**2 for j in range(J,2*J)))
power_sums = [0]*N
for j in range(J,2*J):
    mass_numerator = 16*J*(mass_denominator//((4*j+1)**2))
    power = 1
    for a in range(N):
        power_sums[a] += mass_numerator*power
        power *= j
mass = F(power_sums[0],mass_denominator)
assert 0<mass<1
cardinal = []
integrals = []
cheb_cardinal = []
for i,ji in enumerate(indices):
    poly,denom,cc = [1],1,[F(1)]
    for h,jh in enumerate(indices):
        if h==i:
            continue
        nxt = [0]*(len(poly)+1)
        for a,c in enumerate(poly):
            nxt[a] -= jh*c
            nxt[a+1] += c
        poly = nxt
        denom *= ji-jh
        # Exact Chebyshev multiplication by (t-t_h)/(t_i-t_h).
        cn = [F(0)]*(len(cc)+1)
        for a,c in enumerate(cc):
            cn[a] -= nodes[h]*c
            if a==0:
                cn[1] += c
            else:
                cn[a-1] += c/2
                cn[a+1] += c/2
        cc = [c/(nodes[i]-nodes[h]) for c in cn]
    integral = F(sum(poly[a]*power_sums[a] for a in range(N)),mass_denominator*denom)
    integrals.append(integral)
    cheb_cardinal.append(cc)
    def horner(y):
        value=0
        for c in reversed(poly):
            value=value*y+c
        return F(value,denom)
    at_old = [horner(jh) for jh in indices]
    cheb_at_old = [sum((cc[a]*columns[h][a] for a in range(N)),F(0)) for h in range(N)]
    assert at_old==cheb_at_old==[F(int(i==h)) for h in range(N)]
    cardinal.append({'coordinate':i,'integer_coefficients_ascending':list(map(str,poly)),
        'integer_denominator':str(denom),'chebyshev_coefficients':list(map(str,cc)),
        'integral_exact':str(integral),'all35_cardinal_values':list(map(str,at_old))})

duals=[]
for trial in trials:
    v=list(map(F,trial['cardinal_values_exact']))
    if v[30]>=0:
        coeff={30:F(1)}
    else:
        lower_index=max((i for i in range(N) if v[i]<0),key=lambda i:whi[i]/v[i])
        upper_index=min((i for i in range(N) if v[i]>0),key=lambda i:whi[i]/v[i])
        coeff={upper_index:F(1),lower_index:-v[upper_index]/v[lower_index]}
    assert all(c>0 for c in coeff.values())
    pc=[sum((c*cheb_cardinal[i][a] for i,c in coeff.items()),F(0)) for a in range(N)]
    integral=sum((c*integrals[i] for i,c in coeff.items()),F(0))
    norm_upper=sum(map(abs,pc),F(0))
    extra_value=sum((c*v[i] for i,c in coeff.items()),F(0))
    tc=cheb(F(4*trial['original_index']+1,2*J)-3)
    values=[sum((pc[a]*col[a] for a in range(N)),F(0)) for col in columns+[tc]]
    expected=[coeff.get(i,F(0)) for i in range(N)]+[extra_value]
    assert values==expected and min(values)>=0 and norm_upper>0 and integral<0
    bound=(-integral)/norm_upper
    duals.append({'label':trial['label'],
        'positive_cardinal_combination':{str(i):str(c) for i,c in coeff.items()},
        'chebyshev_coefficients':list(map(str,pc)),
        'all36_support_values_exact':list(map(str,values)),
        'original_integral_exact':str(integral),
        'original_L2_norm_strict_upper':str(norm_upper),
        'residual_strict_lower':str(bound),
        'residual_exceeds_required':bound>F(5,10**19)})
worst=min(duals,key=lambda z:F(z['residual_strict_lower']))
all_negative=all(z['residual_exceeds_required'] for z in duals)

# Full-production preflight, not an executed-work or general complexity claim.
# Each count is tied to source loops explained in C998w section8.
pricing = {
    'retained735_constructor_lower':32505725,
    'retained735_exact_replay_product_sum_loop_lower':61*N*N*(4*N-1),
    'three731_gram_inverse_update_lower':3*N*(34*35*36//3)*4,
    'new61_gram_certificate_lower':61*N**3*12,
    'new61_fixed30_candidate_dot_lower':61*ITER*2*N*N*5,
}
total = sum(pricing.values())
checks.update({
    'bounded94_label_search':len(trials)<=94,
    'all_extra_column_identities':all(all(t['extra_column_identities']) for t in trials),
    'all94_outer_scalar_intervals_empty':len(trials)==94 and all(t['decision']=='EXACT_MATCHING_INFEASIBLE_ONLY' for t in trials),
    'exact_original_mass_between_zero_and_one':0<mass<1,
    'all35_exact_integrals_in736_boxes':all(wlo[i]<=integrals[i]<=whi[i] for i in range(N)),
    'all94_support_nonnegative_negative_integral_duals':len(duals)==94 and all(F(z['original_integral_exact'])<0 and min(map(F,z['all36_support_values_exact']))>=0 for z in duals),
    'all94_original_residual_bounds_exceed_required':all_negative,
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
    'exact_original_measure':{'J':J,'common_mass_denominator':str(mass_denominator),
        'integer_weighted_power_sums_degree0_through34':list(map(str,power_sums)),
        'mass_exact':str(mass)},
    'exact_cardinal_polynomials':cardinal,'residual_duals':duals,
    'worst_residual_bound':{'label':worst['label'],'strict_lower_exact':worst['residual_strict_lower']},
    'pricing_lower_subtotals':pricing,'full_prescription_work_lower':total,
    'complete_work_upper':None,'peak_bytes_upper':None,
    'unexecuted_blocks':list(range(12,72)),
    'status':'ALL94_SUPPORTS_REFUTED_AT_ORIGINAL_RESIDUAL_TOLERANCE_K11',
    'qualification':'all original-measure nonnegative rules on each allowed36-node support fail at k11; no exclusion of larger/changed supports or other mechanisms; exact dual validation needs no Decimal assumption',
    'checks':checks,'failed_checks':[k for k,v in checks.items() if not v],
}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print('Labels tested:',len(trials),'; selected first-block label:',None if selected is None else selected['label'])
if selected:
    print('k11:36 rounded weights positive:',selected['all_rounded_weights_positive'],
          '; original epsilon^2 upper:',format(D(selected['epsilon_squared_upper']),'.7g'),'; required<=2.5e-37')
print('Full fixed30 production mandatory lower:',total,'; required complete upper<=',WORK_CAP,'; STOP')
print('All94 exact original residual duals pass:',all_negative,'; worst label:',worst['label'],
      '; residual strict lower:',format(D(F(worst['residual_strict_lower']).numerator)/D(F(worst['residual_strict_lower']).denominator),'.7g'),'; required<=5e-19')
print('Checks:',sum(checks.values()),'/',len(checks),'; failures:',report['failed_checks'])
print('Certificate:',OUT.relative_to(HERE.parents[2]),'; observed bytes:',OUT.stat().st_size,'; peak bytes upper unproved')
if report['failed_checks']:
    raise SystemExit(1)
