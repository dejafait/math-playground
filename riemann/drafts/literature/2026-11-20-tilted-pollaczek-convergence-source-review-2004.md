# Weighted convergence: source comparison2004

20 November 2026. Literature only. Main gap: L030-L032/C032a
actual-Xi all-degree mixed positivity. Intermediate target: the exact
weighted compact limit nominated2003. Its downstream use is possible
zero transfer, conditional on a separately proved uniform bound on
nonreal roots with appropriate multiplicity control. No such bound is
available. Continue with a matching source statement and standard
theorem; abandon reasoning based only on pointwise multiplier limits.

## Exact primary overlap

Alexey Kuznetsov, *Expansion of the Riemann Xi Function in
Meixner-Pollaczek Polynomials*, Canad. Math. Bull.51(4)(2008),561-569,
[DOI](https://doi.org/10.4153/CMB-2008-055-0),
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-3-function-in-meixner-pollaczek-polynomials.pdf).
Reaccessed p561 definition, pp562-564 basis/(2)-(11)/Theorem2.1 and
full displayed proof, p565 Remark3, pp566-567 asymptotic discussion,
and pp568-569 weighted passage/references. Source Xi(t)=xi(1/2+it),
xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2. Theorem2.1 states ordinary
compact convergence on all C for the basis/coefficients in review2001.
Page568 explicitly states the exact Jensen-weighted compact limit in
nomination2003. This is known source content. Its proof is not separately
displayed. Theorem2.1's displayed proof imports (6)-(8) from upstream[9],
then uses recurrence/cancellation; Remark3 supplies no uniform compact
remainder estimate. Import the named theorem, without claiming an audit
of its upstream proof or inferring convergence merely from entireness.

Exact family: T_N(t)=sum_(k=0)^N m_(N,k) beta_k p_k(t), N>=1,
m_(N,k)=N!/((N-k)!N^k), p_k=P_k^(3/4)(t/2;pi/2), beta_k the source b_k
from (3)-(4), transcribed in review2001. Retain odd terms. The source
limit is exp(-pi*t/4)Xi(t). No identification with C028b coefficients.

## Standard theorem and essential proof case

Pierre-Olivier Parise, *Kernel Summability Methods and Spaces Of
Holomorphic Functions*, [arXiv:2302.06770v2](https://arxiv.org/html/2302.06770v2),
Sections2/4.9/5.1-5.2: inspected Theorem5.2, its Banach-space discussion,
Theorem5.5 and complete sufficient-direction proof. The rendering labels
itself v2 (31 May2023), with body date August24,2026; no date reconciliation
is claimed. Only scalar-entry matrices acting on Banach-valued sequences
and sufficiency are needed, not necessity or operator-entry extensions.

The Silverman-Toeplitz sufficient hypotheses are uniformly bounded
absolute row sums, each fixed column tending to zero, and row sums
tending to one. The conclusion preserves limits in a complex Banach
space X. The row series must exist; finite rows suffice. Theorem5.2
states the scalar theorem; following text extends it to Banach X and
refers the sufficient proof to Theorem5.5.

The latter assumes noncompact locally compact Hausdorff parameter
spaces, sigma-compact input space, a Borel measure and measurable scalar
kernel. Sufficient conditions: integrable rows, uniformly bounded row
L1 norms, vanishing absolute mass on every compact input subset, and
total row integrals tending to one. The proof first uses boundedness
of a convergent X-valued input to ensure the Bochner integrals exist.
It separates the error into an input-minus-limit integral and total-mass
error, then splits the integral into a compact initial part and a tail.
The former vanishes by the compact-mass condition; the latter is bounded
by the uniform L1 bound times the input's small tail norm. This is the
full relevant sufficient proof case. It assumes no root reality or
absolute convergence of an underlying function expansion.

Intended applicability, not performed here: discrete sequence index
with counting measure; X=C(K;C) in sup norm for arbitrary nonempty compact
K in C; ordinary partial sums restricted to K as the input sequence.
Finite summation by parts and all Jensen endpoint weights remain to be
checked. Do not apply the theorem directly to individual expansion terms.

## Comparison, failures and route decision

Compared three mechanisms for this convergence prerequisite:

1. Coefficient-tail domination via source asymptotics. Full uniform
   remainders and upstream[9] remain uninspected; ordinary convergence
   is already covered by named Theorem2.1.
2. Regular summability of ordinary partial sums in C(K). Retained:
   sufficient theorem/proof coverage is inspected, leaving finite
   weight applicability checks independent of the Arb runtime.
3. Jensen real-root multiplier/biorthogonal transfer. Requires separate
   root hypotheses and is unnecessary for the limit. Stops111/1596
   and L530/L955 supply no actual-family uniform root bound; neither
   do they refute this convergence statement.

Reused source-notes2000, finite source-review2001, runtime-park2003 and
October30 weighted-retest overlap. Scoped searches of named Pollaczek
assessments/stops found no local summability specialization; no novelty
inference. Unfinished work and mathematical obstructions are preserved.

Queries: `Silverman Toeplitz theorem Banach space regular summability
theorem proof pdf`; `Kuznetsov Riemann Xi Meixner Pollaczek 2006 convergence
9`; exact upstream title searches; `Jensen Pollaczek converges weights`.
Jardas-Sarapa1997 was a search lead (direct PDF fetch418), not imported;
no repeat fetch. Inoue [1412.1220](https://arxiv.org/pdf/1412.1220), displayed
v1/body July7,2021, introduction and Theorem2.3 hypotheses were inspected:
different completed-zeta normalization/strip scope, not a replacement
for this all-C target. Full proof unread; not imported.

Upstream[7] remains unread and is unnecessary without a root-preserver
claim. Upstream[9] remains unread: standalone Theorem2.1 is imported,
not reproved. Its exact-title publisher lead DOI10.1080/10652460701450773
lists827-835, unlike the reference list's809-817; no theorem content from
that lead was used and no access continuation is nominated. The exact
weighted statement and the summability sufficient direction are directly
accessible, so source access is not the next bottleneck.

Outcome: informative known overlap removes the missing-source premise
and changes routing to a standard finite-weight applicability check.
No canonical mathematical result is installed, no new derivation or
script is produced, and PROOF/DAG are unchanged. This is local coverage,
with no progress beyond checked literature. The new ready continuation
receives separate approval before research. Mathlib coverage unchecked.
No creative central-gap target is supported by a uniform index estimate.
