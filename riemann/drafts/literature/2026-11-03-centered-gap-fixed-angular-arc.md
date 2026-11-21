# Source review: a fixed angular arc for the centered-gap scalar method

TARGET: Assess whether L696's centered-gap method yields |c_(0,n)(exp(i*theta))|<=C*exp(-c*n) for |theta|<=delta with fixed delta,c>0 in L666, retaining both finite endpoints.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 120 searched complex-measure convolution/total variation, complex concentration/large deviations, rational characteristic kernels and Fourier-gap rational sampling; inspected the primary statements below and compared L696/L666, C672a, L688 and L695's qualified stop. No inspected result states the finite fixed-arc bound; the bounded search is not a novelty claim.
SOURCE_EVIDENCE: Kallsen--Kruehner arXiv:1607.02998v1 (11 July 2016), Appendix A, Lemma A.1(6),(9)--(11),(14), pp.29--30; Maiale, Analysis of Sublaplacians on Lie Groups, 28 May 2019, Definition 1.5 and Proposition 1.7 with full proof, pp.8--9, and Proposition 1.8 statement p.9; NIST DLMF v1.2.8 (15 September 2026), Section 1.14(iii), (1.14.17)--(1.14.18),(1.14.30)--(1.14.31) with standing convergence hypotheses. Reuse step 116's precise Durrett/Vershynin/Miller inputs; source details and limits below.
COMPARISON: Finite complex-measure convolution, variation domination and transform multiplication are standard available inputs; probability Bernstein applies only after a verified positive normalization. None pays the actual angular variation, comb samples or finite endpoints. C672a's auxiliary multipliers and L688's n-dependent Taylor-filter zeros at -1 do not decide this fixed-profile upper bound near 1. L696 remains scalar only.
GAP: Verify L666's complex factor measures and a positive majorant whose product mass growth is beaten by fixed-gap concentration on a fixed arc; justify the reflected L1 pairing, zero half-density and other comb samples, and the signed paired endpoint tails without assuming conjugacy at nonreal u. All resulting angular estimates remain unproved.
REASON: Essential standard interfaces are available for one bounded mathematical attempt at the unchanged target. EXPLORE permits that attempt, not an angular theorem; no essential source blocker remains, and no new mathematics was derived during this review.
LITERATURE_REASON: The changed nonreal-u hypothesis is outside step 116/119's real positive-law coverage; finite complex-measure domination was an essential unread interface at invocation start.
SCOPE: The exact TARGET, for every fixed real l1 profile satisfying L696's centered-gap hypotheses, cap 1/8, prescribed omega_* and fixed g>0 before n, n=12q+3, all j including 0, fixed anchor, original unit masses, denominator 1/u and exact indices -2q<=m<2q. A later attempt may test complex finite-measure factorization, positive-majorant concentration, reflected pairing and signed paired endpoint bounds; delta,c,C,N may depend on that fixed profile/gap, never on n. No spatial-moment, complete-logarithmic, H/support or Xi conclusion is covered.

The completed review below supersedes the pending status of the original
nomination retained next. That nomination states questions and thresholds,
not an established angular estimate.

## Purpose and discriminating test

The main gap is actual-Xi all-degree mixed positivity. The independently
audited scalar input is now reliable, but cancellation at one angle
does not control a logarithmic integral. A fixed nonzero arc would be a
concrete intermediate test of whether the mechanism reaches a set of
positive angular measure. Full spatial information, the rest of the
circle, logarithmic integrability estimates, H/support and Xi realization
would remain independent obligations even after a successful arc bound.

The next source review should reuse L696's precise primary citations,
identify the changed hypotheses at nonreal u, and inspect any essential
primary theorem before approving an attempt. Positive-mixture and real
probability concentration cannot simply be assumed there. Compare the
specific local propagation stops rather than repeating their mechanisms
under a new name. L695's absolute-tail cost remains a qualified stop,
not an obstruction already proved for this signed angular target.

The threshold is existence of fixed delta,c>0 and finite C,N such that
the displayed bound holds for every allowed n>=N and |theta|<=delta,
for the same fixed profile. A shrinking arc or continuity for each n
does not meet it. If coverage supports a genuinely different signed
complex-kernel mechanism, prepare its bounded test for a later research
turn. If no adequate interface is found, preserve the exact gap and do
not derive and approve its replacement during the literature turn.

No primary-source passage, mathematical claim beyond the scalar audit,
or matching Mathlib coverage has been added in this pending assessment.

## Completed review — 3 November 2026, step 120

### Primary source interfaces and reading limits

Jan Kallsen and Paul Kruehner, *On uniqueness of solutions to martingale
problems — counterexamples and sufficient criteria*,
[arXiv:1607.02998v1](https://arxiv.org/pdf/1607.02998v1), 11 July 2016,
Appendix A, pp.29--30, Lemma A.1. Read the definitions and entire lemma;
the relevant clauses concern finite complex Borel measures on R^d:
(6) integrability against variation and the integral modulus bound;
(9) |mu*nu|<=|mu|*|nu| as measures; (10) convolution norm
submultiplicativity; (11) product variation; (14) the positive-exponent
Fourier transform is a continuous algebra homomorphism. The lemma
recalls standard facts and cites its reference [6], rather than giving
individual proofs. These supply measure algebra, not concentration.
Do not use (8)'s iterated integral without checking absolute
integrability against the product variation. The infinite counting
measure in L696 is not a finite measure covered by this lemma.
The 2020 journal pagination was not substituted for the inspected v1.

Francesco Paolo Maiale, notes for Fulvio Ricci's course,
*Analysis of Sublaplacians on Lie Groups*, updated 28 May 2019,
[author-hosted PDF](https://poisson.phc.dm.unipi.it/~fpmaiale/notes/HAoLG.pdf),
pp.8--9 (PDF indices 7--8). Read Definition 1.5, Remark 1.6 and the
complete proof of Proposition 1.7: test finite complex-measure
convolution on C_0, bound the double integral by product variation,
then take the supremum over tests of norm at most one. This supplies
an inspected proof of the convolution norm interface. Proposition 1.8
states the density formula when one factor is absolutely continuous;
no proof is printed there. No family-specific density or concentration
conclusion is attributed to these notes. The later sentence suggesting
general L1*L-infinity continuity is not used.

[NIST DLMF Section 1.14(iii)](https://dlmf.nist.gov/1.14.iii), version
1.2.8, released 15 September 2026, inspected (1.14.17)--(1.14.18)
and their convergence paragraph, and (1.14.30)--(1.14.31). Complex
functions and parameters are allowed; the stated hypothesis is piecewise
continuity and an exponential growth bound, with Re(s) above that
growth exponent. The convolution transform identity has those standing
hypotheses. It is a function identity, not a formula for an atom at zero.
These references support checking complex exponential densities; they
do not identify any factor in L666 or justify a boundary contour shift.
Schiff (1999), the DLMF's reference, was not separately read or imported.

Reuse, without renewed retrieval, step 116's inspected Durrett version 5,
Theorems 3.3.1--3.3.2, Example 3.3.8 and Lemma 3.3.9; Vershynin's
first-edition author version dated 20 May 2024, Definition 2.7.5 and
Theorem 2.8.1 with its full proof; and Miller's 15 January 2006 notes,
Theorems 4.1--4.2 and Section 6. Exact statements, pages, links and
reading limits remain in
[the scalar assessment](2026-11-03-fourier-gap-positive-convolution-transfer.md).
Bernstein requires independent, centered, real sub-exponential variables.
Only a verified normalized positive majorant can enter that theorem.
The majorant's normalization cost must be retained, not set equal to one
because the original complex measure has algebraic mass one. Miller
supplies Schwartz Poisson and distributional duality only; the non-Schwartz
limit still needs a local proof. No general source theorem is to be
reproved in the proposed attempt.

### Exact overlap and recorded failures

L696 Sections 3--6 are essential: its real positive law, mean and rate,
the one-sided zero half-density, the reflected multiplier H, and the
whole paired tail are separate obligations. Its fixed-profile centered-gap
existence and L694's inherited L693 construction are ready local inputs;
this review does not change their center, profile or source scope.

Read L666's defining product and its Section 2 rational continuation.
The denominator uses 1/u; the finite index set is invariant under
m -> -m-1 before displacements. A proposed complex continuation must
retain both facts and the j=0 factor. L696's use of 2 Re W_n(y) was
justified at u=1 by conjugacy. No such identity at the same nonreal u
has been approved. The later attempt must use the actual paired sum or
another proved summable remainder, and pay the entire infinite tail.

Read C672a completely. It supplies an upper bound on a different residual
with auxiliary coefficients beta_r, despite coefficient bounds and exterior
normalization. Its stopped inference was an angular lower bound after
discarding polynomial constraints. It neither has all original coefficients
one nor prescribes a fixed l1 centered-gap displacement profile. This is
not a counterexample to the present upper-bound target, and its propagation
relaxation is not proposed again.

Read L688's hypotheses, conclusion and source interface. Its growing
inverse-Taylor polynomial and n-dependent two-shift witness cancel a
filtered scalar at u=-1. The present target is unfiltered, near u=1,
and uses one profile fixed before n. L688 expressly leaves other angles
and the joint norm open. Its obstruction remains recorded; this review
does not generalize it to the new target.

Reuse L695's already assessed qualification: its full angular/spatial
absolute-tail cost is not a signed scalar upper-bound obstruction for a
centered-gap profile. Keep that stop and step 105's parked numerical
screen; neither is repeated here. No sibling notebook was consulted.

### Bounded attempt licensed by this assessment, still unproved

Test complex finite measures on the real frequency half-line, dominated
by positive atom/exponential kernels. This is a proposed representation,
not a derived factorization. First verify the exact rational factors from
L666, their integrable complex densities, and their variation majorants
uniformly in j/n and a neighborhood of u=1, including t=0.

The quantitative test is whether their product variation growth can be
paid by concentration of the normalized positive convolution outside the
same fixed gap. Its mean must remain strictly inside that gap on a fixed
arc; centered sub-exponential norms, normalization factors and positive
decay margins must all be shown uniformly. Pointwise continuity and an
O(delta*n) absolute difference of the original sums are not sufficient.
No candidate value of delta or net exponential rate is asserted here.

Then test the original fixed real signed-interval primitive against this
finite complex law, using product-variation integrability for each Fubini
step. Reuse the established reflected gap identity only in its stated
domain. Independently handle the density at all comb samples, including
zero and its one-sided Gaussian limit, rather than infer pointwise
density bounds from a probability tail. The final test must also control
the actual paired tail and displacement corrections beyond both finite
endpoints, uniformly over the fixed arc. No positivity, conjugacy or
absolute summability of individual unpaired 1/s tails may be assumed.

Continue only with fixed delta,c>0 and finite C,N for the original
finite scalar, uniform in allowed n>=N and |theta|<=delta, or a precise
new obstruction that changes the mechanism. A shrinking arc, lost finite
endpoint, n-dependent profile or rate exhausted by normalization fails
this test. Failure of this majorant method would not disprove the target.
If the method fails, preserve its exact failure before choosing a
materially different continuation. Spatial moments, the rest of the
circle, logarithmic integrability, H/support, Xi realization and all-degree
mixed positivity remain independent gaps even if this test succeeds.

EXPLORE is appropriate: standard inputs cover the proposed interfaces,
while the angular representation, rate and endpoint estimates remain
local proof differences. No matching finite theorem was found in the
bounded search. Any later application must distinguish these known
tools from what the local argument actually establishes. Full matching
Mathlib coverage was not checked; unknown availability is not absence.

### Search and access record

Queries included `"complex measures" convolution "total variation"
Fourier transform lecture notes`; `"complex" "convolution" "Chernoff"
measure concentration`; `"Fourier gap" "rational" lattice exponential`;
`complex exponential convolution kernels concentration total variation
analytic perturbation`; `"complex measures" "concentration" convolution
powers`; `"rational" "spectral gap" "perturbed lattice"`;
`"spectral gap" "complex measures" convolution exponential`;
`"Fourier gap" "rational functions"`; `"complex measures" "large
deviations" convolution`; and `"rational" "characteristic function"
"complex" "exponential" mixture`. Follow-up title/author searches
located the exact sources above. No novelty is inferred from unmatched
queries or irrelevant operator-gap and probability-distribution hits.

Liverpool and CORE copies of Kallsen--Kruehner failed to open; the precise
arXiv v1 was accessible and supplied the needed statements. The notes
and DLMF were accessible. Princeton MAT425 notes (15 May 2025), Section
5.6 and Fubini statements, were inspected as a secondary comparison;
their several TODO proofs are not relied on for a missing interface.
A Poltoratski *Spectral gaps for sets and measures* PDF lead timed out;
no theorem from it is imported or treated as inspected. Lev/L694 already
cover the fixed gap's existence. Other search leads, including general
signed convolution approximations, were not read at theorem level and
are not inputs. These optional leads are not essential source blockers.

No new lemma, mathematical script, angular derivation or modification of
PROOF/DAG was made. The completed task is literature comparison; the
next mathematical attempt requires the supervisor's separate approval
of this newly completed assessment.
