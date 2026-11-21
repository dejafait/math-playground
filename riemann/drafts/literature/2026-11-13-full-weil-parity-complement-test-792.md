# One full-complement parity comparison — nominated source scope

TARGET: Attempt to separate the full even and odd Rayleigh infima of Q on (-1,1) using one even Ritz upper bound and a shifted odd Schur lower certificate with exactly 120 retained modes and the entire complement; stop at this cutoff if the required bounds fail or overlap.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact parity-gap searches and primary/local overlap comparison in 2026-11-13-full-weil-parity-gap-discovery-791.md, step792. Numerical interlacing and the existing L759 finite certificate do not cover the full odd complement. No novelty claim.
SOURCE_EVIDENCE: Suzuki arXiv:2606.09096v2 Theorem1.1, Corollary1.2, Sections3.2,4.1-4.2,4.5; Andrews-Connes-LaGatta arXiv:2611.13129v1 Section2.1 and Lemma8.16 with complete proof; reuse the November4 spectral-triples determinant assessment for Connes-Consani-Moscovici2511.22755v1 Lemma2.3, Proposition3.4 and Section4 defining matrix entries. Local exact smooth normalization is L744(6).
COMPARISON: Closed-form realization, the variational principle and conditional Schur reduction are known. The difference to establish is a quantitative complete odd lower certificate above an even trial value at half-width1; no inspected theorem or local certificate supplies that difference.
GAP: Obtain an even Rayleigh upper bound U and rational tau>U, then certify Q_odd-tau||.||²>=0 on its entire closed form domain by controlling both the retained block and the full complement. No values, complement coercivity, coupling bound or matrix sign is asserted.
REASON: This is an independently testable full-operator comparison, distinct from C998z modulus ordering, L759 finite separation and the stopped flux-only secular identity. Known machinery is cited; its arithmetic bounds require one separate REPRODUCTION attempt.
SCOPE: Only half-width1, full unneutralized Q, real parity sectors, fixed120-mode split and complete prime powers; no cutoff/window sweep, semigroup claim, global positivity, finite-to-infinite extrapolation or source-computation import. Newly written ready continuation requires separate approval next turn.

## Exact object and bounded test

Use L744(6) with its complete archimedean symbol, both poles, and every
prime power whose delay overlaps (-1,1). Do not assume RH, neutrality,
a positive kernel, a source positivity certificate or a gap. In the
multiplicative notation of the sources this window is lambda=e and
L=2log(lambda)=2, not lambda=sqrt(13) or L=log13.

On (-1,1), extended by zero, use the real orthonormal even block
1/sqrt2, cos(pi j x), 1<=j<=120, and odd block sin(pi j x),
1<=j<=120. These are the centered real versions of the source's
log-Fourier block. The source permits the endpoint jumps in its form
domain. Justify that identification, their admissibility and equality
of the smooth parity infima with the closed parity infima before
using block estimates; no smooth minimizer is promised. Symmetric
projection of a smooth core is the relevant applicability check.
L741's specific closed-domain theorem at length log3 is not extended
by assertion to length2. Use the cited full localized-form theorem.

Seek one explicitly enclosed even Rayleigh trial value U from this
block and a rational tau>U. Let V be the specified120-dimensional odd
block and W its L2 orthogonal complement in the full odd space. Apply
Lemma8.16 to the shifted odd form Q-tau||.||². Its hypotheses require
V inside the form domain, a closed semibounded complementary form D,
a rigorous D>=d I with d>0, and a justified form-dual coupling B.
The finite Schur form must have a certified nonnegative lower matrix
bound after *all* coupling, truncation and enclosure errors. The
source criterion then supplies the lower floor tau for the full odd
infimum. This is the intended application of a cited criterion, not
a new lemma or an assertion that its hypotheses hold here.

The sought comparison is U<tau<=lambda_odd, with
lambda_even<=U from the same variational principle. A positive
finite Schur pivot is not itself a positive full spectral gap above
tau: retain the actual shifted lower-floor conclusion of Lemma8.16.
Likewise two Ritz values both being upper bounds cannot suffice.

Begin with analytic complement/coupling estimates and an explicit
resource/error requirement before expensive matrix work. A proven
insufficient lower estimate, uncertified domain/coupling, or overlapping
rigorous bounds is an inconclusive/negative result for this prescribed
certificate, not a failure of the actual parity inequality. Preserve
partial reasoning and stop after this split; no cutoff growth, source
archive retry, another finite-only certificate or repeated bump test.
An exact contrary full-operator ordering would obstruct the conjecture,
but failure of these sufficient estimates cannot establish it.

## Source applicability and unresolved downstream work

Primary URLs:
https://arxiv.org/html/2606.09096v2 ;
https://arxiv.org/html/2611.13129v1 ;
https://arxiv.org/html/2511.22755v1 .

The parent assessment records inspected hypotheses/proof cases. Reuse
its Schur coverage rather than derive a new generic square-completion
lemma. The new source's Hypothesis3.4, conditional Section8 margin,
prolate numerics and Lemma6.1 gap assumption are not inputs. The
November4 general finite-entry source scope may be reused with the
changed explicit window, but L759's numerical enclosures cannot.
No inaccessible external supplement is essential to this proposed
self-contained attempt from the defining Q.

Essential local normalization inputs: L741(7),(13),(16)-(18) as used
in L744(5)-(6). C998z and L759 are comparison/stop evidence, not
positivity premises. The parent review records the nodal, multiplier,
pole-resolvent and finite-certificate source-access limitations.

A successful fixed gap would place a full ground eigenspace in the
even sector; it would not prove its dimension is one, a fixed sign,
Xi realization with multiplicities, any uniform-window estimate or
actual-Xi all-degree mixed positivity. This is established-route
development/REPRODUCTION. No new central creative mechanism is ready:
an arithmetic ground-state-to-Xi bridge remains missing.
Mathlib matching coverage is not checked. No cross-notebook input.
