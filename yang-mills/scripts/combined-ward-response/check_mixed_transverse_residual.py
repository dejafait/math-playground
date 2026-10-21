"""Actual-stencil dual tests of R_0T; finite diagnostics, not a norm proof."""
from pathlib import Path
import json
import numpy as np
from haar_contraction import RelativeBox, gradient


def bump(t):
    value = np.zeros_like(t)
    mask = abs(t) < 1
    value[mask] = np.exp(-1/(1-t[mask]**2))
    return value


def check(n):
    box = RelativeBox(n)
    a = box.a
    vertices = -4+a*np.arange(1, n)
    edges = -4+a*(np.arange(n)+0.5)
    # Transverse envelope is wholly within the exact affine core.
    eta = bump(vertices/2)
    eta_edge = bump(edges/2)
    h = bump((vertices-1.25)/0.75)
    theta2, theta3 = np.pi/2, np.pi
    vphase2 = np.exp(1j*theta2*np.arange(1, n))
    ephase2 = np.exp(1j*theta2*(np.arange(n)+0.5))
    vphase3 = (-1.)**np.arange(1, n)
    phi = a**1.5*(eta*vphase2)[:, None, None]*(eta*vphase3)[None, :, None]*eta[None, None, :]
    y = [np.zeros(shape, dtype=complex) for shape in box.shapes]
    y[0] = np.broadcast_to(phi[None]/np.sqrt(n), box.shapes[0]).copy()
    x = [np.zeros(shape, dtype=complex) for shape in box.shapes]
    x[1] = (-1j*a**1.5/np.sqrt(n)*h[:, None, None, None]
            *(eta_edge*ephase2)[None, :, None, None]
            *(eta*vphase3)[None, None, :, None]*eta[None, None, None, :])
    # Evaluate the two generator pairings and the two actual probe forms.
    cy, cx = box.curl(y), box.curl(x)
    cky, ckx = box.curl(box.generator(y)), box.curl(box.generator(x))
    left = sum(np.vdot(cy[p], ckx[p]) for p in cy)/2
    right = sum(np.vdot(cky[p], cx[p]) for p in cy)/2
    qreal = box.probe_matrices([z.real for z in x])
    qimag = box.probe_matrices([z.imag for z in x])
    q3, q6 = [[r+1j*j for r, j in zip(qr, qi)] for qr, qi in zip(qreal, qimag)]
    triplet = sum(np.vdot(yv, qv) for yv, qv in zip(y, q3))
    shear = sum(np.vdot(yv, qv) for yv, qv in zip(y, q6))
    pair = left+right-triplet-shear
    energy_y = sum(float(np.vdot(gradient(phi[None], ax), gradient(phi[None], ax)).real) for ax in (1, 2, 3))
    # The full relative Hodge energy for a single transverse component.
    energy_x = 0.
    for axis in range(4):
        dx = -np.diff(x[1], axis=axis) if axis == 1 else gradient(x[1], axis)
        energy_x += float(np.vdot(dx, dx).real)
    ratio = abs(pair)/np.sqrt(energy_y*energy_x)
    # Full residual implementation independently verifies both pairings.
    residual_x = [r+1j*j for r, j in zip(box.residual([z.real for z in x]),
                                        box.residual([z.imag for z in x]))]
    direct = sum(np.vdot(yv, rv) for yv, rv in zip(y, residual_x))
    defect = abs(pair-direct)
    tolerance = 1e-10*max(1., abs(pair), abs(direct))
    predicted = (np.sqrt(2)/8*(a*np.sum(vertices*h))*(a*np.sum(eta**2))**3)
    return dict(N=n, a=a, dual_ratio=float(ratio), a_times_dual_ratio=float(a*ratio),
                a_times_pair_real=float(a*pair.real), a_times_pair_imag=float(a*pair.imag),
                leading_riemann_prediction=float(predicted),
                energy_y=energy_y, energy_x=energy_x,
                generator_pairings=[dict(real=float(z.real), imag=float(z.imag)) for z in (left, right)],
                Q3_pair=dict(real=float(triplet.real), imag=float(triplet.imag)),
                Q6_pair=dict(real=float(shear.real), imag=float(shear.imag)),
                decomposition_defect=float(defect), required_defect=float(tolerance),
                passed=bool(defect <= tolerance))


def main():
    rows = [check(n) for n in (24, 32, 40, 48)]
    failures = [r for r in rows if not r['passed']]
    path = Path(__file__).with_name('mixed-transverse-residual-certificate.json')
    certificate = dict(scope='Actual compact oscillatory dual inputs for R_0T',
                       diagnostics=rows, failures=failures,
                       actual_bound='L066 proves c/a <= ||R_0T|| <= C/a; displayed finite dual ratios are diagnostics only',
                       required_bound='O(1) proposed; test a nonzero limit of a times the dual ratio',
                       qualifications='Binary64 actual-stencil diagnostics, all generator outputs, Q3/Q6 and relative endpoints retained. No certified norm or signed-response conclusion.')
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    for row in rows:
        print(f'N={row["N"]}: ratio={row["dual_ratio"]:.7g}, a*ratio={row["a_times_dual_ratio"]:.7g}, a*pair={row["a_times_pair_real"]:.7g}, prediction={row["leading_riemann_prediction"]:.7g}, defect={row["decomposition_defect"]:.3g} <= {row["required_defect"]:.3g}')
    print('Actual/required analytic bound: Theta(1/a) in L066 / proposed O(1), obstructed.')
    print('Displayed finite ratios are diagnostic lower bounds, not the asymptotic proof.')
    print('Failures:', len(failures))
    print('Certificate:', path)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
