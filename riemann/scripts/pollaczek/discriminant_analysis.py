"""Exact symbolic discriminant expansion; no parameter sampling."""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import json


def const(x):
    return {(0, 0, 0, 0): F(x)} if x else {}


def variable(i):
    k = [0]*4
    k[i] = 1
    return {tuple(k): F(1)}


def add(*polys):
    result = defaultdict(F)
    for p in polys:
        for k, v in p.items():
            result[k] += v
    return {k: v for k, v in result.items() if v}


def scale(p, c):
    return {k: v*c for k, v in p.items() if v*c}


def mul(*polys):
    result = const(1)
    for p in polys:
        out = defaultdict(F)
        for k, v in result.items():
            for l, w in p.items():
                out[tuple(a+b for a, b in zip(k, l))] += v*w
        result = {k: v for k, v in out.items() if v}
    return result


def power(p, n):
    return mul(*([p]*n))


def discriminant(a, b, c, d):
    return add(mul(b,b,c,c), scale(mul(a,c,c,c),-4),
               scale(mul(b,b,b,d),-4), scale(mul(a,a,d,d),-27),
               scale(mul(a,b,c,d),18))


def main():
    s, A, B, C = [variable(i) for i in range(4)]
    # 8 * [-720 P_s(y/s)]; here A=m1, B=m2, C=m3.
    a = scale(C,8)
    b = add(scale(B,-240),scale(mul(C,s),-500))
    c = add(scale(A,2880),scale(mul(B,s),4080),
            scale(mul(C,s,s),4802))
    d = add(const(-5760),scale(mul(A,s),-4320),
            scale(mul(B,s,s),-3780),scale(mul(C,s,s,s),-3465))
    delta = discriminant(a,b,c,d)
    grouped = {}
    for j in range(7):
        grouped[str(j)] = [dict(moment_powers=list(k[1:]),coefficient=str(v))
                           for k,v in sorted(delta.items()) if k[0]==j]
    result = dict(status="SYMBOLIC_EXPANSION_ONLY", variables=["s","m1","m2","m3"],
                  normalization="discriminant_y(-5760 P_s(y/s))",
                  coefficients_by_s_degree=grouped, tested_tuples=0,
                  required_additional_tuple_bound=0, failures=[])
    dest = Path(__file__).with_name("discriminant-analysis.json")
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("Exact discriminant expansion saved:",dest)
    print("New tuples: 0; required maximum: 0; degree:",max(k[0] for k in delta))
    for j,terms in grouped.items():
        print("s^"+j, terms)


if __name__ == "__main__":
    main()
