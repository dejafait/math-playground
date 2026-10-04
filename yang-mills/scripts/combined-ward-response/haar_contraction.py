"""L011's isolated coordinate-Haar contraction, not its full coefficient.

The dense diagnostic reuses L017's rational one-site sample (not L008's
smooth displacement). The matrix-free diagnostic uses L008's actual smooth
displacement at an admitted mesh. Its randomized traces have sampling
errors and do not prove an ultraviolet asymptotic or an interacting bound.
Only NumPy is required. Run with PYTHONDONTWRITEBYTECODE=1 and one BLAS
thread; --samples controls the bounded original-probe diagnostic.
"""

import argparse
import json
import runpy
from itertools import combinations
from pathlib import Path

import numpy as np


PLANES = tuple(combinations(range(4), 2))


def take(x, axis, begin, end):
    slices = [slice(None)] * 4
    slices[axis] = slice(begin, end)
    return x[tuple(slices)]


def gradient(x, axis):
    """Pinned vertex -> edge incidence, without a factor 1/a."""
    pads = [(0, 0)] * 4
    pads[axis] = (1, 1)
    return np.diff(np.pad(x, pads), axis=axis)


def gradient_adj(x, axis):
    return -np.diff(x, axis=axis)


def average(x, axis):
    return (take(x, axis, 0, -1) + take(x, axis, 1, None)) / 2


def average_adj(x, axis):
    pads = [(0, 0)] * 4
    pads[axis] = (1, 1)
    padded = np.pad(x, pads)
    return (take(padded, axis, 0, -1) + take(padded, axis, 1, None)) / 2


def central(x, axis, a):
    pads = [(0, 0)] * 4
    pads[axis] = (1, 1)
    padded = np.pad(x, pads)
    return (take(padded, axis, 2, None) - take(padded, axis, 0, -2)) / (2 * a)


def dst(x, axis):
    """Orthonormal DST-I on the N-1 relative vertex entries."""
    n = x.shape[axis] + 1
    shape = list(x.shape)
    shape[axis] = 2 * n
    extended = np.zeros(shape)
    slices = [slice(None)] * 4
    slices[axis] = slice(1, n)
    extended[tuple(slices)] = x
    slices[axis] = slice(n + 1, 2 * n)
    extended[tuple(slices)] = -np.flip(x, axis=axis)
    transformed = np.fft.rfft(extended, axis=axis)
    return -take(transformed.imag, axis, 1, n) / np.sqrt(2 * n)


def dct(x, axis, inverse=False):
    """Orthonormal edge cosine transform, types II and III."""
    n = x.shape[axis]
    shape = [1] * 4
    shape[axis] = n
    phase = np.exp(1j * np.pi * np.arange(n) / (2 * n)).reshape(shape)
    slices = [slice(None)] * 4
    slices[axis] = 0
    if not inverse:
        extended = np.concatenate((x, np.flip(x, axis=axis)), axis=axis)
        result = (take(np.fft.rfft(extended, axis=axis), axis, 0, n)
                  * phase.conj()).real / np.sqrt(2 * n)
        result[tuple(slices)] /= np.sqrt(2)
        return result
    spectrum_shape = list(x.shape)
    spectrum_shape[axis] = n + 1
    spectrum = np.zeros(spectrum_shape, dtype=complex)
    nonzero = [slice(None)] * 4
    nonzero[axis] = slice(0, n)
    spectrum[tuple(nonzero)] = np.sqrt(2 * n) * phase * x
    spectrum[tuple(slices)] *= np.sqrt(2)
    return take(np.fft.irfft(spectrum, n=2 * n, axis=axis), axis, 0, n)


def rho(x):
    def bump(t):
        result = np.zeros_like(t)
        active = t > 0
        result[active] = np.exp(-1 / t[active])
        return result
    first, second = bump(9 - x*x), bump(x*x - 25/4)
    return first / (first + second)


class RelativeBox:
    def __init__(self, n, sample=False):
        self.n, self.a, self.tau = n, 8/n, 1/16
        self.shapes = [tuple(n if r == mu else n-1 for r in range(4))
                       for mu in range(4)]
        self.vertex_shape = (n-1,) * 4
        self.lambdas = []
        for mu in range(4):
            value = np.zeros(self.shapes[mu])
            for axis in range(4):
                modes = np.arange(n) if axis == mu else np.arange(1, n)
                shape = [1] * 4
                shape[axis] = len(modes)
                value += (4 * np.sin(np.pi*modes/(2*n))**2).reshape(shape)
            self.lambdas.append(value)
        if sample:
            assert n == 4
            self.u = [np.zeros(self.vertex_shape) for _ in range(4)]
            for value, field in zip((2/3, -1/2, 3/5, 4/7), self.u):
                field[(1, 1, 1, 1)] = value
        else:
            points = -4 + self.a * np.arange(1, n)
            cutoff = rho(points)
            coordinate = points * cutoff
            derivative = (((points+self.a)*rho(points+self.a)
                           - (points-self.a)*rho(points-self.a)) / (2*self.a))
            self.u = []
            for mu, partner, sign in ((0, 2, 1), (1, 3, 1),
                                      (2, 0, -1), (3, 1, -1)):
                factors = [coordinate if r == mu else derivative if r == partner
                           else cutoff for r in range(4)]
                value = np.ones(self.vertex_shape) * sign
                for axis, factor in enumerate(factors):
                    shape = [1] * 4
                    shape[axis] = n-1
                    value *= factor.reshape(shape)
                self.u.append(value)
        self.w = [central(self.u[mu], mu, self.a) for mu in range(4)]
        self.s = {(mu, nu): central(self.u[nu], mu, self.a)
                  + central(self.u[mu], nu, self.a) for mu, nu in PLANES}
        if not sample:
            assert np.max(np.abs(sum(self.w))) < 2e-13
        self.triplet_weights = {
            (mu, nu): average_adj(average_adj(self.w[mu]+self.w[nu], mu), nu)
            for mu, nu in PLANES}
        if not sample:
            active = np.zeros(self.vertex_shape, dtype=bool)
            for field in [*self.u, *self.w, *self.s.values()]:
                active |= field != 0
            positions = np.nonzero(active)
            self.support_indices = [[int(p.min()+1), int(p.max()+1)] for p in positions]
            assert all(lo >= 2 and hi <= n-2 for lo, hi in self.support_indices), (
                "Mesh is not admitted: an active clover stencil touches a box face")

    def zeros(self):
        return [np.zeros(shape) for shape in self.shapes]

    @staticmethod
    def dot(x, y):
        return sum(float(np.vdot(left, right)) for left, right in zip(x, y))

    def spectral(self, fields, power=0, time=0):
        result = []
        for mu, field in enumerate(fields):
            value = field
            for axis in range(4):
                value = dct(value, axis) if axis == mu else dst(value, axis)
            value *= self.lambdas[mu]**power
            if time:
                value *= np.exp(-time * self.lambdas[mu] / self.a**2)
            for axis in reversed(range(4)):
                value = dct(value, axis, inverse=True) if axis == mu else dst(value, axis)
            result.append(value)
        return result

    @staticmethod
    def curl(x):
        return {(mu, nu): gradient(x[nu], mu) - gradient(x[mu], nu)
                for mu, nu in PLANES}

    def curl_adj(self, curvature):
        result = self.zeros()
        for (mu, nu), value in curvature.items():
            result[nu] += gradient_adj(value, mu)
            result[mu] -= gradient_adj(value, nu)
        return result

    @staticmethod
    def clovers(curvature):
        return {(mu, nu): average(average(value, mu), nu)
                for (mu, nu), value in curvature.items()}

    @staticmethod
    def ordered(curvature, mu, nu):
        return curvature[mu, nu] if mu < nu else -curvature[nu, mu]

    def probe_matrices(self, x, curvature=None, bars=None):
        curvature = self.curl(x) if curvature is None else curvature
        bars = self.clovers(curvature) if bars is None else bars
        triplet = self.curl_adj({p: self.triplet_weights[p] * curvature[p] for p in PLANES})
        shear_bars = {p: np.zeros(self.vertex_shape) for p in PLANES}
        for mu, nu in PLANES:
            for alpha in range(4):
                if alpha in (mu, nu):
                    continue
                left, right = tuple(sorted((mu, alpha))), tuple(sorted((nu, alpha)))
                ls, rs = (1 if mu < alpha else -1), (1 if nu < alpha else -1)
                weight = self.s[mu, nu] * ls * rs / 2
                shear_bars[left] += weight * bars[right]
                shear_bars[right] += weight * bars[left]
        shear = self.curl_adj({(mu, nu): average_adj(average_adj(value, mu), nu)
                               for (mu, nu), value in shear_bars.items()})
        return triplet, shear

    def generator(self, x, bars=None):
        bars = self.clovers(self.curl(x)) if bars is None else bars
        result = []
        for nu in range(4):
            value = sum(self.u[rho] * self.ordered(bars, rho, nu)
                        for rho in range(4) if rho != nu)
            result.append(average_adj(value, nu) / self.a)
        return result

    def generator_adj(self, x):
        bars = {p: np.zeros(self.vertex_shape) for p in PLANES}
        for nu in range(4):
            value = average(x[nu], nu) / self.a
            for rho in range(4):
                if rho != nu:
                    plane = tuple(sorted((rho, nu)))
                    bars[plane] += (1 if rho < nu else -1) * self.u[rho] * value
        return self.curl_adj({(mu, nu): average_adj(average_adj(value, mu), nu)
                              for (mu, nu), value in bars.items()})

    def residual(self, x):
        curvature = self.curl(x)
        bars = self.clovers(curvature)
        q3, q6 = self.probe_matrices(x, curvature, bars)
        lk = self.curl_adj(self.curl(self.generator(x, bars)))
        ktl = self.generator_adj(self.curl_adj(curvature))
        return [(left+right)/2 - first-second
                for left, right, first, second in zip(lk, ktl, q3, q6)]

    def path(self, x, omitted):
        value = np.cumsum(x, axis=0)[:-1].copy()
        value[omitted:] -= np.sum(x, axis=0)
        return value

    def path_adj(self, x, omitted):
        value = np.concatenate((np.flip(np.cumsum(np.flip(x, axis=0), axis=0), axis=0),
                                np.zeros((1, *x.shape[1:]))), axis=0)
        value -= np.sum(x[omitted:], axis=0)
        return value

    def retract(self, x, omitted):
        potential = self.path(x[0], omitted)
        return [value - gradient(potential, mu) for mu, value in enumerate(x)]

    def gauge_metric(self, x, omitted):
        value = self.retract(x, omitted)
        divergence = sum(gradient_adj(field, mu) for mu, field in enumerate(value))
        value[0] -= self.path_adj(divergence, omitted)
        return value


def dense_check():
    reference = runpy.run_path(str(Path(__file__).parents[1] / "forest-ward/check_free.py"))
    box = RelativeBox(4, sample=True)
    edges, index = reference["EDGES"], reference["INDEX"]
    size = len(edges)

    def unpack(vector):
        fields = box.zeros()
        for mu, v in edges:
            location = tuple(v[r] if r == mu else v[r]-1 for r in range(4))
            fields[mu][location] = vector[index[mu, v]]
        return fields

    def pack(fields):
        return np.array([fields[mu][tuple(v[r] if r == mu else v[r]-1 for r in range(4))]
                         for mu, v in edges])

    rng = np.random.default_rng(7104)
    x, y = rng.normal(size=(2, size))
    fx, fy = unpack(x), unpack(y)
    checks = [np.max(np.abs(pack(box.generator(fx)) - reference["K"] @ x)),
              np.max(np.abs(pack(box.generator_adj(fx)) - reference["K"].T @ x)),
              np.max(np.abs(pack(box.spectral(fx, power=-1)) - reference["SIGMA"] @ x)),
              np.max(np.abs(pack(box.spectral(fx, time=box.tau)) - reference["HODGE_HEAT"] @ x))]
    for actual, expected in zip(box.probe_matrices(fx), reference["Q"]):
        checks.append(np.max(np.abs(pack(actual) - expected @ x)))
    residual = ((reference["L"] @ reference["K"]
                 + reference["K"].T @ reference["L"])/2
                - sum(reference["Q"]))
    checks.append(np.max(np.abs(pack(box.residual(fx)) - residual @ x)))
    assert max(checks) < 3e-12

    dense_values = []
    sigma = reference["SIGMA"]
    for omitted in (3, 2):
        remaining = [j for j, (mu, v) in enumerate(edges) if mu != 0 or v[0] == omitted]
        forest = set(range(size)) - set(remaining)
        retracted = box.retract(fx, omitted)
        assert np.max(np.abs(pack(retracted)[list(forest)])) < 3e-15
        assert np.max(np.abs(reference["C"] @ (pack(retracted)-x))) < 3e-15
        potential = rng.normal(size=box.vertex_shape)
        pure_gradient = [gradient(potential, mu) for mu in range(4)]
        assert max(np.max(np.abs(v)) for v in box.retract(pure_gradient, omitted)) < 3e-15
        adjoint_error = abs(box.dot(fx, box.gauge_metric(fy, omitted))
                            - box.dot(box.gauge_metric(fx, omitted), fy))
        assert adjoint_error < 3e-12

        retraction = np.column_stack([pack(box.retract(unpack(np.eye(size)[j]), omitted))
                                     for j in range(size)])
        metric = retraction.T @ retraction
        assert np.max(np.abs(pack(box.gauge_metric(fx, omitted)) - metric @ x)) < 3e-12
        cf = reference["C"][:, remaining]
        hf = cf.T @ cf
        sf = np.linalg.inv(hf)
        kf = (retraction @ reference["K"])[np.ix_(remaining, remaining)]
        rf = (hf @ kf+kf.T @ hf)/2 - sum(q[np.ix_(remaining, remaining)] for q in reference["Q"])
        assert np.max(np.abs(rf - residual[np.ix_(remaining, remaining)])) < 3e-13
        values = []
        for flowed in reference["Q_FLOW"]:
            full = -2 * np.trace(flowed @ sigma @ residual @ sigma @ metric @ sigma)
            bf = flowed[np.ix_(remaining, remaining)]
            sliced = -2 * np.trace(bf @ sf @ rf @ sf @ sf)
            assert abs(full-sliced) < 3e-11
            values.append(float(sliced))
        dense_values.append(values)
        print(f"One-site dense diagnostic, omitted axial edge {omitted}: {values}", flush=True)
    difference = np.array(dense_values[1]) - dense_values[0]
    assert min(abs(difference)) > 1e-5
    print(f"Full/slice contraction equality passes; sample forest difference {difference.tolist()}.", flush=True)
    return {"scope": "N=4 rational one-site diagnostic, not the original smooth displacement",
            "maximum_operator_error": float(max(checks)),
            "forests_omitted_edge": [3, 2], "contributions": dense_values,
            "paired_difference": difference.tolist()}


def density_example(box):
    """Integer-valued field giving an exact change of the quadratic M2."""
    x = box.zeros()
    x[0][(box.n-1, *((box.n//2-1,) * 3))] = 1
    norms = [box.dot(box.retract(x, omitted), box.retract(x, omitted))
             for omitted in (box.n-1, box.n//2)]
    expected = [1, 1+6*(box.n-box.n//2-1)]
    assert norms == expected
    print(f"Exact unit-edge density test: squared norms {expected}; "
          f"M2 changes by {box.n-box.n//2-1}/2.", flush=True)
    return {"squared_norms": expected,
            "one_color_M2_difference": f"{box.n-box.n//2-1}/2",
            "qualification": "integer-valued retraction check; independent of the probe weights"}


def original_check(n, samples, seed):
    box = RelativeBox(n)
    exact_example = density_example(box)
    rng = np.random.default_rng(seed)
    omitted_edges = (n-1, n//2)
    values = []
    for sample in range(samples):
        # Cov(w)=Sigma H_tau. Heat is balanced around the trace; this is
        # an unbiased estimator of -2 Tr(H Q_i H Sigma R Sigma G_F Sigma).
        normal = [rng.normal(size=shape) for shape in box.shapes]
        w = box.spectral(normal, power=-1/2, time=box.tau/2)
        left = box.probe_matrices(w)
        row = []
        for omitted in omitted_edges:
            middle = box.spectral(box.gauge_metric(w, omitted), power=-1)
            right = box.spectral(box.residual(middle), power=-1, time=box.tau)
            row.append([-2 * box.dot(probe, right) for probe in left])
        values.append(row)
        if (sample+1) % 8 == 0 or sample+1 == samples:
            data = np.array(values)
            paired = data[:, 1] - data[:, 0]
            print(f"Original N={n}, samples {sample+1}: means {data.mean(axis=0).tolist()}; "
                  f"paired means {paired.mean(axis=0).tolist()}", flush=True)
    data = np.array(values)
    paired = data[:, 1] - data[:, 0]
    return {"scope": "original L008 displacement and both L010 leading probes; admitted fixed mesh",
            "N": n, "a": box.a, "tau": box.tau, "seed": seed, "samples": samples,
            "relative_one_form_dimension": sum(int(np.prod(shape)) for shape in box.shapes),
            "active_vertex_index_ranges": box.support_indices,
            "exact_density_example": exact_example,
            "forests_omitted_edge": list(omitted_edges),
            "mean_contributions": data.mean(axis=0).tolist(),
            "standard_errors": (data.std(axis=0, ddof=1)/np.sqrt(samples)).tolist(),
            "paired_difference_mean": paired.mean(axis=0).tolist(),
            "paired_difference_standard_error": (paired.std(axis=0, ddof=1)/np.sqrt(samples)).tolist(),
            "individual_samples": data.tolist(),
            "qualification": "randomized trace diagnostics, without confidence guarantee, asymptotic claim or interacting bound"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--N", type=int, default=24)
    parser.add_argument("--samples", type=int, default=64)
    parser.add_argument("--seed", type=int, default=2704)
    parser.add_argument("--dense-only", action="store_true")
    parser.add_argument("--skip-dense", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    assert args.samples >= 2
    result = {"density_term": "-kappa_0(f_i0,r0,M2)", "full_Gamma_evaluated": False}
    if not args.skip_dense:
        result["dense_diagnostic"] = dense_check()
    if not args.dense_only:
        result["original_probe_diagnostic"] = original_check(args.N, args.samples, args.seed)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("Coordinate-Haar term only: no full cutoff logarithm or reflected-error estimate.")


if __name__ == "__main__":
    main()
