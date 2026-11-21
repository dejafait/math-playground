"""Independent exact replay of C033e's finite comparisons; no function samples."""
from fractions import Fraction as F
from pathlib import Path
import json

# Do not import construction1700 or read its certificate.
N = 2336
nodes = [F(2*j+1, 512) for j in range(4096)]
eps = F(1, 2**256)
# Use the sharper node-dependent B bound, independently of 1/33.
separations = [2*v*v/(1+2*v) - v*eps for v in nodes]
min_index = min(range(len(nodes)), key=separations.__getitem__)
# Clear powers of two before comparing the global quotient and sum bounds.
# |Utilde-U| <= (2^65+2)eps, |U| <= 2^65, |Dtilde-D| <=16eps,
# D>2^-23 and Dtilde>2^-24.
product_units = 2**65 + 2
quotient_units = product_units * 2**24 + 2**65 * 16 * 2**47
sum_units = 16 * quotient_units
checks = {
    "all_4096_distinct_nodes": len(set(nodes)) == 4096,
    "all_nodes_in_original_range": all(F(1,512) <= v < 16 for v in nodes),
    "all_G_arguments_within_520": all(2*v*v+v/2 <= 520 for v in nodes),
    "all_other_arguments_within_32": all(2*v <= 32 for v in nodes),
    "all_exact_denominators_above_2m23": all(2*v*v/(1+2*v) > F(1,2**23) for v in nodes),
    "all_perturbed_denominators_above_2m24": all(x > F(1,2**24) for x in separations),
    "degree_N_plus_1_exponent": 1+2080-(N+1) == -256,
    "uniform_coarse_denominator": F(1,33*2**17)-16*eps > F(1,2**24),
    "product_units_below_2p66": product_units <= 2**66,
    "quotient_units_below_2p117": quotient_units <= 2**117,
    "weighted_units_below_2p121": sum_units <= 2**121,
    "sum_majorant_exponent": 121-256 == -135,
    "sum_bound_below_required": F(1,2**135) < F(1,64),
}
failures = [key for key, passed in checks.items() if not passed]
def rat(x):
    return f"{x.numerator}/{x.denominator}"
certificate = {
    "scope": "Exact finite comparisons independent of construction1700; analytic proof is canonical C033e.",
    "nodes_checked": len(nodes),
    "checks": checks,
    "load_bearing": {
        "minimal_separation_node_index": min_index,
        "minimal_separation_node": rat(nodes[min_index]),
        "minimal_separation_lower": rat(separations[min_index]),
        "required_denominator_strict_lower": rat(F(1,2**24)),
        "product_error_units_of_eps": product_units,
        "quotient_error_units_of_eps": quotient_units,
        "weighted_error_units_of_eps": sum_units,
        "weighted_error_bound": rat(sum_units*eps),
        "uniform_sum_majorant": rat(F(1,2**135)),
        "required_sum_error": "1/64",
    },
    "failures": failures,
}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(certificate, indent=2)+'\n')
print(f"Independent exact checks: {sum(checks.values())}/{len(checks)}; nodes: {len(nodes)}")
print(f"Denominator minimum lower at j={min_index}: {rat(separations[min_index])} > 1/{2**24}")
print("Weighted error <= 2^-135; required <= 1/64")
print(f"Failures: {failures}; certificate: {output}")
if failures:
    raise SystemExit(1)
