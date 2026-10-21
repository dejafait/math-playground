"""Exact local word geometry used in L150; no covariance or cutoff diagnostic."""
from itertools import combinations
from pathlib import Path
import json


def shift(x, direction, amount=1):
    y = list(x)
    y[direction] += amount
    return tuple(y)


def word(start, steps):
    x = start
    out = []
    for direction, sign in steps:
        tail = x if sign == 1 else shift(x, direction, -1)
        out.append((tail, direction, sign))
        x = shift(x, direction, sign)
    assert x == start
    return tuple(out)


def clovers(z, rho, nu):
    return [word(z, steps) for steps in (
        ((rho, 1), (nu, 1), (rho, -1), (nu, -1)),
        ((nu, 1), (rho, -1), (nu, -1), (rho, 1)),
        ((rho, -1), (nu, -1), (rho, 1), (nu, 1)),
        ((nu, -1), (rho, 1), (nu, 1), (rho, -1)),
    )]


def cyclic(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def main():
    origin = (0, 0, 0, 0)
    checks = []
    for nu in range(4):
        head = shift(origin, nu)

        def invert_vertex(x):
            return tuple(head[j] - x[j] for j in range(4))

        def invert_word(w):
            return tuple((invert_vertex(shift(tail, direction)), direction, -sign)
                         for tail, direction, sign in w)

        stencil = set()
        for endpoint in (origin, head):
            for rho in range(4):
                if rho == nu:
                    continue
                actual = clovers(endpoint, rho, nu)
                expected = clovers(invert_vertex(endpoint), rho, nu)
                for index, w in enumerate(actual):
                    reflected = invert_word(w)
                    checks.append(dict(kind="based_clover", edge_direction=nu,
                                       plane=[rho, nu], endpoint=endpoint, index=index,
                                       word=w, reflected=reflected,
                                       expected=expected,
                                       passed=reflected in expected))
                    stencil.update((tail, direction) for tail, direction, _ in w)

        incident = []
        for mu in range(4):
            if mu == nu:
                continue
            low, high = sorted((mu, nu))
            for corner in (origin, shift(origin, mu, -1)):
                w = word(corner, ((low, 1), (high, 1), (low, -1), (high, -1)))
                incident.append(w)
                stencil.update((tail, direction) for tail, direction, _ in w)
        expected_cycles = set(map(cyclic, incident))
        checks.append(dict(kind="incident_action_traces", edge_direction=nu,
                           words=incident, reflected=list(map(invert_word, incident)),
                           passed=set(cyclic(invert_word(w)) for w in incident)
                           == expected_cycles))
        reflected_stencil = {(invert_vertex(shift(tail, direction)), direction)
                             for tail, direction in stencil}
        checks.append(dict(kind="complete_stencil_permutation", edge_direction=nu,
                           edges=sorted(stencil), reflected=sorted(reflected_stencil),
                           passed=stencil == reflected_stencil))
    failures = [i for i, row in enumerate(checks) if not row["passed"]]
    target = Path(__file__).with_name("quartic-residual-inversion-certificate.json")
    target.write_text(json.dumps(dict(
        scope="All exact local 4D word mappings in L150; analytic proof supplies covariance, heat and limit bounds",
        checks=checks, failures=failures,
        actual_failure_count=len(failures), required_failure_count=0,
    ), indent=2) + "\n")
    print(f"Exact inversion geometry: {len(checks)-len(failures)}/{len(checks)} pass.")
    print(f"Failures: actual={len(failures)}, required=0; indices={failures}.")
    print(f"Certificate: {target.relative_to(Path.cwd())}")
    assert not failures


if __name__ == "__main__":
    main()
