"""Exact preflight of C032z's literal gamma/digamma error scheme.

No kernel samples, numerical zero coordinates or optimizer are used.
The barrier concerns stated allowances, never actual errors or residuals.
"""
from fractions import Fraction as Q
from pathlib import Path
import json


def exp_partial(x, degree):
    term = total = Q(1)
    for j in range(1, degree + 1):
        term *= x / j
        total += term
    return total


checks = []


def check(name, actual, required, relation):
    passed = actual > required if relation == ">" else actual < required
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       relation=relation, passed=passed))


c_lower = 8 + 704 * exp_partial(Q(121, 32), 24)
check("C_positive_Taylor_lower", c_lower, Q(30000), ">")
check("e_power_nine_upper", Q(3**9), Q(45000), "<")
barrier = Q(21 * 30000**2, 16)

# A+B<eps<=1 implies R>45000/eps, then log(1+R)>9.
# A>21*C/(8R), B>=C*R/(8K), so (A+B)^2>21*C^2/(16K).
costs = []
for eps in [Q(1), Q(1, 2), Q(1, 8), Q(1, 16)]:
    k_lower = barrier / eps**2
    r_lower = Q(45000) / eps
    assert k_lower.denominator == r_lower.denominator == 1
    costs.append(dict(requested_E_allowance_strict_upper=str(eps),
                      necessary_R_strict_lower=str(r_lower),
                      necessary_K_strict_lower=str(k_lower),
                      minimum_integer_K=int(k_lower) + 1,
                      meaning="Necessary for the literal sum T_G+T_psi, not for actual errors"))

series_term_cap = 10_000_000
coarse_squared_lower = barrier / series_term_cap
check("error_allowance_exceeds_ten_at_term_cap_when_R_gt_45000",
      coarse_squared_lower, Q(100), ">")
for row in costs:
    check("series_term_cap_fails_epsilon_" + row["requested_E_allowance_strict_upper"],
          Q(row["necessary_K_strict_lower"]), Q(series_term_cap), ">")

names = [f"{component}_kappa_{axis}_{w}"
         for axis in ["real", "imaginary"]
         for w in ["1/4", "1/2", "1", "2"]
         for component in ["Re", "Im"]]
names += [f"L_{s}" for s in ["1/16", "1/4", "1", "4"]]
certificate = dict(
    assessment="drafts/literature/2026-11-18-bounded-variation-continuum-dual-test-1570.md",
    canonical_proof="lemmas/C032z-direct-integrated-spectral-explicit-formula.md#literal-series-cost-preflight1586",
    scope="Literal uniform errors C032z(8)-(9), R>=1, K>=1; no sharper digamma or integrated-remainder method",
    retained_assumptions=["C032m/q/w/z actual complex divisor and multiplicity",
                          "zero-ordinate exclusion, strip/counting qualifications",
                          "finite-zero, heat, fixed-v1 probability qualifications for the cone interpretation"],
    exact_evidence=dict(C_Taylor_lower_degree=24, C_Taylor_lower=str(c_lower),
                        C_simplified_strict_lower="30000", pi_strict_upper="4",
                        e_strict_upper="3", e_ninth_strict_upper="19683",
                        R_necessary_strict_lower="45000/epsilon",
                        joint_allowance_squared_strict_lower="1181250000/K when R>45000",
                        cost_bounds=costs),
    finite_work_decision=dict(literal_digamma_series_term_cap=series_term_cap,
                              E_allowance_cannot_be_below="1",
                              proof_cases=["R<=45000: T_G>45000/R>=1",
                                           "R>45000: (T_G+T_psi)^2>1181250000/K>=118.125"],
                              caching_qualification="psi values can be reused across widths/w; no repeated 129*K lower bound is claimed",
                              alternative_methods="asymptotic/recurrence digamma or tighter integrated errors are not ruled out"),
    candidate=dict(description="q=0; retained trivial candidate only",
                    coefficients={name: "0" for name in names},
                    exact_uniform_residual="1",
                    nonnegative_L_coefficients=True),
    validation=dict(closed_width_cells=[dict(left="1", right="2", endpoints_included=True,
                                             exact_residual="1", kernel_error_contribution="0")],
                    maximum_allowed_width_cells=4096,
                    rounding_allowance="0; exact rational comparisons, no evaluated kernels",
                    coefficient_amplification="0 for q=0; absent for nonzero candidates, not waived"),
    execution=dict(initial_solves=0, refinement_solves=0, kernel_samples=0,
                   prime_powers_enumerated=0, gamma_quadrature_nodes=0,
                   finite_zero_coordinates_used=0, huge_series_allocated=False),
    results=dict(required_strict_uniform_residual="1/2", actual_certified_residual="1",
                 certificate_succeeded=False, actual_dictionary_lower_bound=False,
                 outcome="NEGATIVE: new cost barrier for this literal direct-E scheme",
                 decision="Park literal C032z(8)-(9) series evaluation; dictionary result inconclusive",
                 dominant_unpaid_cost="More than 1181250000 digamma summands for even a common E allowance below1",
                 residual_qualification="E allowance<1 is a preflight benchmark; no necessary coefficient size or actual-error lower bound is asserted"),
    failures=[dict(name="nontrivial_uniform_residual", actual="1", required="<1/2"),
              dict(name="literal_unit_E_allowance_with_term_cap", actual="unattainable with K<=10000000",
                   required="T_G+T_psi<1"),
              dict(name="remaining_finite_evaluator", actual="not implemented",
                   required="pole/h quadrature, O enclosure, rounding and nonzero-coefficient amplification")],
    arithmetic_checks=checks,
    arithmetic_failures=[c["name"] for c in checks if not c["passed"]])
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print("Residual: certified1; required <1/2; no actual-dictionary lower bound.")
print("Literal E allowance<1 requires R>45000, K>1181250000; allowance<1/8 requires K>75600000000.")
print("Term cap10000000 fails even allowance<1; dominant unpaid cost: literal digamma series.")
print(f"Optimizer solves=0; failed obligations={len(certificate['failures'])}; arithmetic failures={len(certificate['arithmetic_failures'])}.")
print(f"Certificate: {path}; complete proof: {certificate['canonical_proof']}")
raise SystemExit(bool(certificate["arithmetic_failures"]))
