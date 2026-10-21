# L069 — A union-five additional-error pair bounds all triangle recoveries

## Hypotheses

Let F=F_(97^20), H be the order-sixteen subgroup of F_97^*, and
C=RS[F,H,8]. Use the pinned event at 1/4<=delta<5/16 and L057's
gated tau-zero triangle, with its nine distinct labels, normalized
weights p,q,r in F satisfying p(1-p)q(1-q)r(1-r)!=0, nonzero lambda,
and three distinct original finite parameters gamma_0,gamma_1,gamma_2.
Let s(T)=sigma(a_*)+T sigma(b_*) be that actual syndrome pencil.
All original chart parameters and weights remain arbitrary over F.

Let R be the set of distinct eligible finite parameters admitted by
L057's complete recovery criterion over all nonbase four-supports.
Count parameters once, including both-zero quotient lifts and
recoveries with some zero fourth weights. Thus the parameters in R
are different from every gamma_i; zero, minus-one and original infinity
exclusions in L057 are retained.

Assume R contains distinct u,v with full four-error representatives
e_u,e_v whose supports K_u,K_v have union A of size five. The two
representatives have four nonzero weights each; this assumption is
not imposed on the other recoveries.

The finite configuration bound below has explicit computational
dependence on the complete census and its independent replay. A separate
critical audit on 2026-10-11 found no defect in this conditional result.

## Conclusion

For every five-set A' subset H, L015's configuration satisfies
M(A')<=6. For the above syndrome pencil the total original bad set
satisfies |B(a_*,b_*)|<=11, and
\[
                         |R|\le8\le12.
\]
This closes the gate-approved conditional twelve target, with four
parameters of slack. It does not extract such a pair from every
high-count triangle, bound arbitrary triangles, improve the global
11/q–16/q interval, or resolve the challenge's uncertified definitions.
The uniform configuration maximum equals six, but eleven and eight
are upper bounds here, without an attainment assertion for triangles.

## Proof

### Applicability of the established five-coordinate reduction

Use L015's analytic reduction, without reproving it or assuming its
previously recorded numerical maximum. L057 supplies independence of
the coefficient syndromes, nonzero D and every nonzero coordinate
locator in the original finite chart. Its local converse supplies
three full finite base events; no sixteen-count hypothesis is needed.
These are precisely L015's nonpersistence hypotheses on the same F,H
and shifted moments. The underlying distance input is also covered by
J. I. Hall, *Notes on Coding Theory*, GRS chapter, Theorem 5.1.1 and
proof, printed pp. 63–64, undated
[author PDF](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
read 2026-10-11 in the reused assessment: distinct evaluations, nonzero
multipliers and 0<k<=n give distance n-k+1. Here the multipliers are
one, n=16 and k=8, so the distance is nine. L015's moment and
projective specialization is already proved locally.

Both error syndromes lie in the moment image U_A of words supported
on the five-set A. Since u!=v, the exact identities
\[
 \sigma(b_*)=\frac{\sigma(e_v)-\sigma(e_u)}{v-u},
 \qquad \sigma(a_*)=\sigma(e_u)-u\sigma(b_*)
\]
put both coefficient syndromes in U_A. The union-five assumption on
the full four-supports is the final application already covered by
L015. Its bound therefore gives
\[
                     |B(a_*,b_*)|\le5+M(A).             \tag{1}
\]
There is no rationality assumption on u,v or the original affine chart.

### Complete finite bound, independently counted for every orbit

L015 proves the distinctness and nonzero coordinates of its 330 points
for each five-set, multiplicative invariance of M, and 273 free
five-set orbits. Its point for a four-set K in J=H minus A' is
\[
  [f_K(x)]_{x\in A'},\qquad
  f_K(X)=\prod_{y\in J\setminus K}(X-y).
\]
Normalize by the first evaluation, which is nonzero, so every point
is represented by (1,p_1,p_2,p_3,p_4). Reuse L015's extension-field
passage: an extension-field line containing two distinct rational
configuration points descends to their prime-field line. Thus it is
enough to bound the prime-field configuration, without enumerating
extension-field weights.

The full reproducible verification command is
`python3 scripts/coefficient-feasibility/verify_five_coordinate_census.py`.
It preserves the original certificates and performs the following
complete checks, rather than only verifying selected maximal lines.

1. Enumerate H independently as the roots of x^16=1 among all nonzero
   residues mod 97; check equality with the cyclic producer domain.
   For every saved orbit compute its sixteen sets by actual field
   multiplication. These sets are distinct and different orbits do not
   overlap; their union is exactly the separately enumerated 4,368
   five-subsets. Every saved mask and ordered label list are checked.
2. Independently construct every configuration by all 330 four-subsets
   of its eleven-label complement. At each x in A', compute
   f_K(x)=product_(y in J)(x-y)/product_(k in K)(x-k), and check equality
   with the direct seven-factor formula before normalization. Every
   coordinate is nonzero and all 330 normalized points are distinct.
   Division is valid because x is outside J. Full points and supports
   are saved in `scripts/coefficient-feasibility/five-coordinate-audit-points.jsonl`.
3. Replay the complete original C++ Plucker-pair census. Each of the
   273 resulting records agrees exactly with its original record,
   including every line-size histogram, maximum and maximal witness.
   All 14,819,805 unordered pairs are recounted. The fresh records are
   `scripts/coefficient-feasibility/five-coordinate-census-replay.jsonl`.
4. Independently census lines through every anchor using
   `scripts/coefficient-feasibility/five_coordinate_anchor_census.cpp`.
   This program receives the independently constructed points, never
   their Plucker keys. At an anchor p, group all other points q by
   q-p in the four affine coordinates, normalized by the first nonzero
   difference. All 329 other points are processed at each of the
   90,090 anchors, totaling 29,639,610 directed differences. Save every
   anchor's complete direction-group size histogram in
   `scripts/coefficient-feasibility/five-coordinate-anchor-census.jsonl`.

The independent counting formula is exact. A normalized affine
direction identifies the line p+t(q-p); two differences have the same
key iff they are nonzero scalar multiples and identify the same line
through p. A direction group of s neighbors thus gives s+1
configuration points on that line. If a line has m configuration
points, it is counted at exactly those m anchors. Accordingly, summing
the anchor histograms and dividing the multiplicity for size m by m
counts every such line exactly once. All configuration points lie in
this affine chart, so the omitted projective point at infinity contributes
no additional configuration point. Lines with fewer than two
configuration points cannot affect the maximum, which is at least two.
Direction keys use four base-97 digits and are injectively encoded
in an unsigned integer below 97^4<2^32; no hash collision merges
unequal keys because the map also compares the integer keys.

The driver checks every anchor's neighbor sum 329, every division by
m, every full histogram against the freshly replayed Plucker census,
and the identity sum_m binom(m,2)N_m=54,285 for each configuration.
It also checks full membership of every stored maximal line, as a
supplement to the census, and checks the maximum from every histogram.
The complete summary and all 273 per-orbit results are saved in
`scripts/coefficient-feasibility/five-coordinate-complete-census-audit.json`.
The run completed with no failed obligations:

| Orbit maximum | Number of orbits |
| --- | ---: |
| 5 | 265 |
| 6 | 8 |

All 273 complete histograms agree, not just the previously independently
recounted mask 539. Hence every orbit has M(A')<=6, and multiplicative
invariance proves the bound for all 4,368 five-sets. The actual bound
six is below ten, the threshold sufficient for the requested twelve
additional parameters. Source and artifact SHA-256 values are recorded
in the summary. This is an exact finite computation after L015's
proved reduction; it is not a new analytic proof of the maximum.
The two line-count programs use different keys and independently
constructed configurations, but share the C++ compiler and residue
field. No formal verification or absolute implementation independence
is claimed. No selected actual-pencil/root audit is an input.

### Counting all additional finite recoveries

Insert M(A)<=6 in (1) to obtain |B(a_*,b_*)|<=11. Every admitted L057
recovery is bad on the same twelve-coordinate complement of its
four-support, even when some fourth weights vanish. Both-zero
quotients enter R only after all restored coefficient equations and
their finite pivot and exclusions have passed. They are not discarded,
and their mu values need not lie in the prime field.

L057's change of variables mu to original T is injective on its
eligible finite domain, with E!=0 retaining the original infinity
exclusion. R counts distinct T even when a lower-weight representative
has several four-support witnesses. Its excluded three base parameters
are distinct finite members of B, by the same local converse used in
L057. Therefore the disjoint union R union {gamma_0,gamma_1,gamma_2}
is a subset of B, and |R|+3<=|B|<=11 proves |R|<=8. Fullness was
required only for the chosen two-error union-five hypothesis, never
for counting the remaining recoveries. This proves the stated
conditional result, subject to its explicit computational dependence.

### Separate critical audit (2026-10-11)

The approved audit read this proof and L015 completely, L057's exact
hypotheses, restored equations and same-support proof, and the necessary
L010/L041 kernel, distance, original-chart and nonpersistence passages.
It found no mathematical defect. The following checks concern this
conditional result only, not universal pair extraction.

- All nine labels are distinct and the gated base errors have full
  four-supports with empty triple intersection. L041's pointwise formula
  makes D nonzero at each base event. Every coordinate is absent from
  some base support, where its locator is nonzero. Thus L015's polynomial
  nonpersistence hypotheses hold without assuming sixteen events.
- The two distinct finite parameters u,v justify division by v-u in
  the displayed span identities. L015 constructs the unique affine lift
  on A using five-column injectivity. An identically zero coordinate
  would put the whole pencil on at most four coordinates and contradict
  nonpersistence; hence its cancellation count is at most five. Outside
  those cancellations, distance nine forces every sparse representative
  to have full weight four and be disjoint from A. Lower weights are
  thereby included in the cancellation branch rather than discarded.
- L015's independent coefficient syndromes give injective projective
  parameterization. Distinct rational configuration points span a rational
  line even when the original coefficients and finite chart are not
  rational. A line containing fewer than two configuration points is
  harmless because M>=2. No original-chart descent is assumed.
- Both complete C++ programs and the complete Python driver were reviewed.
  The producer enumerates every complement four-set and every unordered
  point pair; normalized ten-minor keys identify projective lines. String
  keys retain embedded zero bytes. The other program processes all 329
  neighbors at every anchor; normalized four-coordinate differences
  identify precisely the affine lines through that anchor. Base-97
  encoding is injective, with 97^4<2^32, and unordered-map collisions do
  not identify unequal keys. Residue products, pair counts and the
  producer's signed mask shifts stay within their integer ranges.
- The driver separately enumerates the sixteen roots, all 4,368 five-sets,
  their disjoint multiplicative orbits, and all 330 distinct nonzero
  normalized points per configuration. Its divided-product formula is
  checked against the seven-factor formula. The anchor histogram for an
  m-point line occurs at exactly m anchors, so division by m gives its
  complete line count; the first-coordinate-one chart contains all the
  configuration points. Every anchor sum, every histogram, every orbit
  maximum and all pair totals are checked. Stored maximal-line membership
  is supplementary, not the argument for the upper bound.
- The full command in the proof was rerun successfully: 14,819,805
  unordered pairs and 29,639,610 directed differences. All three full
  artifacts, all four source/input digests, and the entire summary are
  byte-identical to their pre-audit values. The complete 273-row summary
  was additionally checked against the stronger asserted threshold six
  (the driver's final threshold test alone is only ten). Its maxima are
  five in 265 orbits and six in eight, with no failures. The full critical
  check is `scripts/coefficient-feasibility/five-coordinate-critical-audit-result.json`;
  pre-replay identity evidence is
  `drafts/2026-10-11-five-label-critical-audit-before.json`. The original
  full census artifacts remain at the paths specified above.
- L057 restores every missing equation before asserting a recovery,
  including the nonzero pivot and consistency tests for both-zero
  quotients. Its same-support proof permits zero fourth weights. The
  map T=gamma_0+g*rho/[rho-(1-rho)*mu] is injective on E!=0 because
  g, rho and 1-rho are nonzero. Its excluded mu=0,-1 give gamma_1,
  gamma_2, and gamma_0 is absent from its finite image. Thus the three
  distinct finite base bad events are disjoint from R. Counting distinct
  parameters handles multiple lower-weight witnesses. Only containment
  R union {gamma_0,gamma_1,gamma_2} subset B is needed for subtraction;
  no additional exhaustiveness or full-weight assumption is hidden there.

This validates M<=6, |B|<=11 and |R|<=8 in the stated scope. The two
count paths still share a compiler and residue field; this is an exact
computationally dependent proof, not a formally verified census. No
additional mathematical input or DAG edge was introduced. This review
is local verification of a reproduced result, not a novelty claim.

## Mathlib

Full matching configuration maximum and conditional triangle count:
**not checked**. Supporting projective/affine line, finite-field,
Vandermonde and RS-distance coverage: **not checked**. Unknown
availability is not absence. The pinned event uses the inspected
ArkLib definition cited in L015; ArkLib is separate from Mathlib and
is not identified with the unread July ABF26 event. No Lean-certified
census or complete challenge resolution is claimed.

Classification: REPRODUCTION, applying established local reductions
and validating an existing finite claim. This is local proof/certificate
progress, without an originality claim or an advance beyond the checked
literature. The separate critical review above found no defect in the
application or complete verifier; independent challenge-level gaps remain.
