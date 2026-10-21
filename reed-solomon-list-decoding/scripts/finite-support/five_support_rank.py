"""Exact certificate for the single gate-approved five-support system."""
import hashlib
import itertools
import json
from pathlib import Path

P = 65537
H = 19139
OUT = Path(__file__).with_name("five-support-rank-results.json")


def product(a, b):
    return [[sum(x * y for x, y in zip(row, col)) % P
             for col in zip(*b)] for row in a]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def apply(a, op):
    kind, i, j, c = op
    if kind == "swap":
        a[i], a[j] = a[j], a[i]
    elif kind == "scale":
        assert c % P != 0
        a[i] = [c * x % P for x in a[i]]
    else:
        assert kind == "add" and i != j
        a[i] = [(x + c * y) % P for x, y in zip(a[i], a[j])]


def reduce(matrix):
    a = [row[:] for row in matrix]
    t = identity(len(a))
    ops, pivots, raw_pivots = [], [], []
    determinant, sign = 1, 1

    def step(op):
        ops.append(op)
        apply(a, op)
        apply(t, op)

    for col in range(len(a[0])):
        row = len(pivots)
        candidate = next((i for i in range(row, len(a)) if a[i][col]), None)
        if candidate is None:
            continue
        if candidate != row:
            step(["swap", row, candidate, 0])
            sign = -sign
        pivot = a[row][col]
        raw_pivots.append(pivot)
        determinant = determinant * pivot % P
        step(["scale", row, row, pow(pivot, -1, P)])
        for i in range(len(a)):
            if i != row and a[i][col]:
                step(["add", i, row, -a[i][col] % P])
        pivots.append(col)
    det = sign * determinant % P if len(pivots) == len(a) else 0
    return dict(rref=a, transform=t, operations=ops, pivots=pivots,
                raw_pivots=raw_pivots, determinant_sign=sign,
                swap_count=sum(op[0] == "swap" for op in ops),
                determinant=det, rank=len(pivots))


def independent_determinant(matrix):
    """Forward elimination: last pivot, no normalization, below-only clearing."""
    a = [row[:] for row in matrix]
    det = 1
    for col in range(len(a)):
        candidates = [i for i in range(col, len(a)) if a[i][col]]
        if not candidates:
            return 0
        i = candidates[-1]
        if i != col:
            a[i], a[col] = a[col], a[i]
            det = -det
        pivot = a[col][col]
        det = det * pivot % P
        for i in range(col + 1, len(a)):
            c = a[i][col] * pow(pivot, -1, P) % P
            a[i] = [(x - c * y) % P for x, y in zip(a[i], a[col])]
    return det


def main():
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    domain = [pow(H, e, P) for e in range(1024)]
    check("generator_order", pow(H, 1024, P) == 1 and pow(H, 512, P) == P - 1)
    check("domain_distinct_nonzero", len(set(domain)) == 1024 and 0 not in domain)
    edges = list(itertools.combinations(range(1, 6), 2))
    core = domain[20:79]
    overlaps = [domain[2*r:2*r+2] for r in range(10)]
    private = [[domain[78+i]] for i in range(1, 6)]
    pieces = [core] + overlaps + private
    flat = [x for part in pieces for x in part]
    check("pieces_disjoint", len(flat) == 84 == len(set(flat)))
    check("piece_sizes", len(core) == 59 and all(len(u) == 2 for u in overlaps)
          and all(len(w) == 1 for w in private))
    supports = []
    for i in range(1, 6):
        s = set(core + private[i-1])
        for edge, u in zip(edges, overlaps):
            if i in edge:
                s.update(u)
        supports.append(sorted(s))
        check(f"support_{i}_size", len(s) == 68)
    pair_intersections = []
    for edge, u in zip(edges, overlaps):
        i, j = edge
        intersection = sorted(set(supports[i-1]) & set(supports[j-1]))
        pair_intersections.append(dict(edge=list(edge), points=intersection))
        check(f"intersection_{i}{j}", intersection == sorted(core+u))
    higher_intersections = []
    for size in range(3, 6):
        for indices in itertools.combinations(range(1, 6), size):
            intersection = sorted(set.intersection(*(set(supports[i-1]) for i in indices)))
            higher_intersections.append(dict(indices=list(indices), points=intersection))
            check("intersection_" + "".join(map(str, indices)), intersection == sorted(core))
    maps, matrix, row_labels = [], [], []
    for edge, u in zip(edges, overlaps):
        i, j = edge
        d = [[0] * 20 for _ in range(5)]
        for degree in range(5):
            if i < 5:
                d[degree][5*(i-1)+degree] = 1
            if j < 5:
                d[degree][5*(j-1)+degree] = P-1
        maps.append(dict(edge=list(edge), coefficient_map=d))
        for x in u:
            row = [sum(pow(x, degree, P)*d[degree][col] for degree in range(5)) % P
                   for col in range(20)]
            matrix.append(row)
            row_labels.append(dict(edge=list(edge), point=x))
    reduction = reduce(matrix)
    replay = [row[:] for row in matrix]
    replay_t = identity(20)
    for op in reduction["operations"]:
        apply(replay, op)
        apply(replay_t, op)
    check("operation_replay", replay == reduction["rref"] and replay_t == reduction["transform"])
    check("full_transformation_identity", product(reduction["transform"], matrix) == reduction["rref"])
    independent_det = independent_determinant(matrix)
    check("independent_determinant", independent_det == reduction["determinant"])
    check("full_rank", reduction["rank"] == 20 and reduction["rref"] == identity(20)
          and reduction["pivots"] == list(range(20)) and independent_det != 0)
    # Verify the inverse identity in the other order as well.
    check("right_inverse_identity", product(matrix, reduction["transform"]) == identity(20))
    distinctions = [dict(edge=list(edge), restriction_to_kernel="zero",
                         augmented_rank=20, possible=False) for edge in edges]
    check("all_ten_distinctions_impossible", len(distinctions) == 10 and reduction["rank"] == 20)
    failures = [name for name, ok in checks.items() if not ok]
    certificate = dict(
        modulus=P, generator=H, generator_checks=dict(power_1024=pow(H, 1024, P),
                                                     power_512=pow(H, 512, P)),
        domain=domain, edges=[list(e) for e in edges], core=core, overlaps=overlaps,
        private=private, supports=supports, pair_intersections=pair_intersections,
        higher_intersections=higher_intersections, row_labels=row_labels,
        difference_maps=maps, matrix=matrix, reduction=reduction,
        independent_determinant=independent_det, kernel_basis=[], distinctions=distinctions,
        checks=checks, failures=failures,
        conclusion="forbidden for every m>=1" if not failures else "not certified",
        bounds=dict(actual_rank=reduction["rank"], required_full_rank=20,
                    reduced_degree_max=4, message_degree_max=63, required_message_degree_lt=64),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    OUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps(dict(rank=reduction["rank"], required_rank=20,
                          determinant=reduction["determinant"], checks=len(checks),
                          failures=failures, conclusion=certificate["conclusion"],
                          certificate=str(OUT)), indent=2))
    assert not failures


if __name__ == "__main__":
    main()
