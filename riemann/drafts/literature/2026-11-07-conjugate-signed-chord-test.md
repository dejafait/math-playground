# Residue-corrected conjugate chord test — completed comparison

TARGET: Assess a residue-corrected straight-chord sign test for L884's actual conjugate primitive products, retaining L882's radial domains and the case Re(sigma)=0.
CHECKED: 2026-11-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact/stronger searches for weighted xi primitives, conjugate endpoints, chord integral inequalities, complex quadrature and sector-controlled reverse triangle inequalities; queries, inspected primary ranges and local failure comparison below. No matching signed-product theorem identified; no novelty inference.
SOURCE_EVIDENCE: Dragomir RGMIA22(2019) Article4 Theorem2/Corollary3 pp3-7 and Theorem3 pp8-10, https://rgmia.org/papers/v22/v22a04.pdf ; Article1 Theorem1 proof pp3-4 and Corollary2 pp4-5, https://rgmia.org/papers/v22/v22a01.pdf ; Dragomir math/0406159v1 Theorem1 pp2-3 and Proposition1 p9, https://arxiv.org/pdf/math/0406159v1 ; reused Lebl and predecessor univalence/xi-integral comparisons qualified below.
COMPARISON: General-domain quadrature removes convexity for path identities and absolute remainder bounds, but supplies no actual-G signed-product inequality. Sector-based estimates require pointwise phase control absent from L882. L885 stops the circular unsigned kernel only; neither source comparison nor a change of representative estimates its complementary signed remainders.
GAP: At least one actual full product must be proved nonnegative, or a concrete obstruction to the corrected chord mechanism must be established. Exact detour/winding accounting and actual-G signed compensation remain research tasks; no chord inclusion, sector bound or uniform margin is available.
REASON: Essential comparison is adequate for one bounded EXPLORE test using actual coefficient/derivative data and the existing exact primitives. No theorem import settles the target and no essential source is inaccessible. Newly ready scope requires separate supervisor approval before mathematics; no formula or estimate is derived in this literature turn.
LITERATURE_REASON: Changed mechanism from auditing circular local loss to a signed chord estimate; essential sign coverage and the pole-crossing case are missing.
SCOPE: L847 actual entire G; L882 matched conjugate branch under L879 stationarity/J!=0, fixed fibers, zero-free radial interiors and simple boundary pair; audited L883-L885. Retain both first-label orders, other zeros/multiplicities, label-dependent constants and d=0. No replacement function, graph existence, zero-free disk or added domain symmetry.
COVERED_TARGET: Test L884's actual conjugate product signs using residue-corrected straight-chord integrals, retaining L882's radial domains and Re(sigma)=0.

## Completed comparison — step68, 7 November 2026

LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The invocation TARGET
is unchanged. This comparison does not establish a new mathematical
result or approve its execution in the same invocation. The single
COVERED_TARGET states the mathematical continuation for separate approval.

### Local overlap and limits retained

Used the supplied full overview and DAG, then read L882's hypotheses,
matched-domain conclusions and relevant seed/count proof, L883's exact
H_j/lift formulas, and L884/L885's product thresholds and qualifications.
Read the predecessor actual-conjugate-primitive source assessment and
working records64/65, and the common-line, algebra-only and paired-kernel
ATTEMPTS57/61/65. Scoped searches there found an unused chord suggestion,
not a signed estimate. No cross-notebook result was used.

L882 provides radial Jordan interiors, not convexity, a zero-free disk,
conjugation symmetry of the domains, or inclusion of a chord. L883's
weighted forms are meromorphic only at zero; other G zeros are not
poles. Those existing facts permit a contour accounting problem but
do not supply its sign. Conjugate reality and the total period remain
insufficient by L884's existing formal controls. L885's negative circular
sectors are not counterexamples to full-product compensation or to a
different representative. No new counterexample has been obtained.

### Primary results actually inspected

S. S. Dragomir, *Generalized Ostrowski and Trapezoid Type Rules for
Approximating the Integral of Analytic Complex Functions on Paths from
General Domains*, RGMIA Research Report Collection22 (2019), Article4,
[Theorem2 pp3-5, Corollary3 pp6-7, Theorem3 pp8-10](https://rgmia.org/papers/v22/v22a04.pdf).
Analytic f on a domain D, a smooth path in D from u to w, a chosen
path point x, and integer n>=1 give a finite derivative expansion
with remainder (-1)^n/n! integral K_n(x,z) f^(n)(z) dz; K_n is
(z-u)^n before x and (z-w)^n after x. Read the integration-by-parts
base case, induction, endpoint combination and modulus/Hölder proof.
Bounds are absolute; convexity is unnecessary. For the weighted forms,
fixed paths avoiding zero meet the analytic-domain requirement; a
through-zero path fails it. No uniform shrinking-detour bound or
product sign follows. No specialization was calculated. Theorem4 was
read only as a statement; its proof is omitted as similar.

Dragomir, *Approximating the Integral of Analytic Complex Functions on
Paths from Convex Domains in Terms of Generalized Ostrowski and Trapezoid
Type Rules*, RGMIA22 (2019), Article1,
[Theorem1 and proof pp3-4; Corollary2 pp4-5](https://rgmia.org/papers/v22/v22a01.pdf).
This earlier Taylor-integral method assumes analytic f on a convex
domain containing the path and expansion points; the proof integrates
Taylor's formula and uses Fubini. It gives a finite expansion plus an
explicit remainder, not a sign theorem. It cannot infer convexity of
L882's interiors. For a pole-avoiding segment, applicability to the
weighted forms would require choosing an analytic neighborhood and
checking it, rather than assuming the segment lies in either interior.
The stronger general-domain comparison above avoids that domain
restriction for a detour. No convex-source theorem is being used across
zero, and no new convex-neighborhood construction is proved today.

Dragomir, *Some Reverses of the Continuous Triangle Inequality for
Bochner Integral of Vector-Valued Functions in Complex Hilbert Spaces*,
[arXiv:math/0406159v1, 9 June2004, Theorem1 pp2-3 and Proposition1 p9](https://arxiv.org/pdf/math/0406159v1).
For Bochner-integrable f, unit e, and k1,k2>=0, the hypotheses
k1||f||<=Re<f,e>, k2||f||<=Im<f,e> almost everywhere imply
sqrt(k1^2+k2^2) integral||f||<=||integral f||. Its equality condition
is integral f=(k1+i*k2)(integral||f||)e. Read the Schwarz/integration
proof and equality case. Proposition1 assumes
0<=phi1<=arg f<=phi2<pi/2 and gives factor
sqrt(sin^2(phi1)+cos^2(phi2)); its proof checks the two projections
and applies Theorem1. L882 supplies no such phase inequalities for
the weighted chord integrands. A norm lower bound also does not sign
L884's S-products. Thus this cannot be imported as compensation.
The source has minor printed cross-reference/algebra typos; only the
stated projection-based conclusion is compared, with no new reproof.

Reuse, without reopening unchanged coverage, Lebl, *Guide to Cultivating
Complex Analysis*, v1.10, 5 November2026,
[Theorem4.4.2/Proposition4.4.3 pp104-108](https://www.jirka.org/ca/ca.pdf#page=104)
through audited L883. Laurent convergence and separated polar/logarithmic
primitive terms cover exact integration; the proposition's proof is an
exercise, not a read proof. Reuse the predecessor assessment's inspected
Pascu-Pascu2011 Theorem1.1/Theorem2.4 and Lagarias-Montague1106.4348v3
Theorem2.1/Section4 comparisons. Their missing derivative/convexity and
real-line monotonicity premises do not disappear on choosing a chord.
No univalence or ordinary xi-antiderivative theorem is a sign input here.

### Search and access record

Queries issued in this review:

- `"complex integral" "chord" "inequalities" analytic function`;
- `"Riemann xi" "integral" conjugate zeros weighted`;
- `holomorphic primitive conjugate endpoints zero free starlike domain sign inequality`;
- `Dragomir complex line integrals inequalities segment real part sector reverse triangle inequality analytic functions pdf`;
- `"holomorphic" "conjugate" "primitive" "inequality"`;
- `"complex" "Chebyshev" "functional" "real part" integral inequality Dragomir`;
- `"Approximating the Integral of Analytic Complex Functions" "Dragomir" pdf`;
- `"Generalized Ostrowski and Trapezoid Type Rules" "General Domains" pdf`;
- `"G(z)" "conjugate zeros" "primitive"`.

The author-supplied RGMIA2019 volume index identifies Articles1/4.
Initial unpadded PDF URLs failed; the padded URLs above succeeded.
The university repository identifies a 2023 book chapter with the
general-domain title, DOI10.1142/9789811261572_0010, but supplies no
full text. Its version has not been checked; the inspected source is
explicitly the 2019 author preprint. The double/path-integral Article57
was screened only through its introduction and Theorem1: disk derivative
error bounds, not weighted conjugate signs; no later result is an input.
The quadratic-reverses journal abstract, broader monograph, newer
operator inequalities and unrelated xi-zero papers remain uninspected
leads, not coverage. Search snippets are not theorem evidence.

Shell download failed at DNS; web primary text remained accessible.
Screenshots produced no readable image evidence in this interface and
one timed out. All claimed reads above use complete relevant extracted
text, including proof cases; no screenshot preview establishes them.
No essential access blocker remains. Mathlib full matching and supporting
coverage were not checked; absence is not asserted.

### Bounded mathematical continuation, after separate approval

Use exactly COVERED_TARGET. Starting from L883's full weighted forms,
compare the increasing lifted arc with the conjugate chord using the
existing polar/logarithmic primitives. Keep a specified avoiding detour
when Re(sigma)=0 and its exact lift correction. Do not assert chord
inclusion in either radial interior, and do not replace the forms by
their entire tails without integrating and restoring every removed term.

The discriminating signed test is to conjugate-pair the corrected
integrals, retain residue/chord cross terms in S, and seek a lower
bound for one full product from the actual convergent coefficient or
derivative data. A quadrature remainder can help only with a signed
margin that survives its full bound. This is a proposed test, not a
derived kernel, margin, truncation rule or claimed successful estimate.
No finite numerical scan of unspecified off-real labels is authorized.

Continue on one rigorously nonnegative full product (equality included),
or a specific actual-G obstruction to this representation's sign test.
If only endpoint identities or an unproved phase, convexity, monotonicity,
domain-inclusion or uncompensated absolute bound remains, stop this
bounded chord option and save the precise unpaid condition. Do not
repeat L885's circular pointwise-nonnegativity test. Smaller label ranges
are permissible only if rigorously specified with their complements open.
Retain both label orders, all other zeros/multiplicities, d=0 and
label-dependent constants. Pole-crossing algebra must not be replaced
by a principal value or by dropping divergent individual pieces.

This is a creative actual-function sign mechanism toward L884 branch
exclusion/L868, not routine reproduction of quadrature. Recommend
proof_attempt/creative, deep_research/max after separate approval.
The critical claim is signed compensation sufficient to reverse at
least one of L884's strict products; the bounded test above decides
whether this representation offers information beyond endpoint periods.
Other branches, graph existence/compactness, the sharp bound, higher
signs and Xi transfer remain unresolved. No mathematical exploration
attempt was spent in this source review.

## Original source-review nomination — historical

Nomination after step67 only; not a ready mathematical assessment.
No chord formula, theorem application or sign estimate was derived in
this audit. The predecessor working record preserved this unused option.

The main gap remains L030-L032/C032a actual-Xi mixed positivity.
A nonnegative value of either full product alpha*beta or gamma*beta
would contradict L884's necessary strict products on the stated branch,
potentially narrowing the graph problem toward L868. Other branches,
graph existence/compactness, the sharp bound, higher signs and Xi transfer
are independent gaps. Local signs in L885 agree with the checkerboard
and are not themselves an exclusion.

Review exact and stronger known results on integrals of holomorphic
functions between conjugate critical endpoints, weighted primitive
inequalities and signed chord estimates on zero-free radial domains.
Reuse inspected primitive and univalence comparisons; search the local
contact/primitive failure records narrowly before new primary sources.
Retrieve theorem hypotheses and essential proof cases before adopting
any estimate. Do not infer novelty from a missing match.

The specific alternative to compare is integration of the three
weighted forms G(z) dz/z^(j+1) along the straight segment from sigma
to its conjugate, with exact correction to the increasing lifted arc.
This is a proposed representation, not an asserted admissible contour
or estimate. If the segment meets zero, a precise avoiding detour and
all its polar and logarithmic contributions are necessary; do not
silently take a principal value, remove negative powers, or exclude
Re(sigma)=0. Other G zeros are not poles of these forms. Membership
of the chord in a zero-free radial domain must not be assumed.

Continue only if comparison identifies an applicable signed estimate,
or a concrete bounded signed test that uses actual G information beyond
the endpoint identity. The decisive threshold is one full product >=0,
equivalently the corresponding exact complementary remainder meeting
L885(8); an explicitly justified smaller label range is permissible if
the complement stays open. Abandon this representation if it merely
recovers the same periods, requires an unproved sector/convexity/domain
premise, or repeats the stopped pointwise circular nonnegativity test.
No new lemma or mathematical script is authorized by this nomination.

Mathlib full matching and supporting coverage for this proposed estimate
is unchecked. The next turn is literature_comparison, standard/high;
any newly ready mathematical continuation receives separate approval.
