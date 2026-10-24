# Mask-17 global scalar-square status — source approval

TARGET: Determine whether L124's mask-17 product theta²−9 is trivial in K*/(K*² Q*) by an exact global certificate.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact octic coefficients, rational-scalar square tests and Trager algebraic factorization; compared the scoped October 24 assessments/history and ATTEMPTS/052–054. No inspected source decides this element; the complete factorization method is established, not new.
SOURCE_EVIDENCE: Read Trager (SYMSAC 1976), Section 2 pp.219–221, Theorems 2.1–2.3, Lemma 2.4, Corollary 2.5 and algorithms sqfr_norm/alg_factor with their correctness and termination proofs; Milne ANT v3.08 Theorem 3.35 and its proof pp.60–62, plus valuation conventions; reuse Bruin–Stoll arXiv:0803.2052v2 Section 2 and directly read Section 6 pp.11–13; inspected official SymPy 1.14.0 factorization/domain documentation.
COMPARISON: Known support/ramification and exact number-field factorization methods cover a finite rational-scalar comparison without class/unit enumeration. L124/C124a give only local collisions; the instance's scalar restriction, exact identity or complete nonsquareness certificates remain to be supplied in research.
GAP: Prove the rational-scalar reduction for the fixed supported element, then produce either delta=c*h² in the entire L115 quotient or complete negative certificates for every permitted scalar; no instance square test or new lemma is proved in this review.
REASON: Essential primary method coverage is now available for one separate REPRODUCTION calculation. A genuine relation or certified nontrivial survivor would clarify the bounded family, without settling supported arithmetic or rational/integer points.
LITERATURE_REASON: The saved target moves from finite local membership to exact global triviality with arbitrary rational scalars; prior assessments explicitly did not cover that decision.
SCOPE: Exactly TARGET in L115's entire degree-eight field with L124's fixed product; rational-scalar reduction and exact quadratic factorization only. No complete supported group, new local point image or point-completeness claim is approved.

## Invocation-start proposal (preserved; approval follows below)

Use L115's entire degree-eight field K=Q[t]/(G), with theta=t mod G
and G=3025t^8−31460t^6+76230t^4−39204t²+2673. L124 fixes
g0=−3−theta, g4=3−theta and mask 17=g0*g4=theta²−9. C124a
is now independently audited. These are the essential input IDs;
none of the finite collisions is a premise of global triviality.

The proposed intermediate target asks whether there exist c in Q*
and h in K* with theta²−9=c*h². Testing only c=1 would be an
incomplete negative test. A positive result needs an exact identity
in the entire quotient algebra. A negative result needs a complete
argument covering all rational scalar classes; a failed bounded search
would not suffice. No method of achieving either result is derived
or approved in this turn.

Downstream use: distinguish a genuine global relation in the bounded
generator family from a nontrivial surviving global class. Either result
can guide subsequent supported arithmetic, but neither determines all
classes or rational points. Continue only if the source comparison
identifies a rigorous, executable bounded certificate strategy; otherwise
record the precise obstacle and select a materially different target.
Do not retry the backend probes parked in ATTEMPTS/052 or the unchanged
local test in ATTEMPTS/054. ATTEMPTS/053 remains preserved.

Full units and S-class two-torsion, other supported classes, surviving
cover points, degree-nine root recovery, compatible remaining factors,
both L095 integer systems and minus-eleven remain unresolved. The
known infinity points and identity survive. This is a proposal for
separate review, not a literature assessment approving new mathematics.

## Completed comparison and research contract

The preceding proposal records the invocation-start coverage gap. This
section completes that review and authorizes a separate calculation,
without deciding the fixed element's class. The main gap remains complete
supported arithmetic and point control in this conditional branch, far
short of the residual-signature Beal target. The intermediate question
distinguishes a global relation from a nontrivial surviving class; neither
outcome determines rational points or either L095 integer system.

### Primary results actually read

Barry M. Trager, *Algebraic Factoring and Rational Function Integration*,
Proceedings of SYMSAC '76 (1976), pp.219–226,
[DOI](https://doi.org/10.1145/800205.806338),
[primary scan at SFU](https://www.cecm.sfu.ca/~mmonagan/teaching/TopicsinCA11/TragerFactor.pdf):
Section 2 pp.219–221, Theorems 2.1–2.3, Lemma 2.4, Corollary 2.5,
and algorithms `sqfr_norm`/`alg_factor`, with their proofs. The base
field has characteristic zero and effective arithmetic/factorization;
the finite extension has a monic irreducible defining polynomial.
Theorem 2.2 recovers complete factors by gcds from the completely factored
squarefree norm. Corollary 2.5 supplies termination of the shift search.
Apply over Q with L115's F/275 and X²−(theta²−9)/c. Normality and a
maximal-order basis are unnecessary. Retain the squarefree-norm check.
The ACM PDF returned 403; the SFU scan supplied every essential passage.
No factorization of this instance was performed.

J.S. Milne, *Algebraic Number Theory*, v3.08, 19 July 2020,
[author PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf):
Theorem 3.35 and its full proof pp.60–62 identify ramification with
maximal-ring discriminant divisibility. Its freeness hypothesis holds
over Z. Read the reduction/nonreduced-ring criterion in that proof;
Example 3.26(c) pp.55–56 and Remark 7.43 p.124 give the normalized
valuation conventions. These cover the planned scalar-support argument.
L116 gives the actual field discriminant 2^8*3^7*5^4*11^7; a polynomial
order discriminant must not replace it. L124 supplies S-unit support
for both fixed generators, hence their product. The instance's scalar
reduction remains to be written in research, not imported as an already
proved local result.

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. 78 (2009), 2347–2370,
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2), 21 October 2008:
reuse Section 2 p.3 for the even-degree quotient; directly read Section 6
pp.11–13, especially step 4 and its explanation, the class/unit bottleneck,
and the common-scalar projection ad 12. This is quotient context, not an
evaluation of this product. It does not turn a local collision into a
global relation or make S-units exhaust supported square classes without
class information. The existing support and localization assessments
remain adequate for their unchanged targets and need no refresh.

The official [SymPy 1.14.0 polynomial internals](https://docs.sympy.org/latest/modules/polys/internals.html#sympy.polys.factortools.dup_ext_factor)
document Trager factorization, its squarefree-norm subroutine and
`dup_zz_zassenhaus` for rational factorization. The
[domain documentation](https://docs.sympy.org/latest/modules/polys/domainsref.html#sympy.polys.domains.domain.Domain.alg_field_from_poly)
documents construction from a defining polynomial. These are implementation
options, not execution evidence or a substitute for certificate checks.
The installed version was not probed. Javadi–Monagan's ISSAC 2009
introduction was inspected for discovery only; its different multivariate
algorithm is not an input. Trager's thesis and other search hits remain
unread leads, not additional theorem coverage. Full matching Mathlib
coverage was not checked.

### Search, duplicates and failures

Queries included `"275" "2860" "6930" octic`,
`"square" "rational scalar" "number field" algorithm`, and
`"Trager" "algebraic factoring" pdf 1976`. Followed the primary-paper
lead to its theorem statements, complete relevant proofs and algorithms.
No inspected result evaluates this exact element; this is not a novelty
claim. The known general algorithms suffice for the intended method.

Scoped comparison covered the October 24 bounded-linear assessment,
critical-audit and fixed-five-adic assessments, history/440,446–447,
L115/L116 hypotheses and conclusions, and L124's support and joint-image
proof ranges. The earlier assessment explicitly denies global-relation
certification. C124a's audited local squareness is reusable context,
not a premise for a global square. ATTEMPTS/052 parks full certified
class arithmetic; this fixed-element test does not need that backend.
ATTEMPTS/053 concerns a different witness, and ATTEMPTS/054 stops the
unchanged five-adic removal test. Preserve all three; no repeated backend
probe, local membership test or larger generator search is approved.

### Obligations for one separate REPRODUCTION calculation

Essential inputs are L115's entire field and actual theta, L124's g0,g4
and supported product, L116's audited discriminant, C124a's audited
local status and the cited quotient convention. L117's individual ideal
decompositions and complete S-class/unit data are unnecessary here.

First justify replacing arbitrary c in Q*/Q*² by representatives in

    {(-1)^e0 * 2^e1 * 3^e2 * 5^e3 * 11^e4 : every ei in {0,1}}.

This is the proposed complete list of 32 tests, not an assumption or a
scalar-completeness proof supplied in this literature turn. The research
specialization must combine support, absence of outside ramification,
normalized valuations of a hypothetical delta=c*h², and rational square
removal. Retain both signs and all support primes; justify any smaller
list. No class-two-torsion vanishing may be assumed.

For each required c, decide whether X²−delta/c has a root in the entire
fixed field using the imported exact method. A positive result may stop
immediately after writing h as a rational polynomial of degree below
eight in the actual theta and verifying c*h²−delta=0 modulo F, with all
denominators and nonzero conditions recorded. A complete positive-case
scalar enumeration is unnecessary.

A negative result needs both scalar completeness and complete nonsquare
certificates for every permitted c. Save the exact factorization trace:
shifts, resultants, squarefree checks, complete rational factors, gcds
over K and inverse shifts. Rational irreducibility/completeness needs an
exact algorithm with the required bounds and recombination evidence, or
independently checkable irreducibility certificates; product reconstruction
or a boolean flag alone is insufficient. An exact local nonsquare
certificate can replace an individual global factorization if its field
and scalar are justified. Incomplete computation leaves the decision
open, never certifies nontriviality. No finite-image rank supplies a
global relation.

Continue only to an identity or a complete obstruction under this
contract. If certificate production hits a real execution limit, save
the exact unfinished evidence and obstacle; do not substitute a bounded
search failure. Full supported arithmetic, other classes, surviving
cover points, degree-nine root recovery, compatible remaining factors,
both L095 systems and minus-eleven remain open. No new lemma, mathematical
script, DAG edge or argument-overview change is made in this source review.
