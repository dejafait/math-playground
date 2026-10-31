# Signed-pole resolvent mechanism — completed source comparison

TARGET: Test whether isolating L516's signed pole as a rank-two perturbation yields a resolvent expression whose arithmetic numerator enforces tau_L^2+tau_R^2=O(lambda) near an assumed simple finite first zero.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Narrow local Weil assessments, stops and histories contain no prior assessment of this exact mechanism. Searched finite-rank resolvent/Krein formulas, Feshbach-Schur complement invertibility, and Weil boundary resolvent pole arithmetic trace. Located standard operator identities and a directly overlapping pole-capacity investigation; no inspected theorem supplies the eigenvalue-relative arithmetic bound. This is not a novelty claim.
SOURCE_EVIDENCE: Read Liaw–Treil arXiv:1806.08856v2 Section 2 pp.3–4 and Lemma 3.1 with its complete resolvent-identity proof pp.8–9; Dusson–Sigal–Stamm arXiv:2105.02058v1 Theorem 1.2, (1.10)–(1.11), Corollary 1.3 and the stated complement-invertibility hypotheses; bramble_trace paper 67 v1 (3.4)–(3.5), Section 7 and (9.1)–(9.5); teal-sea revision f2dde1df Sections 2.6 and 8.1–8.3, retaining their unreviewed/numerical qualifications. URLs and precise scope follow below.
COMPARISON: Bounded signed finite-rank perturbations and conditional spectral reductions are standard. The overlapping pole-capacity investigation already relocates the question to interior spectral and eigenvector quantities without an arithmetic mechanism. Neither source supplies bounded-data endpoint traces for arbitrary resolvent forcing, a uniform gap for the pole-removed background, or the required vanishing numerator. Numerical alignments and finite-matrix identities do not close those continuum gaps.
GAP: No independently controlled arithmetic numerator sufficient for the O(lambda) trace rate was found. A real background spectral pole and modes outside the pole-generated cyclic subspace must remain; bounded L2 resolvents alone do not meet L513's trace hypotheses. This comparison supplies no new operator specialization or cancellation.
REASON: The saved continuation test fails for the generic secular/resolvent-only implementation. Park that implementation, preserving the possibility of reopening with a concrete arithmetic estimate and controlled domains. This is source-overlap/scope evidence changing the route, not a mathematical no-go theorem for all finite-rank methods or RH.
LITERATURE_REASON: The start target changed technique beyond moving-interval continuity; primary finite-rank hypotheses and direct overlap were essential unread coverage. That one bounded source comparison is now complete.
SCOPE: Source comparison only for L516's complete fixed finite-mu_A model, c=log(2pi), nu_rho, the signed pole, all prime powers and equality cutoffs, near an assumed simple finite first zero. EXPLORE records lack of a covering theorem; it does not override the failed continuation test or authorize repetition without new arithmetic input.

## Main gap and bounded test

Actual-Xi all-degree positivity remains unproved. The intermediate target
is a single finite C with tau_L(u_a)^2+tau_R(u_a)^2<=C lambda(a)
along the assumed normalized positive simple branch approaching a finite
first zero, with a bounded away from zero. Downstream use would be to
exclude that crossing under a separately justified support law. L512's
full-Weil identification, branch/nullvector existence, collars and Xi
transfer remain independent obligations.

The original nomination required both a domain-valid reduction and an
independently testable arithmetic numerator. Only the generic operator
part is covered by known theory; neither the trace-domain specialization
nor an independent numerator estimate has been supplied. Therefore this
version stops. An estimate equivalent by L516 (5) to its flux inequality
is not independent arithmetic evidence.

## Primary finite-rank coverage

[Liaw–Treil, *Matrix Measures and Finite Rank Perturbations of
Self-adjoint Operators*, arXiv:1806.08856v2, 23 November 2018](https://arxiv.org/pdf/1806.08856v2),
Section 2, printed pp.3–4, treats self-adjoint A and A_Gamma=A+B Gamma B*
with finite-dimensional B and Hermitian Gamma. Its bounded-B case keeps
Dom(A); the signed matrix need not be positive. Lemma 3.1, printed
pp.8–9, gives, for nonreal z and cyclic Ran(B),

    F(z)=B*(A-z)^(-1)B,
    F_Gamma(z)=F(z)(I+Gamma F(z))^(-1).

The proof reads both resolvent identities and establishes matrix
invertibility off the real axis, not at a real limiting eigenvalue.
Section 2 retains the unchanged orthogonal cyclic complement. An
assumption that the pole vectors detect every relevant eigenvector
cannot be silently inserted. The HTML theorem fetch timed out; the
PDF setup and complete Lemma 3.1 proof were successfully read. This
source is not blocked.

[Dusson–Sigal–Stamm, *The Feshbach-Schur map and perturbation theory*,
arXiv:2105.02058v1, 5 May 2021](https://arxiv.org/html/2105.02058v1),
Theorem 1.2 and (1.10)–(1.11), require an invertible compressed complement
and a bounded Schur expression. Corollary 1.3 requires these conditions
through the spectral region used. Their reconstruction operator contains
the complementary inverse. Apply the hypotheses at H-z, not just at
one unrelated parameter. The theorem's proof is referenced there to
Bach–Fröhlich–Sigal Section IV.1 and Gustafson–Sigal Appendix 11.6;
those external proofs were not inspected or independently audited.
No claim of an unconditional complement inverse follows from citation.

These results already cover the abstract machinery. A later use should
cite them, justifying its signed matrix, domain and spectral region;
reproving generic identities would add no arithmetic input. No such
specialization is derived in this literature turn.

## Directly relevant overlap and trace limitation

[teal-sea, *Weil positivity propagation across window size*, compiled
27 October 2026, revision f2dde1df](https://zeta.teal-sea.com/read/hunts/weil_propagation/theory/RESULTS.html),
Sections 2.6 and 8.1–8.3, already studies the pole-free operator,
sectorwise secular equations, pole capacity and eigenvector overlaps.
The notes explicitly leave the arithmetic mechanism unresolved.
Their leading-order comparison assumes spectral separation, and their
matrix boundary observations do not establish the physical continuum
trace rate. The analysis is labeled unreviewed; its numerical tables
and alleged rival certificates were not replayed and are not imported.
This overlap changes the decision to pursue the generic reduction alone;
it is not an independently audited impossibility result.

[bramble_trace, *Boundary traces and support variation for localized
Weil operators*, paper 67 v1, 27 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/67),
(3.4)–(3.5), Section 7 and (9.1)–(9.5), retain the complete measure and
leave the relative flux estimate open. The unversioned page identifies
v1; the /v1 URL failed. Its source proof remains unaudited locally.

Locally L513 requires u and G_I u bounded plus the operator-domain
split; L515 establishes this for eigenvectors. It does not assert it
for arbitrary resolvent outputs. L519 gives continuity under assumed
dilated L2 convergence, not a vanishing rate. Consequently writing a
boundary functional of a background resolvent is an additional task,
not a theorem obtained by replacing an eigenvector in L513's formula.
A background zero mode must be kept or controlled by a justified
reduced inverse. No positivity or invertibility is assumed here.

The raw-adjoint, averaged-Abel and rank-trace stops were checked in
their specific local ATTEMPTS files and retain their original scopes.
No new lemma, mathematical script, canonical proof, DAG edge or PROOF
assembly changed. Mathlib matching coverage was not checked; no claim
of absence, cross-notebook input, new mathematical result or RH
resolution is made. A future arithmetic numerator or an actual spectral
pole treatment could justify a materially refined attempt.
