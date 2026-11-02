# Exact two-pole cancellation — nominated audit coverage

TARGET: Audit C645d's exact two-pole cancellation, including logarithm branches, contraction constants and strict cluster admissibility.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the cluster and parent contour assessments' completed exact-statement/stronger-result searches and duplicate/stop comparisons. New bounded searches were site.jirka.org ra contraction mapping theorem complete metric space and site.complexanalysis.org logarithm power series log(1+z); retrieved the primary theorem statements and essential proof cases below. No renewed novelty search or mathematical audit was conducted.
SOURCE_EVIDENCE: Jiri Lebl, Basic Analysis, online Volume I Section 7.6.1, Definition 7.6.1, Theorem 7.6.2 and complete proof https://www.jirka.org/ra/html/sec_metpicard.html ; Beck et al., A First Course in Complex Analysis, Section 5.2, Definition 5.2.2, (5.2.6), derivative argument and Example 5.2.5/Theorem 5.2.6 https://complexanalysis.org/web/sec_complex-log.html ; NIST DLMF v1.2.8 (2026-09-15), (4.6.1) https://dlmf.nist.gov/4.6.E1 ; Zakeri Notes and Comments Section 8.3 following Example 8.33 https://zakerimath.com/CAbook/COM.html . All inspected 2026-11-01; textbook web pages are unversioned.
COMPARISON: Banach's theorem covers a nonempty complete metric space and a self-map with one Lipschitz constant below one; it supplies exact iterative existence, not C645d's finite-product inequalities. The logarithm sources supply the local series, inverse-exponential identity and derivative, while warning against unrestricted principal-log additivity. None certifies the saved all-n threshold, phase reversal or geometric margins. Reuse the parent comparison of meromorphic approximation and contour methods without importing their different hypotheses.
GAP: The essential standard sources are now covered. Independent conceptual audit of the complete C645d specialization remains: exact product identity, nonvanishing derivative estimate, contraction constants, all-n threshold and strict admissibility. Actual-Xi realization and every contour application remain outside scope.
REASON: Ready coverage authorizes a later audit of the existing construction; it neither certifies that proof nor renews the failed noncancellation mechanism. Named standard tools should be cited, with only the finite-family specialization checked locally. A source citation alone cannot verify those particular inequalities.
SCOPE: Only the stated audit; no actual-Xi sign, pole realization, derivative bound, contour estimate, modified grid or new cancellation construction is covered.

The completed mathematical step used the unchanged ready cluster
assessment. Its new result is canonical in C645d; this file records
future coverage only. At nomination the next invocation was required to complete the source
gate. The source review below now completes that gate for a later
independent mathematical audit; the parent meromorphic/Pick comparison
is reused without repetition.

Essential local inputs for that audit are C645d's entire proof and
L645's exact complex-factor/grid convention. C645a/C645b/C645c are
comparison stops, not noncancellation premises. L018 is conditional Xi
context only, not an input to the synthetic construction. No cross-
notebook result is required. Full matching Mathlib coverage remains
unchecked, not known absent.

The bounded audit test is whether (9)--(14) define an exact admissible
family for every integer n beyond (5), with no logarithm branch error,
lost sign or merely asymptotic solvability. Check that two unit residues
indeed give S_n=0 and that this stops only the geometry/residue-only
lower bound. An unproved actual-Xi realization, grid-interpolating
residual, safe contour, other-zero control or uniform P estimate must
not be smuggled into the conclusion. Those remain unresolved even if
the audit passes.


## Source approval — 1 November 2026

LITERATURE_REASON: The newly nominated audit had REVIEW_REQUIRED coverage because exact primary contraction/logarithm inputs had not been inspected; this turn fills that essential omission, rather than adding literature to a ready mathematical target.

Read C645d in full to identify its asserted inputs, and L645's finite
Blaschke input and grid application through (6). Reused the exact cluster
assessment and the parent assessment's duplicate/failure comparison.
The existing inverse-Blaschke unit-residue stop and completed attempt
history were checked. This is approval of source scope, not an
independent check of C645d's equations. No mathematical scripts ran.

### Imported inputs and restrictions

Lebl's Definition 7.6.1 and Theorem 7.6.2 assume a single global
Lipschitz constant k<1, completeness, nonemptiness and a self-map.
Read the entire proof: arbitrary-start iterates, geometric distance
bound, Cauchy convergence, continuity at the limit and uniqueness.
Its bound before passage to the limit is
 d(x_m,x_n) <= k^n d(x_1,x_0)/(1-k) for m>n.
The proposed closed complex disk is a permissible kind of metric
space; the audit must establish its specified map preserves that disk
and has the asserted uniform contraction constant. The theorem is an
import, requiring no reproof. It does not supply the n-dependent radius,
constants or fixed-point equation of this construction.

Beck Section 5.2 defines the principal logarithm in Definition 5.2.2,
gives exp(Log z)=z in (5.2.6), and proves its derivative is 1/z away
from the nonpositive real axis. Read that derivative argument and
Example 5.2.5 and the forward proof of Theorem 5.2.6: principal-log
additivity needs an argument restriction. Its converse is left as an
exercise and is not an input. C645d proposes exponentiating a sum of
local logarithms, not invoking unrestricted principal-log additivity.
The audit must verify every local argument stays in its claimed domain
and establish the exact rational-product identity. No source establishes
that identity for the saved product by citation alone.

DLMF (4.6.1), version 1.2.8, identifies the alternating series with
ln(1+z), explicitly the principal branch, for |z|<=1, z!=-1. Only the
strict interior |z|<1 is needed. This is the official formula source,
used together with Beck's textbook branch/derivative statements; no
boundary convergence or global logarithm of B_n is needed. The DLMF
reference to Hardy (1952), pp.471–473, was not followed and is not an
inspected input. No local power-series reproof is required.

Reopened Zakeri Section 8.3's paragraph after Example 8.33: it uses
(z-p)/(1-conjugate(p)z), repeats zeros by order, divides them out and
applies the maximum principle using the boundary modulus. This matches
the convention recorded in L645. C645d only retains the explicit
rational factors; the finite-division inequality itself is not a new
premise of its cancellation construction.

An additional inspected author textbook, A. Rechnitzer's online MATH319
Section 5.7, Definition 5.7.1 and Theorem 5.7.4 with proof
(https://arechnitzer.gitlab.io/m319text/sec_contract.html), states the
same metric-space theorem and error bound. Several intermediate proof
displays use a strict inequality where the definition gives <=; use
Lebl's complete proof as the operative reference instead. Two guessed
Lebl HTML URLs failed; following the author's index resolved access.
No essential source remains blocked. No unseen lead is an input.

### Ready audit boundary

DECISION EXPLORE covers only scrutiny of this already-written finite
construction; it makes no claim of originality. No inspected theorem
replaces that audit, so IMPORT would misclassify the whole target.
Use the precise citations above for the standard tools, then independently
check C645d (5), (7)–(15), including the error bound and unit residues.
Accept the obstruction only if exact cancellation holds for every
integer n beyond its stated threshold with all strict conditions;
repair or reject any unsupported step. Keep actual-Xi realization,
symmetries, other poles/multiplicities, interpolation, contour clearance
and uniform boundary control unresolved. This turn does not test those
inequalities or assert the audit passes. Full matching Mathlib coverage
remains unchecked; no formalization claim is made.
