"""Replay the analytically selected counterexample; no grid or random search."""
from fractions import Fraction as F
from functools import reduce
from math import gcd, lcm
from pathlib import Path
import json
from moment_flow import basis, cubic, sturm, variations
from verify_moment_flow import coefficients, discriminant


def primitive(p):
    denominator = lcm(*(x.denominator for x in p))
    ints = [int(x*denominator) for x in p]
    common = reduce(gcd, (abs(x) for x in ints))
    return [x//common for x in ints], F(denominator,common)


def main():
    q,u,v = F(12,25),F(0),F(1)
    endpoints,failures = [],[]
    for radius, expected in [(F(9,32),3),(F(1,3),1)]:
        p = cubic(basis(),q,u,v,radius)
        direct = coefficients(q,u,v,radius)
        if p!=direct:
            failures.append("recurrence/direct coefficient disagreement")
        ints, factor = primitive(p)
        delta = discriminant(list(map(F,ints)))
        chain = sturm(list(map(F,ints)))
        at_zero = [1 if row[0]>0 else -1 if row[0]<0 else 0 for row in chain]
        at_infinity = [1 if row[-1]>0 else -1 for row in chain]
        count = variations(at_zero)-variations(at_infinity)
        if count!=expected or len(chain[-1])!=1:
            failures.append("Sturm count or simplicity failure")
        if (delta>0)!=(expected==3) or delta==0:
            failures.append("discriminant sign failure")
        if not all((-1)**j*x>0 for j,x in enumerate(ints)):
            failures.append("strict alternating coefficient sign failure")
        if delta != factor**4*discriminant(p):
            failures.append("discriminant scaling failure")
        endpoints.append(dict(radius=str(radius),integer_coefficients_ascending=ints,
                              positive_scale_from_original=str(factor),
                              integer_discriminant=str(delta),
                              original_discriminant=str(discriminant(p)),
                              sturm_chain=[[str(x) for x in row] for row in chain],
                              signs_at_zero=at_zero,signs_at_positive_infinity=at_infinity,
                              positive_distinct_roots=count,squarefree=len(chain[-1])==1,
                              real_t_roots=2*count))
    # Preserve failed analytic selections: the first hand calculation
    # subtracted the m0 contribution twice in the normalized q coefficient.
    # These were not additions to or reruns of the exhausted grid sample.
    rejected = []
    for r in [F(2,7),F(9,32),F(1,3)]:
        disc = discriminant(coefficients(F(12,13),F(0),F(1),r))
        rejected.append(dict(q="12/13",radius=str(r),discriminant=str(disc),
                             sign=1 if disc>0 else -1 if disc<0 else 0))
    data = dict(result="EXACT_FINITE_FAMILY_COUNTEREXAMPLE" if not failures else "FAILED",
                parameters=dict(q=str(q),u=str(u),v=str(v),m1=str(q),m2=str(q),m3=str(q)),
                additional_grid_or_random_tuples=0,required_additional_sample_bound=0,
                analytic_witnesses=1,failed_analytic_selection_evaluations=rejected,
                endpoints=endpoints,failures=failures,
                limitation="Not actual Xi; no statement about the actual theta measure or RH.")
    dest = Path(__file__).with_name("collision-certificate.json")
    dest.write_text(json.dumps(data,indent=2)+"\n")
    print(data["result"])
    print("Additional sampled tuples: 0; required maximum: 0; analytic witness: 1")
    print("Positive cubic roots:",[e["positive_distinct_roots"] for e in endpoints],
          "; required: [3, 1]; simple:",[e["squarefree"] for e in endpoints])
    print("Real degree-six roots:",[e["real_t_roots"] for e in endpoints],
          "; required for preservation: [6, 6]")
    print("Failures:",failures,"; certificate:",dest)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
