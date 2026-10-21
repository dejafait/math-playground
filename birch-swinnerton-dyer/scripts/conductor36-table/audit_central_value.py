"""Bounded L060 audit; inherits L056 analytic containment, never rewrites inputs."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "central-value-critical-audit.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def floor(x):
    return x.numerator // x.denominator


def ceil(x):
    return -floor(-x)


def matmul(a, b):
    return [a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]]


def main():
    names = ["central-value-extraction.json", "presentation.json",
             "table_certificate.json",
             "table-critical-audit/signed-isolation-and-relations.json"]
    before = {n: digest(ROOT/n) for n in names}
    extraction, presentation, table, distinct = [
        json.loads((ROOT/n).read_text()) for n in names]
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    for n, expected in extraction["inputs_sha256"].items():
        check("bound_hash:"+n, before[n] == expected)
    check("presentation_binding", table["input_sha256"]["presentation"]
          == before["presentation.json"])
    k = extraction["generator_id"]
    check("generator_id", k == 1)
    path = presentation["basepaths"][k]
    row = table["generators"][k]
    audit = distinct["generators"][k]
    endpoints = [[1, 0], [0, 1]]
    check("all_endpoints", presentation["endpoints"][k] == endpoints
          == row["endpoints"] == extraction["endpoints"]
          == [path["start"], path["end"]])
    check("start_chain", path["start_chain"] ==
          {"target": [1, 0], "terms": [], "segments": []})
    chain = path["end_chain"]
    check("end_chain_shape", chain["target"] == [0, 1]
          and chain["terms"] == [0] and len(chain["segments"]) == 1)
    segment = chain["segments"][0]
    lookup = segment["lookup"]
    check("segment_endpoints", [segment["start"], segment["end"]] == endpoints)
    h = lookup["h"]
    gamma = lookup["gamma"]
    lift = presentation["cosets"]["lifts"][k]
    check("lookup", lookup["coset"] == k and lookup["unit"] == 35
          and lookup["residue"] == [35, 0]
          and h == [0, 1, -1, 0]
          and matmul(gamma, lift) == h
          and gamma[0]*gamma[3]-gamma[1]*gamma[2] == 1
          and gamma[2] % 36 == 0
          and [(35*x) % 36 for x in presentation["cosets"]["representatives"][k]]
          == lookup["residue"])
    raw = [int(i == k) for i in range(72)]
    coordinates = [1] + [0]*12
    check("raw_and_quotient", path["raw"] == raw
          and path["coordinates"] == coordinates
          == presentation["presentation"]["generator_coordinates"][k])

    D = table["scale"]
    check("scale", D == 2**96 and table["bits"] == 96)
    period = [F(x, D) for x in table["arithmetic_evidence"]["period"]["total"]]
    check("total_period", period == list(map(F, distinct["period"]))
          and 0 < period[0] <= period[1]
          and table["arithmetic_evidence"]["period"]["components"] == 1)
    exact = [F(0), F(0)]
    rounded = [0, 0]
    traces = []
    check("occurrence_counts", len(row["occurrence_trace"]) == len(audit["occurrences"]) == 8)
    for j, trace in enumerate(row["occurrence_trace"]):
        point_id, w = trace["point_id"], F(trace["weight"])
        primitive = table["primitives"][point_id]
        check(f"primitive_id:{j}", primitive["point_id"] == point_id)
        term = sorted(w * F(x, D) for x in primitive["enclosure"])
        rounded_term = [floor(D*term[0]), ceil(D*term[1])]
        exact = [exact[i]+term[i] for i in range(2)]
        rounded = [rounded[i]+rounded_term[i] for i in range(2)]
        expected = [point_id, str(w), *map(str, term), *map(str, exact)]
        check(f"complete_occurrence:{j}", trace["term"] == rounded_term
              and trace["partial"] == rounded and audit["occurrences"][j] == expected)
        traces.append(expected)
    check("integral", row["integral"] == rounded
          and list(map(F, audit["exact_integral"])) == exact
          and F(rounded[0], D) <= exact[0] <= exact[1] <= F(rounded[1], D))
    quotients = [F(x, D)/p for x in rounded for p in period]
    check("all_four_quotients", quotients == list(map(F, row["quotient_endpoints"])))
    normalized = [F(floor(D*min(quotients)), D), F(ceil(D*max(quotients)), D)]
    independent = [exact[0]/period[1], exact[1]/period[0]]
    check("positive_division", exact[0] > 0 and audit["sign_case"] == "positive"
          and independent == list(map(F, audit["independent_normalized"]))
          and normalized[0] <= independent[0] <= independent[1] <= normalized[1])
    check("normalized_agreement", normalized == [F(x, D) for x in row["normalized"]]
          == list(map(F, audit["saved_normalized"]))
          == list(map(F, extraction["normalized_interval"])))
    B = table["clearing_integer"]
    check("clearing_integer", B == extraction["clearing_integer"] == 24)
    scaled = [B*x for x in normalized]
    candidates = list(range(ceil(scaled[0]), floor(scaled[1])+1))
    check("isolation", candidates == audit["integer_candidates"] == [4]
          and row["scaled_ceil"] == ceil(scaled[0])
          and row["scaled_floor"] == floor(scaled[1])
          and row["scaled_integer"] == extraction["scaled_integer"] == 4
          and list(map(F, extraction["scaled_interval"])) == scaled)
    m = candidates[0]
    margins = [scaled[0]-(m-1), (m+1)-scaled[1]]
    check("adjacent_exclusions", all(x > 0 for x in margins)
          and list(map(F, audit["adjacent_integer_margins"])) == margins)
    check("independent_isolation", ceil(B*independent[0]) == floor(B*independent[1]) == m)
    qvalues = list(map(F, table["relations"]["quotient_values"]))
    qscaled = distinct["quotient_values_scaled_24"]
    check("complete_quotient_values", len(qvalues) == len(qscaled) == 13
          and [B*x for x in qvalues] == qscaled)
    value = sum(c*v for c, v in zip(coordinates, qvalues))
    check("quotient_value", value == F(m, B) == F(row["value"])
          == F(extraction["value_infinity_to_zero"])
          == F(table["relations"]["reconstructed"][k])
          == F(distinct["reconstructed_scaled_24"][k], B))
    check("reversal_nonzero", value != 0 and -value == F(extraction["value_zero_to_infinity"]))
    width = normalized[1]-normalized[0]
    required = F(1, 2**38)
    check("width", width < required and width == F(extraction["width_actual"])
          == F(row["width"]) == F(audit["width"])
          and required == F(extraction["width_required_strict"]))
    check("input_bytes_preserved", before == {n: digest(ROOT/n) for n in names})
    failures = [k for k, ok in checks.items() if not ok]
    report = dict(schema="bsd-L060-critical-audit-v1", inputs_sha256=before,
                  checks=checks, failures=failures, selected_path=path,
                  selected_occurrences=traces, period=list(map(str, period)),
                  normalized=list(map(str, normalized)), scaled=list(map(str, scaled)),
                  integer_candidates=candidates, adjacent_margins=list(map(str, margins)),
                  quotient_values=list(map(str, qvalues)), value=str(value),
                  reversed_value=str(-value), actual_width=str(width),
                  required_strict_width=str(required),
                  qualification="Selected exact evidence only; L056 supplies analytic containment; theorem applicability is audited in L060.")
    OUT.write_text(json.dumps(report, indent=2)+"\n")
    print(f"checks={len(checks)} failures={failures} value={value} reversed={-value}")
    print(f"width={width} required_strictly_below={required}")
    print(f"certificate={OUT.relative_to(ROOT.parent.parent)}")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
