#!/usr/bin/env python3
"""Finite ER checks for L027; the cited OBDD theorem is not tested here."""
import itertools
import json
from pathlib import Path


def uint_bits(k):
    """Elias gamma code of k+1, for nonnegative integers."""
    return 2 * (k + 1).bit_length() - 1


def clause_bits(clause):
    return uint_bits(len(clause)) + sum(1 + uint_bits(abs(x)) for x in clause)


def build(n):
    gates = []

    def gate(a, b):
        z = n + len(gates) + 1
        gates.append((z, a, b))
        return z

    zero = gate(1, -1)
    exact = {(0, 0): -zero}
    for i in range(1, n + 1):
        for j in range(i + 1):
            a = gate(exact.get((i - 1, j), zero), -i)
            b = gate(exact.get((i - 1, j - 1), zero), i)
            exact[i, j] = -gate(-a, -b)
    terms = [gate(exact[n, j], j) for j in range(1, n + 1)]
    out = terms[0]
    for term in terms[1:]:
        out = -gate(-out, -term)
    hard = gate(out, out)
    circuit_count = len(gates)
    expected = (3 * n * n + 13 * n + 2) // 2
    assert circuit_count == expected

    values = {i: True for i in range(1, n + 1)}

    def value(lit):
        return values[abs(lit)] if lit > 0 else not values[abs(lit)]

    for z, a, b in gates:
        values[z] = value(a) and value(b)
    assert values[hard]
    circuit = list(gates)
    accum = 1
    for z, _, _ in circuit:
        accum = gate(accum, z if values[z] else -z)
        values[accum] = True

    original = [[i] for i in range(1, n + 1)] + [[-1]]
    records = []

    def record(clause, kind, **fields):
        records.append(dict(clause=sorted(set(clause)), kind=kind, **fields))
        return len(records)

    units = {i: record([i], 'initial', index=i) for i in range(1, n + 1)}
    negative = record([-1], 'initial', index=n + 1)

    def resolve(left, right, pivot):
        a = set(records[left - 1]['clause'])
        b = set(records[right - 1]['clause'])
        assert pivot in a and -pivot in b
        return record((a - {pivot}) | (b - {-pivot}), 'resolution',
                      parents=[left, right], pivot=pivot)

    def define(z, a, b):
        return [record([-z, a], 'extension', gate=z, slot=0),
                record([-z, b], 'extension', gate=z, slot=1),
                record([z, -a, -b], 'extension', gate=z, slot=2)]

    def derive(z, a, b, defs):
        if values[z]:
            current = defs[2]
            for lit in (a, b):
                if -lit in records[current - 1]['clause']:
                    current = resolve(current, units[lit], -lit)
            assert records[current - 1]['clause'] == [z]
            units[z] = current
        else:
            operand, projection = (a, defs[0]) if not value(a) else (b, defs[1])
            current = resolve(projection, units[-operand], operand)
            assert records[current - 1]['clause'] == [-z]
            units[-z] = current

    for z, a, b in circuit:
        derive(z, a, b, define(z, a, b))
    for z, a, b in gates[circuit_count:]:
        defs = define(z, a, b)
        derive(z, a, b, defs)
        negative = resolve(defs[0], negative, a)
        assert records[negative - 1]['clause'] == [-z]
    final = resolve(units[accum], negative, accum)
    assert records[final - 1]['clause'] == []
    return dict(n=n, original=original, circuit_gate_count=circuit_count,
                gates=gates, hard_root=hard, final_root=accum, records=records)


def check(proof):
    n = proof['n']
    gates = {z: (a, b) for z, a, b in proof['gates']}
    records = proof['records']
    available = set(range(1, n + 1))
    active_gate = None
    next_slot = 0
    extension_refs = {}
    for k, rec in enumerate(records, 1):
        c = set(rec['clause'])
        assert len(c) <= 3
        if rec['kind'] == 'initial':
            assert c == set(proof['original'][rec['index'] - 1])
        elif rec['kind'] == 'extension':
            z, slot = rec['gate'], rec['slot']
            a, b = gates[z]
            if slot == 0:
                assert next_slot == 0 and z not in available
                assert abs(a) in available and abs(b) in available
                active_gate = z
            assert active_gate == z and slot == next_slot
            expected = ({-z, a}, {-z, b}, {z, -a, -b})[slot]
            assert c == expected
            extension_refs.setdefault(z, []).append(k)
            next_slot += 1
            if next_slot == 3:
                available.add(z)
                active_gate, next_slot = None, 0
        else:
            assert next_slot == 0 and rec['kind'] == 'resolution'
            left, right = rec['parents']
            assert 1 <= left < k and 1 <= right < k
            a, b = set(records[left - 1]['clause']), set(records[right - 1]['clause'])
            pivot = rec['pivot']
            assert pivot in a and -pivot in b
            assert c == (a - {pivot}) | (b - {-pivot})
        assert all(abs(lit) in available or
                   (rec['kind'] == 'extension' and abs(lit) == active_gate)
                   for lit in c)
    assert not records[-1]['clause'] and next_slot == 0
    ancestors, pending = set(), [len(records)]
    while pending:
        k = pending.pop()
        if k not in ancestors:
            ancestors.add(k)
            pending.extend(records[k - 1].get('parents', []))
    used = [z for z, refs in extension_refs.items() if any(k in ancestors for k in refs)]
    assert len(used) == len(gates)
    used_units = {abs(records[k - 1]['clause'][0]) for k in ancestors
                  if len(records[k - 1]['clause']) == 1}
    assert all(z in used_units for z in gates)
    assert any(proof['hard_root'] in map(abs, records[k - 1]['clause']) for k in ancestors)
    # Complete explicit binary code: gamma(n), gamma(clause count), each clause;
    # gamma(record count), 2-bit kind, clause, and gamma-coded rule metadata.
    fbits = uint_bits(n) + uint_bits(len(proof['original']))
    fbits += sum(clause_bits(c) for c in proof['original'])
    pbits = uint_bits(len(records))
    for rec in records:
        pbits += 2 + clause_bits(rec['clause'])
        if rec['kind'] == 'initial':
            pbits += uint_bits(rec['index'])
        elif rec['kind'] == 'extension':
            pbits += uint_bits(rec['gate']) + 2
        else:
            pbits += sum(uint_bits(k) for k in rec['parents'])
            pbits += 1 + uint_bits(abs(rec['pivot']))
    g = proof['circuit_gate_count']
    record_bound = 11 * g + n + 2
    assert len(records) <= record_bound
    # Every record and original clause needs <=64L bits, L=ceil(log2(R+2)).
    # Header terms fit the remaining allowance in this deliberately loose bound.
    ell = (record_bound + 1).bit_length()
    binary_bound = 128 * (record_bound + n + 3) * ell
    t = 2 + fbits + pbits
    assert t <= binary_bound
    exhaustive = []
    if n <= 6:
        for bits in itertools.product((False, True), repeat=n):
            vals = {i: bits[i - 1] for i in range(1, n + 1)}
            for z, a, b in proof['gates']:
                av = vals[abs(a)] if a > 0 else not vals[abs(a)]
                bv = vals[abs(b)] if b > 0 else not vals[abs(b)]
                vals[z] = av and bv
            weight = sum(bits)
            expected = bool(weight and bits[weight - 1])
            assert vals[proof['hard_root']] == expected
            exhaustive.append(dict(bits=list(map(int, bits)), weight=weight,
                                   hard_value=int(vals[proof['hard_root']])))
    return dict(n=n, circuit_gates=g, extensions=len(gates),
                records=len(records), record_bound=record_bound,
                used_extensions=len(used), unused_extensions=[],
                all_extension_units_in_ancestry=True,
                T_bits=t, required_polynomial_bound_bits=binary_bound,
                original_variables=list(range(1, n + 1)),
                exhaustive_hwb_evidence=exhaustive, failures=[])


def main():
    output = Path(__file__).with_name('embedding-results.json')
    certificates, summaries = [], []
    for n in (2, 4, 6, 10, 20, 40):
        proof = build(n)
        summary = check(proof)
        certificates.append(dict(proof=proof, checks=summary))
        summaries.append({k: v for k, v in summary.items()
                          if k not in ('exhaustive_hwb_evidence', 'original_variables')})
    bad = build(2)
    bad['records'][-1]['clause'] = [1]
    try:
        check(bad)
    except AssertionError:
        corruption_rejected = True
    else:
        raise AssertionError('corrupted final resolvent accepted')
    result = dict(summary=summaries, corruption_rejected=corruption_rejected,
                  obdd_lower_bound='Imported primary theorem, not numerically verified',
                  certificates=certificates)
    output.write_text(json.dumps(result, indent=2) + '\n')
    for s in summaries:
        print(f"n={s['n']}: extensions={s['extensions']}, used={s['used_extensions']}, "
              f"records={s['records']}/{s['record_bound']}, "
              f"T={s['T_bits']}/{s['required_polynomial_bound_bits']} bits; failures=[]")
    print(f'Corrupted resolvent rejected: {corruption_rejected}; certificate: {output}')


if __name__ == '__main__':
    main()
