"""Finite encoding checks for L010; not an asymptotic lower-bound test."""

from itertools import combinations, product


def parity_cnf(support, charge):
    return [
        tuple(-v if bit else v for v, bit in zip(support, bits))
        for bits in product((0, 1), repeat=len(support))
        if sum(bits) % 2 != charge
    ]


def cnf_value(clauses, assignment):
    return all(
        any(assignment[abs(lit)] == (lit > 0) for lit in clause)
        for clause in clauses
    )


def brute_sat(clauses):
    variables = sorted({abs(lit) for clause in clauses for lit in clause})
    return any(
        cnf_value(clauses, dict(zip(variables, bits)))
        for bits in product((0, 1), repeat=len(variables))
    )


def parity_solver(clauses):
    """Return SAT truth value, or None when parity-block recognition fails."""
    groups = {}
    for raw_clause in clauses:
        clause = frozenset(raw_clause)
        if any(-lit in clause for lit in clause):
            continue
        if not clause:
            return False
        support = tuple(sorted(abs(lit) for lit in clause))
        forbidden = tuple(int(-v in clause) for v in support)
        groups.setdefault(support, set()).add(forbidden)

    variables = sorted({v for support in groups for v in support})
    positions = {v: i for i, v in enumerate(variables)}
    rows = []
    for support, forbidden in groups.items():
        if len(forbidden) != 1 << (len(support) - 1):
            return None
        parities = {sum(bits) % 2 for bits in forbidden}
        if len(parities) != 1:
            return None
        rhs = 1 - next(iter(parities))
        mask = sum(1 << positions[v] for v in support)
        rows.append((mask, rhs))

    pivots = {}
    for mask, rhs in rows:
        while mask:
            pivot = mask.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (mask, rhs)
                break
            old_mask, old_rhs = pivots[pivot]
            mask ^= old_mask
            rhs ^= old_rhs
        else:
            if rhs:
                return False
    return True


def connected_min_degree_two(n, edges):
    neighbors = [set() for _ in range(n)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    if any(len(row) < 2 for row in neighbors):
        return False
    reached, pending = {0}, [0]
    while pending:
        for v in neighbors[pending.pop()] - reached:
            reached.add(v)
            pending.append(v)
    return len(reached) == n


def main():
    local_cases = 0
    for width in range(1, 7):
        support = tuple(range(1, width + 1))
        for charge in (0, 1):
            clauses = parity_cnf(support, charge)
            for bits in product((0, 1), repeat=width):
                assert cnf_value(clauses, dict(zip(support, bits))) == (
                    sum(bits) % 2 == charge
                )
                local_cases += 1

    graphs = []
    for n in (3, 4):
        possible = list(combinations(range(n), 2))
        for selected in product((0, 1), repeat=len(possible)):
            edges = [edge for edge, bit in zip(possible, selected) if bit]
            if connected_min_degree_two(n, edges):
                graphs.append((n, edges))
    graphs.append((5, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]))
    graphs.append((5, list(combinations(range(5), 2))))

    charge_cases = 0
    for n, edges in graphs:
        incident = [[] for _ in range(n)]
        for edge_id, (u, v) in enumerate(edges, 1):
            incident[u].append(edge_id)
            incident[v].append(edge_id)
        assert len({tuple(row) for row in incident}) == n
        for charges in product((0, 1), repeat=n):
            clauses = [
                clause
                for support, charge in zip(incident, charges)
                for clause in parity_cnf(support, charge)
            ]
            expected = sum(charges) % 2 == 0
            assert brute_sat(clauses) == expected
            assert parity_solver(clauses) == expected
            # Literal and clause order, duplicates, and large labels carry no advice.
            renamed = [
                tuple((1 if lit > 0 else -1) * (10**12 + abs(lit))
                      for lit in reversed(clause))
                for clause in reversed(clauses)
            ]
            assert parity_solver(renamed + renamed[:1]) == expected
            charge_cases += 1

    # All subsets of the eight full-support clauses on three variables.
    # Only the empty set and two complete parity blocks should be recognized.
    full_support = list(product((0, 1), repeat=3))
    recognized = 0
    for selected in product((0, 1), repeat=8):
        clauses = [
            tuple(-v if bit else v for v, bit in zip((1, 2, 3), bits))
            for bits, present in zip(full_support, selected)
            if present
        ]
        result = parity_solver(clauses)
        if result is not None:
            assert result == brute_sat(clauses)
            recognized += 1
    assert recognized == 3
    assert parity_solver([()]) is False
    assert parity_solver([(1,), (-1,)]) is None
    assert parity_solver([(1, -1)]) is True

    print(f"PASS: {local_cases} local parity valuations (widths 1–6).")
    print(f"PASS: {charge_cases} charge vectors on {len(graphs)} graphs; "
          "CNF brute force, elimination, and charge parity agree.")
    print("PASS: 256 full-support clause subsets; exactly the expected 3 recognized.")
    print("PASS: reordered/duplicate clauses, large labels, empty and tautological clauses.")
    print("These finite checks do not establish expansion or asymptotic proof-size bounds.")


if __name__ == "__main__":
    main()
