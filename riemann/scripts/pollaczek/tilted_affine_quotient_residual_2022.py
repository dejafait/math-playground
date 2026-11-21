#!/usr/bin/env python3
"""The approved N=6,7 affine-quotient test, with fixed input enclosures.

Run from riemann:
    python3 scripts/pollaczek/tilted_affine_quotient_residual_2022.py
Standard library and previously inspected local exact-polynomial helpers only.
All numbers used for certification are integers or Fractions; no roots, floats,
eigenvectors, degree campaign, determinant expansion or precision fallback.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

import tilted_bezoutian_n6_2014 as alg

base = alg.base
ROOT = Path(__file__).parent
OUTPUT = ROOT / 'tilted-affine-quotient-residual-2022.json'
TARGET = ('Test the affine-quotient embedding from U_6 to U_7 for a certified '
          'negative quadratic direction in P_6=B_7-E_6 B_6 E_6^t, using the '
          'full Jensen-weighted Kuznetsov coefficients and fixed existing input enclosures.')
PINNED = {
    'tilted-boundary-metric-2010.json': '361e31b72ad348b17f6c2ac785c20f5ab73e27796025bd724af208543e0feaf7',
    'tilted-bezoutian-n6-2014.json': '6870f303d2fa8bd6ec5bd9fcde2a197d6c9987f98b6bccf048a378f3ccdedd47',
    'tilted_boundary_metric_2010.py': '21cc4fb70b084fde19c62d74a7edb04a2bcdb38fe1a376ea5e7de6d3edbb58fc',
    'tilted_bezoutian_n6_2014.py': 'af87c4ec40ea6a93ddb0d9fe3915dd6c2fa403d4729e48639c1b94247ac42709',
}


def isum(terms):
    out = (F(0), F(0))
    for term in terms:
        out = base.iadd(out, term)
    return out


def isub(a, b):
    return base.iadd(a, base.iscale(b, -1))


def reciprocal(a):
    if not (a[1] < 0 or a[0] > 0):
        raise ArithmeticError('Reciprocal denominator not separated from zero')
    return (1/a[1], 1/a[0])


def iv_json_matrix(a):
    return [[base.interval_json(v) for v in row] for row in a]


def matrix_sub(a, b):
    return [[alg.add(x, alg.scale(y, -1)) for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]


def outer(iv):
    """Six-decimal scientific enclosure, still using exact rationals."""
    magnitude = max(abs(iv[0]), abs(iv[1]))
    exponent = 0
    if magnitude:
        exponent = len(str(magnitude.numerator))-len(str(magnitude.denominator))
        unit = F(10)**exponent
        while magnitude < unit:
            exponent, unit = exponent-1, unit/10
        while magnitude >= 10*unit:
            exponent, unit = exponent+1, unit*10
    unit = F(10)**exponent
    bound = base.outward_grid((iv[0]/unit, iv[1]/unit), 6)
    assert bound[0]*unit <= iv[0] <= iv[1] <= bound[1]*unit
    return {'power_of_ten': exponent, 'scaled_interval': base.interval_json(bound)}


def outer_contains(iv, value):
    unit = F(10)**value['power_of_ten']
    bounds = value['scaled_interval']
    return F(bounds['lower'])*unit <= iv[0] <= iv[1] <= F(bounds['upper'])*unit


def main():
    checks = {}
    certificate = {'target': TARGET, 'status': 'STARTED',
                   'normalization': 'U_N=T_N/S, S=sin(pi/8)/sqrt(2)>0; no N-dependent scaling',
                   'exact_encoding': 'Ascending polynomials in X=pi, coefficients rational+sqrt2*s, s=sqrt(2); empty polynomial is zero',
                   'checks': checks}

    def check(name, condition):
        checks[name] = bool(condition)

    def save(stage):
        certificate['status'] = stage
        certificate['failures'] = [name for name, ok in checks.items() if not ok]
        OUTPUT.write_text(json.dumps(certificate, indent=2)+'\n')

    def stop_if_failed(stage):
        if not all(checks.values()):
            save(stage)
            print(json.dumps({'status': stage, 'failures': certificate['failures'],
                              'certificate': str(OUTPUT.relative_to(ROOT.parent.parent))}))
            raise SystemExit(1)

    hashes = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in PINNED}
    certificate['input_sha256'] = hashes
    certificate['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    for name in PINNED:
        check('pinned_'+name, hashes[name] == PINNED[name])
    stop_if_failed('INPUT_CHANGED')
    source = json.loads((ROOT/'tilted-boundary-metric-2010.json').read_text())
    prior = json.loads((ROOT/'tilted-bezoutian-n6-2014.json').read_text())
    pi_iv = tuple(F(source['pi_interval'][k]) for k in ('lower', 'upper'))
    sqrt_iv = tuple(F(source['sqrt2_interval'][k]) for k in ('lower', 'upper'))
    certificate['pi_interval'] = source['pi_interval']
    certificate['sqrt2_interval'] = source['sqrt2_interval']
    check('fixed_input_widths', pi_iv[1]-pi_iv[0] == sqrt_iv[1]-sqrt_iv[0] == F(1,10**60))
    check('sqrt2_squared_endpoints', 0 < sqrt_iv[0]**2 < 2 < sqrt_iv[1]**2)
    check('same_enclosures_as_prior_kernel', prior['pi_interval'] == source['pi_interval']
          and prior['sqrt2_interval'] == source['sqrt2_interval'])

    def evaluate(poly):
        return base.peval(poly, pi_iv, sqrt_iv)

    # Reconstruct the full finite source formula through u_9 (hence B_20).
    bern = [F(1)]
    for m in range(1, 21):
        bern.append(-sum((comb(m+1,k)*bern[k] for k in range(m)), F(0))/(m+1))
    check('B20', bern[20] == F(-174611,330))
    check('all_bernoulli_defining_relations', all(
        sum((comb(m+1,k)*bern[k] for k in range(m+1)), F(0)) == 0
        for m in range(1,21)))
    phase = [(F(1),F(0)), (F(1),F(1)), (F(-1),F(0)), (F(-1),F(-1))]
    u = []
    for n in range(10):
        poly = [alg.Z]*(n+2)
        for h in range(n+1):
            c = -F(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1),
                   factorial(n-h)*factorial(2*h+2))*bern[2*h+2]
            a,b = phase[(n-h) % 4]
            poly[h+1] = (c*a, c*b)
        u.append(alg.trim(poly))
    beta = [alg.add(alg.scale(u[n],8*n*n+12*n+7),
                    alg.scale(u[n+2],(2*n+3)*(2*n+5)),
                    alg.scale(u[n-2],4*n*(n-1)) if n>=2 else []) for n in range(8)]
    weights = {n: [F(factorial(n),factorial(n-k)*n**k) for k in range(n+1)] for n in (6,7)}
    a = {n: [alg.scale(beta[k],weights[n][k]) for k in range(n+1)] for n in (6,7)}
    check('all_prior_u_coefficients', u[:9] == list(map(alg.decode,source['u_over_S_polynomials'])))
    check('all_prior_beta_coefficients', beta[:7] == list(map(alg.decode,source['beta_over_S_polynomials'])))
    check('all_prior_N6_Jensen_coefficients', a[6] == list(map(alg.decode,source['a_over_S_polynomials'])))
    p = [[F(1)]]
    for k in range(7):
        row = [F(0)]+p[k]
        if k:
            for j,c in enumerate(p[k-1]):
                row[j] -= F(2*k+1,2)*c
        p.append([c/F(k+1) for c in row])
    check('basis_leading_coefficients', all(p[k][k] == F(1,factorial(k)) for k in range(8)))
    check('all_prior_basis_coefficients', p[:7] == [list(map(F,row)) for row in prior['basis_p_0_to_6']])
    b = {n: [alg.add(*(alg.scale(a[n][k],p[k][i]) for k in range(i,n+1)))
             for i in range(n+1)] for n in (6,7)}
    check('all_prior_U6_monomial_coefficients', b[6] == list(map(alg.decode,prior['U_monomial_coefficients'])))
    lead_iv = {n:evaluate(b[n][n]) for n in (6,7)}
    check('actual_degree_six', lead_iv[6][1] < 0)
    check('actual_degree_seven', lead_iv[7][1] < 0 or lead_iv[7][0] > 0)
    certificate.update({
        'bernoulli_0_to_20': list(map(base.rational,bern)),
        'u_over_S_polynomials': list(map(alg.encode,u)),
        'beta_over_S_polynomials': list(map(alg.encode,beta)),
        'weights': {str(n):list(map(base.rational,weights[n])) for n in (6,7)},
        'Jensen_coefficients': {str(n):list(map(alg.encode,a[n])) for n in (6,7)},
        'basis_p_0_to_7': [list(map(base.rational,row)) for row in p],
        'U_monomial_coefficients': {str(n):list(map(alg.encode,b[n])) for n in (6,7)},
        'leading_coefficient_intervals': {str(n):base.interval_json(lead_iv[n]) for n in (6,7)},
        'leading_coefficient_outer_bounds': {str(n):outer(lead_iv[n]) for n in (6,7)},
        'degree_requirement': 'Both actual leading coefficients separated from zero; otherwise stop',
    })
    save('COEFFICIENTS_AND_DEGREES')
    stop_if_failed('DEGREE_OR_INPUT_FAILURE')

    # q=alpha*t+gamma is fixed by ordinary Euclidean division BEFORE signs.
    # q=Q/D, D=l^2, Q=(L*l)t+(M*l-L*m). No normalization of U_n.
    l,m,L,M = b[6][6],b[6][5],b[7][7],b[7][6]
    D = alg.mul(l,l)
    Q = [alg.add(alg.mul(M,l),alg.scale(alg.mul(L,m),-1)), alg.mul(L,l)]
    R = [alg.add(alg.mul(D,b[7][i]),
                 alg.scale(alg.mul(Q[0],b[6][i]),-1) if i<=6 else [],
                 alg.scale(alg.mul(Q[1],b[6][i-1]),-1) if i>=1 else []) for i in range(8)]
    check('remainder_degree_below_six', not R[6] and not R[7])
    division_residual = [alg.add(alg.mul(D,b[7][i]),
                                alg.scale(alg.mul(Q[0],b[6][i]),-1) if i<=6 else [],
                                alg.scale(alg.mul(Q[1],b[6][i-1]),-1) if i>=1 else [],
                                alg.scale(R[i],-1) if i<6 else []) for i in range(8)]
    check('all_eight_division_identity_coefficients', not any(division_residual))
    # H is 7 by 6: Q*Phi_6=H^t*Phi_7, and E=H/D.
    H = [[[] for _ in range(6)] for _ in range(7)]
    for j in range(6):
        k = 5-j
        H[5-k][j] = alg.scale(Q[1],k+1)
        H[6-k][j] = Q[0]
        if k:
            H[7-k][j] = alg.scale(Q[1],F(2*k+1,2))
    embedding_residual = []
    for j in range(6):
        k = 5-j
        row = []
        for power in range(7):
            rhs = alg.add(*(alg.scale(H[i][j],p[6-i][power]) for i in range(7)
                            if power < len(p[6-i])))
            lhs = alg.add(alg.scale(Q[0],p[k][power]) if power<=k else [],
                          alg.scale(Q[1],p[k][power-1]) if 1<=power<=k+1 else [])
            row.append(alg.add(rhs,alg.scale(lhs,-1)))
        embedding_residual.append(row)
    check('all_42_embedding_coefficients', not any(v for row in embedding_residual for v in row))
    certificate['quotient'] = {'denominator_D_l_squared':alg.encode(D),
                               'Q_constant_then_linear':list(map(alg.encode,Q)),
                               'remainder_numerators_over_D':list(map(alg.encode,R[:6])),
                               'division_identity_residual':list(map(alg.encode,division_residual))}
    certificate['embedding'] = {'numerator_H':alg.matrix_json(H), 'denominator':'quotient/denominator_D_l_squared',
                                 'identity_residual':alg.matrix_json(embedding_residual)}
    save('QUOTIENT_AND_EMBEDDING_FIXED')
    stop_if_failed('QUOTIENT_OR_EMBEDDING_FAILURE')

    # Standard derivative kernel and exact basis conversion, checked in full.
    B = {}
    kernel_records = {}
    for n in (6,7):
        deriv = [alg.scale(b[n][i+1],i+1) for i in range(n)]+[[]]
        numerator = [[alg.add(alg.mul(b[n][i],deriv[j]),alg.scale(alg.mul(deriv[i],b[n][j]),-1))
                      for j in range(n+1)] for i in range(n+1)]
        K = [[[] for _ in range(n)] for _ in range(n)]
        for i in range(1,n+1):
            for j in range(i):
                for h in range(i-j):
                    K[i-1-h][j+h] = alg.add(K[i-1-h][j+h],numerator[i][j])
        multiplied = [[[] for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                multiplied[i+1][j] = alg.add(multiplied[i+1][j],K[i][j])
                multiplied[i][j+1] = alg.add(multiplied[i][j+1],alg.scale(K[i][j],-1))
        residual = matrix_sub(multiplied,numerator)
        check(f'all_{(n+1)**2}_N{n}_kernel_coefficients', not any(v for row in residual for v in row))
        conversion = []
        for i in range(n):
            rem = [F(int(i==j)) for j in range(n)]
            row = [F(0)]*n
            for k in range(n-1,-1,-1):
                row[k] = rem[k]/p[k][k]
                for j,c in enumerate(p[k]):
                    rem[j] -= row[k]*c
            check(f'N{n}_basis_conversion_row_{i}', not any(rem))
            conversion.append([alg.rat([v]) for v in reversed(row)])
        V = [[alg.rat([p[n-1-j][i] if i<=n-1-j else F(0)]) for j in range(n)] for i in range(n)]
        B[n] = alg.matmul(alg.matmul(alg.transpose(conversion),K),conversion)
        reconstruction = alg.matmul(alg.matmul(V,B[n]),alg.transpose(V))
        conversion_residual = matrix_sub(reconstruction,K)
        check(f'all_{n*n}_N{n}_basis_conversion_coefficients', not any(v for row in conversion_residual for v in row))
        check(f'B{n}_symmetric', B[n] == alg.transpose(B[n]))
        kernel_records[str(n)] = {'derivative_coefficients':list(map(alg.encode,deriv)),
            'numerator':alg.matrix_json(numerator), 'monomial_kernel':alg.matrix_json(K),
            'basis_conversion_R_descending':alg.matrix_json(conversion),
            'B_descending':alg.matrix_json(B[n]), 'kernel_identity_residual':alg.matrix_json(residual),
            'basis_conversion_residual':alg.matrix_json(conversion_residual)}
    check('all_audited_B6_entries_match', B[6] == [[alg.decode(v) for v in row] for row in prior['B_descending']])
    D2 = alg.mul(D,D)
    HBHt = alg.matmul(alg.matmul(H,B[6]),alg.transpose(H))
    PN = [[alg.add(alg.mul(D2,B[7][i][j]),alg.scale(HBHt[i][j],-1)) for j in range(7)] for i in range(7)]
    check('residual_exact_symmetry', PN == alg.transpose(PN))
    certificate['kernels'] = kernel_records
    certificate['residual'] = {'numerator':alg.matrix_json(PN), 'denominator_D_squared':alg.encode(D2),
                               'definition':'P=(D^2*B7-H*B6*H^t)/D^2'}
    save('EXACT_RESIDUAL_FIXED_BEFORE_QUADRATIC_SIGNS')
    stop_if_failed('KERNEL_OR_RESIDUAL_FAILURE')

    # Fixed-input interval arithmetic; reciprocals occur only at l and D>0.
    coeff_iv = {'l':lead_iv[6], 'm':evaluate(m), 'L':lead_iv[7], 'M':evaluate(M)}
    inv_l = reciprocal(coeff_iv['l'])
    D_iv = base.imul(coeff_iv['l'],coeff_iv['l'])
    check('D_strictly_positive', D_iv[0] > 0)
    D2_iv = base.imul(D_iv,D_iv)
    check('D_squared_strictly_positive', D2_iv[0] > 0)
    alpha = base.imul(coeff_iv['L'],inv_l)
    gamma = base.imul(isub(coeff_iv['M'],base.imul(alpha,coeff_iv['m'])),inv_l)
    Q_iv = [isub(base.imul(coeff_iv['M'],coeff_iv['l']),base.imul(coeff_iv['L'],coeff_iv['m'])),
            base.imul(coeff_iv['L'],coeff_iv['l'])]
    inv_D = reciprocal(D_iv)
    check('two_quotient_enclosures_overlap', all(
        max(v[0],w[0]) <= min(v[1],w[1])
        for v,w in zip((gamma,alpha),[base.imul(v,inv_D) for v in Q_iv])))
    E_iv = [[(F(0),F(0)) for _ in range(6)] for _ in range(7)]
    for j in range(6):
        k=5-j
        E_iv[5-k][j] = base.iscale(alpha,k+1)
        E_iv[6-k][j] = gamma
        if k:
            E_iv[7-k][j] = base.iscale(alpha,F(2*k+1,2))
    B_iv = {n:[[evaluate(v) for v in row] for row in B[n]] for n in (6,7)}
    P_iv = [[isub(B_iv[7][i][j],isum(
        base.imul(base.imul(E_iv[i][a],B_iv[6][a][b]),E_iv[j][b])
        for a in range(6) for b in range(6))) for j in range(7)] for i in range(7)]
    certificate['intervals'] = {
        'leading_coefficients':{key:base.interval_json(v) for key,v in coeff_iv.items()},
        'reciprocal_l':base.interval_json(inv_l), 'D':base.interval_json(D_iv),
        'D_squared':base.interval_json(D2_iv), 'reciprocal_D':base.interval_json(inv_D),
        'quotient_alpha':base.interval_json(alpha), 'quotient_gamma':base.interval_json(gamma),
        'quotient_outer_bounds':{'alpha':outer(alpha),'gamma':outer(gamma)},
        'E':iv_json_matrix(E_iv), 'B6':iv_json_matrix(B_iv[6]),
        'B7':iv_json_matrix(B_iv[7]), 'P':iv_json_matrix(P_iv)}
    stop_if_failed('DENOMINATOR_FAILURE')

    # Exactly the predeclared direction set; construction precedes all signs.
    directions = [(f'e{i+1}',[int(j==i) for j in range(7)]) for i in range(7)]
    for i in range(7):
        for j in range(i+1,7):
            for sign in (1,-1):
                directions.append((f'e{i+1}{"+" if sign==1 else "-"}e{j+1}',
                                   [int(k==i)+sign*int(k==j) for k in range(7)]))
    check('exactly_49_distinct_prescribed_directions', len(directions)==49
          and len({tuple(v) for _,v in directions})==49)
    forms = []
    for name,v in directions:
        exact = alg.add(*(alg.scale(PN[i][j],v[i]*v[j]) for i in range(7) for j in range(7) if v[i]*v[j]))
        iv = isum(base.iscale(P_iv[i][j],v[i]*v[j]) for i in range(7) for j in range(7) if v[i]*v[j])
        bound = outer(iv)
        check('outer_contains_'+name, outer_contains(iv,bound))
        sign = 'NEGATIVE' if iv[1]<0 else 'POSITIVE' if iv[0]>0 else 'UNRESOLVED'
        forms.append({'name':name, 'vector':v, 'exact_numerator_over_D_squared':alg.encode(exact),
                      'interval':base.interval_json(iv), 'outer_bound':bound, 'sign':sign})
    negatives = [v for v in forms if v['sign']=='NEGATIVE']
    certificate['quadratic_forms'] = forms
    # A short, separately expanded formula for the already prescribed e2.
    # Parity of p_k means no contribution from p_(n-1) to t^(n-2).
    r,s = b[6][4],b[7][5]
    row_formulas = [alg.scale(alg.mul(l,l),86400),
                    alg.scale(alg.mul(l,m),14400),
                    alg.scale(alg.add(alg.scale(alg.mul(m,m),5),alg.scale(alg.mul(l,r),-2)),576),
                    alg.scale(alg.add(alg.scale(alg.mul(M,M),6),alg.scale(alg.mul(L,s),-2)),14400)]
    row_entries = [B[6][0][0],B[6][0][1],B[6][1][1],B[7][1][1]]
    check('all_four_short_witness_kernel_formulas', row_formulas == row_entries)
    # P22=14400*(-2Ls+2LMm/l-L^2*m^2/l^2+2L^2*r/l).
    scalar_num = alg.scale(alg.add(
        alg.scale(alg.mul(alg.mul(L,s),D),-2),
        alg.scale(alg.mul(alg.mul(alg.mul(L,M),m),l),2),
        alg.scale(alg.mul(alg.mul(L,L),alg.mul(m,m)),-1),
        alg.scale(alg.mul(alg.mul(alg.mul(L,L),r),l),2)),14400)
    check('e2_scalar_identity_after_clearing_D_squared', PN[1][1] == alg.mul(D,scalar_num))
    small_inputs = {'alpha':outer(alpha), 'gamma':outer(gamma),
                    'B6_11':outer(B_iv[6][0][0]), 'B6_12':outer(B_iv[6][0][1]),
                    'B6_22':outer(B_iv[6][1][1]), 'B7_22':outer(B_iv[7][1][1])}

    def unpack_outer(v):
        unit = F(10)**v['power_of_ten']
        return tuple(F(v['scaled_interval'][key])*unit for key in ('lower','upper'))

    small = {key:unpack_outer(v) for key,v in small_inputs.items()}
    aa,gg = small['alpha'],small['gamma']
    coarse_iv = isub(small['B7_22'],isum([
        base.imul(base.imul(gg,gg),small['B6_11']),
        base.iscale(base.imul(base.imul(aa,gg),small['B6_12']),10),
        base.iscale(base.imul(base.imul(aa,aa),small['B6_22']),25)]))
    check('short_rational_table_certifies_e2_below_minus_79e_minus_8', coarse_iv[1] < -F(79,10**8))
    tight_iv = tuple(F(forms[1]['interval'][key]) for key in ('lower','upper'))
    check('e2_is_second_fixed_direction', forms[1]['vector'] == [0,1,0,0,0,0,0])
    check('tight_and_short_table_enclosures_overlap',
          max(tight_iv[0],coarse_iv[0]) <= min(tight_iv[1],coarse_iv[1]))
    certificate['witness_scalar_check'] = {
        'identity':'P22=B7_22-gamma^2*B6_11-10*alpha*gamma*B6_12-25*alpha^2*B6_22',
        'simplified_numerator_over_D':alg.encode(scalar_num),
        'exact_identity_residual':alg.encode(alg.add(PN[1][1],alg.scale(alg.mul(D,scalar_num),-1))),
        'six_small_rational_input_bounds':small_inputs,
        'coarse_interval':base.interval_json(coarse_iv),
        'coarse_outer_bound':outer(coarse_iv),
        'strict_comparison_upper_bound':base.rational(-F(79,10**8)),
        'strict_upper_margin':base.rational(-F(79,10**8)-coarse_iv[1])}
    certificate['sign_counts'] = {s:sum(v['sign']==s for v in forms) for s in ('NEGATIVE','POSITIVE','UNRESOLVED')}
    certificate['sign_threshold'] = 'An exact upper endpoint strictly below 0; otherwise no negative certificate'
    certificate['selected_witness'] = negatives[0] if negatives else None
    certificate['scope'] = 'Only this N=6,7 embedding; no eventual-only or other embedding claim, no RH inference'
    certificate['incomplete_certification'] = [v['name'] for v in forms if v['sign']=='UNRESOLVED']
    stop_if_failed('REPORTING_FAILURE')
    save('NEGATIVE_DIRECTION_CERTIFIED' if negatives else 'INCONCLUSIVE')
    print(json.dumps({'status':certificate['status'], 'degree_bounds':certificate['leading_coefficient_outer_bounds'],
                      'required_degree_bound':'0 excluded',
                      'witness':None if not negatives else {'name':negatives[0]['name'], 'vector':negatives[0]['vector'],
                                                           'outer_bound':negatives[0]['outer_bound']},
                      'required_quadratic_upper_bound':'<0', 'sign_counts':certificate['sign_counts'],
                      'checks_passed':sum(checks.values()), 'failures':certificate['failures'],
                      'incomplete_certification':certificate['incomplete_certification'],
                      'certificate':str(OUTPUT.relative_to(ROOT.parent.parent))},indent=2))


if __name__ == '__main__':
    main()
