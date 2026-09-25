"""Construct and independently check small ER certificates for L012.

Only input clauses, fresh AND definitions, weakening, and binary resolution
appear in the certificates. Truth tables are used by the producer, never as
an inference rule of the checker. These finite tests do not prove the bound.
"""

from itertools import combinations, product


def clause(literals):
    return frozenset(literals)


def tautological(c):
    return any(-lit in c for lit in c)


def xor_clauses(a, b, out):
    candidates = (
        clause((a, b, -out)),
        clause((a, -b, out)),
        clause((-a, b, out)),
        clause((-a, -b, -out)),
    )
    return list(dict.fromkeys(c for c in candidates if not tautological(c)))


class Producer:
    def __init__(self, formula):
        self.records = []
        self.lines = []
        self.known = {}
        self.original = {abs(lit) for c in formula for lit in c}
        self.next_variable = max(self.original, default=0) + 1
        for c in dict.fromkeys(formula):
            self.records.append(("input", c))
            self.append(c)

    def append(self, c):
        self.lines.append(c)
        ref = len(self.lines) - 1
        self.known[c] = ref
        return ref

    def and_gate(self, a, b):
        z = self.next_variable
        self.next_variable += 1
        self.records.append(("and", z, a, b))
        refs = [
            self.append(clause((-z, a))),
            self.append(clause((-z, b))),
            self.append(clause((z, -a, -b))),
        ]
        return z, refs

    def weaken(self, ref, target):
        if target in self.known:
            return self.known[target]
        assert self.lines[ref] <= target
        self.records.append(("weak", target, ref))
        return self.append(target)

    def resolve(self, left, right, pivot):
        pivot = abs(pivot)
        if pivot not in self.lines[left]:
            left, right = right, left
        assert pivot in self.lines[left] and -pivot in self.lines[right]
        target = (self.lines[left] - {pivot}) | (self.lines[right] - {-pivot})
        if target in self.known:
            return self.known[target]
        self.records.append(("res", target, left, right, pivot))
        return self.append(target)

    def consequence(self, premises, target):
        """Compile a local consequence by a full binary resolution tree."""
        assert not tautological(target)
        if target in self.known:
            return self.known[target]
        variables = {abs(lit) for ref in premises for lit in self.lines[ref]}
        variables |= {abs(lit) for lit in target}
        assert len(variables) <= 6, (len(variables), target)
        fixed = {abs(lit): lit < 0 for lit in target}
        free = sorted(variables - fixed.keys())

        def tree(depth, assignment):
            if depth == len(free):
                blocking = clause(-v if bit else v for v, bit in assignment.items())
                falsified = next(
                    ref for ref in premises
                    if not any(assignment[abs(lit)] == (lit > 0)
                               for lit in self.lines[ref])
                )
                return self.weaken(falsified, blocking)
            v = free[depth]
            assignment[v] = False
            left = tree(depth + 1, assignment)
            assignment[v] = True
            right = tree(depth + 1, assignment)
            del assignment[v]
            return self.resolve(left, right, v)

        result = tree(0, dict(fixed))
        assert self.lines[result] == target
        return result

    def xor_gate(self, a, b):
        u, first = self.and_gate(a, b)
        v, second = self.and_gate(-a, -b)
        out, third = self.and_gate(-u, -v)
        definitions = first + second + third
        refs = [self.consequence(definitions, c) for c in xor_clauses(a, b, out)]
        return out, refs


def check_certificate(formula, records, require_empty=True):
    """A syntax-only verifier, independent of the producer's macros."""
    initial = set(formula)
    available = {abs(lit) for c in formula for lit in c}
    verified = []

    def earlier(ref):
        assert isinstance(ref, int) and 0 <= ref < len(verified)
        return verified[ref]

    for record in records:
        op = record[0]
        if op == "input":
            c = record[1]
            assert c in initial
            verified.append(c)
        elif op == "and":
            _, z, a, b = record
            assert z > 0 and z not in available
            assert abs(a) in available and abs(b) in available
            available.add(z)
            verified.extend((frozenset((-z, a)), frozenset((-z, b)),
                             frozenset((z, -a, -b))))
        elif op == "weak":
            _, c, ref = record
            assert earlier(ref).issubset(c)
            assert all(abs(lit) in available for lit in c)
            verified.append(c)
        elif op == "res":
            _, c, left, right, pivot = record
            assert pivot > 0
            a, b = earlier(left), earlier(right)
            assert pivot in a and -pivot in b
            assert c == (a - {pivot}) | (b - {-pivot})
            verified.append(c)
        else:
            raise AssertionError("Unknown proof rule")
    if require_empty:
        assert verified and verified[-1] == frozenset()
    return verified


def parity_block(support, charge):
    return [clause(-v if bit else v for v, bit in zip(support, bits))
            for bits in product((0, 1), repeat=len(support))
            if sum(bits) % 2 != charge]


def chain(proof, support, variables, zero):
    roots = [zero]
    gates = [[]]
    for x in variables:
        if x in support:
            root, refs = proof.xor_gate(roots[-1], x)
        else:
            root, refs = roots[-1], []
        roots.append(root)
        gates.append(refs)
    return {"support": set(support), "roots": roots, "gates": gates}


def initial_row(proof, support, charge, variables, zero, zero_ref):
    row = chain(proof, support, variables, zero)
    ordered = sorted(support)
    positions = {x: j + 1 for j, x in enumerate(variables)}
    output_literal = row["roots"][-1] if charge else -row["roots"][-1]
    leaves = []
    for bits in product((0, 1), repeat=len(ordered)):
        blocking = clause(-v if bit else v for v, bit in zip(ordered, bits))
        if sum(bits) % 2 != charge:
            ref = proof.weaken(proof.known[blocking], blocking | {output_literal})
        else:
            ref = proof.weaken(zero_ref, blocking | {-zero})
            parity = 0
            for x, bit in zip(ordered, bits):
                j = positions[x]
                previous = row["roots"][j - 1]
                lit_previous = previous if parity else -previous
                lit_input = x if bit else -x
                parity ^= bit
                output = row["roots"][j]
                lit_output = output if parity else -output
                gate_clause = clause((-lit_previous, -lit_input, lit_output))
                ref = proof.resolve(ref, proof.known[gate_clause], previous)
                assert proof.lines[ref] == blocking | {lit_output}
        leaves.append(ref)
    for x in reversed(ordered):
        leaves = [proof.resolve(leaves[j], leaves[j + 1], x)
                  for j in range(0, len(leaves), 2)]
    row.update(charge=charge, unit=leaves[0])
    assert proof.lines[row["unit"]] == clause((output_literal,))
    return row


def add_rows(proof, a, b, variables, zero, zero_ref):
    c = chain(proof, a["support"] ^ b["support"], variables, zero)
    invariant = [proof.consequence([zero_ref], q)
                 for q in xor_clauses(zero, zero, zero)]
    for j in range(1, len(variables) + 1):
        premises = invariant + a["gates"][j] + b["gates"][j] + c["gates"][j]
        invariant = [proof.consequence(premises, q)
                     for q in xor_clauses(a["roots"][j], b["roots"][j],
                                          c["roots"][j])]
    charge = a["charge"] ^ b["charge"]
    output_literal = c["roots"][-1] if charge else -c["roots"][-1]
    unit = proof.consequence(invariant + [a["unit"], b["unit"]],
                             clause((output_literal,)))
    c.update(charge=charge, unit=unit)
    return c


def graph_certificate(n, edges, charges):
    variables = list(range(1, len(edges) + 1))
    supports = [{j + 1 for j, edge in enumerate(edges) if v in edge}
                for v in range(n)]
    formula = [c for support, charge in zip(supports, charges)
               for c in parity_block(sorted(support), charge)]
    proof = Producer(formula)
    zero, definitions = proof.and_gate(variables[0], -variables[0])
    zero_ref = proof.resolve(definitions[0], definitions[1], variables[0])
    accumulated = chain(proof, set(), variables, zero)
    accumulated.update(charge=0, unit=zero_ref)
    for support, charge in zip(supports, charges):
        row = initial_row(proof, support, charge, variables, zero, zero_ref)
        accumulated = add_rows(proof, accumulated, row, variables, zero, zero_ref)
    assert not accumulated["support"] and accumulated["charge"] == 1
    proof.resolve(accumulated["unit"], zero_ref, zero)
    checked = check_certificate(formula, proof.records)
    assert checked == proof.lines
    return formula, proof


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


def local_template_checks():
    # Use six distinct wire variables to exercise every coefficient pair.
    # These are macro entailment proofs; premises are supplied as inputs here.
    total = 0
    for alpha, beta in product((0, 1), repeat=2):
        a, b, c, x = 1, 2, 3, 4
        a_new, b_new, c_new = (5 if alpha else a), (6 if beta else b), c
        if alpha ^ beta:
            c_new = 6 if alpha else 5
        premises = xor_clauses(a, b, c)
        if alpha:
            premises += xor_clauses(a, x, a_new)
        if beta:
            premises += xor_clauses(b, x, b_new)
        if alpha ^ beta:
            premises += xor_clauses(c, x, c_new)
        proof = Producer(premises)
        initial_refs = list(range(len(proof.lines)))
        for q in xor_clauses(a_new, b_new, c_new):
            proof.consequence(initial_refs, q)
        check_certificate(premises, proof.records, require_empty=False)
        total += 1
    return total


def main():
    templates = local_template_checks()
    graphs = []
    for n in (3, 4):
        possible = list(combinations(range(n), 2))
        for bits in product((0, 1), repeat=len(possible)):
            edges = [edge for edge, bit in zip(possible, bits) if bit]
            if connected_min_degree_two(n, edges):
                graphs.append((n, edges))
    graphs += [(5, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]),
               (5, list(combinations(range(5), 2)))]
    count = total_lines = maximum_lines = maximum_width = 0
    example = None
    for n, edges in graphs:
        for charges in product((0, 1), repeat=n):
            if sum(charges) % 2 == 0:
                continue
            formula, proof = graph_certificate(n, edges, charges)
            count += 1
            total_lines += len(proof.lines)
            maximum_lines = max(maximum_lines, len(proof.lines))
            maximum_width = max(maximum_width, max(map(len, proof.lines)))
            example = formula, proof
    formula, proof = example
    damaged = list(proof.records)
    assert damaged[-1][0] == "res"
    damaged[-1] = ("res", frozenset((1,)), *damaged[-1][2:])
    try:
        check_certificate(formula, damaged)
    except AssertionError:
        pass
    else:
        raise AssertionError("Checker accepted a corrupted resolution line")
    print(f"PASS: {templates} row-addition coefficient templates.")
    print(f"PASS: {count} odd-charge ER refutations on {len(graphs)} small graphs.")
    print(f"Checked {total_lines} clauses; maximum per proof {maximum_lines}; "
          f"maximum width {maximum_width}.")
    print("PASS: checker rejected a corrupted final resolution inference.")
    print("Only input, fresh AND extension, weakening, and resolution rules were checked.")
    print("Finite verification does not establish the asymptotic bound or P versus NP.")


if __name__ == "__main__":
    main()
