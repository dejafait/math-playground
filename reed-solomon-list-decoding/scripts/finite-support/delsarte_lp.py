"""Basic constant-weight Delsarte LP: discover a basis, verify it exactly.

Only the prior assessed inequalities are used. Decimal simplex is discovery;
the final certificate uses fractions and checks every inequality.
"""
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from math import comb
from pathlib import Path

N, W, D = 1024, 68, 10
OUT = Path(__file__).with_name("delsarte-lp-results.json")


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def hahn(j, i):
    numerator = sum((-1)**h * choose(j, h) * choose(W-j, i-h)
                    * choose(N-W-j, i-h) for h in range(i+1))
    return Fraction(numerator, comb(W, i)*comb(N-W, i))


def solve_exact(matrix, rhs):
    """Fraction Gaussian elimination, including full back substitution."""
    a = [[Fraction(x) for x in row]+[Fraction(b)]
         for row, b in zip(matrix, rhs)]
    n = len(a)
    for k in range(n):
        p = next((p for p in range(k, n) if a[p][k]), None)
        if p is None:
            raise ValueError("singular reconstructed basis")
        a[k], a[p] = a[p], a[k]
        pivot = a[k][k]
        for j in range(k, n+1):
            a[k][j] /= pivot
        for r in range(k+1, n):
            factor = a[r][k]
            if factor:
                for j in range(k+1, n+1):
                    a[r][j] -= factor*a[k][j]
                a[r][k] = Fraction(0)
    x = [Fraction(0)]*n
    for i in reversed(range(n)):
        x[i] = a[i][n]-sum(a[i][j]*x[j] for j in range(i+1, n))
    return x


def enc(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


def main():
    distances = list(range(D//2, W+1))
    q = [[hahn(j, i) for i in distances] for j in range(1, W+1)]
    a = [[-v for v in row] for row in q]
    count, rows = len(distances), W
    trace = []
    with localcontext() as ctx:
        ctx.prec = 220
        dec = lambda x: Decimal(x.numerator)/Decimal(x.denominator)
        # max sum x, A x <= 1; basic slacks initially all equal to one.
        tableau = [[dec(v) for v in row]
                   +[Decimal(int(j == r)) for j in range(rows)]+[Decimal(1)]
                   for r, row in enumerate(a)]
        tableau.append([-Decimal(1)]*count+[Decimal(0)]*(rows+1))
        basis = list(range(count, count+rows))
        tolerance = Decimal("1e-170")
        status = "iteration_limit"
        for iteration in range(500):
            entering = next((j for j, v in enumerate(tableau[-1][:-1])
                             if v < -tolerance), None)
            if entering is None:
                status = "decimal_optimal"
                break
            options = [(row[-1]/row[entering], basis[r], r)
                       for r, row in enumerate(tableau[:-1])
                       if row[entering] > tolerance]
            if not options:
                status = "decimal_unbounded_or_scaling_failure"
                break
            _, _, leaving = min(options)
            pivot = tableau[leaving][entering]
            tableau[leaving] = [v/pivot for v in tableau[leaving]]
            pivot_row = tableau[leaving]
            for r, row in enumerate(tableau):
                if r != leaving:
                    factor = row[entering]
                    if factor:
                        tableau[r] = [v-factor*p for v, p in zip(row, pivot_row)]
                        tableau[r][entering] = Decimal(0)
            trace.append({"iteration": iteration, "entering": entering,
                          "leaving_variable": basis[leaving],
                          "objective_decimal": str(tableau[-1][-1])})
            basis[leaving] = entering
        discovery = {"status": status, "iterations": len(trace),
                     "precision": ctx.prec, "basis": basis,
                     "objective_decimal": str(tableau[-1][-1]), "trace": trace}
    certificate = {"parameters": {"n": N, "w": W, "d": D,
                    "threshold_numerator": 65537**28,
                    "threshold_denominator": 2**128},
                   "discovery": discovery,
                   "q_matrix": [[enc(v) for v in row] for row in q],
                   "failures": []}
    # Reduce the basis system: nonbasic slack variables give active rows;
    # nonbasic distance variables are zero. This usually leaves few unknowns.
    active_cols = sorted(v for v in basis if v < count)
    active_rows = [r for r in range(rows) if count+r not in basis]
    certificate["active_distances"] = [distances[c] for c in active_cols]
    certificate["active_hahn_rows"] = [r+1 for r in active_rows]
    try:
        assert len(active_rows) == len(active_cols)
        bmatrix = [[a[r][c] for c in active_cols] for r in active_rows]
        xsmall = solve_exact(bmatrix, [1]*len(active_rows))
        x = [Fraction(0)]*count
        for c, v in zip(active_cols, xsmall):
            x[c] = v
        slacks = [1-sum(v*z for v, z in zip(row, x)) for row in a]
        primal_feasible = all(v >= 0 for v in x+slacks)
        # Dual from the transpose of the same basis; objective equality
        # plus exact feasibility certifies the optimum, when both hold.
        ysmall = solve_exact(list(map(list, zip(*bmatrix))), [1]*len(active_cols))
        y = [Fraction(0)]*rows
        for r, v in zip(active_rows, ysmall):
            y[r] = v
        dual_slacks = [sum(y[r]*a[r][c] for r in range(rows))-1
                       for c in range(count)]
        dual_feasible = all(v >= 0 for v in y+dual_slacks)
        primal_value, dual_value = sum(x), sum(y)
        primal_floor_bound = 1+primal_value.__floor__()
        dual_floor_bound = 1+dual_value.__floor__()
        excess = 2**128*primal_floor_bound-65537**28
        certificate["exact"] = {
            "primal": [enc(v) for v in x], "primal_slacks": [enc(v) for v in slacks],
            "dual": [enc(v) for v in y], "dual_slacks": [enc(v) for v in dual_slacks],
            "primal_feasible": primal_feasible, "dual_feasible": dual_feasible,
            "primal_objective": enc(primal_value), "dual_objective": enc(dual_value),
            "equal_objectives": primal_value == dual_value,
            "primal_floor_bound": primal_floor_bound,
            "dual_floor_bound": dual_floor_bound,
            "primal_scaled_threshold_excess": excess,
            "basic_lp_cannot_certify_threshold": primal_feasible and excess > 0,
            "dual_certifies_threshold": dual_feasible and
                2**128*dual_floor_bound <= 65537**28,
            "optimality_verified": primal_feasible and dual_feasible and
                primal_value == dual_value,
            "primal_negative_distances": [distances[i] for i,v in enumerate(x) if v < 0],
            "primal_failed_hahn_rows": [j+1 for j,v in enumerate(slacks) if v < 0],
            "dual_negative_hahn_rows": [j+1 for j,v in enumerate(y) if v < 0],
            "dual_failed_distances": [distances[i] for i,v in enumerate(dual_slacks) if v < 0]}
        if not primal_feasible:
            certificate["failures"].append("reconstructed primal is infeasible")
        if not dual_feasible:
            certificate["failures"].append("reconstructed dual is infeasible")
        if primal_value != dual_value:
            certificate["failures"].append("objectives differ")
    except (ValueError, AssertionError) as e:
        certificate["failures"].append(str(e))
    OUT.write_text(json.dumps(certificate, indent=2)+"\n")
    print(f"Discovery: {status}, pivots={len(trace)}, basis size={len(active_cols)}")
    if "exact" in certificate:
        result = certificate["exact"]
        print(f"Exact primal feasible={result['primal_feasible']}; dual feasible={result['dual_feasible']}; optimum verified={result['optimality_verified']}")
        print(f"Actual LP floor bound={result['primal_floor_bound']}; required <= {65537**28}/{2**128}")
        print(f"Scaled threshold excess={excess}; threshold excluded for basic LP={result['basic_lp_cannot_certify_threshold']}")
    print(f"Failures: {certificate['failures']}; full certificate: {OUT}")


if __name__ == "__main__":
    main()
