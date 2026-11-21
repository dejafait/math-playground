#!/usr/bin/env python3
"""Read and check every exact entry/product/endpoint in certificate2017.

This is finite certificate consistency checking, not an independent audit
of the source extraction or C029o's algebraic construction.
"""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import hashlib
import json
import math
import sys

if hasattr(sys,'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent


def interval(obj):
    return Q(obj['lower']),Q(obj['upper'])


def times(a,b):
    corners = a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]
    return min(corners),max(corners)


def main():
    path = ROOT/'tilted-bezoutian-entrywise-2017.json'
    raw = path.read_bytes()
    cert = json.loads(raw)
    checks = {}
    for name,expected in cert['required_sha256'].items():
        actual = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
        checks['pin_'+name] = actual == expected == cert['input_sha256'][name]
    old = json.loads((ROOT/'tilted-bezoutian-n6-2014.json').read_text())
    original = json.loads((ROOT/'tilted-boundary-metric-2010.json').read_text())
    checks['all_36_polynomial_entries_unchanged'] = cert['B_descending'] == old['B_descending']
    checks['unchanged_pi'] = cert['pi_interval'] == original['pi_interval']
    checks['unchanged_sqrt2'] = cert['sqrt2_interval'] == original['sqrt2_interval']
    checks['construction_checks_all_true'] = all(cert['checks'].values()) and not cert['failures']
    pi_bounds = interval(cert['pi_interval'])
    sqrt_bounds = interval(cert['sqrt2_interval'])
    entries = [[interval(iv) for iv in row] for row in cert['entry_intervals']]
    checks['matrix_dimensions'] = len(entries)==6 and all(len(row)==6 for row in entries)
    for i in range(6):
        for j in range(6):
            lo,hi = Q(0),Q(0)
            for coefficient in reversed(cert['B_descending'][i][j]):
                a,b = Q(coefficient['rational']),Q(coefficient['sqrt2'])
                ca,cb = a+b*sqrt_bounds[0],a+b*sqrt_bounds[1]
                lo,hi = times((lo,hi),pi_bounds)
                lo,hi = lo+min(ca,cb),hi+max(ca,cb)
            checks[f'complete_entry_{i}_{j}'] = (lo,hi)==entries[i][j]
    details,outer,signs = [],[],[]
    for n,minor in enumerate(cert['minors'],1):
        records = minor['permutations']
        expected = set(permutations(range(n)))
        seen = [tuple(r['permutation_zero_based']) for r in records]
        checks['complete_unique_permutations_'+str(n)] = (
            len(records)==math.factorial(n) and len(set(seen))==len(seen) and set(seen)==expected)
        lo,hi = Q(0),Q(0)
        term_checks = []
        for k,record in enumerate(records):
            perm = tuple(record['permutation_zero_based'])
            parity = sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
            sign = -1 if parity%2 else 1
            prod = Q(1),Q(1)
            for i in range(n):
                prod = times(prod,entries[i][perm[i]])
            signed = prod if sign==1 else (-prod[1],-prod[0])
            valid = (parity==record['inversions'] and sign==record['sign']
                     and prod==interval(record['product_interval'])
                     and signed==interval(record['signed_product_interval']))
            term_checks.append({'term':k,'parity_product_and_signed_endpoints_match':valid})
            lo,hi = lo+signed[0],hi+signed[1]
        checks['every_term_recomputed_'+str(n)] = all(t['parity_product_and_signed_endpoints_match'] for t in term_checks)
        checks['complete_raw_endpoints_match_'+str(n)] = (lo,hi)==interval(minor['interval'])
        short = minor['readable_outer_enclosure']
        outlo,outhi = interval(short['scaled_interval'])
        unit = Q(10)**short['power_of_ten']
        checks['exact_outer_bound_comparison_'+str(n)] = outlo*unit<=lo<=hi<=outhi*unit
        actual_sign = 1 if lo>0 else -1 if hi<0 else 0
        short_sign = 1 if outlo>0 else -1 if outhi<0 else 0
        checks['raw_and_outer_sign_'+str(n)] = actual_sign==minor['sign']==short_sign!=0
        details.append({'minor':n,'all_term_checks':term_checks})
        outer.append({'minor':n,**short,'raw_endpoints_checked_in_full':checks['complete_raw_endpoints_match_'+str(n)]})
        signs.append(actual_sign)
    checks['six_minors'] = len(cert['minors'])==6
    checks['all_signs_match'] = signs==cert['leading_determinant_signs']
    sequence = [1]+signs
    negative = sum(a!=b for a,b in zip(sequence,sequence[1:]))
    actual = {'positive':6-negative,'negative':negative,'zero':0}
    checks['Jacobi_inertia'] = actual==cert['actual_inertia']
    checks['threshold_and_unresolved'] = (cert['threshold_pass']==(negative<=1)
                                          and not cert['unresolved_determinants'])
    failed = [k for k,v in checks.items() if not v]
    report = {
        'certificate_sha256':hashlib.sha256(raw).hexdigest(),
        'reproduction':'python3 scripts/pollaczek/tilted_bezoutian_entrywise_check_2017.py',
        'checks':checks,'all_permutation_term_checks':details,
        'complete_exact_outer_bounds':outer,'signs':signs,'actual_inertia':actual,
        'permutation_terms_checked':sum(len(d['all_term_checks']) for d in details),
        'failures':failed,
        'scope':'Full finite arithmetic consistency check; no independent source/construction audit',
    }
    out = ROOT/'tilted-bezoutian-entrywise-check-2017.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print('Exact entry intervals checked: 36; permutation terms:',report['permutation_terms_checked'])
    print('All six complete determinant endpoint pairs and outer comparisons checked; signs:',signs)
    print('Jacobi inertia:',actual,'; required: six nonzero signs and negative index<=1')
    print('Checks:',len(checks),'; failures:',failed,'; certificate:',out.relative_to(Path.cwd()))
    if failed:
        raise SystemExit(1)


if __name__=='__main__':
    main()
