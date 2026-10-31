"""Exact fixed-example audit; does not import or execute the generator.

Run from the notebook: python3 scripts/signed-allocation/l511_independent_audit.py
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[2]
SOURCE = BASE / "scripts/signed-allocation/genuine-shared-budget-certificate.json"
LEMMA = BASE / "lemmas/L511-individual-compensation-without-joint-allocation.md"
OUT = BASE / "scripts/signed-allocation/l511-independent-audit.json"
saved = json.loads(SOURCE.read_text())
text = LEMMA.read_text()
checks, evidence = [], {}


def check(name, condition):
    checks.append({"name": name, "passed": bool(condition)})


def add(*polys):
    out = [F(0)] * max(map(len, polys))
    for p in polys:
        for i, c in enumerate(p):
            out[i] += c
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(p, c):
    return [c * a for a in p]


def mul(*polys):
    out = [F(1)]
    for p in polys:
        nxt = [F(0)] * (len(out) + len(p) - 1)
        for i, a in enumerate(out):
            for j, b in enumerate(p):
                nxt[i+j] += a*b
        out = nxt
    return out


def affine(p, offset, slope):
    # Horner composition, independent of the certificate generator.
    out = [F(0)]
    for c in reversed(p):
        out = add(mul(out, [offset, slope]), [c])
    return out


def fractions(values):
    return [F(v) for v in values]


def integers(vector):
    return [int(v.strip()) for v in vector.split(",")]


h, r = F(11, 16), F(5, 4)
check("fixed parameters", F(saved["h"]) == h and F(saved["r"]) == r)
A = [h*h+1, -2*h, F(1)]
B = [h*h+1, 2*h, F(1)]
M = [-r*r, F(0), F(1)]
Nh, Nm = add(A, [-2]), add(B, [-2])
real_num = [2*r*r, F(0), F(2)]
P = add(scale(mul(Nh, M, M), 2), mul(real_num, A, A))
Qx = add(scale(mul(Nh, B, B, M, M), 2),
         scale(mul(Nm, A, A, M, M), 2), mul(real_num, A, A, B, B))
check("aggregate numerator even", all(c == 0 for c in Qx[1::2]))
Q = Qx[::2]
check("individual reflection numerator", affine(P, F(0), F(-1)) ==
      add(scale(mul(Nm, M, M), 2), mul(real_num, B, B)))

for name, p, printed_label in [("individual", P, "P"), ("aggregate_y", Q, "Q")]:
    section = saved["full_domain_certificates"][name]
    check(name + " saved numerator", p == fractions(section["polynomial_ascending"]))
    match = re.search(r"\b" + printed_label + r": \(([^)]+)\)", text)
    check(name + " printed numerator", p == fractions(match.group(1).replace("\n", "").split(",")))

table_rows = re.findall(r"^\| \[([^]]+)\] \| ([0-9, ]+) \|$", text, re.M)
tail_matches = re.findall(r"\n    \(([0-9,\s]+)\)[,.]", text)
check("printed table/tail counts", len(table_rows) == 8 and len(tail_matches) == 3)

for name, p, expected_intervals, factor, start, tail_defs in [
    ("individual", P, [(F(-2),F(0)), (F(0),F(1,2)), (F(1,2),F(1)), (F(1),F(2))],
     7864320, 0, [("right", F(2), F(1), 524288, 0), ("left", F(-2), F(-1), 524288, 1)]),
    ("aggregate_y", Q, [(F(0),F(1,2)), (F(1,2),F(1)), (F(1),F(2)), (F(2),F(4))],
     171798691840, 4, [("right", F(4), F(1), 34359738368, 2)])]:
    section = saved["full_domain_certificates"][name]
    n = len(p)-1
    rows = []
    check(name + " interval count", len(section["leaves"]) == 4)
    for j, (lo, hi) in enumerate(expected_intervals):
        leaf = section["leaves"][j]
        check(f"{name} interval {j} endpoints", (F(leaf["lo"]),F(leaf["hi"])) == (lo,hi))
        power = affine(p, lo, hi-lo)
        # Invert the triangular Bernstein-to-power expansion. This avoids
        # using the displayed forward formula to reproduce its own output.
        bern = []
        for m in range(n+1):
            known = sum(bern[k]*comb(n,k)*comb(n-k,m-k)*(-1)**(m-k) for k in range(m))
            bern.append((power[m]-known)/comb(n,m))
        rebuilt = [sum(bern[k]*comb(n,k)*comb(n-k,m-k)*(-1)**(m-k)
                       for k in range(m+1)) for m in range(n+1)]
        check(f"{name} interval {j} identity", rebuilt == power)
        check(f"{name} interval {j} saved coefficients", bern == fractions(leaf["bernstein"]))
        row_lohi, row_values = table_rows[start+j]
        check(f"{name} interval {j} printed endpoints", tuple(fractions(row_lohi.split(","))) == (lo,hi))
        check(f"{name} interval {j} printed coefficients", scale(bern, factor) == integers(row_values))
        check(f"{name} interval {j} strict bound", min(bern) == F(leaf["lower_bound"]) and min(bern) > 0)
        rows.append({"lo":lo,"hi":hi,"power":power,"bernstein":bern,"lower_bound":min(bern)})
    tails = {}
    for direction, offset, slope, tail_scale, printed_index in tail_defs:
        coeff = affine(p, offset, slope)
        check(name + " " + direction + " saved tail", coeff == fractions(section["tails_power_coefficients"][direction]))
        check(name + " " + direction + " printed tail", scale(coeff, tail_scale) == integers(tail_matches[printed_index]))
        check(name + " " + direction + " strict tail", coeff[0] > 0 and all(c >= 0 for c in coeff))
        tails[direction] = {"offset":offset,"slope":slope,"coefficients":coeff,"lower_bound":coeff[0]}
    evidence[name] = {"numerator":p,"intervals":rows,"tails":tails}

# Construct the original rows from evaluation definitions, not saved entries.
s = F(9,32)
kernel = lambda c,x: 2*((x-c)**2-1)/((x-c)**2+1)**2
a, b, k = 1/(s+r)**2, 1/(s-r)**2, kernel(h,s)
matrix = [[-a,0,-b,0], [0,-b,0,-a], [1,1,0,0], [0,0,1,1],
          [-1,0,0,0], [0,-1,0,0], [0,0,-1,0], [0,0,0,-1]]
rhs = [k,k,1,1,0,0,0,0]
lam = [1,1,b,b,b-a,0,0,b-a]
transpose = [sum(lam[i]*matrix[i][j] for i in range(8)) for j in range(4)]
value = sum(lam[i]*rhs[i] for i in range(8))
dual = saved["dual"]
check("reflected evaluation and excluded poles", kernel(-h,-s) == k and s not in (-r,r) and -s not in (-r,r))
check("evaluation scalars", (s,a,b,k) == tuple(F(dual[v]) for v in ("s","A","B","K")))
check("row and variable order", dual["variable_order"] == ["alpha_h","alpha_minus_h","beta_h","beta_minus_h"] and
      dual["row_order"] == ["pair h at s","pair -h at -s","alpha budget","beta budget",
                            "alpha_h>=0","alpha_minus_h>=0","beta_h>=0","beta_minus_h>=0"])
check("original eight rows", matrix == [fractions(row) for row in dual["matrix"]])
check("original rhs", rhs == fractions(dual["rhs"]))
check("multipliers", lam == fractions(dual["multipliers"]) and min(lam) >= 0 and 0 < a < b)
check("annihilation", transpose == fractions(dual["transpose_times_multipliers"]) == [0]*4)
check("strict contradiction", value == F(dual["dual_value"]) == F(-450684928,1367742289) and value < 0)
check("printed k+b", k+b == F(dual["K_plus_B"]) == F(-225342464,1367742289))
check("individual at selected point", k+a+b == F(dual["individual_full_budget_at_s"]) and k+a+b > 0)
# Degree checks justify both stated limits once denominators are restored.
check("individual infinity limit", len(P)-1 == 6 and P[-1] == F(saved["tails"]["individual_x_squared_limit"]) == 4)
check("aggregate infinity limit", len(Qx)-1 == 10 and Qx[-1] == F(saved["tails"]["aggregate_x_squared_limit"]) == 6)
evidence["dual"] = {"s":s,"a":a,"b":b,"k":k,"matrix":matrix,"rhs":rhs,
                    "multipliers":lam,"transpose":transpose,"value":value}
failures = [c["name"] for c in checks if not c["passed"]]
report = {"source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
          "method":"Independent stdlib Fraction polynomial construction and triangular Bernstein inversion; generator never imported or executed",
          "checks":checks,"evidence":evidence,"failures":failures,"passed":not failures,
          "required":{"bernstein_minimum":">0","tail_constant":">0","other_tail_coefficients":">=0","dual_value":"<0"},
          "limitations":"Finite first-sign theorem only. Analytic domain/reflection and dual logical applicability reviewed in L511. No Xi realization, higher signs or novelty certification."}
OUT.write_text(json.dumps(report, default=str, indent=2)+"\n")
print(json.dumps({"passed":not failures,"checks":len(checks),"failures":failures,
                  "actual_bounds":{name:min(row["lower_bound"] for row in evidence[name]["intervals"])
                                   for name in ("individual","aggregate_y")},
                  "required_bounds":">0 on listed intervals; positive constant/nonnegative coefficients on tails",
                  "dual_actual":value,"dual_required":"<0","certificate":str(OUT.relative_to(BASE))}, default=str))
raise SystemExit(bool(failures))
