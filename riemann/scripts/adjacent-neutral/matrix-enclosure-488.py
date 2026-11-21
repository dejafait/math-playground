#!/usr/bin/env python3
"""Enclose an expanded principal section; never the full neutral margin.

Reuse the step487 exact/dyadic action and integration implementation.
Keep all257 projection rows. Save every matrix and shifted LDL operand.
No floating point decides an inequality. No analytic input audit claimed.
"""
import gzip
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('matrix487', HERE/'matrix-enclosure-487.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
B, S, ZERO, ONE = m.B, m.S, m.ZERO, m.ONE
INDICES = tuple(range(2,18))+(256,)


def ball(x):
    return B(int(x['lower_numerator']), int(x['upper_numerator']))


def shifted_ldl(matrix, shift):
    """Interval recurrence encloses exact LDL of every symmetric member.

    Inductively all earlier pivots have positive lower endpoints, so
    division is licensed. Every exact L,D satisfies A-shift I=L D L^T.
    Strict positivity of every enclosed D implies A>=shift I. Pivots
    themselves are not lower eigenvalue bounds.
    """
    size = len(matrix)
    lower = [[ZERO for _ in range(size)] for _ in range(size)]
    pivots = []
    for j in range(size):
        pivot = matrix[j][j]-shift
        for k in range(j):
            pivot = pivot-lower[j][k]*lower[j][k]*pivots[k]
        pivots.append(pivot)
        if pivot.lo<=0:
            return {'passed':False, 'failed_column':j,
                    'pivots':[x.json() for x in pivots],
                    'lower':[[x.json() for x in row] for row in lower]}
        lower[j][j] = ONE
        for i in range(j+1,size):
            value = matrix[i][j]
            for k in range(j):
                value = value-lower[i][k]*lower[j][k]*pivots[k]
            lower[i][j] = value/pivot
    return {'passed':True, 'failed_column':None,
            'pivots':[x.json() for x in pivots],
            'lower':[[x.json() for x in row] for row in lower]}


def encode(matrix):
    return [[x.json() for x in row] for row in matrix]


def main():
    started = time.monotonic()
    checks = {
        'all_257_integer_legendre_recurrences':m.check_integer_polynomials(),
        'all_unsimplified_kernel_identity_comparisons':m.check_kernel_identity(),
    }
    # Test all LDL entries on a nontrivial exact rational L D L^T.
    expected = [[F(1),F(0),F(0)],[F(-2,3),F(1),F(0)],
                [F(1,7),F(3,5),F(1)]]
    diag = [F(1,3),F(2,7),F(5,11)]
    test = [[m.rational(sum(expected[i][k]*diag[k]*expected[j][k]
                            for k in range(3))) for j in range(3)] for i in range(3)]
    replay = shifted_ldl(test,ZERO)
    checks['known_rational_ldl_all_operands'] = replay['passed'] and all(
        F(ball(replay['lower'][i][j]).lo,S)<=expected[i][j]<=F(ball(replay['lower'][i][j]).hi,S)
        for i in range(3) for j in range(3)) and all(
        F(ball(x).lo,S)<=d<=F(ball(x).hi,S) for x,d in zip(replay['pivots'],diag))
    checks['indefinite_ldl_rejected'] = not shifted_ldl(
        [[ONE,B.rational(2)],[B.rational(2),ONE]],ZERO)['passed']
    const,_,ratios,_ = m.scalar.scalar_inputs()
    q = [m.rational(x) for x in m.action.quotient_coefficients(F(1,2),97)[1:]]
    h = [m.rational(x/2) for x in m.action.quotient_coefficients(F(-3,2),97)[1:]]
    source_path = HERE/'matrix-coefficients-487.json.gz'
    with gzip.open(source_path,'rt') as fp:
        source = json.load(fp)
    assert source['precision_bits']==m.scalar.BITS
    columns = {}
    for n in INDICES:
        if str(n) in source['columns']:
            columns[n] = [{'g':[ball(x) for x in piece['g']],
                'signs':{int(s):([ball(x) for x in pair['P']],
                                 [ball(x) for x in pair['Q']])
                         for s,pair in piece['signs'].items()}}
                for piece in source['columns'][str(n)]]
        else:
            columns[n] = m.build_column(n,const,ratios[n-2],q,h)
        print(f'Enclosed column {n}; elapsed {time.monotonic()-started:.1f}s',flush=True)
    arrays = {'precision_bits':m.scalar.BITS,'indices':list(INDICES),'columns':{}}
    for n,pieces in columns.items():
        arrays['columns'][str(n)] = [{'g':[x.json() for x in piece['g']],
            'signs':{str(s):{'P':[x.json() for x in pair[0]],
                            'Q':[x.json() for x in pair[1]]}
                     for s,pair in piece['signs'].items()}} for piece in pieces]
    coeff_path = HERE/'matrix-coefficients-488.json.gz'
    with gzip.open(coeff_path,'wt') as fp:
        json.dump(arrays,fp,separators=(',',':'))
    del source, arrays
    half,b = B.rational(1,2),const['split_b']
    lengths = (b,half-b,half)
    transforms = [m.projection_polynomials(u,v)
                  for u,v in ((ZERO,b),(half,b-half),(ONE,-half))]
    size = len(INDICES)
    result = {'precision_bits':m.scalar.BITS,'interval_denominator':str(S),
        'indices':list(INDICES),'projection_rows':257,
        'coefficient_artifact':str(coeff_path.relative_to(HERE.parent.parent)),
        'coefficient_artifact_sha256':hashlib.sha256(coeff_path.read_bytes()).hexdigest(),
        'source_coefficient_artifact_sha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),
        'scope':'Expanded17 by17 principal blocks only; all257 projection rows retained.',
        'full_two_sign_margin_certified':False,'shift':B.rational(1,25).json(),
        'ratios':[ratios[n-2].json() for n in INDICES],
        'checks':checks,'signs':{}}
    path = Path(__file__).with_suffix('.json')
    for s in (-1,1):
        projected = []
        for n in INDICES:
            moments = [m.power_moments(piece['signs'][s]) for piece in columns[n]]
            row = []
            for k in range(257):
                value = ZERO
                for j in range(3):
                    value = value+m.interval_dot(transforms[j][k],moments[j])*lengths[j]
                row.append(value)
            projected.append(row)
        print(f'sign{s:+}: all257 moments for all17 columns; elapsed {time.monotonic()-started:.1f}s',flush=True)
        # <z_n,T_m>=<p_n,T_m>-r_n<p_(n mod2),T_m> uses the
        # already enclosed orthonormal projection moments, without quadrature.
        head = [[projected[j][n]-ratios[n-2]*projected[j][n%2]
                 for j in range(size)] for n in INDICES]
        gram = [[ZERO for _ in range(size)] for _ in range(size)]
        for i,n in enumerate(INDICES):
            for j in range(i,size):
                other = INDICES[j]
                value = ZERO
                for piece in range(3):
                    value = value+m.exact_integral(columns[n][piece]['signs'][s],
                        columns[other][piece]['signs'][s])*lengths[piece]
                gram[i][j] = gram[j][i] = value
            print(f'sign{s:+}: complete Gram row {n}; elapsed {time.monotonic()-started:.1f}s',flush=True)
        cov = [[gram[i][j]-m.interval_dot(projected[i],projected[j])
                for j in range(size)] for i in range(size)]
        schur = [[(head[i][j]+head[j][i]).integer_div(2)-cov[i][j]*B.rational(250,171)
                  for j in range(size)] for i in range(size)]
        ldl = shifted_ldl(schur,B.rational(1,25))
        width = max(x.hi-x.lo for mat in (head,gram,cov,schur) for row in mat for x in row)
        checks[f'{s}_exact_interval_symmetry'] = all(
            schur[i][j].json()==schur[j][i].json() for i in range(size) for j in range(size))
        checks[f'{s}_matrix_width_below_1e_minus_30'] = F(width,S)<F(1,10**30)
        checks[f'{s}_shifted_ldl_all_pivots_positive'] = ldl['passed']
        result['signs'][str(s)] = {
            'projected_moments':encode(projected),'unsymmetrized_head':encode(head),
            'total_gram':encode(gram),'complete_covariance':encode(cov),
            'schur':encode(schur),'shifted_ldl':ldl,
            'maximum_matrix_interval_width':m.scalar.frac_json(F(width,S)),
            'minimum_pivot_lower':m.scalar.frac_json(F(min(ball(x).lo for x in ldl['pivots']),S))}
        # Preserve a completed sign even if the next calculation is interrupted.
        result['completed_signs'] = list(result['signs'])
        result['failures'] = [k for k,v in checks.items() if not v]
        path.write_text(json.dumps(result,indent=2)+'\n')
        print(f'sign{s:+}: shifted LDL at1/25 passed={ldl["passed"]}; '
              f'min pivot lower {min(float(F(ball(x).lo,S)) for x in ldl["pivots"]):.12g}; '
              f'width<={m.scalar.up(F(width,S))}',flush=True)
    result['checks_pass'] = not result['failures']
    result['unresolved'] = ['Columns18,...,255 and every coupling to them remain unenclosed.',
        'Positive principal blocks do not imply either full matrix bound.',
        'C744i/j/k/l remain independently unaudited; no full mu, beta_1 or RH conclusion.']
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Checks {sum(checks.values())}/{len(checks)}; failures {result["failures"]}',flush=True)
    print(f'Principal threshold1/25 only; full255-dimensional threshold unpaid. Certificate: {path}',flush=True)
    if result['failures']:
        raise SystemExit(1)


if __name__=='__main__':
    main()
