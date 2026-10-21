#!/usr/bin/env python3
"""Finite full-data checks for L028; no complexity lower bound is tested."""
import importlib.util
import itertools
import json
from pathlib import Path

SOURCE = Path(__file__).parents[1] / 'used-extension-obdd' / 'check_embedding.py'
spec = importlib.util.spec_from_file_location('hwb_family', SOURCE)
family = importlib.util.module_from_spec(spec)
spec.loader.exec_module(family)


class Circuit:
    def __init__(self, n):
        self.nodes = []
        self.degrees = []
        self.zero = self.put('const', 0)
        self.one = self.put('const', 1)
        self.x = {i: self.put('var', i) for i in range(1, n + 1)}
        self.plus = self.put('placeholder', '+')
        self.minus = self.put('placeholder', '-')
        self.j = self.add(self.plus, self.minus)

    def put(self, op, *args):
        if op in ('var', 'placeholder'):
            degree = 1
        elif op == 'const':
            degree = 0
        elif op == 'add':
            degree = max(self.degrees[a] for a in args)
        else:
            degree = sum(self.degrees[a] for a in args)
        self.nodes.append([op, *args])
        self.degrees.append(degree)
        return len(self.nodes) - 1

    def add(self, a, b):
        return self.put('add', a, b)

    def mul(self, a, b):
        return self.put('mul', a, b)

    def complement(self, a):
        return self.add(self.one, a)

    def evaluate(self, bits):
        vals = []
        for op, *args in self.nodes:
            if op == 'const':
                v = args[0]
            elif op == 'var':
                v = bits[args[0] - 1]
            elif op == 'placeholder':
                v = 0
            elif op == 'add':
                v = vals[args[0]] ^ vals[args[1]]
            else:
                v = vals[args[0]] & vals[args[1]]
            vals.append(v)
        return vals

    def words(self, mode):
        vals = []
        for op, *args in self.nodes:
            if op == 'const':
                v = {()} if args[0] else set()
            elif op == 'var':
                v = {(f'x{args[0]}',)}
            elif op == 'placeholder':
                if mode == 'zero':
                    v = set()
                elif mode == 'axioms':
                    v = {(), ('x1',)} if args[0] == '+' else {('x1',)}
                else:
                    v = {(f't{args[0]}',)}
            elif op == 'add':
                v = vals[args[0]] ^ vals[args[1]]
            else:
                v = word_product(vals[args[0]], vals[args[1]])
            vals.append(v)
        return vals


def word_product(a, b):
    result = set()
    for left in a:
        for right in b:
            word = left + right
            if word in result:
                result.remove(word)
            else:
                result.add(word)
    return result


def build_data(n, corrupt_cutoff=False):
    proof = family.build(n)
    c = Circuit(n)
    positive = dict(c.x)
    signed = {i: c.complement(root) for i, root in c.x.items()}
    original_count = proof['circuit_gate_count']
    gates = proof['gates']
    cursor = 0
    tags = {}

    def signed_root(lit):
        return positive[lit] if lit > 0 else signed[-lit]

    def assign(tag, root, operands):
        nonlocal cursor
        z, a, b = gates[cursor]
        assert (a, b) == operands
        positive[z] = root
        signed[z] = c.complement(root)
        tags[z] = tag
        cursor += 1
        return z

    z0 = assign(['zero'], c.zero, (1, -1))
    exact = {(0, 0): -z0}
    q = {(0, 0): c.one}
    for i in range(1, n + 1):
        for j in range(i + 1):
            prev = exact.get((i - 1, j), z0)
            prev_left = exact.get((i - 1, j - 1), z0)
            u = c.mul(q.get((i - 1, j), c.zero), signed[i])
            v = c.mul(q.get((i - 1, j - 1), c.zero), c.x[i])
            uvar = assign(['u', i, j], u, (prev, -i))
            vvar = assign(['v', i, j], v, (prev_left, i))
            q[i, j] = c.add(u, v)
            wvar = assign(['w', i, j], c.complement(q[i, j]), (-uvar, -vvar))
            exact[i, j] = -wvar
    terms = []
    for j in range(1, n + 1):
        terms.append(assign(['t', j], c.mul(q[n, j], c.x[j]), (exact[n, j], j)))
    disjunction_lit = terms[0]
    disjunction_root = positive[terms[0]]
    for j, term in enumerate(terms[1:], 2):
        disjunction_root = c.add(disjunction_root, positive[term])
        dvar = assign(['d', j], c.complement(disjunction_root), (-disjunction_lit, -term))
        disjunction_lit = -dvar
    assign(['h'], disjunction_root, (disjunction_lit, disjunction_lit))
    assert cursor == original_count
    all_one = {i: 1 for i in range(1, n + 1)}
    for z, a, b in gates[:original_count]:
        av = all_one[abs(a)] ^ (a < 0)
        bv = all_one[abs(b)] ^ (b < 0)
        all_one[z] = av & bv
    prefix = {1: c.x[1]}
    for i in range(2, n + 1):
        prefix[i] = c.mul(prefix[i - 1], c.x[i])
    active_prefix = 1
    accum = 1
    accum_prefixes = {}
    for z, _, _ in gates[:original_count]:
        tag = tags[z]
        if tag[0] == 'u' and tag[1] >= 2:
            threshold = tag[1] if corrupt_cutoff else tag[1] - 1
            if tag[2] == threshold:
                active_prefix = tag[1]
        eps = z if all_one[z] else -z
        accum = assign(['accumulator', z, active_prefix], prefix[active_prefix], (accum, eps))
        accum_prefixes[accum] = active_prefix
    assert cursor == len(gates)
    relations, deltas = {}, {}
    for z, a, b in gates:
        delta = c.add(positive[z], c.mul(signed_root(a), signed_root(b)))
        deltas[z] = delta
        relations[z] = c.mul(delta, c.j)
    return proof, c, positive, signed, relations, deltas, accum_prefixes


def check_assignments(proof, c, positive, signed):
    n = proof['n']
    evidence = []
    for bits in itertools.product((0, 1), repeat=n):
        expected = {i: bits[i - 1] for i in range(1, n + 1)}
        values = c.evaluate(bits)
        for z, a, b in proof['gates']:
            av = expected[abs(a)] ^ (a < 0)
            bv = expected[abs(b)] ^ (b < 0)
            expected[z] = av & bv
            assert values[positive[z]] == expected[z], (n, bits, z)
            assert values[signed[z]] == 1 ^ expected[z], (n, bits, z, 'sign')
        evidence.append(dict(bits=bits, all_positive_extension_values=[expected[z] for z, _, _ in proof['gates']]))
    return evidence


def check(n):
    proof, c, positive, signed, relations, deltas, prefixes = build_data(n)
    g = proof['circuit_gate_count']
    s = 2 * n + 4 * g + 2
    roots = list(positive.values()) + list(signed.values()) + [c.zero, c.one] + list(relations.values())
    d, h = n + 1, 2 * n + 3
    assert max(c.degrees[root] for root in positive.values()) <= d
    assert max(c.degrees[root] for root in signed.values()) <= d
    assert max(c.degrees[root] for root in relations.values()) <= h
    node_bound = 100 * (n + 2) ** 2
    assert len(c.nodes) <= 4 * ((n*n + 3*n)//2) + 8*g + 6*n + 5 <= node_bound
    assert len(roots) == s + 2*g <= 20 * (n + 2) ** 2
    ell = (node_bound + 1).bit_length()
    rooted_bits = 0
    for root in roots:
        pending, reachable = [root], set()
        while pending:
            node = pending.pop()
            if node in reachable:
                continue
            reachable.add(node)
            op, *args = c.nodes[node]
            if op in ('add', 'mul'):
                pending.extend(args)
        rooted_bits += 16 * (len(reachable) + 1) * ell
    # Fully padded root encodings plus abstract records and original axiom framing.
    e_bits = rooted_bits + 16*s*ell + 128*(n+2)**2*ell
    e_bound = 16*len(roots)*(node_bound+1)*ell + 16*s*ell + 128*(n+2)**2*ell
    assert e_bits <= e_bound
    assignments = check_assignments(proof, c, positive, signed) if n <= 6 else []
    formal_evidence = []
    omission_detected = None
    if n == 2:
        substituted = c.words('axioms')
        zero = c.words('zero')
        independent = c.words('independent')
        for z, _, _ in proof['gates']:
            assert substituted[relations[z]] == substituted[deltas[z]]
            assert not zero[relations[z]]
            assert max(map(len, independent[relations[z]]), default=0) <= h
            formal_evidence.append(dict(gate=z, delta_words=sorted(substituted[deltas[z]]),
                                        H_words=sorted(independent[relations[z]]),
                                        substituted_H_words=sorted(substituted[relations[z]]), zero_H_words=[]))
        first = proof['gates'][0][0]
        bad = word_product(substituted[deltas[first]], {(), ('x1',)})
        omission_detected = bad != substituted[deltas[first]]
        assert omission_detected
    summary = dict(n=n, extensions=2*g, abstract_nodes=s, gates=len(c.nodes), gate_bound=node_bound,
                   representative_degree_actual=max(c.degrees[r] for r in positive.values()), d=d,
                   witness_degree_actual=max(c.degrees[r] for r in relations.values()), h=h,
                   E_padded_bits=e_bits, E_bound_bits=e_bound, exhaustive_assignments=len(assignments),
                   formal_relations_checked=len(formal_evidence), failures=[])
    certificate = dict(n=n, nodes=c.nodes, degrees=c.degrees, original_axioms=proof['original'],
                       boolean_axioms=list(range(1,n+1)), pair_axioms=list(itertools.combinations(range(1,n+1),2)),
                       positive_roots=positive, signed_roots=signed, relation_roots=relations, delta_roots=deltas,
                       actual_signed_and_definitions=proof['gates'], accumulator_prefixes=prefixes,
                       assignments=assignments, formal_evidence=formal_evidence,
                       omitted_clause_corruption_detected=omission_detected, summary=summary)
    return summary, certificate


def main():
    summaries, certificates = [], []
    for n in (2, 4, 6, 10, 20, 40):
        summary, certificate = check(n)
        summaries.append(summary)
        certificates.append(certificate)
    proof, c, positive, signed, *_ = build_data(2, corrupt_cutoff=True)
    try:
        check_assignments(proof, c, positive, signed)
    except AssertionError as error:
        cutoff_failure = str(error)
    else:
        raise AssertionError('corrupted accumulator cutoff accepted')
    output = Path(__file__).with_name('data-results.json')
    output.write_text(json.dumps(dict(summary=summaries, cutoff_corruption_failure=cutoff_failure,
                                      certificates=certificates), indent=2) + '\n')
    for row in summaries:
        print(f"n={row['n']}: gates={row['gates']}/{row['gate_bound']}, "
              f"degree={row['representative_degree_actual']}/{row['d']}, "
              f"H degree={row['witness_degree_actual']}/{row['h']}, "
              f"E={row['E_padded_bits']}/{row['E_bound_bits']} bits, "
              f"assignments={row['exhaustive_assignments']}, formal relations={row['formal_relations_checked']}; failures=[]")
    print(f'Accumulator corruption rejected: {cutoff_failure}; omitted-clause corruption rejected; certificate: {output}')


if __name__ == '__main__':
    main()
