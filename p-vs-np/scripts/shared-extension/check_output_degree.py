#!/usr/bin/env python3
"""Fixed L021 output: independent free-word and placeholder-projection checks.

Finite expansions are diagnostics. The all-m degree proof is in L022.
No axiom substitution, Boolean reduction, or commuting of letters occurs.
"""

import importlib.util
import json
from pathlib import Path

from check_assembly import Assembly, verify
from check_witnesses import ZERO, ONE, add_poly, mul_poly


def load_family():
    path = Path(__file__).resolve().parents[1] / "er-unfolding" / "check_literal_substitution.py"
    spec = importlib.util.spec_from_file_location("used_extension_degree", path)
    family = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(family)
    return family


T1 = ("t", ("f", 0))


def expand_free(circuit, projected):
    values = []
    for spec in circuit.nodes:
        kind = spec[0]
        if kind == "c":
            value = ONE if spec[1] else ZERO
        elif kind == "x":
            value = frozenset({(("x", spec[1]),)})
        elif kind == "t":
            value = (ZERO if projected and spec[1] != ("f", 0)
                     else frozenset({(("t", spec[1]),)}))
        else:
            a, b = values[spec[1]], values[spec[2]]
            value = add_poly(a, b) if kind == "+" else mul_poly(a, b)
        values.append(value)
    return values


def projected_degree_upper(circuit):
    """Only an upper bound: None means known zero; ties may cancel."""
    values = []
    for spec in circuit.nodes:
        kind = spec[0]
        if kind == "c":
            degree = 0 if spec[1] else None
        elif kind == "x":
            degree = 1
        elif kind == "t":
            degree = 1 if spec[1] == ("f", 0) else None
        else:
            a, b = values[spec[1]], values[spec[2]]
            if kind == "*":
                degree = None if a is None or b is None else a + b
            else:
                degree = b if a is None else a if b is None else max(a, b)
        values.append(degree)
    return values


def scalar_recurrence(m):
    lengths = [1, 1]
    degrees = [0, None]
    for i in range(2, m + 1):
        lengths.append(lengths[-1] + lengths[-2])
        degrees.append(lengths[i] if i == 2 else
                       degrees[i - 1] + lengths[i - 2] + lengths[i])
    fib = [0, 1]
    for _ in range(m + 2):
        fib.append(fib[-1] + fib[-2])
    assert degrees[m] + 1 == fib[m + 3] + fib[m + 1] - 4
    assert degrees[m] + 1 >= 2 ** (m // 2)
    return degrees, lengths


def word_recurrence(m):
    words = [(('x', 1),), (('x', 2),)]
    residues = [ONE, ZERO]
    leading = None
    for i in range(2, m + 1):
        words.append(words[i - 1] + words[i - 2])
        residues.append(mul_poly(
            add_poly(mul_poly(residues[i - 1], frozenset({words[i - 2]})),
                     residues[i - 2]),
            add_poly(ONE, frozenset({words[i]}))))
        leading = words[2] if i == 2 else leading + words[i - 2] + words[i]
        top_degree = max(map(len, residues[i]))
        assert [word for word in residues[i] if len(word) == top_degree] == [leading]
    return words, residues, leading


def main():
    family = load_family()
    small = []
    for m in range(2, 11):
        proof, _ = family.make_proof(m)
        verify(family.ORIGINAL, proof)
        assembly = Assembly(family.ORIGINAL, proof)
        values = expand_free(assembly.circuit, True)
        words, residues, leading = word_recurrence(m)
        degrees, _ = scalar_recurrence(m)
        positive_checks = negative_checks = 0
        for record, root in zip(proof, assembly.roots):
            c = record["clause"]
            if len(c) == 1 and c[0] > 0:
                i = c[0] - 1
                expected = frozenset({(T1,) + word for word in residues[i]})
                assert values[root] == expected
                positive_checks += 1
            if len(c) == 1 and c[0] < 0:
                assert values[root] == ZERO
                negative_checks += 1
        final = values[assembly.roots[-1]]
        assert final == frozenset({(T1,) + word for word in residues[m]})
        assert max(map(len, final)) == degrees[m] + 1
        assert (T1,) + leading in final
        full_degree = None
        if m <= 6:
            full = expand_free(assembly.circuit, False)[assembly.roots[-1]]
            assert all(sum(token[0] == "t" for token in word) == 1 for word in full)
            assert frozenset(word for word in full if T1 in word) == final
            full_degree = max(map(len, full))
        small.append({"m": m, "projected_formal_degree": degrees[m] + 1,
                      "projected_monomials": len(final), "full_formal_degree": full_degree,
                      "positive_unit_checks": positive_checks,
                      "negative_unit_checks": negative_checks})
    large = []
    for m in (16, 32, 64, 128):
        proof, _ = family.make_proof(m)
        verify(family.ORIGINAL, proof)
        assembly = Assembly(family.ORIGINAL, proof)
        degrees, _ = scalar_recurrence(m)
        upper = projected_degree_upper(assembly.circuit)[assembly.roots[-1]]
        assert upper == degrees[m] + 1
        large.append({"m": m, "T_bits": 2 + sum(family.binary_cost(proof)),
                      "projected_degree_upper": str(upper),
                      "proved_surviving_degree": str(degrees[m] + 1),
                      "word_expansion": False})
    result = {"scope": "Exact projected words through m=10 and full free-placeholder words through m=6; larger DAG upper bounds only. General lower bound requires L022's induction.",
              "small_cases": small, "large_cases": large}
    Path(__file__).with_name("output-degree-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
