#!/usr/bin/env python3
"""Exact-rational terminal checks of complete stored interval evidence.

This checks aggregation, directions and stopping budgets, not an
independent recomputation of the exponential or polynomial primitives.
"""
from fractions import Fraction as Q
from pathlib import Path
from decimal import Decimal as D
import json

ROOT = Path(__file__).resolve().parents[2]
results = []
for n in (64,128):
    path = ROOT/f'scripts/target-radau/finite-penalty-screen-{n}-414.json'
    r = json.loads(path.read_text())
    iv = lambda x: tuple(Q(v) for v in x)
    d,lam,budget,penalty,screen = map(iv,[r['d'],r['lambda'],r['B'],r['penalty'],r['screen_d_minus_penalty']])
    sum_lo = sum_hi = Q(0)
    for p in r['products']:
        lo,hi = iv(p['integral']['re'])
        sum_lo += p['multiplicity']*lo
        sum_hi += p['multiplicity']*hi
    checks = {
        'complete_five_terms':len(r['target_terms'])==5,
        'complete_fifteen_products':[(p['i'],p['j']) for p in r['products']]==[(i,j) for i in range(5) for j in range(i,5)],
        'all_products_strict_negative_real_exponent':all(Q(p['alpha'][0])<=-Q(n,2) and p['case']=='nonzero' for p in r['products']),
        'diagonal_imaginary_intervals_contain_zero':all(iv(p['integral']['im'])[0]<=0<=iv(p['integral']['im'])[1] for p in r['products'] if p['i']==p['j']),
        'exact_rational_product_sum_enclosed':d[0]<=sum_lo<=sum_hi<=d[1],
        'positive_lambda_and_budget':lam[0]>0 and budget[0]>0,
        'penalty_product_enclosed':penalty[0]<=lam[0]*budget[0]**2 and lam[1]*budget[1]**2<=penalty[1],
        'screen_encloses_subtraction':screen[0]<=d[0]-penalty[1] and d[1]-penalty[0]<=screen[1],
        'F_upper_valid_and_negative':d[1]-penalty[0]<=Q(r['F_upper'])<0,
        'actual_d_nonnegative':0<=d[0],
        'all_entry_widths_le_2^-256':all(hi-lo<=Q(1,2**256) for lo,hi in [d,lam,budget]),
        'screen_arithmetic_width_le_2^-60':screen[1]-screen[0]<=Q(1,2**60),
        'safe_d_bound':d[1]< (Q(1323,10**9) if n==64 else Q(1683,10**10)),
        'safe_penalty_bound':penalty[0]> (162754 if n==64 else 2252197),
        'safe_negative_F_bound':Q(r['F_upper'])< (-162754 if n==64 else -2252197),
        'zero_lanczos_steps':r['lanczos_steps']==0,
        'no_hidden_computed_matrix':r['not_computed']==['G','h','Gauss endpoint','Radau endpoint','inverse form']}
    # The safe penalty bound alone is weaker than the safe F bound;
    # each is checked against its own complete stored rational value.
    failures=[k for k,v in checks.items() if not v]
    results.append({'n':n,'checks':checks,'failures':failures,
                    'input':str(path.relative_to(ROOT)),
                    'actual_d_width_exact':str(d[1]-d[0]),
                    'required_d_width_exact':str(Q(1,2**256)),
                    'actual_screen_width_exact':str(screen[1]-screen[0]),
                    'required_screen_width_exact':str(Q(1,2**60))})
    print(f"n={n}: d upper approx {D(r['d'][1]):.9E}, penalty lower approx {D(r['penalty'][0]):.9E}, F upper approx {D(r['F_upper']):.9E}")
    print(f"  d width {D(r['entry_widths']['d']):.4E} <= {D(r['entry_required']):.4E}; screen width {D(r['screen_arithmetic_width']):.4E} <= {D(r['screen_width_required']):.4E}; failures={failures}")
out=ROOT/'scripts/target-radau/check-penalty-screen-414.json'
out.write_text(json.dumps({'results':results,'failures':[{'n':r['n'],'failures':r['failures']} for r in results if r['failures']]}))
print('certificate:',out.relative_to(ROOT))
if any(r['failures'] for r in results):
    raise SystemExit(1)
