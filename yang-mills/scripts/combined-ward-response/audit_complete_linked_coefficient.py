"""Independent exact grid/unisolvence audit of L220, with no production imports.

Every polynomial has degree at most five in EACH energy variable. Values
on {0,...,5}^3 therefore determine it, by repeated univariate root bounds.
The analytic zero-integral and source-normalization arguments remain in
L220 section 5. No frequency sampling or numerical integration is used.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from pathlib import Path
import hashlib
import json


PERMS = tuple(permutations(range(3)))
FORMS = ('P_D', 'P_A', 'P_X', 'P_C', 'B_R', 'D', 'B_G')


def numerators(v):
    x, y, z = v
    ell = sum(v)
    f, h, k = (1-e/4 for e in v)
    first = f*x+h*y+k*z
    second = f*f*x+h*h*y+k*k*z
    hd = x*(4+z)*h*h*ell/2-2*f*h*z*(h*(x+z)+k*y)
    hx = f*h*z*((h+k)*(x+z)+2*k*y)
    return dict(
        gx=ell*(1-(1-x/2)*(1-y/2)),
        gy=ell*(1-x/2)*(1-y/2)*z/2,
        g=-x*y*(x-y)**2/4,
        gamma=(ell*second-first**2)/3,
        q=4*f*y*ell,
        t=Q(4, 3)*(ell**2*(f*f+h*h+k*k)-2*ell*second+first**2),
        hd=hd, hx=hx, ha=2*f*(h*y+k*z)*ell-hd-2*hx,
        tau=-f*h*z*(y*ell+(y-z)*(x+z)/2),
        xi=f*y*z*(z-y)**2/8)


def assembled(v):
    """Use the imported group formulas BEFORE collecting the six scalars."""
    s = numerators(v)
    e2 = sum(v)**2
    x, y, g = s['gx'], s['gy'], s['g']
    lam = (-Q(17, 2)*e2+45*x-Q(15, 2)*y,
           5*e2-39*x+Q(9, 2)*y,
           Q(3, 4)*e2-3*x-Q(3, 2)*y,
           -6*e2+30*x+15*y, 14*e2-72*x+6*y, Q(0), Q(0))
    action_hessian = (17*e2-90*x+15*y, -10*e2+78*x-9*y,
                      -Q(3, 2)*e2+6*x+3*y, 12*e2-60*x-30*y,
                      Q(0), Q(0), Q(0))
    vmix = (-3*g/2, Q(0), Q(0), Q(0), 3*g/2, 3*g, -3*g)
    axial = (3*s['t']/2, Q(0), Q(0), Q(0), Q(0), Q(0), Q(0))
    subtraction = (-3*s['q'], -3*s['q']+e2/2, -e2/4,
                   Q(0), Q(0), Q(0), Q(0))
    gg = (Q(0), Q(0), Q(0), Q(0), Q(0), Q(0), 3*g)
    rr = (Q(0), Q(0), Q(0), Q(0), -9*g/2, Q(0), Q(0))
    transverse = (3*(s['hd']+s['tau']), 3*s['ha'],
                  3*(s['hx']-s['tau']/2), 3*(s['xi']+2*s['tau']),
                  Q(0), Q(0), Q(0))
    mixed = (Q(0), Q(0), Q(0), Q(0), Q(0), 12*s['gamma'], Q(0))
    return tuple(map(sum, zip(lam, action_hessian, vmix, axial,
                              subtraction, gg, rr, transverse, mixed)))


def collected(v):
    s = numerators(v)
    ell2 = sum(v)**2
    x, y, g = s['gx'], s['gy'], s['g']
    return (
        Q(17, 2)*ell2-45*x+Q(15, 2)*y+3*s['t']/2-3*s['q']
        +3*s['hd']+3*s['tau']-3*g/2,
        -Q(9, 2)*ell2+39*x-Q(9, 2)*y-3*s['q']+3*s['ha'],
        -ell2+3*x+Q(3, 2)*y+3*s['hx']-3*s['tau']/2,
        6*ell2-30*x-15*y+3*s['xi']+6*s['tau'],
        14*ell2-72*x+6*y-3*g, 12*s['gamma']+3*g, Q(0))


def divergence(v, exponents):
    """Evaluate the polynomial divergence numerator, including at ell=0."""
    x = v[0]
    ell = sum(v)
    p = Q(1)
    for value, degree in zip(v, exponents):
        p *= value**degree
    dp = Q(0)
    if exponents[0]:
        dp = Q(exponents[0])
        for j, (value, degree) in enumerate(zip(v, exponents)):
            dp *= value**(degree-int(j == 0))
    return (2-x)*ell*p+x*(4-x)*(ell*dp-p)


def required_unsymmetrized(v):
    x, y, z = v
    m1, m2 = sum(v)**2*(z-2), sum(v)**2*(y*z-4)
    return (
        3*m1/2+9*m2/16, -3*m1/2-3*m2/16, -3*m1/2+3*m2/16,
        3*m1+m2/8+divergence(v, (0, 1, 2))/4
        +divergence(v, (1, 1, 1))/8,
        6*m1-3*m2/4-3*divergence(v, (0, 0, 2))
        -3*divergence(v, (0, 1, 1))/2, Q(0), Q(0))


def source_quotients(v):
    """Canonical source formulas, separately evaluated before denominator clearing.

    t is evaluated by actual matrix multiplication QFQ, unlike the trace
    expansion used in numerators(). A rational rank-one projector uses
    energy coordinates via similarity; trace is unchanged. Entries
    P_ij=v_j/ell give P^2=P and Tr(P F^m)=sum(v_j f_j^m)/ell,
    the same traces as d d^T/ell for all nonnegative energies.
    """
    x, y, z = v
    ell = sum(v)
    f, h, k = filters = tuple(1-e/4 for e in v)
    proj = [[Q(int(i == j))-v[j]/ell for j in range(3)] for i in range(3)]
    qfq = [[sum(proj[i][m]*filters[m]*proj[m][j] for m in range(3))
            for j in range(3)] for i in range(3)]
    tr = sum(qfq[i][j]*qfq[j][i] for i in range(3) for j in range(3))
    hd = x*(4+z)*h*h/(2*ell)-2*f*h*z*(h*(x+z)+k*y)/ell**2
    hx = f*h*z*((h+k)*(x+z)+2*k*y)/ell**2
    # gamma: weighted-variance pair identity, independently of S1/S2.
    gamma = sum(v[i]*v[j]*(filters[i]-filters[j])**2
                for i in range(3) for j in range(i+1, 3))/(3*ell**2)
    return dict(
        gx=(1-(1-x/2)*(1-y/2))/ell,
        gy=(1-x/2)*(1-y/2)*(z/2)/ell,
        g=-x*y*(x-y)**2/(4*ell**2), gamma=gamma,
        q=4*f*y/ell, t=Q(4, 3)*tr, hd=hd, hx=hx,
        ha=2*f*(h*y+k*z)/ell-hd-2*hx,
        tau=-f*h*z/ell*(y+(y-z)*(x+z)/(2*ell)),
        xi=f*y*z*(z-y)**2/(8*ell**2))


def main():
    records = []
    failures = []
    counts = dict(assembly=0, fixed_identity=0, source_scalar=0)
    for integers in product(range(6), repeat=3):
        v = tuple(map(Q, integers))
        before, after = assembled(v), collected(v)
        assembly = tuple(a-b for a, b in zip(before, after))
        signed = [Q(0)]*len(FORMS)
        for perm in PERMS:
            w = tuple(v[j] for j in perm)
            got, want = assembled(w), required_unsymmetrized(w)
            signed = [r+(a-b)/6 for r, a, b in zip(signed, got, want)]
        source = {}
        if sum(v):
            numer, quot = numerators(v), source_quotients(v)
            source = {key: numer[key]-sum(v)**2*quot[key] for key in numer}
        counts['assembly'] += len(assembly)
        counts['fixed_identity'] += len(signed)
        counts['source_scalar'] += len(source)
        if any(assembly) or any(signed) or any(source.values()):
            failures.append(list(integers))
        records.append(dict(energies=list(integers),
                            assembly_defects=list(map(str, assembly)),
                            identity_defects=list(map(str, signed)),
                            source_defects={k: str(v) for k, v in source.items()}))
    certificate = dict(
        method='Exact Cartesian interpolation/unisolvence, no production imports',
        source_scope='L220 section 5; canonical analytic formulas only',
        degree_bound_each_variable=5, grid_each_variable=list(range(6)),
        forms=list(FORMS), complete_records=records, failures=failures,
        actual=dict(nodes=len(records), checks=counts, failure_count=len(failures)),
        required=dict(nodes=216, failure_count=0,
                      each_complete_defect='exact rational zero'),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    dest = Path(__file__).with_name('complete-linked-coefficient-independent-audit.json')
    dest.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Actual:', certificate['actual'])
    print('Required:', certificate['required'])
    print('Failures:', failures)
    print('Full certificate:', dest)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
