# Auxiliary-to-actual complex-zero transfer — review2058

TARGET: Review whether a complex-zero loss bound for the explicit auxiliary-Jensen-to-U_N coefficient map can transfer Kuznetsov Proposition4.2's real-rooted inputs to at most two nonreal zeros, with N=6 as the sole proposed operator-applicability test.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Review2058 reused discovery2026, review2004, October30 moment-weight coverage and stops111/1596; searched the named November20–21 Pollaczek/Jensen records and exact complex-zero-decreasing, loss-bound, apolarity, Grace/Walsh and biorthogonal terminology. The bounded search found no inspected theorem supplying the full composed-map loss<=2. This does not establish novelty or nonexistence; queries and scope are below.
SOURCE_EVIDENCE: Kuznetsov2008 Propositions4.1–4.2 and complete displayed proof pp567–568, doi:10.4153/CMB-2008-055-0; Bunton et al.2015 Theorems7–8 and proofs pp132–133, doi:10.2140/involve.2015.8.129; Craven–Csordas1995 definitions/Theorem1.4 pp420–422; Borcea–Branden2009 Theorems2/11, Corollary5 and Lemma4/proof pp470,478–480; Iserles–Saff1989 Sections1–2/Theorem2 pp560–563 and Proposition6/proof pp566–567. Exact links, hypotheses and access qualifications are below.
COMPARISON: The auxiliary input has a standard source route via scalar Jensen polynomials and Proposition4.1; Jensen weights cannot simply be applied to an arbitrary Pollaczek expansion. The inspected additive nonreal-zero theorem requires qD+alpha q' with alpha>=0; symbol stability classifies full preservation, without a two-exception allowance. Neither identifies the prescribed composition as an admissible operator. No map identity, input root certificate or new zero bound was computed.
GAP: No inspected source supplies an applicable uniform loss<=2 for undoing input weights/damping, applying the beta map and using the output's own weights. A full operator factorization or independently justified restricted-input theorem remains missing. No N=6 operator test or all-N calculation is approved by this review.
REASON: Complete this bounded source search as inconclusive EXPLORATION, park automatic auxiliary-to-actual transfer without declaring it false, and nominate a separate direct actual-coefficient partial-biorthogonality question. That nomination requires its own review and is not an approved mathematical continuation.
LITERATURE_REASON: Changed mechanism from supplied-measure Gram construction to a quantitative auxiliary-to-actual polynomial operator. Essential complex-zero-loss coverage is missing; this is not additional browsing on the completed ready audit or the parked measure lead.
SCOPE: Completed literature-only comparison2058. No new coefficient computation, lemma, mathematical script or preserver reproof. EXPLORE records the bounded-search result, not permission to run the parked N=6 composite-map test. Reuse the inspected statements if a materially new factorization or restricted-input hypothesis is later supplied.

## Completed comparison2058

The main gap is L030–L032/C032a; the branch threshold remains C029m's
eventual Hermite index<=1. A multiplicity-counted nonreal-zero bound<=2
would suffice for its distinct-root interface C029l. No such bound for
the actual family is obtained here. The continuation test in nomination2057
required an applicable quantified theorem and an independently checkable
operator hypothesis; this review has not met that test. It is not a
counterexample to the map, the restricted actual inputs, or RH.

### Auxiliary input: distinguish the bases

Kuznetsov, *Expansion of the Riemann Xi Function in Meixner–Pollaczek
Polynomials*, CMB51(4)(2008),561–569,
[primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-3-function-in-meixner-pollaczek-polynomials.pdf),
Propositions4.1–4.2 and displayed proof pp567–568 were reaccessed.
The former tests the scalar polynomial with coefficients
(2k+1)!! b_k/(2k)!!; the latter concerns the entire auxiliary Pollaczek
series, using the real-polynomial approximability of f(x)=sum u_k x^k/k!.
Its product-truncation proof is not a statement about every basis truncation.

For source matching, the nominated finite Pollaczek input has coefficients
m_(M,k)u_k/(2k+1)!!, M=N+2. Proposition4.1's scalar test is therefore
sum m_(M,k)u_k x^k/(2k)!!: this is the scalar Jensen polynomial of f(x/2).
The standard named Jensen theorem is the relevant finite-input theorem,
under the source's Laguerre–Polya approximability premise. This explains
the normalization match; it is not an independent audit of that premise
or a new finite root certificate. If “input” instead means the monomial
polynomial with coefficients m_(M,k)u_k/(2k+1)!!, that is a different
object and is not covered by this identification. Fix the Pollaczek
interpretation before any later operator application. All odd terms,
M's input weights and N's output weights remain essential.

### Quantified theorem, but no supplied operator specialization

Bunton, Jacobs, Jenkins, McKenry, Piotrowski and Scott,
*Nonreal zero decreasing operators related to orthogonal polynomials*,
Involve8(1)(2015),129–147,
[Theorems7–8, pp132–133](https://msp.org/involve/2015/8-1/involve-v8-n1-p11-s.pdf):
for real polynomials p,q and alpha>=0,
Z_C(q p'+alpha q' p)<=Z_C(p)+Z_C(q), with algebraic multiplicities
and Z_C(0)=0. The complete proof cases were inspected: alpha=0 uses
Rolle; positive alpha accounts for common-root multiplicities and uses
signed powers of q between real zeros. Constants and the zero output
are separate cases; the nonconstant case computes the leading degree
before subtracting the real count. Thus the statement really allows
exceptions through q, rather than merely asserting preservation.

No identity expressing the prescribed whole map as this operator or
an admissible composition was supplied. Its three-term coefficient
stencil is not such an identity. C029s already obstructs the *different*
fixed q=t^2+1/4 output-range representation; this review neither repeats
that test nor extends its conclusion to other factorizations.

Craven–Csordas, *Complex zero decreasing sequences*, Methods Appl.Anal.
2(4)(1995),420–441,
[definitions1.2–1.3 and Theorem1.4, pp421–422](https://www.intlpress.com/site/pub/files/_fulltext/journals/maa/1995/0002/0004/MAA-1995-0002-0004-a004.pdf),
distinguishes multiplier sequences from complex-zero-decreasing
sequences. Theorem1.4 requires a diagonal scalar multiplier interpolated
by a polynomial with real zeros outside (0,n), or the stated
Laguerre–Polya analogue. It does not cover arbitrary coefficient mixing
or show that inverses of damping/weights retain a zero-count property.
These statements were inspected, not reproved. No interpolation or
diagonalization for the composed map is asserted.

Borcea–Branden, *Polya-Schur master theorems for circular domains and
their boundaries*, Ann.Math.170(2009),465–492,
[Theorems2/11, Corollary5, Lemma4](https://annals.math.princeton.edu/wp-content/uploads/annals-v170-n1-p14-p.pdf),
printed pp470,478–480: for T:R_n[z]->R[z], hyperbolicity preservation
has the low-range interlacing alternative or real-stability of one of
T[(z+w)^n], T[(z-w)^n]. Here stability excludes zeros when both
variables lie in the open upper half-plane. Grace–Walsh–Szego requires
a symmetric multiaffine polynomial, a circular domain containing the
points, and full total degree or convexity. Lemma4's complete sufficient
proof was inspected: perturb into strict stability, polarize the symbol,
then use Hurwitz; lower-degree inputs require an extra approximating
factor. This is a full-preservation test. A stable symbol with “one
exception” is not a conclusion of these statements. No symbol for our
map was computed or asserted stable.

### Direct-transform lead; not a second attempt

Iserles–Saff, *Zeros of expansions in orthogonal polynomials*,
Math.Proc.Camb.Phil.Soc.105(1989),559–573,
[author PDF](https://www.math.vanderbilt.edu/saffeb/texts/101.pdf),
Sections1–2/Theorem2 pp560–563 and Proposition6 with its displayed
justification pp566–567 were inspected. Theorem2 assumes a convergent
strictly sign-consistent generating kernel and *all* scalar input roots
in its parameter interval. The output uses inverse norm/generating
weights. Proposition6 treats Meixner polynomials of the second kind
with real delta, eta>0 and the stated open parameter interval; its
proof invokes Theorem2 and kernel sign consistency. This is not an
explicit partial-root theorem. Upstream Iserles–Norsett proofs are
unread. The author PDF timed out through the connected search tool;
the other web tool supplied the indexed primary text. PDF screenshot
calls supplied reference labels without image payloads; no visual
verification is claimed.

This suggests a different, unapproved question: use partial
biorthogonality/sign changes on the *actual scalar coefficient
polynomial* rather than invert auxiliary weights and damping. Whether
N-2 input zeros suffice, in which interval, with what multiplicity
and normalization, is not derived here. Its exact theorem comparison
and actual scalar input condition belong to the next REVIEW_REQUIRED
assessment. No root count, determinant or transform estimate for it
has been attempted. In particular no two-atom/theta, fixed quadratic,
residue, homotopy or inter-degree update condition is being recycled.

### Search, reuse, outcome and limits

Reused discovery2026/review2004, the October30 Romik moment-weight
assessment and its narrower L530 scope, stops111/1596, and the
imaginary-shift comparison2032. Read C029l/m, C029q's finite setup and
C029s's fixed-range hypotheses/conclusion. These stops are contrasts,
not global prohibitions or premises. No cross-notebook input was used.
The October quasi-RH sources are unnecessary: no zero-free estimate or
reciprocal continuation is proposed. Matching Mathlib coverage unchecked.

Queries included `complex zero decreasing linear operators polynomials
number nonreal zeros`, `linear operators at most nonreal zeros symbol`,
`complex zero loss apolarity Walsh Grace polynomials`, `Borcea Branden
master theorems Grace pdf`, and the exact Iserles–Saff title. Cardon's
strip-reduction abstract and finite-difference/dissertation hits were
leads only; strip width is not a bound on the number of exceptional
zeros. An unrelated arXiv URL was opened in error and is not evidence.
No API key, mathematical script, lemma, PROOF or DAG write occurred.

The result is EXPLORATION: a completed bounded source comparison,
with a useful input-normalization route and explicit operator-hypothesis
limits, but no applicable composed-map loss bound. Failure to locate
one is not an impossibility theorem or new mathematical discovery.
Park this dependent proposal without an N/precision sweep. The only
new continuation is the separately nominated direct-transform review;
uniform actual-family index, initialization, degree drops, weighted
convergence/upstream[9] qualifications and Xi transfer remain open.

## Original nomination2057 (historical; not current approval)

## Exact proposed map and relevance

The main gap remains L030–L032/C032a actual-Xi mixed positivity; on
this branch C029m's eventual Hermite index at most one is unproved.
The intermediate question is whether one can bound the increase in
nonreal zeros through the *prescribed* auxiliary-to-actual coefficient
map. A bound of two nonreal zeros, even with algebraic multiplicity,
would be stronger than the distinct-pair condition needed by C029l.
No such bound, source applicability, or real-rooted-input premise is
asserted by this nomination.

For later source comparison only, specify the input as the degree
N+2 Jensen-weighted polynomial of the auxiliary series with coefficients
u_k/(2k+1)!! from Proposition4.2, using that input degree's own weights.
The proposed linear map first recovers its finite auxiliary coefficients
by undoing those nonzero weights and the double-factorial normalization;
then applies C029m's exact three-term coefficient formula for beta_k,
0<=k<=N; finally uses degree N's own Jensen weights and the fixed
Pollaczek basis to form U_N=T_N/S. All these component formulas are
already recorded in C029m/n/q. This specification is a question about
their composition, not a derived identity or a theorem on its zeros.
Do not substitute the input degree's weights for the output weights.

The prospective N=6 applicability discriminator therefore concerns
exactly nine auxiliary coefficients u_0,...,u_8 and the full seven
output coefficients beta_0,...,beta_6, with all odd entries retained.
A later test must use a coefficient-defined operator hypothesis, for
example the precise symbol condition of a genuinely applicable
zero-count theorem. Its definition and threshold must be fixed before
any output inspection. No symbol formula, test polynomial, certificate
or numerical experiment has been chosen or executed here.

## Continuation and abandonment test

First reuse the known generic multiplier assessment referred to by
discovery2026 and the stops111/1596 cited in review2004; read their exact
scope rather than reinterpret historical stops as global bans. Retrieve
only the necessary primary theorem statements and proof cases for a
quantitative nonreal-zero bound (potentially apolarity or complex-zero
decreasing operators); these are search directions, not inspected
theorems. Check whether the auxiliary finite-input construction really
matches the cited real-zero result before using it.

Continue only if the theorem gives a bound without assuming the desired
output zero count, with explicit hypotheses on this composed operator
or on the actual auxiliary inputs and one independently checkable N=6
condition. A bare real-rootedness-preserver classification, a change of
coefficients/damping, or the existence of some factorization is not
enough. If the generic operator bound fails, record its precise scope;
do not reject the restricted actual inputs or RH. If the needed source
coverage or restriction is unavailable, park this proposal and choose
a materially different mechanism; no automatic degree/precision sweep.

Essential inputs: C029m's full family, C029l's distinct-root and actual-
degree convention, C029n/q's fixed coefficients and constants, and
discovery2026's qualified auxiliary-source comparison. Preserve
C029q/r/s/t/v/w/x, stop2047 and the measure-source stop2057. The
uniform eventual bound, initialization, singular/degree-drop cases,
weighted convergence/upstream[9] and Xi transfer remain unresolved.
No cross-notebook input; Mathlib matching coverage remains unchecked.

Creative priority considered: a genuinely new all-N complex-zero-loss
mechanism could merit proof_attempt/creative, but no theorem hypotheses
or bounded mathematical test are ready. The immediate routing is
literature_comparison/standard/high; do not label this nomination or
a routine operator specialization creative merely to meet scheduling
preferences. A successful assessment must recommend the purpose of
the exact subsequent attempt on its mathematical merits.
