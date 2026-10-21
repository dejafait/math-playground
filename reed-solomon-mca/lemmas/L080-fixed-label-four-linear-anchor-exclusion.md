# L080 — Fixed-label exclusion of four linear isolated triangle anchors

## Hypotheses

Use audited L057's local triangle converse over F=F_(97^20), with
C=RS[F,H,8], shifted moments sigma_j(e)=sum_(x in H)e(x)x^j for
j=1,...,8, and the pinned cell 1/4<=delta<5/16. Fix

\[
H=\{1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96\},
\quad P=(a,b,c)=(64,75,33),
\quad Y=(1,96),\ Z=(18,79),\ W=(8,50).
\]

The base supports are {a,b} union Y, {a,c} union Z, and {b,c} union W.
Put U=P union Y union Z union W, Q(X)=product_(h in H minus U)(X-h),
and c_x=Q(x) for x in U. Normalized weights w=(p,q,r) range over
(F_97 minus {0,1})^3. The original finite gamma_0,gamma_1,gamma_2
are arbitrary distinct elements of F and lambda is any nonzero element
of F. Write g=gamma_1-gamma_0 and rho=(gamma_2-gamma_0)/g.
Neither the original chart nor lambda is required to be rational.

An anchor here means an additional recovery on a four-subset K disjoint
from P, whose two scalar projections in L057 (5) are both nonzero,
whose restored equations hold, whose four actual weights are nonzero,
and whose mu is not 0 or -1 and satisfies E=rho-(1-rho)mu!=0.
Both-zero recoveries, lower-weight errors and base parameters are outside
this anchor definition. No equality-family, extraction or challenge-level
definition hypothesis is imposed.

## Conclusion

There are no four anchors at one normalized weight triple with distinct
additional parameters and supports intersecting pairwise in at most one
label. In fact, any two distinct anchors at one weight triple have
support intersection of size three.

The complete chart-free row table has 423 weight triples with exactly
one full isolated row each. The only other full isolated fiber is
w=(71,5,17), with supports

\[
\{22,27,47,85\},\ \{22,27,47,89\},\ \{22,27,85,89\},
\ \{22,47,85,89\},\ \{27,47,85,89\},
\]

and respective scalars 30,50,22,34,63. Original E gates may delete rows.
Every other gated weight triple has no such row. This is an exact
finite-computation-dependent exclusion for this assignment only. It
does not exclude arbitrary-label quartets, prove the uniform triangle
twelve bound, improve 11/q–16/q, or settle the challenge. Its separate
critical proof/certificate audit on 2026-10-13 found no defect in this
restricted exclusion.

## Proof

### Existing inputs and exhaustive reduction

Import audited L057's recovered-weight and all-eight-moment criterion,
and L059's exact chart-free table interpretation. The underlying
recurrence input already assessed there is P. Chojecki, *Shortening
Bounds for Reed–Solomon MCA*, author TeX v9.2, July 17, 2026,
DR2 (`drc:lem-locator-recurrence`) and DR6–DRC
(`drc:thm-exact-compiler`), statements and complete proofs at lines
2785–2935 of the
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
The specialization has distinct nonzero labels, nonzero multiplier x,
R=8 and t=4<R, as verified in L057. The mutable source is not certified
identical to ePrint 2026/1463. No general theorem is reproved; the new
work is a bounded collision certificate using already justified formulas.
The prior assessment is
`drafts/literature/2026-10-12-four-linear-isolated-anchors.md`; this
calculation establishes no certified originality beyond checked sources.

There are exactly binom(13,4)=715 possible K. Because J=P, both
projections are single scalars. Both-zero and exactly-one-zero cases
cannot be isolated anchors. Otherwise mu=z_K/y_K is a unique nonzero
prime-field scalar. Reject mu=-1; the restored equations force exactly
one triple w, given by L057 (11), equivalently L059 (4). Ungated w
gives no admitted base triangle. For gated w, L057 (13) gives the unique
four numerator weights omega on K. The common factor lambda/(gE) is
nonzero whenever the finite gate holds, so fullness is all omega!=0.
This exhausts every isolated disjoint-P support at every admitted w;
enumerating all 95^3 weight triples separately is unnecessary.

Omitting E produces a superset for every original chart, as in L059 (1).
The map T=gamma_0+g rho/E is injective on admitted mu, since g,rho and
1-rho are nonzero. Thus a quartet must occur among four same-weight
rows with distinct scalars in this table. Enforcing E deletes rows only
and cannot create a quartet. Both-zero and zero-fourth-weight rows are
classified in the certificate and excluded solely by this target's
definition, not from any full recovery count.

### Complete finite certificate and independent replay

Run from the active notebook directory:

```sh
python3 scripts/triangle-recovery/four_linear_anchor_collisions.py
python3 scripts/triangle-recovery/verify_four_linear_anchor_collisions.py
```

The producer uses L057 (5), (6), (11) and (13), saving every support,
projection, beta pair, isolated scalar, forced weight triple, rejection,
gated numerator and eight-moment residual. The full artifact is
`scripts/triangle-recovery/four-linear-anchor-collisions.json`, SHA256
`e49d40177f74444e2f175b9f8ed24ae522794e0a8190b73af83be805952ae517`.
The verifier compares its complete support list, in order and without
duplicates, against every four-subset of H minus P.

The replay uses a different formula path. For each K, let M have columns
v_x=(x,...,x^8)^tr for K followed by P. Its first seven rows are an
invertible shifted Vandermonde matrix: the determinant is the product
of the seven nonzero labels times their Vandermonde determinant. Solve
these rows independently for Y=sum_(x in Y)c_x v_x and
Z=sum_(x in Z)c_x v_x. The eighth-row residual is exactly the functional
with polynomial X product_(x in K union P)(X-x), with leading coefficient
one and zeros at all seven columns. Hence its two residuals equal the
producer's scalar projections, including every zero case.

For nonzero residuals, take their ratio mu. If d_a,d_b,d_c are the last
three coefficients of the solved Z-mu Y, cancelling the P-coefficients
gives independently

\[
p=(1+d_a/c_a)/(1+\mu),\qquad
q=d_b/(\mu c_b),\qquad r=-d_c/c_c.
\]

All divisions are nonzero after the isolated/mu!=-1 gates. The first
four coefficients of that difference give omega. For every gated row,
the verifier reconstructs N_K directly from w and mu and checks all
eight moments against those recovered coefficients, including the 64
rows with a zero fourth coefficient. It imports only the inspected
modular Gaussian arithmetic in `verify_fixed_union_table.py`, not the
producer or its interpolation, beta or restored-point formulas. Both
paths share Python and residue-field representation: this is formula-path
independence, not independent arithmetic foundations or a critical audit.

Complete actual/required coverage is 715/715 supports: 595 isolated,
114 one-zero and 6 both-zero rows. Isolated rows partition into 57 with
mu=-1, 46 ungated, 64 gated lower-weight and 428 full rows. All 492 gated
eight-moment checks have zero residuals; failures are 0/0. The 428 full
rows occupy 424 weight points: 423 singleton fibers and one five-row
fiber. Every fiber's scalars are checked distinct. The exceptional fiber
is precisely the displayed one. L068 is a comparison/regression, not
an assumed count or mathematical input.

The producer saves all ten same-weight pairs and all five same-weight
four-subsets. The verifier reconstructs the pairs, builds their graph
with an edge only for intersection size at most one, and enumerates its
increasing four-cliques; it also replays every rejected four-subset.
Each of the ten pair intersections has size three, and every quartet's
six intersections have size three. There are zero qualifying pairs and
quartets. The full replay, all gated numerator/recovered moment vectors,
complete fibers, pair intersections, quartet rejections and empty failure
array are saved in
`scripts/triangle-recovery/four-linear-anchor-collisions-verification.json`.
The complete small summary, exceptional fiber, ten pairs and five quartet
rejections were inspected, not inferred from a preview. Every large case
set is checked by the executed complete replay.

The superset has no desired quartet, proving the conclusion for every
original E restriction. This ends the fixed-assignment test; no expanded
label sweep or arbitrary-label exclusion follows.

### Separate critical proof/certificate audit (2026-10-13)

The pre-existing EXPLORE assessment
`drafts/literature/2026-10-12-four-linear-anchor-exclusion-audit.md`
approved this audit. The full two programs above and imported `invert`
and `mul` functions were inspected. Both reproduction commands were
executed. Complete relevant case sets were checked by the replay,
rather than inferred from printed counts or selected positives.

**Scope and coverage.** The programs independently fix the same ordered
P,Y,Z,W. They generate H from x^16=1 in F_97, check the nine distinct
labels, and evaluate Q using exactly its seven complementary roots.
Thus every c_x is nonzero. The ordered combinations of H minus P
contain all 715 four-subsets exactly once; none is a base support.
The verifier compares the entire saved list with this list. Since m=3,
the projected quotient is scalar: the 6 both-zero, 114 one-zero and
595 nonzero-pair cases exhaust all ranks. A nonzero-pair ratio is
automatically rational and nonzero, even over F_(97^20). Rejecting its
57 mu=-1 cases precedes division by 1+mu. The remaining three restored
equations each have a nonzero coefficient of its respective weight,
so no other weight triple can be missed for these isolated supports.
The claimed theorem remains the specified rational-weight target.

**Formula bridges and signs.** The producer evaluates exactly L057
(5), (6), (11), (12), (13), including the minus signs in beta and in
the b coefficient. All interpolation differences, x f_K(x) for x in P,
c_x, mu and 1+mu used as divisors are nonzero. For the verifier, the
first seven moment rows on K followed by P have nonzero determinant
(product of labels) times the Vandermonde product. Its Gaussian
elimination normalizes each nonzero pivot and eliminates that column
in every other row modulo 97; `mul` uses the same modulus and the
correct array dimensions at every call.

The eighth-moment residual has a polynomial with leading term X^8,
no constant term and roots at all seven labels. It is therefore
X product_(x in K union P)(X-x), with positive leading coefficient.
This equals X f_K(X) G_P(X), proving the exact projection comparison
for Y and Z, including all zeros. For a permitted ratio, Z-mu Y lies
in the seven-column span. If d are its three solved P coefficients,
the cancelling coefficients are -d. L057's unique restored beta
combination is consequently -d, not d. Matching the three numerator
coefficients with -d gives exactly the verifier's p,q,r formulas above.
Cancellation leaves its first four coefficients as omega. No individual
beta^Y or beta^Z is identified with a full eight-moment solve when its
projection is nonzero.

The verifier does not independently compare the redundant stored beta
arrays term by term; the audit checked their defining code against
L057 (6). Every load-bearing restored weight and every gated omega
is instead compared with the independent seven-column solve. All 538
mu!=-1 isolated cases have their forced weights compared: 46 fail the
base gate and 492 pass. Every passing row is checked against all eight
original numerator moments, including all 64 lower-weight rows. Thus
the 428 full rows do not come from a first-four-moment test or a
premature full-weight assumption. Lower-weight and both-zero rows are
excluded only from the defined anchor set, not a total bad-set bound.

**Complete collision evidence.** The replay independently groups all
428 full rows by their forced weights, compares all 424 fibers exactly,
and verifies distinct scalars within each fiber. There are 423 singleton
fibers and the displayed five-row fiber only. Its complete rows and all
ten pair and five quartet entries were also inspected explicitly. All
ten intersections have size three; each quartet has all six intersection
sizes equal to three. The independent adjacency traversal has no
four-clique, and every rejected four-subset is compared as well. There
is no selected-positive or threshold-only check in this conclusion.

**Original chart and extension field.** L057 and L059 apply to precisely
these nine labels and nonzero normalized base weights. For arbitrary
distinct original gamma_i, g,rho,1-rho are nonzero. At E!=0, the factor
lambda/(gE) is nonzero, so fullness agrees exactly with omega fullness.
The inverse t=rho/E is finite and avoids 0,1,rho when mu!=0,-1.
Equality of two surviving T values forces equal E and then equal mu.
Consequently an actual simultaneous pair or quartet injects into a
single enumerated weight fiber. The original infinity gate removes
rows only and never creates an intersection-qualified pair or quartet.
All computations on prime-field data remain valid in F_(97^20);
neither gamma_i nor lambda nor the excluded direction is rationalized.
No equality premise or absence of other recovery types is used.

Both complete artifacts reproduced byte for byte. The producer hash
is the recorded e49d40177f74444e2f175b9f8ed24ae522794e0a8190b73af83be805952ae517;
all three inspected source files were also unchanged. Pre-replay hashes
are in `drafts/2026-10-13-four-linear-anchor-audit-before.json`; the
hash comparison, exact summary and exceptional fiber are in
`scripts/triangle-recovery/four-linear-anchor-critical-audit.json`.
Actual/required checks were 715/715 supports, 492/492 gated moment
vectors, 10/10 pairs, 5/5 quartet rejections and 0/0 failures. The two
paths still share Python and residue arithmetic; this is not a Lean
verification or independent arithmetic implementation. No repair was
needed. The audit validates the finite restricted theorem, not a new
stronger bound or certified originality beyond the sources checked.
The direct mathematical inputs remain L057 and L059; no DAG change or
change to the main argument follows.

## Mathlib

The full matching fixed-label collision exclusion is **not checked** in
Mathlib. Supporting finite-field arithmetic, shifted Vandermonde
independence, enumeration and clique tests are also **not checked** here.
The canonical informal inputs are audited L057 and L059; no Mathlib
absence claim or Lean verification is made.
