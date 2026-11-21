#!/usr/bin/env python3
"""Exact rational normalization of imported C999l/audit561 metric bounds.
This checks scalar consequences, not the original matrix/source certificates.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
checks, failures = [], []
values = {}

def record(name, value):
    values[name] = str(value)
    return value

def check(name, actual, relation, required):
    ok = {'<': actual < required, '>': actual > required,
          '<=': actual <= required, '==': actual == required}[relation]
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=ok))
    if not ok:
        failures.append(name)

# C999l Sections2,6,7: all constants are exact rational upper bounds.
z = F('1.008')
conversion = F('1e-14')
zh = F('1.009')
mz = F('6.190001')
check('enlarged exact dyadic basis norm', z+conversion, '<', zh)
u = F(1, 2**53)
gamma = record('gamma_1024', 1024*u/(1-1024*u))
check('inherited gamma upper bound', gamma, '<', F('1.2e-13'))
# Ahat=fl(fl(Zhat^t Mhat) Zhat), first-slot linear convention translated.
e1 = record('first_product_error_upper', gamma*23*400)
check('first intermediate Frobenius bound', 23*400+e1, '<', F(9201))
e2 = record('second_product_error_upper', gamma*9201*23)
eassembly = record('Ahat_vs_exact_dyadic_assembly_upper', e1*zh+e2)
check('whole Ahat assembly error', eassembly, '<', F('1e-7'))
eta = record('eta_A', F('.00024')*z*z+F('1e-7'))
check('full inherited head error value', eta, '==', F('.00024395536'))
metric_bound = record('full_metric_upper', zh*mz+F('1e-7')+eta)
check('full energy metric norm', metric_bound, '<', F(7))
free_margin = F('.000999')
normalized_margin = F('.00014')
record('coarse_normalized_lower', free_margin/7)
check('normalized constant fits coefficient margin', 7*normalized_margin,
      '<', free_margin)
check('positive claimed normalized margin', normalized_margin, '>', F(0))

inputs = [BASE/'neutral-head-covariance-audit-561.json',
          BASE/'neutral-head-covariance-559.json',
          BASE.parent.parent/'lemmas/C999l-neutral-head-family-covariance.md',
          BASE.parent.parent/'lemmas/C744z-neutral-shared-middle-completion.md']
result = dict(scope='Fixed W_512=A0^(1/2)H_512; independent complex endpoints',
    source_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    input_hashes={str(p.relative_to(BASE.parent.parent)):hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in inputs},
    imported_bounds=dict(basis_norm=str(z),basis_conversion=str(conversion),
        dyadic_basis_norm_upper=str(zh),Mhat_Zhat_norm=str(mz),
        Mhat_frobenius_upper='400',Zhat_frobenius_upper='23',
        free_coordinate_margin=str(free_margin)),
    rational_values=values,checks=checks,failures=failures,
    summary=dict(passed=not failures,required_normalized_lower='0',
        proposed_normalized_lower=str(normalized_margin),metric_upper_required='7',
        metric_upper_actual=str(metric_bound)),
    qualifications=['C999l and audit561 imported, not replayed.',
        'Inherited analytic, IEEE754/Decimal, neutral-core and unreplayed c_star contracts remain.',
        'No complement or mixed-block bound, finite inverse square root, or RH claim.'])
output = BASE/'energy-image-margin-610.json'
output.write_text(json.dumps(result,indent=2)+'\n')
print('Checks:',len(checks),'failures:',failures)
print('Full metric upper:',metric_bound,'required < 7')
print('Normalized margin:',normalized_margin,'required > 0')
print('Certificate:',output.relative_to(BASE.parent.parent))
if failures:
    raise SystemExit(1)
