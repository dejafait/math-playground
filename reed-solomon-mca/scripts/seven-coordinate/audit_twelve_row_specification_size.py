"""Independent circuit/degree and complete small-certificate audit; no solver.

Nodes carry formal degree upper bounds, not polynomial values. Constant table
entries are charged even when zero. Thus this reconstructs an upper-bound
circuit template, not a concrete pair instance or a polynomial certificate.
No producer routines or count dictionaries are imported.
"""
import hashlib
import json
from itertools import combinations
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
counts = {}
group = ""


class Node:
    def __init__(self, degree):
        self.degree = degree

    def __add__(self, other):
        counts[group] = counts.get(group, 0) + 1
        return Node(max(self.degree, other.degree))

    __sub__ = __add__

    def __mul__(self, other):
        counts[group] = counts.get(group, 0) + 1
        return Node(self.degree + other.degree)


constant = Node(0)
unknowns = []


def variable():
    n = Node(1)
    unknowns.append(n)
    return n


def total(nodes):
    nodes = list(nodes)
    result = nodes[0]
    for n in nodes[1:]:
        result = result + n
    return result


def product(nodes):
    nodes = list(nodes)
    result = nodes[0]
    for n in nodes[1:]:
        result = result * n
    return result


generators = {}


def equation(kind, node):
    generators.setdefault(kind, []).append(node.degree)


theta = [variable() for _ in range(9)]
m11, m12, m21, m22, det_inverse = [variable() for _ in range(5)]
tables = [[constant] * 51 for _ in range(2)]
for slot in range(10):
    bits = [variable() for _ in range(10)]
    group = "bit_complements"
    complements = [constant - b for b in bits]
    group = "indicators"
    indicators = [product(bits[i] if (a >> i) & 1 else complements[i]
                          for i in range(10)) for a in range(comb(7, 2)*comb(9, 2))]
    group = "lookup_tables"
    tables.append([total(d * constant for d in indicators) for _ in range(16+7+4*7)])
    group = "validity"
    equation("valid_support", total(indicators) - constant)
    group = "boolean"
    for b in bits:
        equation("boolean", b * (b - constant))

group = "kernel_coordinates"
p = {pair: total(t * constant for t in theta) for pair in combinations(range(7), 2)}
group = "signed_frame"
# All pivots have the same degree/gate bounds. Each of fourteen aliases
# is charged a sign multiplication, including zero and positive aliases.
pivot = (0, 1)
def exterior(i, j):
    return constant if i == j else p[tuple(sorted((i, j)))]
U = [exterior(x, pivot[1]) * constant for x in range(7)]
V = [exterior(pivot[0], x) * constant for x in range(7)]
group = "chart_vectors"
u = [m11 * x + m12 * y for x, y in zip(U, V)]
v = [m21 * x + m22 * y for x, y in zip(U, V)]
group = "pivot"
equation("pivot", p[pivot] - constant)
group = "plucker"
for i, j, k, l in combinations(range(7), 4):
    equation("plucker", p[i,j]*p[k,l] - p[i,k]*p[j,l] + p[i,l]*p[j,k])
group = "chart_inverse"
equation("chart_invertible", det_inverse*(m11*m22-m12*m21)-constant)
group = "pair_incidence"
for s, t in combinations(range(12), 2):
    c = total(tables[s][x]*tables[t][x] for x in range(16))
    equation("pair_incidence", c*(c-constant))
group = "label_degree"
for x in range(16):
    n = total(tables[s][x] for s in range(12))
    equation("label_degree", product([n]+[n-constant for _ in range(4)]))
for table in tables:
    gamma, lam, inverse = [variable() for _ in range(3)]
    weights = [variable() for _ in range(7)]
    eta = [variable() for _ in range(4)]
    group = "shortening"
    errors = []
    for x in range(7):
        error = u[x]+gamma*v[x]-lam*table[16+x]
        errors.append(error)
        equation("row_gates", (constant-table[x])*error)
    group = "overlap_weights"
    for x in range(7):
        equation("row_gates", table[x]*(errors[x]*weights[x]-constant))
    group = "lambda_inverse"
    equation("row_gates", lam*inverse-constant)
    group = "projection"
    projections = [total(table[23+7*r+x]*v[x] for x in range(7)) for r in range(4)]
    equation("row_gates", total(e*y for e, y in zip(eta, projections))-constant)

before_field_count = sum(map(len, generators.values()))
before_field_gates = sum(counts.values())
degree_bound = max(d for ds in generators.values() for d in ds)
Q = 97**20
group = "field_equations"
for x in unknowns:
    power = x
    for digit in bin(Q)[3:]:
        power = power*power
        if digit == "1":
            power = power*x
    equation("field_equations", power-x)

source = HERE / "twelve-row-specification-size.json"
saved = json.loads(source.read_text())
checks = []
def check(name, actual, required):
    checks.append({"name": name, "actual": actual, "required": required,
                   "pass": actual == required})

supports = comb(7,2)*comb(9,2)
pairs = comb(7,4)*comb(9,4)*3*6
branches = pairs*comb(7,2)
derived = {
    "variables_per_branch": len(unknowns),
    "equations_before_field_total": before_field_count,
    "field_equations": len(unknowns),
    "equations_per_branch": sum(map(len, generators.values())),
    "field_order": str(Q), "field_order_bits": len(bin(Q))-2,
    "field_order_popcount": bin(Q).count("1"),
    "power_gates_per_variable": counts["field_equations"]//len(unknowns)-1,
    "nonfield_degree_upper_bound": degree_bound,
    "gates_per_branch_upper_bound": sum(counts.values()),
    "pair_branches": pairs, "plucker_charts": comb(7,2),
    "pair_chart_branches": branches,
    "factored_projection_pivot_combinations": 4**12,
    "ordered_extra_support_assignments_before_gates": str(supports**10),
    "explicit_all_branch_variables": branches*len(unknowns),
    "explicit_all_branch_equations": branches*sum(map(len, generators.values())),
    "explicit_all_branch_gate_upper_bound": branches*sum(counts.values()),
}
for key, value in derived.items():
    check(key, value, saved[key])
check("variable_partition", {"kernel":9, "chart_matrix":4, "chart_inverse":1,
      "support_bits":10*10, "row_witnesses":12*(3+7+4)}, saved["variables"])
check("generator_partition", {k:len(v) for k,v in generators.items()
      if k != "field_equations"}, saved["equations_before_field"])
check("circuit_partition", counts, saved["arithmetic_gate_upper_bounds"])
check("field_generator_degrees", sorted(set(generators["field_equations"])), [Q])
check("fixed_coefficient_variant", derived["equations_per_branch"]+2*7, 717)
# Complete finite records, checked using binary-word uniqueness and root sets,
# independently of the producer's products. No truncated preview is evidence.
expected_codes = [{"code":n, "selected":[n] if n < supports else []}
                  for n in range(2**10)]
check("all_1024_selector_records", saved["lookup_domain_checks"], expected_codes)
expected_counts = [{"integer_count":n, "linear_gate":n in {0,1},
                    "degree_gate":n in {0,1,2,3,4}} for n in range(17)]
check("all_17_integer_records", saved["integer_gate_checks"], expected_counts)
check("producer_failures", saved["failures"], [])
failures = [c for c in checks if not c["pass"]]
result = {
    "scope":"Independent formal circuit upper bounds and complete size-record comparison; no feasibility test",
    "derived":derived, "nonfield_gate_count":before_field_gates,
    "gate_groups":counts, "generator_degrees":generators,
    "checks":checks, "failures":failures,
    "summary":{"checks":len(checks), "failures":len(failures),
               "variables":len(unknowns), "equations":sum(map(len,generators.values())),
               "gates":sum(counts.values()), "nonfield_degree_bound":degree_bound},
    "input_sha256":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in (source, HERE/"twelve_row_specification_size.py",
                              ROOT/"drafts/2026-10-25-twelve-row-certificate-specification.md")},
    "qualifications":["Degree propagation ignores cancellations and is an upper bound",
                      "Lookup constants and signs are charged symbolically, not instantiated",
                      "Input pair kernels are imported from L153, not replayed",
                      "No certificate-multiplier degree or tractability bound",
                      "Shared Python integer arithmetic; no formal verification"],
}
path = HERE / "twelve-row-specification-critical-audit.json"
path.write_text(json.dumps(result, indent=2)+"\n")
print(f"checks={len(checks)}; failures={len(failures)}; variables={len(unknowns)}; equations={sum(map(len,generators.values()))}")
print(f"derived degree bound={degree_bound}; required<=50; gates={sum(counts.values())}; required<=907486")
print(f"branches={branches}; required=1666980; certificate={path}")
for failure in failures:
    print(f"FAIL: {failure['name']}; inspect complete actual/required values in certificate")
if failures:
    raise SystemExit(1)
