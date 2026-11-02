# Two-atom confluent Hardy remainder — approved bounded specialization

TARGET: Test whether L637's complete remainder is o((log T)^5) times its actual Gram form uniformly for mu=c0 delta_0+c1(delta_h-delta_0)/h, 0<|h|<=1/2, complex c0,c1, and T<=X<=2T.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed parent comparison drafts/literature/2026-11-01-hardy-translate-gram-relative-error-review.md records exact/Gram-relative/coalescing-shift queries and scoped duplicate/failure checks; no exact two-atom relative-remainder theorem was identified. No originality claim.
SOURCE_EVIDENCE: Hughes--Young https://arxiv.org/pdf/0709.2345v2#page=4 Thm 1.1/(16)--(17), pp. 4--5; Bettin https://arxiv.org/pdf/1111.0925v1#page=2 Thm 1 p. 2 and relevant proof pp. 9--10; Hartmann--Lesch https://ems.press/content/serial-article-files/52597 DOI 10.4171/DM/1060 Section 3 and Appendix A.2/(A.5)--(A.8), pp. 20--21. URLs opened 2026-11-01; reuse parent proof-case assessment, prior two-height assessment, L473 Section 1 and L637/L622/L465 local scopes.
COMPARISON: Known holomorphic absolute moment and divided-difference tools support a bounded two-dimensional specialization including the antisymmetric near-null direction. The exact smooth-window Gram lower bound and complete relative-error estimate remain to be proved; no unrestricted atom-count theorem follows.
GAP: Control both observer divided differences of the full remainder, actual complex Gram coercivity and curvature uniformly as h tends to zero at an arbitrary T-dependent rate; the smooth-window second-moment conversion is part of the specialization.
REASON: Separate scope review completed using the unchanged primary comparison and exact local definitions. Known inputs cover the moment generators and holomorphic tools; the finite-dimensional relative estimate remains mathematical work, not a theorem imported by this approval.
LITERATURE_REASON: This is a newly written continuation requiring separate scope approval; reuse the parent comparison and inspect only any specific uncovered hypothesis, rather than repeat browsing.
SCOPE: Only the exact two-atom family below under L637's unmodified w,T,X,L,Z,W,M,E,G. No changing weights, discarding swaps, freezing phase, amplifier, large atom family, realization or pointwise sign conclusion.

## Proposed mathematical attempt, not a result

Use L637's exact definitions, including the complete holomorphic six-term
M in (18)--(19), and write

    mu_(h,c)=c0 delta_0+c1(delta_h-delta_0)/h,
    U_(h,c)(t)=c0 Z(t)+c1[Z(t+h/L)-Z(t)]/h,
    G(mu)=integral w_XT |U_mu|^2,
    E(mu)=integral w_XT W |U_mu|^2-M(mu).

Here 0<|h|<=1/2 is real; c0,c1 are arbitrary complex, not both zero;
T<=X<=2T, L=log T and fixed w are exactly as in L637. The coefficients
and h may depend on T,X without restriction. This parametrization is a
definition, not an estimate, and is a subfamily of finite atoms on [-1,1].
No value at h=0 is assumed. The desired result is a single eta(T)->0 with

    |E(mu_(h,c))|<=eta(T)L^5 G(mu_(h,c))

uniformly over this family. The whole actual two-dimensional Gram form,
including complex cross terms, must be controlled; checking only the pure
difference vector or an entrywise finite grid is insufficient.

Essential existing local inputs are L637 Section 4, L622 Sections 1--4
and L465's phase/gamma estimates. L473 Section 1/(4)--(6) supplies a
previous sharp-dyadic Hardy conversion of Bettin; its abstract-law
countermodel is not used. Bettin's uniform small-complex-shift theorem,
with physical shifts fixed at every primitive endpoint, is the source
tool for a smooth-window second moment. The partial integration with
w_XT and the analytic Hardy phase is a required local specialization,
not an already imported smooth-window conclusion.

Hughes--Young and the zero-safe curvature identity supply the full
numerator framework. Apply holomorphic divided-difference tools in the
two observer variables before using absolute bounds, if legitimate;
fixed complex neighborhoods and compact t support must justify every
interchange. The contour must remain separated from the node interval.
A confluent extension, Gram lower bound and any L4 curvature estimates
must be proved. The standard source inputs are imported by citation;
reproving them is unnecessary. No exponent, lower bound or quotient limit
has been calculated in this nomination. Mathlib coverage is not checked.

Main gap: actual-Xi first signs at unbounded heights and all-degree mixed
positivity. A relative theorem could bypass TV amplification in moment
transfer. This test asks only whether first coalescence already obstructs
that possibility. A successful two-atom bound leaves higher cancellation
orders, unbounded atom counts, microscopic realization, signed approximation
and useful main-term margins open.

Continue only with a uniform bound including h arbitrarily close to zero,
or informative evidence identifying its actual failed hypothesis or
error/Gram direction. An oversized TV envelope or generic matrix example
is not an obstruction for this actual Hardy family. Success does not
justify iteration to arbitrary atom counts; that needs a separately
specified and reviewed test. Failure of a required source specialization
parks this exact attempt without erasing its source coverage.

The separate scope approval below authorizes the next bounded mathematical
attempt as fixed-dimensional reproduction/specialization. It does not
certify the proposed estimate. No further browsing is needed absent a
named source gap.


## Separate scope review — 1 November 2026

Reused the completed parent primary-source comparison, rather than
repeating its searches or treating snippets as theorem evidence. Read
L637 hypotheses and Section 4, L622's analytic-phase/weight and curvature
passages, L473 Section 1, and the saved two-height second-input assessment.
The parent records the precise primary statements and relevant proof
cases; none of those target assumptions or sources has changed.

The Hughes--Young application has no twist (h=k=1); its source shift
variables must not be confused with the real node separation h here.
L637 (18)--(20) retain the complete six-term holomorphic generator on a
fixed complex polydisc, with compact t support and exact analytic phase.
The contemplated two observer slots lie within that domain. The reviewed
Hartmann--Lesch formulas require a contour enclosing the whole node
interval inside this domain; separate contours/variables are required
before specializing to real nodes. This is applicability coverage, not
an evaluation of their divided differences or a relative error proof.

Bettin's primitive uses fixed physical shifts at each endpoint. L473
already records their Hardy-phase conversion and its coincident-pole
qualification. The changed window requires partial integration against
w_XT as well as that phase; the source does not directly assert the
new smooth-window Gram conclusion. Its derivation, full complex
coercivity, and any uniform confluent limit are explicit proof obligations.
L622's real-unit-observer curvature bound alone is not the desired bound
for arbitrary complex divided-difference coefficients. The next attempt
must supply that specialization using the holomorphic fourth-moment
input, keeping the zero-safe curvature term.

The duplicate/failure comparison is unchanged: the absolute-TV stop in
ATTEMPTS/2026-11-01-hardy-translate-absolute-error-budget-stop.md is not
an actual remainder obstruction; the full-arithmetic-Gram signed-jet
stop concerns a different coefficient space. No new source or mathematical
evidence was found in this approval. SPECIALIZE marks sufficient coverage
to attempt the exact saved target; it does not mark the target true.
No new theorem, exponent, Gram lower bound or limiting quotient was
derived. Mathlib matching coverage remains not checked. The continuation
and its success/abandonment tests above are unchanged. Record this turn
as a STALLED scope approval, with no exploration-budget reset claimed.


## Direct-source URL recovery — 1 November 2026

The recovery defect was missing direct URLs in this ready assessment,
not missing theorem coverage. Opened all three primary PDFs above and
rechecked Hughes--Young Theorem 1.1/(16)--(17) and its holomorphy remark
(pp. 4--5), Bettin Theorem 1 including its coincident-shift qualification
(p. 2), and Hartmann--Lesch Appendix A.2/(A.5)--(A.8) (pp. 20--21).
The sources were accessible. Existing detailed proof-case comparisons
remain reused; they were not independently reaudited in full this turn.

Hughes--Young retains the small complex shifts, smooth nonnegative weight,
support and derivative-scale hypotheses, full six-term expression and
absolute error. The analytic-phase/complex-weight adaptation is local
coverage recorded in the parent, not a verbatim source conclusion. Bettin
retains the complete two-term primitive and limiting bracket at coincidence.
Hartmann--Lesch retains the convex-hull condition for its simplex formula
and the enclosing contour condition for its residue formula. No source
asserts the requested two-atom Gram-relative bound.

SPECIALIZE and TARGET are unchanged. The duplicate/failure assessment,
including the distinction between the L637 TV envelope and actual error,
is reused unchanged. No new lemma, calculation, source comparison result,
or Mathlib coverage claim is made. This is a STALLED process repair; the
next step is the already nominated bounded specialization, not another
source search.
