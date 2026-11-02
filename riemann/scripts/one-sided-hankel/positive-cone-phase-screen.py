"""Bounded floating design for a sign-compatible interpolation witness.

The node/sign and remainder arguments must be proved separately. This
screen certifies neither a continuous bound nor the 1/100 discriminator.
"""
import json
from pathlib import Path
import numpy as np

d, U, r = 1.25, 121/64, 0.45
c = 10*np.pi/27


def primitive(s, v):
    if s == 0:
        return v*np.log(abs(v))-v
    return v*np.log(s*s+v*v)/2-v+s*np.arctan(v/s)


def kernel(z):
    s, y = abs(z.real), z.imag
    return (10/27)*(2*r*(np.log(r)-1)
                   -primitive(s, y+r)+primitive(s, y-r))


def series(v):
    total = np.zeros(v.shape)
    power = np.ones(v.shape, complex)
    for k in range(1, 201):
        power *= v
        total += power.real/(k*(k+1))
    return total


angles = np.linspace(0, 2*np.pi, 1024, endpoint=False)
u = np.exp(1j*angles)
cache = {}


def profile(z):
    if z not in cache:
        a = -d+z
        f = (np.log(d/abs(a))+series(u/a)-series(-u/d)
             +series(-d/(U*u))-series(a/(U*u)))
        index = int(np.argmax(f))
        cache[z] = (float(f[index]+kernel(z)-c*z.real), index)
    return cache[z]


rows = []
polynomial_rows = []


def minimax_even(contour, base, degree):
    """Small log-barrier design only; no optimization certificate."""
    zz = np.array(contour)/0.5
    basis = np.array([(zz**(2*j)).real for j in range(1, degree+1)]).T
    design = np.column_stack((-basis, np.ones(len(base))))
    state = np.zeros(degree+1)
    state[-1] = max(base)+1
    objective = np.zeros(degree+1)
    objective[-1] = 1
    issues = []
    for mu in (0.1, 0.02, 0.004, 0.0008, 0.00016, 0.000032, 0.0000064, 0.00000128, 0.000000256):
        for _ in range(60):
            slack = design@state-base
            gradient = objective-mu*(design.T@(1/slack))
            hessian = mu*((design/slack[:, None]).T@(design/slack[:, None]))
            direction = np.linalg.solve(hessian, -gradient)
            if -gradient@direction < 1e-13:
                break
            changes = design@direction
            negative = changes < 0
            step = min(1, 0.99*np.min(-slack[negative]/changes[negative])) if np.any(negative) else 1
            before = state[-1]-mu*np.sum(np.log(slack))
            while step > 1e-12:
                candidate = state+step*direction
                after_slack = design@candidate-base
                after = candidate[-1]-mu*np.sum(np.log(after_slack))
                if after <= before+0.01*step*(gradient@direction):
                    state = candidate
                    break
                step *= 0.5
            if step <= 1e-12:
                issues.append("line search floor")
                break
    values = base+basis@state[:-1]
    index = int(np.argmax(values))
    return dict(even_degree=2*degree, coefficients_in_z_over_half=state[:-1].tolist(),
                sampled_max=float(values[index]),
                witness=[contour[index].real, contour[index].imag,
                         float(angles[profile(contour[index])[1]])], issues=issues)


for left in (0.06, 0.09):
    for right in (0.025, 0.035, 0.045, 0.06, 0.09):
        contour = ([complex(-left, y) for y in np.linspace(0, 0.5, 101)]
                   + [complex(right, y) for y in np.linspace(0, 0.5, 101)]
                   + [complex(s, 0.5) for s in np.linspace(-left, right, 31)])
        base = np.array([profile(z)[0] for z in contour])
        for gamma in (0, 0.2, 0.4, 0.6, 0.8):
            values = [profile(z)[0]-gamma*(z*z).real for z in contour]
            index = int(np.argmax(values))
            z = contour[index]
            rows.append(dict(left=left, right=right, height=0.5, gamma=gamma,
                             sampled_max=values[index],
                             witness=[z.real, z.imag, float(angles[profile(z)[1]])]))
        for degree in (1, 2, 3, 4):
            candidate = minimax_even(contour, base, degree)
            candidate.update(left=left, right=right, height=0.5)
            polynomial_rows.append(candidate)

best = min(rows, key=lambda row: row["sampled_max"])
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(dict(
    status="FLOATING DESIGN ONLY", phase_center=c,
    target_required=-0.01, rows=rows, best=best,
    polynomial_rows=polynomial_rows,
    best_even_polynomial=min(polynomial_rows, key=lambda row: row["sampled_max"]),
    point_at_old_right=profile(complex(0.09, 0))[0],
    failures=[]), indent=2)+"\n")
print(f"Best sampled contour: {best}")
print(f"Old right side at y=0: {profile(complex(0.09, 0))[0]}")
print(f'Best sampled even polynomial: {min(polynomial_rows, key=lambda row: row["sampled_max"])}')
print(f"Required: <= -0.01 with complete continuous enclosure. Full diagnostic: {path}")
