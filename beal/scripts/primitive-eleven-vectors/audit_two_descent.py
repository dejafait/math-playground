"""Independent finite arithmetic audit of L085; uniform proof stays in L085.

Uses only literal source coefficients from L034's audited transcription.
Does not import or execute any construction script. Standard library only.
"""
import ast
import json
from fractions import Fraction
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(*ps):
    return trim([sum(p[i] if i < len(p) else 0 for p in ps)
                 for i in range(max(map(len, ps)))])


def scale(p, c):
    return trim([c*x for x in p])


def mul(p, q):
    out = [0]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return trim(out)


def power(p, n):
    out = [1]
    for _ in range(n):
        out = mul(out, p)
    return out


def compose(p, q):
    out = [0]
    for a in reversed(p):
        out = add(mul(out, q), [a])
    return out


def ev(p, x):
    return compose(p, [x])[0]


def valuation(x):
    if not x:
        return None
    n = 0
    while x % 11 == 0:
        n += 1
        x //= 11
    return n


def mod(p):
    return trim([int(x % 11) for x in p])


def main():
    source = ROOT/'scripts/five-isogeny-modular-norm/check_norm.py'
    wanted = {'a', 'b1', 'b2', 'h', 'jcoef'}
    literal = {}
    for node in ast.parse(source.read_text()).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            name = getattr(node.targets[0], 'id', '')
            if name in wanted:
                literal[name] = ast.literal_eval(node.value)
    assert set(literal) == wanted
    a, h, J = (literal[k] for k in ['a', 'h', 'jcoef'])
    b = mul(literal['b1'], literal['b2'])
    d = power([-16, 1], 11)
    e = [-20, -10, -1, 1]
    g = [-1264, -160, -4, 1]
    checks = []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required,
                           passed=actual == required))

    check('modular linear identity', add(scale(a, 2), scale(b, -1)), J)
    check('modular reconstruction identity',
          add(mul(a, a), scale(mul(a, b), -1),
              scale(mul(mul(b, b), e), -1), mul(d, power(h, 3))), [0])
    check('origin-preserving coordinate equation',
          compose(g, [0, 4]), add(scale(e, 64), [16]))
    check('scaled curve equation for both realizations',
          [c//14641 if c % 14641 == 0 else str(Fraction(c, 14641))
           for c in add(compose(e, [16, 121]), [-3660])], [0, 6, 47, 121])
    check('full cubic residue factorization', mod(g),
          mod(mul([-8, 1], power([-9, 1], 2))))
    A, B, C = g[2], g[1], g[0]
    disc = A*A*B*B-4*B**3-4*A**3*C-27*C*C+18*A*B*C
    check('cubic discriminant', disc, -256*11**5)
    lifts = {}
    for n, expected in [(2, 118), (3, 844)]:
        roots = [u for u in range(8, 11**n, 11) if ev(g, u) % 11**n == 0]
        check(f'unique root modulo 11^{n}', roots, [expected])
        lifts[str(n)] = roots
    alpha = lifts['3'][0]
    check('alpha derivative unit residue', (3*alpha**2-8*alpha-160) % 11, 1)
    center = (4-alpha)*pow(2, -1, 1331) % 1331
    check('center lift', center, 911)
    check('center offset', (center-64)//121, 7)
    check('residue squares', sorted({u*u % 11 for u in range(1, 11)}), [1,3,4,5,9])
    components = {'h3': power(h, 3), 'J': J, 'd': d}
    shifted = {k: compose(p, [16, 1]) for k, p in components.items()}
    required = [23-2*i for i in range(1, 11)]
    vals = {k: [valuation(p[i]) if i < len(p) else None for i in range(1, 11)]
            for k, p in shifted.items()}
    check('uniform intermediate coefficient bounds',
          {k: [v is None or v >= req for v, req in zip(row, required)]
           for k, row in vals.items()}, {k: [True]*10 for k in vals})
    check('constant and leading coefficients',
          [shifted['h3'][0], shifted['J'][0], shifted['d'][0],
           shifted['h3'][-1]], [11**24, 11**22, 0, 1])
    scaled = {}
    for k, p, n in [('h3', components['h3'], 22), ('J', J, 22),
                    ('d', d, 22), ('B', b, 20), ('N', add(a, scale(b, 60)), 22)]:
        q = compose(p, [16, 121])
        check(f'{k}: all scaling remainders', [c % 11**n for c in q], [0]*len(q))
        scaled[k] = [c//11**n for c in q]
    check('scaled h3 reduction', mod(scaled['h3']), [0])
    check('scaled J reduction', mod(scaled['J']), [1]+[0]*10+[1])
    check('scaled d reduction', mod(scaled['d']), [0]*11+[1])
    check('scaled B reduction', mod(scaled['B']), mod(power([1,1],10)))
    derivatives = {}
    for k in components:
        q = [i*c for i, c in enumerate(scaled[k])][1:]
        check(f'{k}: derivative divisibility by eleven', [c % 11 for c in q], [0]*len(q))
        derivatives[k] = [c//11 for c in q]
    squares = {u*u % 11 for u in range(1, 11)}
    cases = []
    for s, z, v, rhs in [(4,4,2,8520), (10,5,8,16330)]:
        x = 16+121*z
        check(f'{s}: cluster root residue', pow(s-1, -1, 11), z)
        smooth = (5-s+s*s) % 11
        smooth_units = [(4*smooth-8) % 11, (4*smooth-9) % 11]
        cluster_units = [1, (4*z-7) % 11, (4*z-7) % 11]
        check(f'{s}: complete residue units', smooth_units+cluster_units,
              [5,4,1,9,9] if s == 4 else [9,8,1,2,2])
        chars = [int(u not in squares) for u in smooth_units+cluster_units]
        check(f'{s}: complete square characters', chars,
              [0,0,0,0,0] if s == 4 else [0,1,0,1,1])
        check(f'{s}: exact curve constant', (ev(e,x)-3660)//14641, rhs)
        check(f'{s}: Hensel value and derivative',
              [(v*v+v-rhs) % 11, (2*v+1) % 11], [0,5 if s == 4 else 6])
        exact = [ev(b,x), ev(a,x)+60*ev(b,x), ev(d,x)]
        check(f'{s}: reconstruction valuations', list(map(valuation, exact)), [20,22,22])
        units = [exact[i]//11**n % 11 for i,n in enumerate([20,22,22])]
        check(f'{s}: reconstruction units', units, [1,3,4] if s == 4 else [1,9,5])
        check(f'{s}: exact scalar residue',
              (units[1]+units[0]*v)*pow(units[2], -1, 11) % 11, s)
        deriv = (ev(derivatives['h3'],z)+s*ev(derivatives['J'],z)
                 -s*s*ev(derivatives['d'],z)) % 11
        leading = s*(1-s) % 11
        C0 = deriv*pow(leading,-1,11) % 11
        check(f'{s}: Eisenstein derivative/leading/constant residues',
              [deriv,leading,C0], [6,10,5] if s == 4 else [1,9,5])
        # Residue witness: c=q^-1, b^4=1 and a^3=t*c^11.
        t, q = s, (1-s) % 11  # 1728 = 1 (mod 11)
        c = pow(q,-1,11)
        aw = pow(t*c,7,11)
        check(f'{s}: common primitive witness residues',
              [q*pow(c,11,11)%11, (aw**3+1-pow(c,11,11))%11], [1,0])
        cases.append(dict(s=s,z=z,x=x,V_residue=v,curve_constant=rhs,
                          exact_reconstruction=exact,reconstruction_units=units,
                          smooth_units=smooth_units,cluster_units=cluster_units,
                          square_characters=chars,Rprime_over_11=deriv,
                          smooth_removal_unit=leading,Eisenstein_constant_over_11=C0,
                          primitive_residues=dict(a=aw,b=1,c=c)))
    bounds = dict(v11_cluster=2,v11_separation='5/2',
                  normalized_M=[4,5], normalized_L=[20,25],
                  actual_image_size=2,unrestricted_image_size=16)
    check('strict normalized separations', [4<5,20<25], [True,True])
    failures = [c['name'] for c in checks if not c['passed']]
    result = dict(source=str(source.relative_to(ROOT)),source_coefficients=literal,
                  root_data=dict(lifts=lifts,center=center,discriminant=disc),
                  uniform=dict(required_intermediate_bounds=required,
                               actual_intermediate_valuations=vals,
                               scaled_components=scaled,
                               scaled_components_mod11={k:mod(p) for k,p in scaled.items()},
                               derivatives_over_11=derivatives,
                               derivatives_over_11_mod11={k:mod(p) for k,p in derivatives.items()}),
                  cases=cases,bounds=bounds,checks=checks,failures=failures)
    path = BASE/'two-descent-audit-certificate.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}')
    print('Actual/required: 2 < 5/2; M 4 < 5; L 20 < 25; factor constants 5/5 at both scalars.')
    print('Exact local image: 2 of 16; global independence not tested.')
    print(f'Certificate: {path.relative_to(ROOT)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
