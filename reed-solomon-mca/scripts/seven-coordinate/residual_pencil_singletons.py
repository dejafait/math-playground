"""Exact necessary singleton equations in L161's three residual pencils.

This checks scalar coefficient identities, not original quadruple ranks.
Run from the active notebook with python3 scripts/seven-coordinate/residual_pencil_singletons.py.
"""
from itertools import combinations, permutations
from pathlib import Path
import json

P = 97
S = (1, 8, 12, 18, 22, 27, 33)
J = (47, 50, 64, 70, 75, 79, 85, 89, 96)


def run():
    groups, failures = [], []
    for h in (8, 12, 22):
        fibers = {}
        for r in S:
            fibers.setdefault((r + h * pow(r, -1, P)) % P, []).append(r)
        paired = sorted(z for z, roots in fibers.items() if len(roots) == 2)
        lone = [z for z, roots in fibers.items() if len(roots) == 1]
        root_pairs = [pair for pair in combinations(J, 2) if pair[0]*pair[1] % P == h]
        sums = sorted(sum(pair) % P for pair in root_pairs)
        if len(paired) != 3 or len(lone) != 1 or len(sums) != 4 or len(set(sums)) != 4:
            failures.append(f'Unexpected pencil/fiber shape for h={h}')
            continue
        if set(fibers) & set(sums):
            failures.append(f'Zero reciprocal denominator for h={h}')
        records = []
        for B, D in permutations(paired, 2):
            R = next(z for z in paired if z not in (B, D))
            for A, C in ((R, lone[0]), (lone[0], R)):
                for a, b, c, d in permutations(sums):
                    # z/t equality and w equality, with denominators cleared.
                    f = ((D-c)*(B-d)*(C-b) - (D-b)*(B-c)*(C-d)) % P
                    g = ((C-d)*(D-a)*(A-c) - (C-a)*(D-c)*(A-d)) % P
                    # Independently evaluate the original rational identities.
                    def ratio(n, den):
                        return n * pow(den % P, -1, P) % P
                    v = ratio(D-c, D-b)
                    u = ratio(D-c, D-a)
                    f_rat = (v*ratio(B-d, B-c) - ratio(C-d, C-b)) % P
                    g_rat = (ratio(C-d, C-a) - u*ratio(A-d, A-c)) % P
                    if (f == 0) != (f_rat == 0) or (g == 0) != (g_rat == 0):
                        failures.append(f'Clearing-denominator mismatch: {h,B,D,A,C,a,b,c,d}')
                    records.append(dict(B=B,D=D,A=A,C=C,s=[a,b,c,d],
                                        residues=[f,g],rational_residues=[f_rat,g_rat]))
        # Independent Cartesian domain check, not just a count.
        expected = {(B,D,A,C,a,b,c,d)
                    for B in paired for D in paired if B != D
                    for A in fibers for C in fibers
                    if {A,C} == (set(fibers)-{B,D}) and A != C
                    for a in sums for b in sums for c in sums for d in sums
                    if len({a,b,c,d}) == 4}
        keys = {(r['B'],r['D'],r['A'],r['C'],*r['s']) for r in records}
        if keys != expected or len(keys) != len(records):
            failures.append(f'Coverage mismatch for h={h}')
        survivors = [i for i,r in enumerate(records) if r['residues'] == [0,0]]
        groups.append(dict(h=h,fibers=[dict(value=z,coordinates=roots) for z,roots in sorted(fibers.items())],
                           J_pairs=[dict(roots=pair,sum=sum(pair)%P) for pair in root_pairs],
                           records=records,actual_tests=len(records),required_tests=288,
                           first_equation_survivors=sum(r['residues'][0] == 0 for r in records),
                           simultaneous_survivors=survivors,
                           independent_domain_size=len(expected)))
    total = sum(g['actual_tests'] for g in groups)
    survivors = sum(len(g['simultaneous_survivors']) for g in groups)
    if total != 864:
        failures.append(f'Total coverage {total}, required 864')
    out = dict(modulus=P,S=S,J=J,groups=groups,actual_tests=total,required_tests=864,
               actual_simultaneous_survivors=survivors,required_for_exclusion=0,failures=failures)
    path = Path(__file__).with_name('residual-pencil-singletons.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(f'Scalar compatibility tests: actual {total}, required 864')
    for g in groups:
        print(f'h={g["h"]}: first equation survivors {g["first_equation_survivors"]}; '
              f'both equations {len(g["simultaneous_survivors"])}; coverage {g["actual_tests"]}/288')
    print(f'Simultaneous survivors: actual {survivors}, required for exclusion 0; failures: {failures}')
    print(f'Full certificate: {path}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
