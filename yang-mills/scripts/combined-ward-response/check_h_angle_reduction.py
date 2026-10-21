"""Exact rational supporting checks for L129's physical H reduction.

Run: python3 scripts/combined-ward-response/check_h_angle_reduction.py
The canonical proof is analytic; finite checks do not establish a torus
identity or quadrature bound. No numerical coefficient is certified here.
"""
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def dot(v, w):
    return sum((a*b for a, b in zip(v, w)), F(0))


def mv(a, v):
    return [dot(row, v) for row in a]


def outer(v, w):
    return [[a*b for b in w] for a in v]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(q, a):
    return [[q*x for x in row] for row in a]


def physical_check(ds, etas, m, a, b):
    # Indices 0,1,2 correspond to physical components 2,3,4.
    x, y, z = ds
    lam = dot(ds, ds)
    zz = [[-y, x, F(0)], [-z, F(0), x], [F(0), -z, y]]
    dd = [F(0)]*3
    dd[m] = etas[m]
    xx, yy, zzv = dd
    zp = [[-yy, xx, F(0)], [-zzv, F(0), xx], [F(0), -zzv, yy]]
    ep = [F(0)]*3
    ep[m] = -ds[m]/4
    n, np = [z, -y, x], [zzv, -yy, xx]
    identity = [[F(i == j) for j in range(3)] for i in range(3)]
    ss = add(identity, scale(-1/lam, outer(n, n)))
    sp = add(scale(-1/lam, add(outer(np, n), outer(n, np))),
             scale(2*dot(ds, dd)/lam**2, outer(n, n)))
    fs = [[F(0)]*3 for _ in range(3)]
    planes = [(0, 1), (0, 2), (1, 2)]
    for row, (mu, nu) in enumerate(planes):
        fs[mu][row] = 2*ds[nu]*etas[mu]
        fs[nu][row] = -2*ds[mu]*etas[nu]
    jj = [[F(0)]*3 for _ in range(3)]
    # Both complete ordered generators at rho=2, including all output rows.
    for nu, plane in [(1, 0), (2, 1)]:
        av = [etas[nu]*row[nu] for row in zz]
        ap = [ep[nu]*row[nu]+etas[nu]*rowp[nu]
              for row, rowp in zip(zz, zp)]
        c = etas[0]*etas[nu]
        cp = ep[0]*etas[nu]+etas[0]*ep[nu]
        w = [c*s for s in ss[plane]]
        wp = [cp*s+c*t for s, t in zip(ss[plane], sp[plane])]
        jj = add(jj, add(outer(av, wp), scale(-1, outer(ap, w))))
    actual = -(dot(fs[b], mv(jj, fs[a]))
               +dot(fs[a], mv(jj, fs[b])))/(4*lam)
    xx, yy, zzv = x*x, y*y, z*z
    aa, bb, cc = (q*q for q in etas)
    k = xx+zzv
    if (m, a, b) == (0, 1, 1):
        required = (xx*(4+zzv)*bb**2/(2*lam)
                    -2*aa*bb*zzv*(bb*k+cc*yy)/lam**2)
    elif (m, a, b) == (1, 0, 1):
        required = aa*bb*zzv*((bb+cc)*k+2*cc*yy)/lam**2
    else:
        assert (m, a, b) == (0, 0, 0)
        required = 2*aa*(bb*yy+cc*zzv)/lam
    return actual, required


def moment_check(k, z, j0, j1):
    x = k-z
    aa, cc = 1-x/4, 1-z/4
    u0 = ((k+4)*j0-1)/4
    u1 = ((k+4)*j1-j0)/4
    v0 = ((k+4)**2*j0-k-6)/16
    v1 = ((k+4)**2*j1-2*(k+4)*j0+1)/16
    w = u0-k*u1
    fd = x*(4+z)*v0/2-2*aa*z*(k*v1+cc*w)
    fx = aa*z*(k*v1+cc*k*u1+2*cc*w)
    f0 = 2*aa*(F(1, 2)-k*u0+cc*z*u0)
    fa = aa-2*aa*k*u0-x*(4+z)*v0/2
    return f0-fd-2*fx, fa


def main():
    choices = [(F(6, 5), F(4, 5)), (F(8, 5), F(3, 5)),
               (F(24, 13), F(5, 13))]
    records, failures = [], []
    for selected in product(choices, repeat=3):
        for signs in product((-1, 1), repeat=3):
            ds = [p[0]*s for p, s in zip(selected, signs)]
            etas = [p[1] for p in selected]
            for entry in [(0, 1, 1), (1, 0, 1), (0, 0, 0)]:
                actual, required = physical_check(ds, etas, *entry)
                row = {"d": list(map(str, ds)),
                       "eta": list(map(str, etas)),
                       "entry": [v+2 for v in entry],
                       "actual": str(actual), "required": str(required),
                       "residual": str(actual-required)}
                records.append(row)
                if actual != required:
                    failures.append(row)
    moments = []
    # Formal arbitrary j0,j1; this tests cancellation, not inverse integration.
    for k, z, j0, j1 in product((F(1, 2), F(2)), repeat=4):
        actual, required = moment_check(k, z, j0, j1)
        row = {"inputs": list(map(str, (k, z, j0, j1))),
               "actual": str(actual), "required": str(required),
               "residual": str(actual-required)}
        moments.append(row)
        if actual != required:
            failures.append(row)
    cert = {"schema": "physical-h-angle-reduction-rational-check-v1",
            "stencil_records": records, "moment_records": moments,
            "actual_checks": len(records)+len(moments),
            "required": "Every exact rational residual is zero",
            "failures": failures,
            "qualification": "Supporting finite checks only. L129 proves the "
                             "general identity, angle integration and corner "
                             "limits. No scalar numerical values are certified."}
    path = Path(__file__).with_name("h-angle-reduction-certificate.json")
    path.write_text(json.dumps(cert, indent=2)+"\n")
    print(f"Exact matrix checks: {len(records)}; moment checks: {len(moments)}")
    print(f"Actual: {len(failures)} failed residuals; required: 0")
    print(f"Full certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
