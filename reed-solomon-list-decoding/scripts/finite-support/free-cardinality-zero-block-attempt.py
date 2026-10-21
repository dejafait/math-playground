"""One capped full-variable proposal, with lossless model and exact rejection.

Run once. No optimization package, old witness, or restricted ansatz.
Exact source recipes are saved before the numerical run. A floating result
is never a feasibility or infeasibility certificate.
"""
import hashlib
import itertools
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np

BASE = Path(__file__).parent
PREFIX = BASE / "free-cardinality-zero-block-"
START = time.monotonic()
N = 65537**28 // 2**128 + 1
H = math.comb(1024, 68)
G = [math.comb(68, i)*math.comb(956, i) for i in range(69)]
CAP = dict(coordinates=1501000, scalar_pair_rows=4600000,
           contractions=69, matrices=2, coefficient_visits=20000000,
           array_bytes=2*2**30, output_bytes=512*2**20,
           exact_bits=262144, total_seconds=1800,
           numerical_seconds=600, sweeps=200)
R = dict(stage="starting", cap=CAP, coefficient_visits=0, failures=[],
         verdict="UNDECIDED", numerical_sweeps=0, reconstruction_count=0)


def path(suffix):
    return Path(str(PREFIX)+suffix)


def save():
    R["elapsed_seconds"] = time.monotonic()-START
    path("results.json").write_text(json.dumps(R, indent=2)+"\n")


def guard():
    if time.monotonic()-START > CAP["total_seconds"]:
        raise RuntimeError("total_seconds cap")
    if R["coefficient_visits"] > CAP["coefficient_visits"]:
        raise RuntimeError("coefficient_visits cap")


def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def beta(i, j, t, n):
    return sum((-1)**(u-t)*choose(u, t)*choose(n, u) *
               choose(n-u, i-u)*choose(n-u, j-u)
               for u in range(t, min(i, j)+1))


def enc(x):
    x = F(x)
    if max(abs(x.numerator).bit_length(), x.denominator.bit_length()) > CAP["exact_bits"]:
        raise RuntimeError("exact_bits cap")
    return [x.numerator, x.denominator]


def floorlog(x):
    x = F(x)
    e = x.numerator.bit_length()-x.denominator.bit_length()
    if x < (F(2)**e):
        e -= 1
    return e


def main():
    save()
    count = 1500625
    # columns: i,j,t,s,h,coordinate ID. The complete ordered lift is saved.
    orbit = np.empty((count, 6), dtype=np.int32)
    keys = [(0, i, i, 0) for i in range(69)]
    keymap = {k: i for i, k in enumerate(keys)}
    factors = []
    pos = 0
    forbidden = repeated = 0
    R["stage"] = "source_model"
    for i in range(69):
        for j in range(69):
            ts = list(range(max(0, i+j-68), min(i, j)+1))
            ss = list(range(max(0, i+j-956), min(i, j)+1))
            dt = [choose(i, t)*choose(68-i, j-t) for t in ts]
            ds = [choose(i, s)*choose(956-i, j-s) for s in ss]
            bw = [beta(i, j, t, 68) for t in ts]
            bv = [beta(i, j, s, 956) for s in ss]
            # Literal beta vs region counts; no old certificate is used.
            assert bw == [choose(68, i)*a for a in dt]
            assert bv == [choose(956, i)*a for a in ds]
            # Independent included-point counts in the four regions.
            assert dt == [choose(i, i-t)*choose(68-i, 68-i-j+t) for t in ts]
            assert ds == [choose(i, s)*choose(956-i, j-s) for s in ss]
            begin = pos
            for t in ts:
                for s in ss:
                    h = i+j-t-s
                    if any(0 < a < 5 for a in (i, j, h)):
                        q = 1
                        forbidden += 1
                    elif min(i, j, h) == 0:
                        a, b, c = sorted((i, j, h))
                        assert b == c and t-s == 0
                        q = b
                        repeated += 1
                    else:
                        k = (*sorted((i, j, h)), t-s)
                        if k not in keymap:
                            keymap[k] = len(keys)
                            keys.append(k)
                        q = keymap[k]
                    orbit[pos] = (i, j, t, s, h, q)
                    pos += 1
            factors.append(dict(i=i, j=j, t=ts, s=ss, D_t=dt, D_s=ds,
                                beta_w=bw, beta_v=bv, start=begin, end=pos))
        guard()
        if i % 16 == 0:
            R.update(constructed_through=i, constructed_orbits=pos)
            save()
            print("source row", i, "orbits", pos, flush=True)
    assert pos == count
    R["coefficient_visits"] += pos
    # Verify all six presentations for every class, not distance-only merging.
    presentation_checks = 0
    for q, (a, b, c, u) in enumerate(keys[69:], 69):
        for i, j, h in itertools.permutations((a, b, c)):
            assert (i+j-h+u) % 2 == 0
            t, s = (i+j-h+u)//2, (i+j-h-u)//2
            assert min(i-t, j-t, t, 68-i-j+t,
                       i-s, j-s, s, 956-i-j+s) >= 0
            assert keymap[(*sorted((i, j, h)), t-s)] == q
            presentation_checks += 1
    R["coefficient_visits"] += presentation_checks
    # Reconstruct each map entry via the atom-derived distances and invariant.
    for row in orbit:
        i, j, t, s, h, q = map(int, row)
        assert h == (i-t)+(j-s)
        if q >= 69:
            assert keys[q] == (*sorted((i, j, h)), t-s)
        elif q != 1:
            assert min(i, j, h) == 0 and q == max(i, j, h)
        else:
            assert any(0 < z < 5 for z in (i, j, h))
    R["coefficient_visits"] += count
    nv = len(keys)
    R.update(orbits=count, coordinates_before_quotient=count,
             quotient_coordinates=nv, free_coordinates_before_cardinality=nv-5,
             scalar_rows=3*count, pair_rows=68, pair_sign_rows=69,
             forbidden_orbits=forbidden, permitted_repetitions=repeated,
             source_presentation_checks=presentation_checks)
    assert count <= CAP["coordinates"] and 3*count+68+69 <= CAP["scalar_pair_rows"]
    np.savez_compressed(path("model.npz"), orbit=orbit,
                        keys=np.array(keys, dtype=np.int32))
    # p_i = 2^pe*x_i; distinct y = 2^ye*x_q. Fixed p0=1, forbidden=0.
    pe = floorlog(F(N, H))
    ye = 2*pe
    exponents = np.full(nv, ye, dtype=np.int32)
    exponents[:69] = pe
    exponents[0] = 0
    scale = np.exp2(exponents.astype(float))
    rho = math.ldexp(1., pe)
    # Same power-of-two diagonal congruence, then independent positive
    # scalar scaling of the two blocks; all fixed before iteration.
    de = [0]+[-max(0, floorlog(F(G[i])*F(2)**pe)) for i in range(1, 69)]
    e_row = floorlog(F(H)*F(2)**ye)
    objective_exp = -floorlog(N)
    pair_int = [[sum((-1)**h*choose(j, h)*choose(68-j, i-h) *
                     choose(956-j, i-h) for h in range(i+1))
                 for i in range(69)] for j in range(1, 69)]
    pair_exp = [-max(0, max(abs(a).bit_length()-1+int(exponents[i])
                            for i, a in enumerate(row) if a))
                for row in pair_int]
    Q = np.array([[math.ldexp(float(a), int(exponents[i])+pair_exp[j])
                   for i, a in enumerate(row)] for j, row in enumerate(pair_int)])
    pivots = [keymap[(i, i, i, i)] for i in range(5, 69)]
    # The i-th selected class occurs only in row i, with the sole
    # presentation t=i,s=0. Objective first eliminates p68.
    pivot_D = [choose(956-i, i) for i in range(5, 69)]
    assert all(x > 0 for x in pivot_D) and len(set(pivots)) == 64
    model = dict(parameters=dict(n=1024, w=68, v=956, d=10, N=N, H=H),
                 G=G, entries=factors, pair_integer_coefficients=pair_int,
                 pair_row_exponents=pair_exp, pair_variable_exponent=pe,
                 triple_variable_exponent=ye, diagonal_exponents=de,
                 included_block_exponent=0, excluded_block_exponent=pe,
                 contraction_row_exponent=-e_row, objective_exponent=objective_exp,
                 equality_pivots=[68]+pivots, pivot_D=pivot_D,
                 equality_rank_after_source_lift=65,
                 effective_free_dimension=nv-5-65,
                 scalar_recipe=["y", "p_i-y", "1+y-p_i-p_j"],
                 equality_recipe="sum D*y-N*p_i=0 for ALL 69 i",
                 algorithm="simultaneous product-cone residual gradient; diagonal row-l1 majorizer; step 1/2",
                 initialization="p_i=N/H on permitted nonzero pairs; y=(N/H)^2 on distinct permitted triples",
                 rounding="once: nearest 2^-40 in scaled nonpivot coordinates, ties to even",
                 limits=CAP)
    path("model.json").write_text(json.dumps(model, separators=(",", ":"))+"\n")
    R["stage"] = "model_saved_before_iteration"
    R["equality_rank_after_source_lift"] = 65
    R["effective_free_dimension"] = nv-70
    save()
    i, j, h, ids = (orbit[:, k] for k in (0, 1, 4, 5))
    entry = i*69+j
    dc = np.empty(count)
    cy = np.empty(count)
    ey = np.empty(count)
    ep = np.empty(count)
    for f in factors:
        a, b = f["i"], f["j"]
        p = f["start"]
        for at in f["D_t"]:
            for bs in f["D_s"]:
                d = at*bs
                dc[p] = math.ldexp(float(d), int(exponents[ids[p]])-e_row)
                z = G[a]*d
                cy[p] = math.ldexp(float(z), de[a]+de[b]+int(exponents[ids[p]]))
                ey[p] = math.ldexp(cy[p], pe)
                ep[p] = math.ldexp(float(z), de[a]+de[b]+pe+int(exponents[h[p]]))
                p += 1
    R["coefficient_visits"] += count
    # Scalar rows each receive a positive power-of-two row scaling.
    upper_exp = np.maximum(exponents[i], exponents[ids])
    ui = np.exp2(exponents[i]-upper_exp)
    uy = np.exp2(exponents[ids]-upper_exp)
    sy, si, sj = scale[ids], scale[i], scale[j]
    rhs = np.array([math.ldexp(float(N), int(e)-e_row) for e in exponents[:69]])
    obj = np.array([math.ldexp(float(g), int(exponents[k])+objective_exp)
                    for k, g in enumerate(G)])
    objrhs = math.ldexp(float(N), objective_exp)

    def bc(index, weights):
        return np.bincount(index, weights=weights, minlength=nv)

    # A diagonal majorizer of sum A^T A: each original scalar/equality
    # row contributes |a_q|*sum |a|. PSD negative-part projection is
    # nonexpansive in Frobenius norm; include every ordered matrix entry.
    pre = bc(ids, np.ones(count))
    pre += bc(i, ui*(ui+uy))+bc(ids, uy*(ui+uy))
    total = sy+si+sj
    pre += bc(ids, sy*total)+bc(i, si*total)+bc(j, sj*total)
    pre[:69] += (abs(Q)*abs(Q).sum(axis=1)[:, None]).sum(axis=0)
    pre[:69] += 1+abs(obj)*abs(obj).sum()
    sums = np.bincount(i, weights=abs(dc), minlength=69)+abs(rhs)
    pre += bc(ids, abs(dc)*sums[i])
    pre[:69] += abs(rhs)*sums
    for ac, pc in ((cy, None), (ey, ep)):
        rowsum = np.bincount(entry, weights=abs(ac)+(0 if pc is None else abs(pc)),
                              minlength=4761)
        pre += bc(ids, abs(ac)*rowsum[entry])
        if pc is not None:
            pre += bc(h, abs(pc)*rowsum[entry])
    pre = np.maximum(pre, 1e-300)
    assert np.isfinite(pre).all()
    x = np.full(nv, (float(F(N, H))**2)/math.ldexp(1., ye))
    x[:69] = float(F(N, H))/rho
    x[0], x[1:5] = 1., 0.
    np.savez_compressed(path("numerical-contract.npz"),
                        exponents=exponents, preconditioner=pre, initialization=x)
    # Conservative declared bound includes all named arrays, gradient
    # temporaries, bincounts, npz buffers and eigensolver work.
    declared = orbit.nbytes + 50*count*8 + 20*nv*8 + 64*2**20
    R["declared_live_array_bytes"] = int(declared)
    assert declared <= CAP["array_bytes"]
    assert all(np.isfinite(a).all() for a in (dc, cy, ey, ep, Q, rhs))
    R["stage"] = "numerical"
    save()
    ns = time.monotonic()
    log = []
    for sweep in range(1, 201):
        guard()
        y = x[ids]
        r0 = np.minimum(y, 0)
        ru = np.minimum(ui*x[i]-uy*y, 0)
        rl = np.minimum(1+sy*y-si*x[i]-sj*x[j], 0)
        grad = bc(ids, r0)-bc(ids, uy*ru)+bc(i, ui*ru)
        grad += bc(ids, sy*rl)-bc(i, si*rl)-bc(j, sj*rl)
        rp = np.minimum(Q@x[:69], 0)
        grad[:69] += Q.T@rp+np.minimum(x[:69], 0)
        rc = np.bincount(i, weights=dc*y, minlength=69)-rhs*x[:69]
        grad += bc(ids, dc*rc[i])
        grad[:69] -= rhs*rc
        ro = float(obj@x[:69]-objrhs)
        grad[:69] += obj*ro
        mins = []
        for family in (0, 1):
            vals = cy*y if family == 0 else ep*x[h]-ey*y
            a = np.bincount(entry, weights=vals, minlength=4761).reshape(69, 69)
            assert np.allclose(a, a.T, rtol=1e-10, atol=1e-12)
            a = (a+a.T)/2
            ev, vv = np.linalg.eigh(a)
            neg = (vv*np.minimum(ev, 0))@vv.T
            rr = neg.ravel()[entry]
            if family == 0:
                grad += bc(ids, cy*rr)
            else:
                grad += bc(h, ep*rr)-bc(ids, ey*rr)
            mins.append(float(ev[0]))
        record = dict(sweep=sweep, seconds=time.monotonic()-ns,
                      maximum_scaled_contraction_residual=float(max(abs(rc))),
                      scaled_objective_residual=ro,
                      minimum_scaled_scalar=float(min(r0.min(), ru.min(), rl.min())),
                      minimum_scaled_pair=float(rp.min()), minimum_block_eigenvalues=mins)
        log.append(record)
        x -= .5*grad/pre
        x[0], x[1:5] = 1., 0.
        assert np.isfinite(x).all()
        R["numerical_sweeps"] = sweep
        if sweep % 20 == 0 or time.monotonic()-ns >= 600:
            R["last_numerical_diagnostic"] = record
            save()
            print("sweep", sweep, "contraction residual", record["maximum_scaled_contraction_residual"],
                  "seconds", round(record["seconds"], 2), flush=True)
        if time.monotonic()-ns >= 600:
            break
    R["numerical_seconds"] = time.monotonic()-ns
    R["numerical_stop"] = "200 sweeps" if sweep == 200 else "600 seconds"
    path("iteration.json").write_text(json.dumps(log, indent=2)+"\n")
    np.savez_compressed(path("proposal.npz"), x=x)
    # One rational reconstruction, no scan or second proposal.
    R["stage"] = "exact_reconstruction"
    R["reconstruction_count"] = 1
    save()
    rounded = [int(round(float(z)*2**40)) for z in x]
    rounded[0] = 2**40
    for q in range(1, 5):
        rounded[q] = 0
    common_exp = min(ye, pe, 0)-40
    common_den = 2**(-common_exp)
    numerators = [z*2**(int(exponents[q])-40-common_exp)
                  for q, z in enumerate(rounded)]
    numerators[0] = common_den
    p = [F(numerators[q], common_den) for q in range(69)]
    p[68] = (N-sum(G[a]*p[a] for a in range(68)))/G[68]
    override = {68: p[68]}
    pivset = set(pivots)
    sums = [0]*69
    pivot_counts = [0]*69
    # Accumulate all nonpivot contraction coefficients at the single
    # power-of-two denominator. Pair68 overrides are handled explicitly.
    extras = [F(0)]*69
    for f in factors:
        a, off = f["i"], f["start"]
        for at in f["D_t"]:
            for bs in f["D_s"]:
                q = int(ids[off])
                d = at*bs
                if q in pivset:
                    assert q == pivots[a-5] and a >= 5
                    assert d == pivot_D[a-5]
                    pivot_counts[a] += 1
                elif q == 68:
                    extras[a] += d*p[68]
                else:
                    sums[a] += d*numerators[q]
                off += 1
        guard()
    R["coefficient_visits"] += count
    assert pivot_counts == [0]*5+[1]*64
    for a in range(5, 69):
        override[pivots[a-5]] = (N*p[a]-F(sums[a], common_den)-extras[a])/pivot_D[a-5]
    residuals = []
    for a in range(69):
        lhs = F(sums[a], common_den)+extras[a]
        if a >= 5:
            lhs += pivot_D[a-5]*override[pivots[a-5]]
        residuals.append(lhs-N*p[a])
    assert all(z == 0 for z in residuals)
    # This exact elimination has rank65: the objective p68 coefficient
    # is G68>0 and the other64 pivots occur in only their own rows.
    certificate = dict(common_denominator=common_den,
                       scaled_rounded_integers=rounded,
                       exact_overrides={str(q): enc(z) for q, z in override.items()},
                       all_69_contraction_residuals=[enc(z) for z in residuals],
                       pivot_counts=pivot_counts,
                       equality_rank=65,
                       scope="complete assignment; not a feasible certificate")
    path("reconstruction.json").write_text(json.dumps(certificate, separators=(",", ":"))+"\n")
    def val(q):
        return override[q] if q in override else F(numerators[q], common_den)
    # A single exact negative required scalar suffices to reject this
    # reconstructed point; omitted sign/PSD checks then prove nothing.
    bad = next((q for q in range(nv) if val(q) < 0), None)
    if bad is not None:
        positions = np.flatnonzero(ids == bad)
        assert len(positions)
        witness = orbit[int(positions[0])].tolist()
        R["exact_failure"] = dict(coordinate=bad, key=list(keys[bad]),
                                 ordered_orbit=witness, value=enc(val(bad)),
                                 required="y >= 0")
        R["verdict"] = "RECONSTRUCTED_POINT_REJECTED"
        R["remaining_validation"] = "other scalar/pair/PSD signs not certified; one exact violation suffices"
    else:
        R["verdict"] = "UNDECIDED_NONNEGATIVE_RECONSTRUCTION"
        R["remaining_validation"] = "full upper/lower/pair/PSD certification remains required"
    R["all_69_exact_contractions_zero"] = True
    R["max_saved_rational_bits"] = max(max(abs(z.numerator).bit_length(),
                                           z.denominator.bit_length()) for z in override.values())
    R["stage"] = "complete"
    R["output_bytes"] = sum(f.stat().st_size for f in BASE.glob("free-cardinality-zero-block-*") if f.is_file())
    assert R["output_bytes"] <= CAP["output_bytes"]
    guard()
    save()
    print(json.dumps({k: R[k] for k in ("verdict", "numerical_sweeps",
                     "numerical_seconds", "coefficient_visits", "output_bytes")}))
    print("Full evidence:", path("results.json"), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        R["failures"].append(repr(exc))
        R["stage"] = "stopped"
        save()
        print("STOP:", repr(exc), "evidence:", path("results.json"), flush=True)
        raise
