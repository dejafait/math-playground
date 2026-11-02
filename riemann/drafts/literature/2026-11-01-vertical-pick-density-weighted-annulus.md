# Vertical Pick annulus — completed horizontal-density comparison

TARGET: Assess whether unconditional zero-density and rational-kernel estimates imply that the height average of L642's exterior E_N complex-evaluation majorant over 1<|Re(zeta)-(X+1/2)|<sqrt(N) is o((log T)^2), uniformly for N=floor(log T) and retaining all horizontal displacements and multiplicities.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the saved fixed-displacement, restricted L485 and vertical-Pick source assessments and two relevant failure records; searched uniform near-line density, its primary provenance, rational strip evaluation and model conjugation. No inspected theorem gives the exact W_T estimate; queries, read ranges and qualifications are below.
SOURCE_EVIDENCE: Baluyot, 2017 Rochester thesis, Section 1.2/Theorem 1.2.1 p.16, Section 3.2 pp.111--114 and Section 3.6 pp.140--143; Maples--Rodgers 1404.3080v2 Theorem 2.4/Proposition 2.5 and Section 4 (18)--(23); Baranov--Zarouf 1310.1182v1 Section 1.1; Baranov--Jaming--Kellay--Speckbacher 2304.02385v2 Section 3.1; Camara--Klis-Garlicka--Lanucha--Ptak (2020) Section 4; Poisson integral Theorem 10.3.1 cited below. Reused all-zero-count coverage; arithmetic source proofs remain cited inputs, not independently audited manuscripts.
COMPARISON: Primary near-line density is uniform in displacement and has only one log H factor, unlike the previously reused explicit Ingham log^3 H estimate. Finite rational kernels/conjugation and Poisson representation supply standard tools for an application test; none states concentration of E_N at complex arguments. The count-only L485 theorem is neither a general weighted theorem nor needed for the proposed first-moment route.
GAP: Prove or quantitatively obstruct the exact pole-product growth versus density decay, a shrinking-displacement exterior E_N estimate, and the resulting full W_T=o(N^2) comparison. Keep every log/power, the zero-displacement atom and padded height endpoints. Simultaneous favorable-height selection remains a separate unresolved step.
REASON: Essential theorem coverage for one bounded known-tool specialization is now available. No W_T estimate, source import into a lemma, new lemma or mathematical script is produced in this literature-only turn. A later attempt must prove the identified quantitative differences; approval is not a claim that these inequalities hold.
LITERATURE_REASON: The new mean estimate introduces horizontal zero-density information and shrinking-displacement rational evaluation weights beyond the completed constrained-projection gate; fixed-positive-displacement coverage is insufficient without an exact comparison.
SCOPE: Exactly the fixed H_N, E_N, F_N and W_T below, N=floor(log T), all actual Xi zero occurrences with |Im(zeta)|<1/2. Known density, finite rational kernels, elementary contour/Poisson estimates and finite spectral theory may be specialized with written applicability proofs. No RH, simplicity, spacing, positive paired zero measure, general-weight source (19), or uniform shifted E_N theorem is assumed.
COVERED_TARGET: Test W_T=o(N^2) for L642's fixed E_N annulus majorant, N=floor(log T), using uniform near-line zero density and the exact distinct-pole product, with a shrinking-displacement E_N estimate and all multiplicities retained.

## Completed review — 1 November 2026

This is LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. The source
comparison is new local coverage, not a mathematical saving or a
discovery beyond the inspected literature. The original TARGET is
unchanged. The covered application above is nominated for separate
next-turn approval; it has not been attempted here.

### Primary density statement and essential near-line cases

S. A. C. Baluyot, *On the Zeros of Riemann's Zeta-function*, PhD thesis,
University of Rochester (2017), [repository record](https://hdl.handle.net/1802/32855),
[primary PDF](https://urresearch.rochester.edu/fileDownloadForInstitutionalItem.action?itemFileId=183460&itemId=33320),
Section 1.2, pp.13--16, Theorem 1.2.1 p.16:

    N(sigma,H) <<_theta H^[1+theta(1-2sigma)] log H,
    fixed 0<theta<4/7, uniformly sigma>=1/2, large H.

Here beta>sigma, 0<gamma<=H. This is unconditional; the subsequent
chapter's RH premise does not apply. Read Section 3.2's Littlewood
argument, pp.111--114/(3.2.2)--(3.2.9), and Section 3.6 pp.140--143:
fixed parameter margins (3.6.3)--(3.6.7), integrated count (3.6.12),
the total-count case within 1/log H, monotonic averaging over that
width, and dyadic summation. Littlewood's counting retains zero orders;
there is no simplicity restriction. Full arithmetic/Kloosterman proofs
in preceding sections were not audited. No effective onset is supplied
here. This primary theorem supersedes relying on an unread Jutila
original or a Conrey announcement; it does not estimate W_T.

The finite multiplicity-count interpretation is also consistent with
the already assessed total counts and source conventions. Its future
application must explicitly use L018's zero correspondence and
reflection, retain the displacement-zero part separately, and justify
any inclusive horizontal cutoff by a strict lower threshold. The
annulus requires a padded positive height range; a cumulative bound
at H=3T is an available *application to justify*, not an assumed
short-interval density theorem. Constants must remain fixed as T grows.

Maples--Rodgers, [1404.3080v2](https://arxiv.org/html/1404.3080v2),
Theorem 2.4 p.5, states the weaker uniform cumulative estimate
N(sigma,H)<<_b H log H exp(-b(sigma-1/2)log H), fixed 0<b<1,
with strict beta>sigma and 0<gamma<H. Re-read Proposition 2.5
and Section 4 (18)--(23), including its Holder and convolution steps.
The passage from upper-tail counts to arbitrary positive weights in
(19) is not licensed by L485's restricted repair. Do not import (19)
or Lemma 4.3 for F_N. The direct cumulative theorem and finite
nonnegative band summation avoid that claim; they still need a
separate application proof. L485's local second moment is unnecessary
unless a later target actually needs it. No source reproof is planned.

Chourasiya--Simonic, [2507.15184v1](https://arxiv.org/html/2507.15184v1),
Corollary 1/(3), Table 1 p.2, retains beta>=sigma and multiplicities.
Reuse its saved proof coverage. Its H^[3(1-sigma)/(2-sigma)] log^3 H
term and additive log^2 H/log H terms must not be treated as a
single-log near-line estimate. The fixed-displacement assessment is
adequate in its original scope; the new primary theorem above supplies
the changed shrinking-parameter coverage.

### Rational inputs and what they do not assert

Reuse Baranov--Zarouf [1310.1182v1](https://arxiv.org/html/1310.1182v1),
Section 1.1, finite P/Q model spaces with prescribed poles and kernel.
Reconfirmed those formulas and compared Theorem 2.1's boundary
derivative estimate; that estimate is not an E_N shifted-concentration
theorem. Baranov--Jaming--Kellay--Speckbacher,
[2304.02385v2](https://arxiv.org/pdf/2304.02385v2), Section 3.1,
(3.1)--(3.3), supplies the upper-half-plane kernel and its diagonal
with Lebesgue norm. The existing source assessment covers its proofs
and boundary sampling theorem. L641's dx/(2pi) normalization and
distinct grid remain controlling. The real-boundary measure theorem
does not sample complex zeros.

M. C. Camara, K. Klis-Garlicka, B. Lanucha and M. Ptak,
*Conjugations in L^2*, Analysis and Mathematical Physics **10**, 22
(2020), [Section 4, preceding Proposition 4.1](https://link.springer.com/article/10.1007/s13324-020-00364-5),
defines the disk conjugation C_theta f=theta bar(z) bar(f) and states
that it preserves K_theta. Read that statement and Proposition 4.1.
Its half-plane rational specialization, action on the real-symbol
concentration eigenspace, and any consequence for paired diagonals
must be justified in research. They are not established in this review.

The online textbook *Complex Analysis*, [Theorem 10.3.1 and proof](https://complexanalysis.org/web/sec_poisson-integral-formula.html),
gives the upper-half-plane Poisson integral for bounded piecewise
continuous real boundary data, harmonic with the prescribed values
at continuity points. Read the statement and proof. Applying it to
our finite rational functions requires checking decay, uniqueness and
the complex/absolute-square estimate used; it is not a ready theorem
about E_N. Two Garnett mirrors failed (timeout/404), but that duplicate
lead is not essential to a finite rational Poisson application.

### Bounded application test, with all losses still to prove

The proposed research target remains W_T=o(N^2), not a new density
theorem. Compare an exact-product envelope with the density exponent
2theta: seek a proved growth coefficient rho<2theta uniformly in
the exterior spatial range and 0<|y|<=1/2. Keep grid discretization
errors, prefactors, spatial integrability and the y=0 limit. No value
of rho or such inequality has been proved here. L642's worst-factor
envelope (13) does not decide the finer product comparison.

Separately test an integrated E_N complex-evaluation estimate for
|y|<=a log N/N with some fixed a>0; include y=0. It must preserve
the concentration gain after the shift. Poisson representation and
model conjugation are candidate standard tools; checking eigenspace
invariance and the interval-edge contribution is part of the target.
An unrestricted H_N bound cannot replace this part. The choice of a,
the boundary leakage N^(-1/2), any exponential shift factor and every
power of N/log N must be displayed before claiming o(N^2).

For larger displacement, use the cumulative density statement with
nonnegative bands or a justified Stieltjes integration, retaining its
single log H, all band endpoints and all multiplicities. Do not infer
an arbitrary weighted inequality from an upper-tail count without
proving its hypotheses. Do not introduce Holder losses by reflex:
this is a first-moment height average. The exact finite F_N, the
X integration and height padding must all be matched before any
exchange or bound. These are research obligations, not hidden premises.

Continue only with the required normalized saving, or an explicit
failed coefficient/core estimate that decides this certificate. If
every proved comparison retains a full-scale or exponential loss,
park this mean-majorant mechanism. Such a failure would not lower-bound
the actual signed trace. Even success leaves simultaneous count/trace
height selection, L641/L642 audits, eigenvalue signs and RH unresolved.

### Search, overlap and routing record

Queries included `zeta zero density near critical line Selberg uniform`,
`Jutila Zeros of the zeta-function near the critical line pdf`,
`Baluyot density critical line 2017 theorem pdf`, `rational model
space strip norm finite Blaschke product complex evaluation concentration`,
`finite model space conjugation Hardy Poisson inequality`, and
`Hardy upper half plane Poisson integral theorem`. Baluyot's thesis
was followed from its repository record; his conference slides and
secondary density compilations were discovery leads only. Simonic
1910.08274v2 was checked only at its introduction; no additional
theorem/proof from it is imported. Jutila's original remains unread
and nonessential because the primary stronger theorem is accessible.

Local overlap check: L641's exact definitions/concentration passage,
L642's conclusions and entire envelope/tail argument, the two
vertical-Pick assessments, fixed-displacement and restricted-density
assessments, L485's hypotheses/exclusion of (19), and the constrained
trace/boundary-transfer failures. None establishes the proposed weighted
mean. Preserve those stops and unfinished proofs. No sibling notebook
was read. Full matching Mathlib coverage is unchecked, not absent.

This is established-tool specialization, not a creative mechanism.
A justified central creative attempt still requires a new signed
cancellation idea or independently testable mechanism; no such target
is manufactured to satisfy routing preferences. The present source
coverage makes a bounded mathematical application available after the
supervisor's separate approval of this changed continuation.

## Original nomination (preserved; completed review above controls)

## Exact proposed quantity and downstream use

Keep L641's H_N, E_N, c=X+1/2 and actual Xi normalization. Let
k_E(z,v) be the reproducing kernel of E_N with its boundary norm
dx/(2pi). This is the fixed concentration space for N, before imposing
the X-dependent local zero constraints. Define

    F_N(x,y)=sqrt(k_E(x+iy,x+iy) k_E(x-iy,x-iy)),
    W_T=(1/T) integral_T^(2T)
          sum_(zeta: 1<|Re(zeta)-(X+1/2)|<sqrt(N))
            F_N(Re(zeta)-(X+1/2), Im(zeta)) dX.

The sum counts every actual zero occurrence. No critical-line-only
replacement or positive *paired* zero measure is made: F_N is a
nonnegative majorant of the absolute mixed kernel by Cauchy--Schwarz,
not an identity for that mixed kernel. At each finite T the displayed
sum ranges over finitely many zeros in a bounded rectangle and the
functions have no poles in the zero strip. The target is W_T=o(N^2).

L642 provides the exact constrained projection and, outside this
annulus, a uniform O(N^(3/2)) bound for the complete zero tail. It
also records the explicit rational-envelope growth g(y) in (13).
These are separately unaudited local inputs. The new comparison must
keep the much finer E_N boundary concentration, when applicable,
rather than replace the entire mean by the full H_N worst-case bound.
No estimate on the shifted E_N diagonal is assumed.

If the weighted mean were small, Markov-type selection could be
tested against the local-count requirement needed for dim U_X~N.
That simultaneous selection, and L641's separate audit, remain open;
do not assume a positive proportion of its count-selected heights.
Even a successful small trace would give only a small Rayleigh
quotient for this diagnostic, not initial signs or RH.

## Required source comparison and stopping test

Reuse the saved fixed-displacement and restricted local-density source
assessments. Retrieve precise primary statements and essential proof
cases only where the new application needs more: dependence on sigma,
shrinking sigma-1/2, strict/inclusive cutoffs, multiplicities, padded
height intervals, logarithmic factors and any restrictions on weights.
Do not import a general weighted theorem from the count-only L485
specialization. A density bound at one fixed sigma is not a uniform
shrinking-displacement bound. Inspect known rational strip-norm
estimates if needed; a real-boundary sampling theorem alone is inadequate.

Approve an attempt only if the comparison leaves a concrete parameter
range or weighted estimate plausibly reaching W_T=o(N^2), or a precise
independently testable failure of that certificate. Record every power
and logarithmic loss needed for that comparison. If all available
estimates leave an exponential or full-scale loss, park this particular
density-majorant mechanism; that would not lower-bound the signed trace.
Do not renew the deterministic projection attempt or its unconstrained
test pair under a new name.

This nomination is not source approval. A known-density specialization
is not creative merely because its weight changes. A justified central
creative attempt remains blocked by the missing quantitative comparison
or by the need for a genuinely signed cancellation mechanism. No
cross-notebook input or full matching Mathlib theorem is claimed.
