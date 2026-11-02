# Stationary Hardy-path feasibility: source comparison

TARGET: Assess source coverage for a stationary C2-process test of L473's paired Hardy-jet counterlaws at clipped mass log H/288.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched stationary prescribed derivative moments, spectral bounded-path constructions, occupation/holonomic realization, random trigonometric Laguerre inequalities and Hardy stationary jets; inspected primary random-phase and generalized-curve results and reused the finite-interval occupation assessment. No full matching realization or separator was established; no novelty inference follows.
SOURCE_EVIDENCE: Rahimi--Recht NIPS 2007 Section 3, Theorem 1 and the real random-phase formula, PDF pp. 2--4; Bernard arXiv:math/0701451v2 Definitions 4/7/26/28, Lemmas 6/8/29/30 and Theorems 19/27/31 with relevant gluing/approximation cases; Feldheim et al. arXiv:1801.10392v2 Section 2, PDF pp. 2--3. Reuse 2026-10-17-jet-trajectory-compatibility.md and 2026-10-28-two-height-hardy-jet-moment-coverage.md for finite-interval and arithmetic imports.
COMPARISON: Covariance realization and generalized-curve superposition do not supply all 147 moment constraints, the paired norm bound and C2 derivative consistency simultaneously. Gaussian smoothness does not give bounded marginal support. A bounded random-phase bulk is an independently testable intermediate; its covariance and clipping threshold still need calculation, and it does not settle the full path target.
GAP: Full stationary path feasibility at ell/288 remains open, including all 126 fourth entries and a derivative-preserving replacement for L473's rare component/covariance correction. Exact stationarity and ell^2 support are not proved for actual dyadic Hardy sampling; no process separation can be transferred without those comparisons.
REASON: Park direct import of the inspected realization theorems. Essential sources suffice for the explicitly covered two-wave bulk test below without a process-extension theorem or an actual-Hardy stationarity assumption. This changed assessment and continuation require separate supervisor approval next turn; no mathematics is performed here.
LITERATURE_REASON: The supplied target was REVIEW_REQUIRED for derivative-consistent stationary paths and bounded support, outside the preceding finite-dimensional/generalized-function screen. This turn supplies that comparison and prepares a bounded mathematical subtarget rather than repeating a ready review.
SCOPE: Proposed real processes F_H(u), u in R, stationary in joint finite-dimensional law with almost surely C2 paths, ell=log H; paired microscopic jets (F_H(r),F_H'(r),F_H''(r)), r=0,1. Retain L473 (2)'s entire 21 second/126 fourth tolerances, including all four tight odd second entries, common constants/onset and its paired support |v|<=ell^2. Proposed clipped threshold is E(F_H(0)F_H''(0)-F_H'(0)^2)_+>=ell/288. No equation, distribution or realization for actual Xi is assumed.
COVERED_TARGET: Test whether the two-wave random-phase process S(u)=cos(Uu+B)+cos(Vu+C) has paired jet covariance L473 (6) and E(S(0)S''(0)-S'(0)^2)_+>=1/288, retaining bounded derivatives and exact stationarity.

The following nomination is preserved as the pre-review record. Its
missing-source status is superseded only as stated above and in the
completed comparison below.

Main gap: actual-Xi signs at unbounded heights and all-degree positivity.
Intermediate source target: determine whether adding sample paths gives
a meaningful discriminator beyond L473's stopped finite-data test.
A feasible process would identify an additional limit of a generic
moment-plus-path argument; a rigorous obstruction could nominate an
extra constraint to compare with actual Hardy data. Neither would itself
prove an actual negative-mass bound or pointwise positivity.

Essential input IDs: L471 (the negative-part relevance and gauge transfer),
L472 and L473 (the established one-/two-height counterlaws). Use their
canonical hypotheses and all tolerances; their arithmetic sources remain
imports with the recorded unaudited-proof qualifications. L477/L575 are
contrasts, not premises of a process construction. No cross-notebook input.

The next review must search exact stationary jet occupation/realization
terminology and stronger results, retrieve primary covariance/spectral
and sample-regularity hypotheses, and check bounded derivative support
and integrability rather than invoking a Gaussian process by name.
An unbounded Gaussian surrogate does not automatically meet the proposed
support restriction or the complete fourth moments. Stationarity of a
model is not exact stationarity of a uniformly sampled finite Hardy
interval; assess that distinction before claiming applicability.

Continuation/abandonment test: approve a concrete process-feasibility or
separation test only with source coverage of its added hypotheses and a
clear connection to the missing joint-law information. Preserve the
ell/288 threshold rather than silently weaken it. If known results
already decide the test, import them; if the added hypothesis cannot
usefully distinguish the relevant models, park it. Do not reopen the
identical finite-coordinate test or repeat the generalized-function
source blocker. No proof attempt, source approval, original-result
claim or Mathlib absence assertion has been made in this nomination.

## Completed source review, 2026-10-31

### Primary comparisons and qualifications

Ali Rahimi and Benjamin Recht, *Random Features for Large-Scale Kernel
Machines*, Advances in NIPS 20 (2007),
[author PDF](https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf),
Section 3, Theorem 1, equation (2), the subsequent real random-phase
formula and Algorithm 1, PDF pp. 2--4, were inspected. The theorem assumes
a continuous positive definite translation-invariant kernel; normalization
gives a probability spectral measure. The real construction is
sqrt(2) cos(omega x+b), with frequency sampled from that measure and an
independent uniform phase on [0,2pi]. The source verifies its expected
product by the angle-addition identity. This supplies a concrete bounded
spectral comparison. Its kernel-approximation tail bounds are not needed.
It does not prescribe the nonlinear clipped expectation or full fourth
tensor here. Differentiability, derivative bounds, joint-law stationarity
and normalization of the proposed two-wave sum must be checked in the
later specialization; none is established for that sum in this review.

Patrick Bernard, *Young measures, superposition and transport*, Indiana
Univ. Math. J. 57 (2008), 247--276,
[arXiv:math/0701451v2, 9 July 2008](https://arxiv.org/pdf/math/0701451v2),
was inspected at Definitions 4/7, Lemmas 6/8 (pp. 4--6), Theorem 19 and
Proposition 20 (p. 11), and Definitions 26/28, Theorems 27/31 and
Lemmas 29/30 (pp. 15--19). The setting is a complete Riemannian manifold
without boundary and finite-first-velocity transport measures satisfying
all compactly supported transport tests. Generalized curves retain a
velocity distribution whose barycenter is the derivative. Closedness
requires equal endpoint marginals. Theorem 27's invariance is for unit
time shifts; its proof glues conditional unit-interval pieces. Theorem 31,
on compact connected manifolds, gives closure by periodic smooth curves;
the joining argument uses geodesics. These cases do not assert C2
derivative-consistent paths with the prescribed lag-one jet tensor and
hard paired support. A finite collection of moment equalities is not
the required transport identity. No realization theorem is imported.

Naomi Feldheim, Ohad Feldheim, Benjamin Jaye, Fedor Nazarov and Shahaf
Nitzan, *On the probability that a stationary Gaussian process with
spectral gap remains non-negative on a long interval*,
[arXiv:1801.10392v2, 21 October 2018](https://arxiv.org/pdf/1801.10392v2),
Section 2, pp. 2--3, was read through the compact-spectral-support
derivative identity. Compact spectral support yields random entire
Gaussian functions with jointly stationary Gaussian derivatives. This
addresses smoothness, not a deterministic bound on the six-coordinate
jet: a nondegenerate Gaussian marginal has unbounded support. No Gaussian
truncation preserving all moments, derivatives and stationarity is
supplied. The spectral-gap persistence theorem is not an input or a
statement about the clipped quadratic form.

For the finite-interval comparison reuse
`2026-10-17-jet-trajectory-compatibility.md`, specifically its inspected
Lasserre--Henrion--Prieur--Trelat (2008) Sections 2.1--2.3,
(2.7),(2.10)--(2.12), manuscript pp. 3--5, and Henrion--Korda--Kruzik--
Rios-Zertuche (2023-03-04), Definitions 2.4/2.7 and Lemma B.1 with proof.
These are necessary transport identities with boundary terms and
integrability qualifications, not an asymptotic realization theorem.
L424 was read at its hypotheses, conclusions and exact source interface:
its moving divisor log(2+t) differs from the fixed ell in L473. Its
specific endpoint estimate cannot be copied to a changed test.
Uniform sampling on a sharp finite interval is not exactly invariant
under arbitrary microscopic translation. Any actual-data separator must
retain both boundaries and justify its error for the chosen observable.
No new boundary estimate is derived here.

### Search, duplicates and source access

Queries included `stationary process prescribed marginal derivative joint
distribution spectral moments bounded sample paths random trigonometric
polynomial`; `stationary differentiable process occupation measure joint
derivatives integration by parts stationary measure realizability`;
`Bochner theorem random phase cosine stationary non Gaussian process
bounded spectral measure`; `stationary process prescribed fourth moments
derivative bounded`; `holonomic measures closed measures periodic curves
Bernard`; `random trigonometric Laguerre inequality stationary`; and
`Hardy stationary process derivatives moments`. Discovery snippets and
nonprimary search hits were not theorem evidence.

Read L473 Sections 1--7, including the complete definitions of S_ab/F_m,
kernel K, rare spherical law and covariance correction; L471/L472's
hypotheses/conclusions and the paired arithmetic assessment. Their
imported arithmetic proofs, including Bui--Hall's omitted Proposition 3
proof, retain the existing qualifications. L473's sphere-dependent
rescaling and general six-coordinate matrix correction have no supplied
path-consistency argument. This is a missing hypothesis, not a proof
that every such extension is impossible.

Compared `ATTEMPTS/2026-10-28-paired-hardy-moment-discriminator.md` and
`ATTEMPTS/2026-10-17-gaussian-jet-trajectory-diagnostic.md`. The latter
retains an unresolved exact bulk observable and supplies no separator.
A scoped random-phase/two-wave/process search in lemmas/,
drafts/literature/ and ATTEMPTS/ found no completed test of the specified
two-wave threshold. Prime-phase and actual-phase hits are different
models; replacing actual arithmetic phases by uniform ones remains
unjustified. This is a duplicate check, not a novelty claim.

Kurtz--Stockbridge, *Stationary Solutions and Forward Equations for
Controlled and Singular Martingale Problems*, EJP 6 (2001), paper 17,
[DOI 10.1214/EJP.v6-90](https://doi.org/10.1214/EJP.v6-90), remains an
unread theorem-level lead: the EMIS PDF timed out and Project Euclid's PDF
was inaccessible. Its abstract was discovery only. It is not essential
to the explicit finite-wave test, so it neither licenses an import nor
blocks that independent calculation. A failed unrelated arXiv HTML URL
was not treated as a source. No repeated source-access attempt is the
continuation. Full matching Mathlib coverage is unchecked; no absence
claim is made.

### Restricted mathematical continuation, pending separate approval

The full original stationary C2 feasibility target, with all 147 entries,
is retained as unresolved. Do not weaken its fourth tolerances or claim
that stationarity is a necessary exact property of the actual data.
The following bulk-only calculation is a useful intermediate, with
independent gaps expressly left open.

In the COVERED_TARGET, U,V are independent uniform random variables on
[-1/2,1/2], B,C are independent uniform phases on [0,2pi], and all four
are mutually independent. Jets at r=0,1 mean ordinary u derivatives in
the order used in L473. Compare their whole second matrix with K in
L473 (6), including every cross entry and the four zero odd entries.
The exact unscaled clipped threshold is 1/288; the proposed H-dependent
bulk would be sqrt(ell) S. Its norm bound after scaling must be checked
against ell^2 on a common eventual ray before claiming support.
These are proposed verifications, not results of this source turn.

One bounded attempt should determine the clipped integral rigorously
(an analytic comparison or validated integration with full error bounds
is acceptable). Continue this particular bulk only if covariance,
stationarity, derivative support and the 1/288 threshold all pass.
A numerical preview or positive but smaller constant does not pass.
If the value is below 1/288, record an upper bound below that threshold
and abandon this two-wave choice; that would not exclude other
stationary models or disprove the full target. An undecided interval
straddling 1/288 is exploration, not evidence of feasibility.

Passing would provide only a derivative-consistent bulk candidate.
Every fourth entry, the rare path component and a correction preserving
derivatives would remain independent obligations. A future full
feasibility theorem could limit generic moment-plus-path arguments;
a failure of this explicit bulk would only reject that choice. Neither
outcome gives actual N(T)=o(T(log T)^3), actual Xi signs, or RH. No
creative actual-phase mechanism is source-ready: nonlinear actual
joint-law/tail and finite-interval-transfer inputs are still missing.
This is a routine source specialization/calculation, not a creative
central-gap proof attempt. No new lemma, process construction or
mathematical script was produced in this literature-only turn.
