"""Floating necessary-slice/design screen. No continuous or optimality proof.

Save all tested parameters and slice minima; never treat sampled extrema as
bounds. The exact rational family and finite-n transfer remain in L673.
"""
import json
import heapq
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

d, U, r = 1.25, 121/64, 0.45
c = 10*np.pi/27
angles = np.linspace(0, 2*np.pi, 1024, endpoint=False)
u = np.exp(1j*angles)


def series(v):
    return (1+(1/v-1)*np.log(1-v)).real


def primitive(s, v):
    return v*np.log(s*s+v*v)/2-v+s*np.arctan2(v, s)


def kernel(z):
    s, y = np.abs(z.real), z.imag
    return (10/27)*(2*r*(np.log(r)-1)
                   -primitive(s, y+r)+primitive(s, y-r))


def envelope(z):
    a = -d+z
    vals = (np.log(d/np.abs(a))[..., None]+series(u/a[..., None])
            -series(-u/d)+series(-d/(U*u))-series(a[..., None]/(U*u)))
    idx = np.argmax(vals, axis=-1)
    best = np.take_along_axis(vals, idx[..., None], axis=-1)[..., 0]
    return best+kernel(z)-c*z.real, idx


ys = np.linspace(0, .44, 89)
fractions = np.linspace(.002, .998, 160)
ss = (d-np.sqrt(1-ys*ys))[:, None]*fractions
zz = ss+1j*ys[:, None]
base = np.empty(zz.shape)
angle_idx = np.empty(zz.shape, int)
for j in range(len(ys)):
    base[j], angle_idx[j] = envelope(zz[j])
basis2, basis4 = (zz**2).real, (zz**4).real
rows = []


def test(g2, g4):
    vals = base-g2*basis2-g4*basis4
    idx = np.argmin(vals, axis=1)
    mins = vals[np.arange(len(ys)), idx]
    witness = int(np.argmax(mins))
    row = dict(gamma2=float(g2), gamma4=float(g4),
               sampled_slice_barrier=float(mins[witness]),
               worst_y=float(ys[witness]),
               worst_s=float(ss[witness, idx[witness]]))
    rows.append(row)
    return row, idx, mins


for g2 in np.linspace(-2, 12, 71):
    for g4 in np.linspace(-40, 160, 101):
        test(g2, g4)
coarse = min(rows, key=lambda row: row['sampled_slice_barrier'])
for g2 in np.linspace(coarse['gamma2']-.3, coarse['gamma2']+.3, 61):
    for g4 in np.linspace(coarse['gamma4']-3, coarse['gamma4']+3, 61):
        test(g2, g4)
best = min(rows, key=lambda row: row['sampled_slice_barrier'])
_, idx, mins = test(best['gamma2'], best['gamma4'])
report = dict(status='FLOATING DIAGNOSTIC ONLY; NO BOUND OR GLOBAL OPTIMALITY',
              required=-.01, best=best, failures=[], rows=rows,
              ys=ys.tolist(), ss=ss.tolist(), base=base.tolist(),
              angle_indices=angle_idx.tolist(), angular_count=len(u),
              best_slices=dict(s=ss[np.arange(len(ys)), idx].tolist(),
                               minima=mins.tolist()),
              qualifications='Slice minima can jump between disconnected components; '
              'no contour or finite-n witness follows. Search boxes are bounded.')
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(report, indent=2)+'\n')
print('Best sampled slice barrier:', best)
print('Required below -0.01 on a complete continuous contour; failures: []')
print('Full diagnostic:', path)

# A second test keeps connectivity: paths in the upper half-plane must
# connect negative and positive real axes above the removed node segment.
sx = np.arange(-60, 51)/100
yy = np.arange(121)/100
grid = sx[None, :]+1j*yy[:, None]
valid = (np.abs(-d+grid)>1.000001)
valid[:, 60] &= yy > r
valid[0, 60] = False
gb = np.full(grid.shape, np.inf)
gi = np.full(grid.shape, -1, int)
for j in range(len(yy)):
    gb[j, valid[j]], gi[j, valid[j]] = envelope(grid[j, valid[j]])
g2basis, g4basis = (grid**2).real, (grid**4).real
height, width = grid.shape


def connected(g2, g4):
    vals = gb-g2*g2basis-g4*g4basis
    distances = np.full(grid.size, np.inf)
    parent = np.full(grid.size, -1, int)
    heap = []
    for col in range(60):
        distances[col] = vals[0, col]
        heapq.heappush(heap, (distances[col], col))
    target = None
    while heap:
        cost, ix = heapq.heappop(heap)
        if cost > distances[ix]:
            continue
        row, col = divmod(ix, width)
        if row == 0 and col > 60:
            target = ix
            break
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = row+dr, col+dc
            if not (0 <= nr < height and 0 <= nc < width and valid[nr, nc]):
                continue
            jx = nr*width+nc
            newcost = max(cost, vals[nr, nc])
            if newcost < distances[jx]:
                distances[jx], parent[jx] = newcost, ix
                heapq.heappush(heap, (newcost, jx))
    if target is None:
        return dict(gamma2=g2, gamma4=g4, sampled_path_max=None, path=[])
    sequence = []
    while target >= 0:
        row, col = divmod(target, width)
        sequence.append([int(row), int(col)])
        target = int(parent[target])
    return dict(gamma2=float(g2), gamma4=float(g4),
                sampled_path_max=float(cost), path=sequence[::-1])


connected_rows = []
for g2 in np.linspace(0, 4, 21):
    for g4 in np.linspace(-5, 35, 21):
        connected_rows.append(connected(g2, g4))
best_path = min(connected_rows, key=lambda row: row['sampled_path_max'])
for g2 in np.linspace(best_path['gamma2']-.2, best_path['gamma2']+.2, 21):
    for g4 in np.linspace(best_path['gamma4']-2, best_path['gamma4']+2, 21):
        connected_rows.append(connected(g2, g4))
best_path = min(connected_rows, key=lambda row: row['sampled_path_max'])
report['connected'] = dict(sx=sx.tolist(), yy=yy.tolist(),
    base=[[float(v) if np.isfinite(v) else None for v in row] for row in gb],
    valid=valid.tolist(), angle_indices=gi.tolist(), rows=connected_rows,
    best=best_path, qualifications='4-neighbor grid, bounded parameter box; '
    'neither interpolation nor all-angle coverage nor optimality is certified.')
path.write_text(json.dumps(report, indent=2)+'\n')
print('Connected path best:', {k:v for k,v in best_path.items() if k != 'path'})
print('Required below -0.01 continuously; no global optimality claimed. Full diagnostic:', path)

# Refine the selected neighborhood and spatial mesh. This is still design,
# not an error enclosure; retain every earlier failed or inconclusive screen.
sx = np.arange(-100, 161)/400
yy = np.arange(281)/400
grid = sx[None, :]+1j*yy[:, None]
valid = np.abs(-d+grid)>1.000001
axis_col = 100
valid[:, axis_col] &= yy > r
gb = np.full(grid.shape, np.inf)
gi = np.full(grid.shape, -1, int)
for j in range(len(yy)):
    gb[j, valid[j]], gi[j, valid[j]] = envelope(grid[j, valid[j]])
g2basis, g4basis = (grid**2).real, (grid**4).real
height, width = grid.shape


def fine_connected(g2, g4):
    vals = gb-g2*g2basis-g4*g4basis
    distances = np.full(grid.size, np.inf)
    parent = np.full(grid.size, -1, int)
    heap = []
    for col in range(axis_col):
        distances[col] = vals[0, col]
        heapq.heappush(heap, (distances[col], col))
    target = None
    while heap:
        cost, ix = heapq.heappop(heap)
        if cost > distances[ix]:
            continue
        row, col = divmod(ix, width)
        if row == 0 and col > axis_col:
            target = ix
            break
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = row+dr, col+dc
            if not (0 <= nr < height and 0 <= nc < width and valid[nr, nc]):
                continue
            jx = nr*width+nc
            newcost = max(cost, vals[nr, nc])
            if newcost < distances[jx]:
                distances[jx], parent[jx] = newcost, ix
                heapq.heappush(heap, (newcost, jx))
    if target is None:
        return dict(gamma2=g2, gamma4=g4, sampled_path_max=None, path=[])
    sequence = []
    while target >= 0:
        row, col = divmod(target, width)
        sequence.append([int(row), int(col)])
        target = int(parent[target])
    return dict(gamma2=float(g2), gamma4=float(g4),
                sampled_path_max=float(cost), path=sequence[::-1])


fine_rows = []
for g2 in np.linspace(best_path['gamma2']-.1, best_path['gamma2']+.1, 9):
    for g4 in np.linspace(best_path['gamma4']-.6, best_path['gamma4']+.6, 9):
        fine_rows.append(fine_connected(g2, g4))
fine_best = min(fine_rows, key=lambda row: row['sampled_path_max'])
report['fine_connected'] = dict(sx=sx.tolist(), yy=yy.tolist(),
    base=[[float(v) if np.isfinite(v) else None for v in row] for row in gb],
    valid=valid.tolist(), angle_indices=gi.tolist(), rows=fine_rows,
    best=fine_best, qualifications='Local parameter search, spatial step 1/400; '
    'no continuous coverage or global optimality is certified.')

# Check the selected path at intermediate points and twice as many angles.
# This diagnostic checks implementation consistency, not a rigorous supremum.
indices = fine_best['path']
vertices = np.array([grid[j, k] for j, k in indices])
points = []
for a, b in zip(vertices[:-1], vertices[1:]):
    points.extend(a+(b-a)*np.arange(8)/8)
points.append(vertices[-1])
points = np.array(points)
angles = np.linspace(0, 2*np.pi, 2048, endpoint=False)
u = np.exp(1j*angles)
dense_values = []
dense_angle_indices = []
for start in range(0, len(points), 100):
    block = points[start:start+100]
    bv, ai = envelope(block)
    dense_values.extend(bv-fine_best['gamma2']*(block**2).real
                        -fine_best['gamma4']*(block**4).real)
    dense_angle_indices.extend(ai)
peak = int(np.argmax(dense_values))
report['selected_path_dense_check'] = dict(
    angular_count=2048, subdivisions_per_edge=8,
    points=[[float(z.real), float(z.imag)] for z in points],
    values=[float(v) for v in dense_values],
    angle_indices=[int(v) for v in dense_angle_indices],
    sampled_max=float(dense_values[peak]),
    witness=dict(z=[float(points[peak].real), float(points[peak].imag)],
                 angle=float(angles[dense_angle_indices[peak]])),
    threshold_pass=bool(dense_values[peak]<-.01))

# Exact geometric checks for the selected polygon only. They do not bound E.
exact_vertices = [(Q(col-100, 400), Q(row, 400)) for row, col in indices]
minimum_pole_distance2 = None
geometry_failures = []
for (s1, y1), (s2, y2) in zip(exact_vertices[:-1], exact_vertices[1:]):
    if abs(s1-s2)+abs(y1-y2) != Q(1, 400):
        geometry_failures.append('non-neighbor edge')
    # Closest point on a horizontal/vertical segment to the pole disk center d.
    if y1 == y2:
        nearest_s = min(max(Q(5, 4), min(s1, s2)), max(s1, s2))
        dist2 = (nearest_s-Q(5, 4))**2+y1*y1
    else:
        nearest_y = min(max(Q(0), min(y1, y2)), max(y1, y2))
        dist2 = (s1-Q(5, 4))**2+nearest_y*nearest_y
    minimum_pole_distance2 = (dist2 if minimum_pole_distance2 is None
                              else min(minimum_pole_distance2, dist2))
    if (s1 <= 0 <= s2 or s2 <= 0 <= s1) and min(y1, y2) <= Q(9, 20):
        geometry_failures.append('edge meets limiting node segment')
if minimum_pole_distance2 <= 1:
    geometry_failures.append('edge enters pole disk')
if len(set(exact_vertices)) != len(exact_vertices):
    geometry_failures.append('repeated vertex')
if not (exact_vertices[0][0] < 0 < exact_vertices[-1][0]
        and exact_vertices[0][1] == exact_vertices[-1][1] == 0
        and all(y > 0 for _, y in exact_vertices[1:-1])):
    geometry_failures.append('axis endpoints/interior mismatch')
report['selected_path_geometry'] = dict(
    status='Exact rational polygon geometry only; no exponent enclosure',
    vertex_count=len(exact_vertices),
    minimum_pole_distance_squared=str(minimum_pole_distance2),
    required_pole_distance_squared='>1', failures=geometry_failures)
report['failures'].append('No tested connected quartic contour reaches the required -0.01.')
report['failures'].extend(geometry_failures)
report['summary'] = dict(
    initial_slice_parameter_rows=len(rows),
    coarse_and_refined_connected_parameter_rows=len(connected_rows),
    fine_connected_parameter_rows=len(fine_rows),
    required_continuous_max=-.01,
    best_fine_sampled_max=fine_best['sampled_path_max'],
    dense_selected_path_sampled_max=float(dense_values[peak]),
    dense_threshold_deficit=float(dense_values[peak]+.01),
    selected_gamma2=fine_best['gamma2'], selected_gamma4=fine_best['gamma4'],
    geometry_failures=geometry_failures,
    conclusion='No passing design found; global quartic optimum and cone target unresolved.')
path.write_text(json.dumps(report, indent=2)+'\n')
print('Fine connected best:', {k:v for k,v in fine_best.items() if k != 'path'})
print('Dense selected-path sampled maximum:', float(dense_values[peak]), '; required < -0.01')
print('Failures:', report['failures'])
print('Exact selected-path geometry failures:', geometry_failures)
print('Full diagnostic:', path)
