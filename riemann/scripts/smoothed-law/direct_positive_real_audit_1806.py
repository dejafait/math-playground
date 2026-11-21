"""Independent finite-evidence audit of C033y/z; no scalar evaluation.

Read all relevant stored entries, independently reconstruct Legendre
coefficients by Rodrigues, integrate cardinal products, check every root
bracket and suppression decision, and reconstruct the error/cost ledger.
No original mathematical program is imported or original artifact changed.
"""
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
checks = {}
evidence = {}


def check(name, condition):
    checks[name] = bool(condition)


def load(stem):
    path = HERE / (stem + ".json")
    raw = path.read_bytes()
    evidence[str(path.relative_to(HERE))] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def poly_value(c, x):
    # Direct powers, independent of the original Horner evaluator.
    return sum((a*x**k for k, a in enumerate(c)), Q(0))


def cardinal_integral(nodes, i):
    c = [Q(1)]
    den = Q(1)
    for j, r in enumerate(nodes):
        if j == i:
            continue
        out = [Q(0)]*(len(c)+1)
        for k, a in enumerate(c):
            out[k] -= r*a
            out[k+1] += a
        c = out
        den *= nodes[i]-r
    return sum((2*a/Q(k+1) for k, a in enumerate(c) if k % 2 == 0), Q(0))/den


def verify_rule(rule, n):
    # Rodrigues: P_n = (2^n n!)^-1 (d/dx)^n (x^2-1)^n.
    c = [Q(0)]*(n+1)
    for j in range((n+1)//2, n+1):
        c[2*j-n] = Q((-1)**(n-j)*comb(n, j)*factorial(2*j),
                      2**n*factorial(n)*factorial(2*j-n))
    check(f"P{n}:Rodrigues_coefficients", c == list(map(Q, rule["coefficients_ascending"])))
    grid = [Q(j, 128) for j in range(129)]
    signs = [poly_value(c, x) for x in grid]
    positive_seeds = [(grid[j], grid[j+1]) for j in range(128) if signs[j]*signs[j+1] < 0]
    check(f"P{n}:positive_seed_count", len(positive_seeds) == n//2)
    check(f"P{n}:grid_zeros", [j for j, v in enumerate(signs) if v == 0] == ([0] if n % 2 else []))
    seeds = [(-b, -a) for a, b in reversed(positive_seeds)]
    if n % 2:
        seeds.append((Q(0), Q(0)))
    seeds += positive_seeds
    check(f"P{n}:seed_separation", all(seeds[j+1][0]-seeds[j][1] > Q(1, 32) for j in range(n-1)))
    roots = rule["roots"]
    check(f"P{n}:complete_root_count", len(roots) == n)
    nodes = []
    weights = []
    for i, (row, seed) in enumerate(zip(roots, seeds)):
        lo, hi, mid = (Q(row[k]) for k in ("left", "right", "midpoint"))
        va, vb = poly_value(c, lo), poly_value(c, hi)
        nodes.append(mid)
        weights.append(Q(row.get("cardinal_weight", row.get("weight"))))
        check(f"P{n}:root{i}:containment", -1 < seed[0] <= lo <= hi <= seed[1] < 1)
        check(f"P{n}:root{i}:values", va == Q(row["left_value"]) and vb == Q(row["right_value"]))
        check(f"P{n}:root{i}:existence", (lo == hi and va == 0) or va*vb < 0)
        check(f"P{n}:root{i}:midpoint_radius", mid == (lo+hi)/2 and (hi-lo)/2 <= Q(1, 2**168))
    for i in range(n):
        check(f"P{n}:weight{i}:exact_cardinal_integral", weights[i] == cardinal_integral(nodes, i))
    for k in range(n):
        check(f"P{n}:moment{k}", sum((w*x**k for w, x in zip(weights, nodes)), Q(0)) == (Q(2, k+1) if k % 2 == 0 else 0))
    return {"degree": n, "roots_checked": len(roots), "weights_checked": len(weights),
            "all_exact_brackets_checked": True, "independent_coefficients": list(map(str, c))}


def main():
    analytic = load("direct_positive_real_preflight_1800")
    core = load("direct_positive_real_inner_core_1801")
    inputs = load("direct_positive_real_inputs_1802")
    finish = load("direct_positive_real_completion_1803")
    rules = [verify_rule(r, n) for r, n in zip(inputs["rules"], (12, 13))]
    rules.append(verify_rule(finish["root_rule"], 14))

    c = [Q(row["c_k"]) for row in core["coefficients"]]
    for n in range(29):
        rhs = Q(1, 2**(n+1)*factorial(n+1))-(Q(1, factorial(n+2)) if n % 2 else 0)
        lhs = 2*sum((c[n-2*j]/factorial(2*j+1) for j in range(n//2+1)), Q(0))
        check(f"core:coefficient{n}", lhs == rhs and abs(c[n]) <= Q(6, 2**n))
    dE = Q(8*2**15, factorial(17))
    dS = Q(4**22, factorial(23))/(1-Q(16, 600))
    dR = (dE+dS/4)/2+2*dS
    check("core:quotient_remainder", dR == Q(core["bounds"]["quotient_remainder"]) and dR < Q(1, 2**28))
    delta = Q(1, 2**60)
    check("core:both_difference_errors", max(Q(6, 2**28)+512*delta+4*dR+1024*delta, 8*dR+2048*delta) < Q(1, 2**24))

    e16 = Q(3, 8)**16
    analytic_bounds = {
        "small_levy_tail": Q(9, 32768)+Q(13, 2**30),
        "large_levy_tail": 202*e16,
        "outer_quadrature": Q(12000, 4**13),
        "archimedean_propagated": 13*(Q(2400, 4**14)+4*e16+2*(Q(600, 4**12)+Q(3, 8)*e16))/6,
        "prime_tail": Q(20, 3)*Q(3, 8)**10,
    }
    for k, value in analytic_bounds.items():
        row = analytic["allowances"][k]
        check("analytic:"+k, value == Q(row["proved_upper_bound"]) and value < Q(row["required_strict_bound"]))
    check("analytic:dyadic_total", sum((Q(v["required_strict_bound"]) for v in analytic["allowances"].values()), Q(0)) == Q(25, 16384))
    for w, k in ((128, 1), (32, 2), (8, 3), (4, 4)):
        check(f"analytic:adaptive{k}", w*(k*Q(2, 3))**2-Q(3, 2)*k*Q(7, 10) > 20 and k*Q(2, 3) >= Q(5, 4*w))
    check("analytic:cutoff32", 25*Q(56, 81)**2-Q(5, 2)*Q(25, 36) > 10)

    log2tail = Q(9, 4*129*3**129)
    verror = 30*log2tail+Q(7, 10*2**168)
    Eerror = Q(96*3**21, factorial(41))+3**21*verror
    qerror = Q(1, 2**65)+Eerror/8
    check("inputs:log2", log2tail < Q(1, 2**200))
    check("inputs:v", verror == Q(inputs["bounds"]["outer_argument_error_bound"]) and verror < Q(1, 2**160))
    check("inputs:E", Eerror == Q(inputs["bounds"]["outer_exp_total_error_bound"]) and Eerror < Q(1, 2**120))
    check("inputs:q", qerror == Q(inputs["bounds"]["q_error_bound"]) and qerror < Q(1, 2**64))
    check("inputs:Gaussian", Q(48, factorial(41))+Q(8, 2**169) < Q(1, 2**150))
    check("inputs:weight_gradient_n13", 13*2**95 < 2**99)
    check("inputs:weight_gradient_n14", 14*2**102 < 2**106)

    # Trial factorization, independent of the construction's sieve.
    powers = {}
    for n in range(2, 33):
        r, factors = n, []
        for d in range(2, n+1):
            if r % d == 0:
                factors.append(d)
                while r % d == 0:
                    r //= d
        if len(factors) == 1:
            powers[n] = factors[0]
    check("prime:complete_powers", len(powers) == 18 and set(map(int, finish["prime_logs"])) == set(powers))
    ell = 2*sum((Q(1, (2*j+1)*3**(2*j+1)) for j in range(64)), Q(0))
    logs = {}
    for n, p in powers.items():
        k = n.bit_length()-1
        z = Q(n-2**k, n+2**k)
        logs[n] = k*ell+2*sum((z**(2*j+1)/(2*j+1) for j in range(32)), Q(0))
        row = finish["prime_logs"][str(n)]
        check(f"prime:log{n}", row["prime_base"] == p and Q(row["lower_log"]) == logs[n])
    check("prime:schedule_complete", {(r["panel"], Q(r["sigma"])) for r in finish["prime_schedule"]} == {(j, s) for j in range(1, 21) for s in (Q(1), Q(3, 2), Q(2))} and len(finish["prime_schedule"]) == 60)
    slots = 0
    suppressed = 0
    for row in finish["prime_schedule"]:
        j, s = row["panel"], Q(row["sigma"])
        lower = s+2**((140-7*j)//5)
        kept = sorted(n for n in powers if lower*logs[n]**2 < 32)
        omitted = sorted(set(powers)-set(kept))
        check(f"prime:panel{j}:sigma{s}:partition", row["keep"] == kept and row["omit"] == omitted and Q(row["lower_width"]) == lower)
        for n in omitted:
            x = lower*logs[n]**2
            check(f"prime:panel{j}:sigma{s}:omit{n}", x >= 32 and x == Q(row["omitted_lower_exponents"][str(n)]))
        slots += 13*len(kept)
        suppressed += len(omitted)
    check("prime:slots", slots == 1534)

    tau = Q(3, factorial(21))
    epsA = 256*tau+Q(32, 2**169)
    epsu = 8*tau+Q(1, 2**170)
    epsI = 16*(512*epsA+2**21*epsu)+Q(224*7, 2**63)
    epspi = Q(16, 65*5**65)+Q(4, 65*239**65)
    epsgamma = Q(1, 8*4096**2)+12*log2tail
    epsclog = Q(49, 24*33*7**33)+4*log2tail+epspi
    epsK = (epsgamma+epsclog+2*epsI)/12+32*epspi
    epsl = 5*log2tail+Q(9, 4*65*3**65)
    epsx = Q(16, 2**120)+2**30*8*epsl
    epsP = 18*(Q(1, 2**60)+4*(32*tau+epsx+Q(1, 2**44)))
    epslogw = Q(1, 99*2**30)+Q(8, 2**120)+Q(1, 2**160)+2*log2tail
    epspole = Q(2, 2**60)+Q(2, 16**11*factorial(11))+Q(4, 2**64)
    epsF = epsK+epspole+epslogw/24+Q(1, 6*2**24)+epsP/6+128*epspi
    epsr = Q(96*3**11, factorial(21))+Q(3**11, 2**161)
    epsg = 2*epsr+2*2**16*(tau+Q(2, 2**120))+Q(2**16, 2**64)
    epsB = 13*epsF+7*(20*epsg+Q(260*4, 2**68))
    radius = Q(25, 16384)+epsB+128*tau
    computed = {"Ihat_arithmetic_error": epsI, "pi_error": epspi,
                "gamma_error": epsgamma, "log4pi_error": epsclog, "K_error": epsK,
                "prime_log_error": epsl, "prime_argument_error": epsx, "prime_sum_error": epsP,
                "logw_error": epslogw, "pole_error": epspole, "profile_error": epsF,
                "outer_r_error": epsr, "outer_g_error": epsg,
                "exponent_arithmetic_error": epsB, "final_exp_error": 128*tau,
                "final_scalar_radius": radius}
    required = {"Ihat_arithmetic_error": 30, "pi_error": 140, "gamma_error": 26,
                "log4pi_error": 60, "prime_log_error": 100, "prime_argument_error": 66,
                "prime_sum_error": 37, "logw_error": 35, "pole_error": 55,
                "profile_error": 22, "outer_r_error": 40, "outer_g_error": 35,
                "exponent_arithmetic_error": 17, "final_scalar_radius": 8}
    for k, value in computed.items():
        check("arithmetic:stored:"+k, value == Q(finish["bounds"][k]))
        if k in required:
            check("arithmetic:bound:"+k, value < Q(1, 2**required[k]))
    check("arithmetic:denominator", 4*epsu < Q(1, 512))
    check("arithmetic:threshold", 2*Q(3, 8)**32 < Q(1, 2**44) and epsx < Q(1, 2))
    check("arithmetic:both_allowances", epsB < Q(1, 1024) and 128*tau < Q(1, 1024))
    check("arithmetic:display_exponent_bound", epsB < Q(1374, 10**10))
    check("arithmetic:display_radius_bound", radius < Q(1526017, 10**9))

    coefficient_cost = 30+30+29+29+14+29+2*sum(n//2 for n in range(29))
    core_cost = coefficient_cost+48*6+48*2+48*(28+29+29)+29+780*2+663*58+118*(48*58+1)+780
    input_items = [500, 129*(28+30), 6*160*(28+30), 100, 100,
                   sum(n*((n-1)**2+2*(n-1)+3*((n+1)//2)+1) for n in (12, 13))+25,
                   48*3+12, 81, 48*88, 400, 260*12, 260*86, 260*4, 780*(64*5+2)]
    final_items = [63, 129*32, 7*160*32, 120, 14*(13**2+26+21+1)+14,
                   224*3+14+224*2, 224*108, 8200, 1500, 2000, 18*(70+322+2),
                   60+60*18*2, slots*53, 260*3, 780*36+260, 780*24, 780*7,
                   260*46, 520*45, 260+520, 60, 520+1560*2, 8*53]
    check("cost:all_input_rows", input_items == list(inputs["cost"]["generation_breakdown"].values()))
    check("cost:all_final_rows", final_items == list(finish["cost"]["additional_breakdown"].values()))
    check("cost:core", core_cost == core["core_cost"]["total_upper"] == 374518)
    total = core_cost+sum(input_items)+sum(final_items)
    check("cost:aggregate", total == finish["cost"]["full_upper"] == 989767 and total <= 10**6)
    failures = [k for k, ok in checks.items() if not ok]
    result = {"status": "FINITE_EVIDENCE_PASS" if not failures else "FAIL",
              "scope": "Exact evidence only; conceptual proof audit is canonical in C033y/z.",
              "inputs_sha256": evidence, "rule_verification": rules,
              "all_root_brackets_checked": 39, "all_cardinal_weights_checked": 39,
              "prime_powers_checked": powers, "suppression_decisions_checked": 60*18,
              "suppressed_panel_terms": suppressed, "runtime_slots": slots,
              "bounds": {k: str(v) for k, v in computed.items()},
              "required": {"exponent_arithmetic": "1/1024", "final_exponential": "1/1024", "scalar_radius": "1/256"},
              "cost": {"core": core_cost, "inputs": sum(input_items), "completion": sum(final_items),
                       "total": total, "required": 10**6, "remaining": 10**6-total},
              "checks": checks, "failures": failures,
              "transforms_evaluated": False,
              "limitations": ["Source-wide and finite-zero validity remain qualified",
                              "Operation count excludes bit complexity and verification work",
                              "No interpolation, conditioning, TV, signed-height or Xi conclusion"]}
    path = HERE / "direct_positive_real_audit_1806.json"
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Exact audit: {len(checks)} checks; failures={failures}")
    print(f"Roots/weights: 39 each; suppression decisions: 1080; runtime slots: {slots}")
    print(f"Exponent arithmetic {float(epsB):.12g} < {2**-10}; final exponential {float(128*tau):.12g} < {2**-10}")
    print(f"Scalar radius {float(radius):.12g} < {2**-8}; cost {total} <= 1000000; slack {10**6-total}")
    print(f"Certificate: {path.relative_to(HERE.parent.parent)}; no scalars evaluated")
    assert not failures, failures


if __name__ == "__main__":
    main()
