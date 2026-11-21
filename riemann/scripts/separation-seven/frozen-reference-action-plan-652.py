#!/usr/bin/env python3
"""Exact conservative grid plan for C999(13)-(16), not an action certificate.

No evaluations on these grids are run. This records why the direct uniform
implementation was not completed; these sufficient counts are not necessary
complexity lower bounds. No reference parameter or frozen endpoint changes.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
import numpy as np
B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ceil(q):return -(-q.numerator//q.denominator)
def enc(q):return dict(numerator=str(q.numerator),denominator=str(q.denominator))
proposal=json.loads((B/'frozen-reference-proposal-652.json').read_text())
archive=B/'frozen-reference-proposal-652.npz'
assert sha(archive)==proposal['archive']['sha256']
with np.load(archive,allow_pickle=False) as z:Y=z['free_middle_dyadics'].copy()
assert Y.shape==(254,3) and np.isfinite(Y).all()
# A smooth neutral cosine trial has |q_p|<=sum_same_parity |Y_n|,
# since each exact completion ratio r_n<1. On a parity block its
# amplitude normalization sqrt(2)*nu_n<3 (ell>1/2). Consequently
# |v|<=6 sum|Y_n| and |v'|<=24 sum(n+1)|Y_n| (pi/ell<8).
# M includes one unit for rounded step values; no such steps are made.
eps=Q(1,10000)  # requested entire Carleman-action tolerance per block
term=eps/3
records=[]
for col in range(3):
    yy=[abs(Q.from_float(float(v))) for v in Y[:,col]]
    M=1+6*sum(yy,Q(0))
    L=24*sum(((n+1)*v for n,v in enumerate(yy,start=2)),Q(0))
    # pi<4, sqrt(a)<1, a<3/10. Split the input error term into
    # discretization and scalar value errors, each at most term/2.
    nin=ceil(Q(12,10)*L/term)
    ein=term/8
    s=0
    while M*M*Q(3,10)*Q(1,2**s)*((s+1)**2+2*(s+1)+2)>term*term:
        s+=1
    endpoint2=M*M*Q(3,10)*Q(1,2**s)*((s+1)**2+2*(s+1)+2)
    # tau=a*2^-s. Split output approximation error likewise.
    nout=ceil(M*2**s/term)
    eout=term/2
    in_error=Q(6,10)*L/nin+4*ein
    out_error=M*2**s/(2*nout)+eout
    assert in_error<=term and endpoint2<=term*term and out_error<=term
    records.append(dict(column=col,M_upper=enc(M),L_upper=enc(L),
        input_intervals=nin,input_scalar_error=enc(ein),
        endpoint_tau_over_a=enc(Q(1,2**s)),endpoint_squared_bound=enc(endpoint2),
        output_intervals=nout,output_scalar_error=enc(eout),
        input_error_upper=enc(in_error),output_error_upper=enc(out_error),
        allocated_each_term=enc(term),checks_pass=True))
report=dict(result='CONSERVATIVE_UNIFORM_PLAN_NOT_EXECUTED',
    certified_action=False,source_archive_sha256=sha(archive),
    script_sha256=sha(Path(__file__)),requested_action_tolerance_per_parity=enc(eps),
    records=records,failures=['No step arrays, Carleman actions or complete residuals evaluated'],
    qualification='Counts are sufficient for this deliberately coarse uniform prescription, not necessary complexity bounds or a mathematical obstruction to another solver.')
out=B/'frozen-reference-action-plan-652.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(report['result'])
for r in records:print('Column',r['column'],'input cells',r['input_intervals'],
    'output cells',r['output_intervals'],'required action error <=1e-4; actual action error unverified')
print('Failures:',report['failures']);print('Full plan:',out.relative_to(B.parent.parent))
