"""Nonnegative retained Fourier-error contraction; binary64 diagnostic only.

The conditional algebra is L035. This does not validate eta, coefficient
quadrature, time weights or arithmetic. Full evidence is saved, not printed.
"""
import argparse
import json
from functools import lru_cache
from pathlib import Path

import numpy as np

from check_continuum_tensor import OMEGA2, TensorKernel, inverse_checks, time_rule


class SensitivityKernel(TensorKernel):
    def __init__(self, m, degree, eta):
        super().__init__(m, degree)
        self.eta = eta

    @lru_cache(None)
    def allowance(self, alpha, axis, d, a, b, component):
        """eta H_q times the absolute Fourier multiplier sum, before error."""
        k = np.array([0] if axis == 0 else range(1, self.m + 1))[:, None]
        ell = np.array(range(0 if axis == component else 1, self.m + 1))[None, :]
        omega = np.sqrt(OMEGA2)
        left = np.where(k == 0, 1 / (2 * np.sqrt(8)) if axis == 0 and a == 0 else 0,
                        0.25 * (omega * k) ** a)
        right = np.where(ell == 0, 1 / (2 * np.sqrt(8)) if axis == component and b == 0 else 0,
                         0.25 * (omega * ell) ** b)
        # Duplicate zero waves with half coefficients: same sum as one zero wave.
        mult = sum((omega * np.abs(s * k + t * ell)) ** d
                   for s in (-1, 1) for t in (-1, 1))
        odd = int(axis in self.integrations[alpha].pair)
        lp = k if axis == 0 else k + 1
        rp = ell if axis == component else ell + 1
        allowed = (odd + d + a + b + lp + rp) % 2 == 0
        return self.eta * (9 if odd else 6) * left * right * mult * allowed

    def feature(self, alpha, axis, first, second, component):
        integ = self.integrations[alpha]
        b1 = np.abs(integ.matrix(axis, *first, component))
        b2 = np.abs(integ.matrix(axis, *second, component))
        d1 = self.allowance(alpha, axis, *first, component)
        d2 = self.allowance(alpha, axis, *second, component)
        return b1 * b2, d1 * b2 + b1 * d2 + d1 * d2

    def sensitivity(self, s, r):
        """Return baseline/allowance heat tensors, without overall factor 8."""
        values = np.zeros((2, 2, 2, 2, len(s), len(r)))
        for alpha in range(2):
            for component in range(4):
                ops = [self.products[alpha, i, component] for i in range(2)]
                features = [sorted({key[j] for op in ops for key in op}) for j in range(4)]
                tables, positions = [], []
                for axis in range(4):
                    ks = np.array([0] if axis == 0 else range(1, self.m + 1))
                    ls = np.array(range(0 if axis == component else 1, self.m + 1))
                    es = np.exp(-np.asarray(s)[:, None] * OMEGA2 * ks[None, :] ** 2)
                    er = np.exp(-np.asarray(r)[:, None] * OMEGA2 * ls[None, :] ** 2)
                    rows = []
                    for first, second in features[axis]:
                        bd = self.feature(alpha, axis, first, second, component)
                        if axis == 0:
                            masks = [(ls == 0), (ls > 0) & (ls % 2 == 0)]
                            rows.append(np.array([[es @ (x * mask[None, :]) @ er.T
                                                   for mask in masks] for x in bd]))
                        else:
                            rows.append(np.array([es @ x @ er.T for x in bd]))
                    tables.append(np.asarray(rows))
                    positions.append({key: index for index, key in enumerate(features[axis])})
                for i, op in enumerate(ops):
                    keys = list(op)
                    for start in range(0, len(keys), 16):
                        selected = keys[start:start + 16]
                        coeff = np.array([float(abs(op[key])) for key in selected])
                        indices = [[positions[j][key[j]] for key in selected] for j in range(4)]
                        baseline = tables[1][indices[1], 0].copy()
                        error = tables[1][indices[1], 1].copy()
                        for axis in (2, 3):
                            b, d = tables[axis][indices[axis], 0], tables[axis][indices[axis], 1]
                            error = error * (b + d) + baseline * d
                            baseline *= b
                        for part in range(2):
                            b = tables[0][indices[0], 0, part]
                            d = tables[0][indices[0], 1, part]
                            for kind, x in enumerate((baseline * b,
                                                      error * (b + d) + baseline * d)):
                                values[kind, i, alpha, part] += np.einsum('p,psr->sr', coeff, x)
        return values

    def dense_sensitivity(self, s, r):
        """Independent explicit finite-mode product, for small-cutoff checks."""
        values = np.zeros((2, 2, 2, 2, len(s), len(r)))
        for alpha in range(2):
            for component in range(4):
                domains = [range(0 if j == component else 1, self.m + 1) for j in range(4)]
                domains[0] = [n for n in domains[0] if n % 2 == 0]
                for k2 in range(1, self.m + 1):
                    for k3 in range(1, self.m + 1):
                        for k4 in range(1, self.m + 1):
                            k = [0, k2, k3, k4]
                            for ell in np.ndindex(*(len(x) for x in domains)):
                                ls = [domains[j][ell[j]] for j in range(4)]
                                positions = [(0 if j == 0 else k[j] - 1,
                                              ls[j] - (0 if j == component else 1)) for j in range(4)]
                                lk, ll = OMEGA2 * sum(x*x for x in k), OMEGA2 * sum(x*x for x in ls)
                                heat = np.exp(-np.asarray(s)[:, None] * lk - np.asarray(r)[None, :] * ll)
                                for i in range(2):
                                    for key, v in self.products[alpha, i, component].items():
                                        bs, ds = [], []
                                        for j in range(4):
                                            bd = self.feature(alpha, j, *key[j], component)
                                            bs.append(bd[0][positions[j]])
                                            ds.append(bd[1][positions[j]])
                                        # Explicit nonempty-subset expansion, not tensor recurrence.
                                        base = np.prod(bs)
                                        err = sum(np.prod([ds[j] if mask & (1 << j) else bs[j]
                                                           for j in range(4)]) for mask in range(1, 16))
                                        values[:, i, alpha, int(ls[0] != 0)] += (
                                            float(abs(v)) * np.array([base, err])[:, None, None] * heat)
        return values


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cutoff', type=int, default=112)
    parser.add_argument('--coefficient-degree', type=int, default=144)
    parser.add_argument('--time-degrees', type=int, nargs='+', default=[8, 12])
    parser.add_argument('--eta', type=float, default=1e-12)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('retained-tensor-sensitivity-certificate.json'))
    args = parser.parse_args()
    result = dict(scope='Conditional Fourier coefficient sensitivity only; binary64 diagnostic, no enclosure.',
                  eta=args.eta, cutoff=args.cutoff, coefficient_degree=args.coefficient_degree,
                  required_coefficient_budgets=[100, 1000], input_error_established=False,
                  arithmetic_enclosed=False, rigorous_sign_certified=False, rows=[], failures=[])
    def save():
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    save()
    small = SensitivityKernel(2, 96, args.eta)
    times = np.array([1/16, 1/8])
    tensor = small.sensitivity(times, times)
    dense = small.dense_sensitivity(times, times)
    differences = np.abs(tensor - dense)
    scales = np.maximum(np.abs(dense), [1e-30][0])
    err = float(np.max(differences / scales))
    result['small_dense_check'] = dict(cutoff=2, times=times.tolist(), tensor=tensor.tolist(), dense=dense.tolist(),
                                     actual_max_relative_difference=err, required=1e-11, passed=err < 1e-11)
    if err >= 1e-11:
        result['failures'].append('small dense sensitivity mismatch')
    save()
    print(json.dumps(dict(check='small dense sensitivity', actual=err, required=1e-11,
                          passed=err < 1e-11, path=str(args.output))), flush=True)
    if result['failures']:
        return
    kernel = SensitivityKernel(args.cutoff, args.coefficient_degree, args.eta)
    previous = None
    for degree in args.time_degrees:
        times, ds, dr, rule = time_rule(degree, 0.5, 80, 8)
        inverses = inverse_checks(args.cutoff, times, ds, dr)
        if not inverses['passed']:
            result['failures'].append(dict(check='inverse rule', degree=degree))
            save()
            continue
        heat = kernel.sensitivity(times, times)
        values = 8 * np.einsum('kiapst,s,t->kiap', heat, ds, dr, optimize=True)
        totals = values.sum(axis=(2, 3))
        row = dict(time_rule=rule, inverse_checks=inverses, baseline_and_allowance_parts=values.tolist(),
                   baseline_and_allowance_totals=totals.tolist(),
                   coefficient_budget_passed=(totals[1] < [100, 1000]).tolist())
        if previous is not None:
            diff = np.abs(totals - previous)
            rel = float(np.max(diff / np.maximum(np.abs(totals), 1e-30)))
            row['refinement'] = dict(actual_differences=diff.tolist(), actual_max_relative_difference=rel,
                                     required_max_relative_difference=1e-9, passed=rel < 1e-9)
            if rel >= 1e-9:
                result['failures'].append(dict(check='time refinement', degree=degree))
        result['rows'].append(row)
        previous = totals
        save()
        print(json.dumps(dict(cutoff=args.cutoff, degree=degree, actual_allowances=totals[1].tolist(),
                              required_budgets=[100, 1000], passed=row['coefficient_budget_passed'],
                              failures=result['failures'], path=str(args.output))), flush=True)


if __name__ == '__main__':
    main()
