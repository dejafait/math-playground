# Fixed H2 energy density: eventual-sign source scope

TARGET: Assess source coverage for an eventual-sign asymptotic of L938's fixed density v(E) as E tends to infinity, retaining all 34 signed terms and the M_0^12 normalization.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step51 reused step46/47 duplicate/failure comparisons, searched the November9 actual-H2 literature/history/attempt paths for eventual signs and balanced saddles, and searched exact theta/logarithmic-Hankel signed-convolution and higher-order Laplace terminology; no inspected theorem states this density's eventual sign. Queries and source scope are recorded below; no novelty inference follows.
SOURCE_EVIDENCE: Read Kirwin arXiv:0810.1700v2 Theorems1.1/2.1 and Lemma2.3's localization case, https://arxiv.org/pdf/0810.1700v2 ; Katsevich arXiv:2406.12706v3 Assumptions2.1–2.3, Remarks2.4–2.5, Theorem2.12, Lemma4.4 and LemmaE.1's outer-integral proof, https://arxiv.org/pdf/2406.12706v3 ; Asmussen et al. arXiv:1712.04070v1 Section4/Theorem4.1(ii) and Appendix10's explicit BKR dependency, https://arxiv.org/pdf/1712.04070v1 . Original BKR proof inaccessible and not imported.
COMPARISON: Fixed-phase asymptotics cannot be applied uniformly to L938 merely by replacing the large parameter with E. Katsevich's nonasymptotic signed-amplitude expansion exposes local-derivative, Gaussian-complement and actual outer-integral errors, permitting a concrete applicability test without presupposing an eventual sign. None of the inspected sources evaluates the complete 34-term coefficient or verifies actual-theta localization.
GAP: Prove candidate saddle dominance and nondegeneracy, evaluate the full signed leading amplitude, and control all local/boundary/full-theta errors relative to its nonzero value; finite-energy variation, parameter endpoint signs and all-degree positivity remain independent gaps.
REASON: Completed one literature-only comparison and nominated a bounded balanced-saddle proof attempt in 2026-11-09-l938-balanced-tail-attempt-51.md. No asymptotic, coefficient, sign or new lemma is derived here; the newly saved continuation receives separate approval next turn.
LITERATURE_REASON: Changed scope from the certified compact energy interval to E tending to infinity; signed saddle cancellation and uniform boundary remainders are essential unread source cases.

The main gap is still L030–L032/C032a actual-Xi all-degree mixed
positivity. The proposed intermediate result would be an eventual
strict sign for the single fixed density in L938, with a proved
remainder relative to its first nonzero term. It could control the
unbounded energy tail in a later full sign-variation argument. It
would not control all finite-energy crossings, determinant endpoints,
contacts, tangencies, other degrees, initialization, realization or
global continuation.

Essential local inputs: L019 and L058 for the exact kernel and
domination; L874/L917 for the logarithmic normalization and finite
coefficient algebra; L938 for the fixed 34-term density and its
qualifications. Preserve the original M_0^12 normalization, all twelve
factors, factorials, signs and every cancellation. No alternate positive
factor, generic positive-kernel replacement, larger cell set or numerical
refinement is proposed. No cross-notebook input is needed.

Continue only if inspected primary results cover enough of the
large-energy concentration/remainder mechanism to state one bounded
proof target that retains the signed cancellations. If they require
an unproved nonvanishing leading coefficient, locate that precise
obligation and assess it before mathematics. If no controlled signed
term or independently testable remainder target emerges, park this
tail mechanism and select another central-gap target. A theorem for
an unsigned convolution alone is insufficient.

Reuse the scoped L915/L916/L922/L937 stops and the L938 fixed-test
inconclusiveness. The latter supplies no bound on global variation
and does not rule out a different tail argument. This file nominates
source comparison only; it does not certify mathematical coverage.


## Completed source comparison — step51, 9 November 2026

Outcome EXPLORATION: new method/hypothesis comparison and a bounded test,
without an actual-theta asymptotic, coefficient evaluation or sign result.
The top fields describe the completed review; the preceding nomination
text records the earlier uncovered scope. No lemma, mathematical script,
PROOF argument or DAG row changed. Full/supporting Mathlib coverage for
the tail theorem is unchecked, not known absent.

### Local object, duplicates and failures

Read the exact polynomial and simplex representation in L938, L019's
kernel series, L058's full domination, L874's logarithm/H2 convention
and L917's finite coefficient algebra. L938's equation (9) is the starting
point: twelve factors, weighted degree twelve and the fixed E^17 factor.
The 34 coefficients and factorials remain canonical there. No extra
multinomial factor, deleted A_0^6 factor or alternate kernel is allowed.

Reused the step46/47 Laplace zero-count assessment and the concise
fixed-cell ATTEMPTS record, including step50's audit qualification.
Scoped searches of the November9 actual-H2 assessments, histories and
attempts for eventual signs, balanced saddles and energy asymptotics
found no ready duplicate. A separate name search in local literature,
foundations and ATTEMPTS found no Kirwin/Katsevich/BKR assessment.
L915/L916/L922/L937 stops remain as compared in step46; this review
does not reopen spatial contacts, independent boxes or Taylor panels.
No cross-notebook input was read.

External queries included `multivariate Laplace method vanishing amplitude
higher order asymptotic expansion remainder theorem`, `convolution density
light tails rapidly varying saddle point asymptotics exp exp square root`,
`"Riemann" "theta" "signed convolution" asymptotic determinant`,
`"Hankel" "logarithmic" "theta" convolution density asymptotic`,
`"light tails" "convolutions" "Balkema" density asymptotic`,
`"Katsevich" "Laplace" "vanishing" amplitude`, and the exact titles below.
No inspected theorem supplied the actual signed density conclusion.
Search misses do not establish novelty. Unrelated indexed Hankel-transform
and random-matrix articles were not mathematical inputs.

### Primary statements and relevant proof cases

William D. Kirwin, *Higher Asymptotics of Laplace's Approximation*,
[arXiv:0810.1700v2](https://arxiv.org/pdf/0810.1700v2), 5 June 2010.
Read Theorem1.1 (printed p3), Theorem2.1/its following remainder remark
(pp4–5), and Lemma2.3's localization proof (pp7–8).
Theorem2.1 assumes a measurable region containing the minimum as an
interior point; a fixed phase with a unique minimum zero, separated
from zero outside each sufficiently small neighborhood; finite radial
expansions of phase and amplitude, with positive leading phase and
positive radial integrability exponent; and convergence for some
positive transform parameter. It provides coefficients and a little-o
remainder through the stipulated order. The proof uses local sublevel
sets and an exponentially small outer integral. Its positivity reduction
is referenced to Fulks–Sather, not separately checked here. No uniform
theorem for E-dependent phases follows from this fixed-data statement.
It is background comparison, not an imported signed-tail proof.

Anya Katsevich, *The Laplace asymptotic expansion in high dimensions*,
[arXiv:2406.12706v3](https://arxiv.org/pdf/2406.12706v3), posting
12 June 2025 (manuscript title page dated 13 June 2025).
Read Assumptions2.1–2.3, Remarks2.4–2.5 and derivative-bound definitions
(printed pp8–10), complete Theorem2.12 (p11), the signed Taylor
decomposition Lemma4.4 and its proof (pp23–25), and LemmaE.1's
outer-integral proof (p38).

This is a nonasymptotic expansion for an integral over R^d. It requires
a unique minimizer with positive definite Hessian H; C^(2L) amplitude
and C^(2L+2) phase on the closed H-scaled local ball of radius
R sqrt(d/n), with R>=40; and specified growth bounds on its complement.
The normalized expansion retains the signed amplitude at the minimum
and Gaussian coefficient expectations. Its three errors separately
bound local Taylor terms, the Gaussian complement and the actual
outer integral. The bounds depend on Hessian-normalized derivative
suprema, d, n and R; fixing d alone does not make them small for
variable data. The proof's Taylor/dominated-differentiation step
requires local regularity, but no amplitude-positivity premise.
Remark2.5 permits a separately proved small outer-integral bound in
place of the pointwise growth assumptions. It does not supply that
bound. This explicit finite-parameter dependence is the useful
method coverage for a concrete theta application; no general theorem
will be reproved locally.

S. Asmussen, E. Hashorva, P. J. Laub and T. Taimre, *Tail asymptotics
of light-tailed Weibull-like sums*,
[arXiv:1712.04070v1](https://arxiv.org/pdf/1712.04070v1),
11 December 2017. Read Section4, Theorem4.1(ii) (printed pp8–9),
and its explicit dependence in Appendix10 (p20).
Its convolution class uses nonnegative convex C^2 phases with derivative
tending to infinity, eventually positive curvature, self-neglecting
inverse square-root curvature, and measurable prefactors flat on that
local scale. The density convolution theorem is explicitly a
reformulation of BKR Theorem1.1, rather than a new proof in this paper.

BKR is A. A. Balkema, C. Klüppelberg and S. I. Resnick, *Densities
with Gaussian tails*, Proc. London Math. Soc. (3)66 (1993), 568–588,
[DOI10.1112/plms/s3-66.3.568](https://doi.org/10.1112/plms/s3-66.3.568).
The indexed author-repository PDF at
https://mediatum.ub.tum.de/doc/1127867/document.pdf returned HTTP429;
the DOI returned HTTP403 and alternate retrieval did not yield the
proof. No original BKR theorem or boundary proof was inspected or
imported. Its dependent convolution shortcut is parked, not queued
for repeated access attempts. Laub's 2017 talk was inspected only to
locate the paper, not used for theorem hypotheses. The independently
read Katsevich theorem makes BKR access nonessential to the bounded
direct-Laplace applicability test below. If that mechanism instead
needs BKR, stop and report the dependency; do not silently reprove it.

### Comparison and bounded continuation

The proposed balanced simplex point t_i=1/12 is a candidate to test,
not a proved minimizer or dominance statement. L938's kernel factors
depend on E, so a pointwise expansion with E-dependent constants is
insufficient. The singular boundary factors t_i^(k_i-1/2) also require
an outer estimate. A legitimate application of the R^d theorem must
justify any extension/cutoff and pay the omitted simplex contribution.

All signed terms must enter the same leading coefficient before any
sign inference. L938's constant-kernel cancellation concerns a different
limit and supplies no answer at the proposed large-energy saddle.
Conversely, an unsigned convolution asymptotic is insufficient unless
its errors survive the signed sum relative to a nonzero coefficient.
Neither nonvanishing nor a rate has been derived in this literature turn.

Nominate the single bounded target in
`drafts/literature/2026-11-09-l938-balanced-tail-attempt-51.md`.
First evaluate the complete signed leading amplitude exactly; proceed
only on a nonzero result. Then test the actual phase's localization,
Hessian and relative remainder using the cited nonasymptotic theorem.
Stop at cancellation or an unpaid localization/remainder estimate;
do not automatically move to higher expansion order or another grid.
This can produce an intermediate tail input while leaving independent
finite-energy crossings and parameter endpoint signs unresolved.
No complete solution or progress beyond checked source methods is claimed.
