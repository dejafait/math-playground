# C001b — Nested-floor packing fails to improve the fixed-instance bracket

## Hypotheses

Use C001a's instance: n=1024, k=64, Q=65537, F=F_(Q^28), the order-1024
subgroup domain, epsilon*=2^(-128), and any integer m>=1. Use the pinned
closed simultaneous column-Hamming list B_m. Put b=1024-t for t in {956,957}.

## Conclusion

B_m(t/1024)<=U_b, where U_b is the strength-64, multiplicity-one
Johnson-Schonheim nested-floor packing bound. Its exact values and positive
scaled threshold excesses are:

```text
t=956, b=68
U=5905247973195993239152842496518180450627576423113466173203800016363350871797056968017279005139727
2^128*U-65537^28=1282302430295334488820103619533667045107349170110648428326572674447441070428498906558538797636181983139301471866077828083306954802593791
```

```text
t=957, b=67
U=100389235806631189872705443378407944903091452419010809366882178017250185056570793908272887550561921
2^128*U-65537^28=33433537446385815684176608401789507268107394368231522928623311550490359743455530953386811935753288503751207816330352651040875394590048255
```

The ratios U_b/(epsilon*|F|) lie in [2763/1000,2764/1000) at t=956
and [46978/1000,46979/1000) at t=957. Neither certificate proves safety.
C001a's bracket 955<=t_star(m)<=957 remains unchanged. These upper bounds
prove neither unsafety nor sharpness nor exact packing numbers.

## Proof

**Imported theorem.** Robert F. Bailey and Andrea C. Burgess,
[Generalized packing designs](https://www.math.mun.ca/rbailey00/papers/packings.pdf),
November 14, 2011 author manuscript, p. 2, Definitions 1.1.1/1.1.3 and
Proposition 1.1.4, bounds a family of b-subsets of a v-set in which every
r-subset belongs to at most lambda blocks, for integers v>=b>=r>=1 and
lambda>=1, by

\[
\left\lfloor\frac vb\left\lfloor\frac{v-1}{b-1}\cdots
\left\lfloor\frac{\lambda(v-r+1)}{b-r+1}\right\rfloor
\cdots\right\rfloor\right\rfloor.
\]

This is an imported known theorem, without reproof. The prior
[SPECIALIZE assessment](../drafts/literature/2026-10-05-nested-floor-support-endpoint.md)
approves exactly this application and arithmetic.

**Applicability.** Fix an arbitrary received array. Each candidate has at
least b simultaneous agreement columns. Order the domain and select the
first b such columns. By L001, no 64-subset can occur in two distinct
candidates' full agreement sets, hence none can occur in two selected
blocks. Repeated blocks are impossible since b>=64. Extra agreements
cause no problem because selection only deletes columns. Thus the blocks
form a packing with v=1024, r=64 and lambda=1, satisfying all theorem
hypotheses. Its uniform bound can be maximized over centers. This uses
whole tuples and common columns; no scalar-only assumption or exponent m
is introduced. C001a supplies the instance, threshold and existing bracket.

**Arithmetic.** Start u=1 and for i=63,62,...,0 replace u by
floor((1024-i)u/(b-i)). This evaluates the theorem from its innermost floor
outward and gives the displayed U_b. Safety would be certified by
2^128*U_b<=65537^28, with equality safe. The displayed strictly positive
excesses prove that this condition fails at both indices. Integer division
of 1000*2^128*U_b by 65537^28 gives the stated ratio intervals. Since
failure of an upper certificate is not a lower bound on any list, actual
safety at both indices remains unresolved, as does the ABF-model comparison.

**Verification.** Run `python3 scripts/finite-support/nested_floor_bound.py`.
The complete certificate `scripts/finite-support/nested-floor-results.json`
retains all 128 stages with previous value, numerator, denominator,
quotient and remainder, plus complete endpoint comparisons. Every stage
checks the Euclidean identity and remainder range. An independent
exact-rational floor implementation agrees at both endpoints; the bounds
also do not exceed L001's elementary support bounds. No failures were
reported. Both complete threshold excesses were inspected. These checks
verify arithmetic; the cited theorem and support argument justify its
application, rather than asserting an exact list maximum.

## Mathlib

Full matching packing theorem and this finite-instance result: **not
checked** in Mathlib. L001 supplies support uniqueness locally. The separate
ArkLib radius conventions cited there do not provide this packing bound.
This is REPRODUCTION of an inspected known theorem, with an informative
local negative result and no novelty claim.
