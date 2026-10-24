# C123a — The fixed dyadic witness already fails the real filter

## Hypotheses

Use L118's unchanged curve, entire degree-eight algebra, descending
ordering theta_1>...>theta_8 and common real scalar quotient. Use
L123's supported global norm-square class delta=[1−theta²] in H_Q(S).
No survival at another place or complete supported-group computation
is assumed.

## Conclusion

The ordered signs of 1−theta² are --++++--. Its common-scalar orbit
is {--++++--, ++----++}, disjoint from L118's exact real point image.
Thus delta already fails the real filter. L123's rejection at two
remains valid, but this witness does not demonstrate further pruning
after imposing the real test. This does not prove that the dyadic
filter is redundant on the real-filtered supported ambient space.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-marked-octic-witness-real-filter-comparison.md`.
The imported localization rule is Bruin–Stoll, *Two-cover descent on
hyperelliptic curves*, Math. Comp. 78 (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8),
inspected version [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008, Section 2 p.3, Section 5 p.11 and Remark 6.1 p.13.
L118 already specializes its complete real image, including every
branch point and both infinity points. Only the signs of this fixed
global representative require calculation; no general reproof or new
root isolation is needed.

At an embedding with theta_i in (a,b), evaluate the identical polynomial
1−theta_i². The exact intervals certified in audited L118 give:

| i | Interval for theta_i | Strict bounds for 1−theta_i² | Sign |
| --- | --- | --- | --- |
| 1 | (5/2,3) | (−8,−21/4) | − |
| 2 | (3/2,2) | (−3,−5/4) | − |
| 3 | (3/4,1) | (0,7/16) | + |
| 4 | (1/4,1/2) | (3/4,15/16) | + |
| 5 | (−1/2,−1/4) | (3/4,15/16) | + |
| 6 | (−1,−3/4) | (0,7/16) | + |
| 7 | (−2,−3/2) | (−3,−5/4) | − |
| 8 | (−3,−5/2) | (−8,−21/4) | − |

Each bound follows by squaring the absolute-value interval and
subtracting from one. All bounds are strict. In particular entries
3 and 6 are positive, not zero; no root equals ±1. This also certifies
invertibility at every real component. The vector has four negatives,
so its positive norm sign agrees with L123's exact square norm and
the positive leading coefficient 3025.

Squares in R⁸ are positive in every coordinate. One common nonzero
real scalar either preserves all signs or reverses all eight. Hence
there are exactly the two vectors stated in the conclusion in this
scalar-square orbit, not independent choices at the embeddings.
L118's complete image representatives are

    ++++++++, --++++++, ----++++, ------++.

None equals --++++-- or ++----++. For the first vector, the four
negative positions are {1,2,7,8}; it differs from the sole four-negative
representative, whose negative positions are {1,2,3,4}, and from the
representatives with zero, two or six negatives. The reversed vector
starts with + and has four negatives, so differs from the all-positive
representative and from all three representatives starting with −.
Comparing both orbit members with every representative proves
nonmembership, including exceptional-point images already covered
by L118. No subgroup property of the point image is used.

Consequently this global class belongs neither to the real-filtered
supported ambient nor to its intersection with the dyadic filter.
Its two-adic rejection therefore cannot witness strictness of that
intersection inside the real-filtered ambient. L123's different claim,
strictness inside the unfiltered supported ambient, remains intact.
No statement about redundancy for other classes follows from failure
of this one witness. Identity and both known rational infinity points
survive. Complete supported units, S-class two-torsion, simultaneous
local survival, points on surviving covers, degree-nine root recovery,
remaining factors, both L095 systems and minus-eleven remain unresolved.
This is a negative route decision by specializing the checked methods,
not a rational-point classification or a Beal exclusion.

## Mathlib

Full matching coverage of this fixed-element comparison and even-degree
fake point-image quotient was not checked. The exact rational inequalities
above use the canonical audited real intervals; no formal-verification
or absence claim is made.
