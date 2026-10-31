"""Independent formula/discriminant replay of the entire recorded grid."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json


def coefficients(q,u,v,r):
    a = ((1-q)*u + q*v)*r**2
    b = ((1-q)*u**2 + q*v**2)*r**4
    c = ((1-q)*u**3 + q*v**3)*r**6
    return [1+F(3,4)*a+F(21,32)*b+F(77,128)*c,
            -F(1,2)*a-F(17,24)*b-F(2401,2880)*c,
            F(1,24)*b+F(25,288)*c, -c/720]


def discriminant(p):
    d,c,b,a = p
    return b*b*c*c - 4*a*c**3 - 4*b**3*d - 27*a*a*d*d + 18*a*b*c*d


def evaluate(p,x):
    y = F(0)
    for c in reversed(p):
        y = y*x+c
    return y


def main():
    folder = Path(__file__).parent
    data = json.loads((folder / "moment-flow-certificate.json").read_text())
    failures, histogram, examples = [], Counter(), []
    for i,row in enumerate(data["tuples"]):
        q,u,v,r0,r1 = map(F,row["parameters"])
        domain = (0<=q<=1 and 0<=u<=v<=1 and v>0 and
                  (1-q)*u**3+q*v**3>0 and 0<r0<r1<=1 and
                  all(x.denominator<=32 for x in [q,u,v,r0,r1]))
        if not domain:
            failures.append([i,"domain"])
        predictions=[]
        for j,r in enumerate([r0,r1]):
            p = coefficients(q,u,v,r)
            if not (p[0]>0 and p[1]<0 and p[2]>0 and p[3]<0):
                failures.append([i,j,"coefficient signs"])
            disc = discriminant(p)
            # With the strict coefficient signs, P(-x)>0 for x>=0;
            # all real roots are positive. Nonzero cubic discriminant
            # decides between three distinct reals and one real.
            if disc == 0:
                failures.append([i,j,"discriminant zero: separate replay required"])
                continue
            n = 3 if disc>0 else 1
            predictions.append(n)
            if n != row["positive_roots"][j] or not row["squarefree"][j]:
                failures.append([i,j,"Sturm/discriminant disagreement"])
        if len(predictions)==2:
            histogram[tuple(predictions)] += 1
            initial = predictions[0]==3
            if initial != row["initial_simple_hyperbolic"]:
                failures.append([i,"initial flag"])
            if initial:
                examples.append((sum(x.denominator for x in [q,u,v,r0,r1]),i))
    count_initial = sum(count for (a,b),count in histogram.items() if a==3)
    if count_initial != data["initial_hyperbolicity_successes"]:
        failures.append("initial success total")
    if len(data["tuples"]) != data["tested_tuples"] or data["tested_tuples"]>10000:
        failures.append("tuple bound/count")
    if any(a==3 and b<3 for a,b in histogram) != bool(data["witness"]):
        failures.append("witness flag")
    _,i = min(examples)
    row = data["tuples"][i]
    q,u,v,r0,r1 = map(F,row["parameters"])
    selected = dict(index=i, parameters=row["parameters"],
                    cubic_coefficients=[[str(c) for c in coefficients(q,u,v,r)] for r in [r0,r1]],
                    discriminants=[str(discriminant(coefficients(q,u,v,r))) for r in [r0,r1]])
    # An additional elementary sign-change certificate for this recorded
    # initial example, without adding any new parameter tuple.
    p = coefficients(q,u,v,r0)
    points = list(range(0,1025))
    crossings = []
    for left,right in zip(points,points[1:]):
        vl,vr = evaluate(p,F(left)),evaluate(p,F(right))
        if vl*vr<0:
            crossings.append(dict(interval=[left,right],values=[str(vl),str(vr)]))
    selected["initial_integer_sign_changes"] = crossings
    if len(crossings)!=3:
        failures.append("selected example needs finer isolating intervals")
    verification = dict(result="VERIFIED_FINITE_SAMPLE" if not failures else "FAILED",
        checked_tuples=len(data["tuples"]), required_maximum_tuples=10000,
        root_count_histogram={str(k):v for k,v in sorted(histogram.items())},
        initial_successes=count_initial, selected_example=selected,failures=failures,
        limitation="Finite sample only; no universal preservation conclusion.")
    dest = folder / "moment-flow-verification.json"
    dest.write_text(json.dumps(verification,indent=2)+"\n")
    print(json.dumps({k:v for k,v in verification.items() if k!="selected_example"}))
    print("Verification:",dest)
    print("Selected recorded tuple index:",i)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
