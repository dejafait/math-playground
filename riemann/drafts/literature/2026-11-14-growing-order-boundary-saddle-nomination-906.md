# Growing-order reciprocal-density boundary estimate: nomination906

TARGET: Assess whether C466a's saddle estimates imply D_m(p;x_s)>0 for every sufficiently large s and every integer 2<=m<=floor((log s)^(1/4)), with one s-independent onset and without assuming global PF.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review907 searched reciprocal-Xi boundary PF, growing-order Hankel/Gaussian saddle estimates and quantitative Hermite/Jensen limits; compared C466a/assessment882, assessments883/888 and the hybrid determinant-stability assessment. Exact queries and inspected cases appear below; no matching growing-order density theorem was established.
SOURCE_EVIDENCE: Reuse audited C466a and assessment882; inspected Sra arXiv:2611.02944v1 Proposition C.25/full proof and C.18 boundary proof through (C.68)/Schur complement; Ipsen--Rehman (2008) Corollaries2.7/2.14 with proofs, pp767/770; DLMF5.11.1/5.11(ii); coefficient-Jensen theorem statements and object definitions cited below.
COMPARISON: Known fixed-order boundary convergence and general determinant perturbation cover the tools, but the order-dependent error/conditioning comparison remains a specialization to prove. Explicit order-four bounds and coefficient-Jensen hyperbolicity do not establish the proposed density range. No novelty is inferred.
GAP: Prove weighted Fourier errors through 2m-2 with explicit order dependence and control their determinant amplification uniformly for 2<=m<=floor((log s)^(1/4)); no such estimate or common onset has been established in this review.
REASON: Essential source comparison is complete for one bounded quantitative extension of the audited saddle argument; a proof attempt can now test the precise missing estimate without assuming global PF or repeating the global-head diagnostic.
SCOPE: Covers the exact TARGET as one mathematical test after separate supervisor approval; actual p=theta_1, B=log h, x_s=B'(s), signed D_m and all C466a external-density qualifications. Fixed-order inputs and standard perturbation may be imported; growing-order bounds, determinant signs and onset must be proved in the later attempt. No new result is derived here.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED target changes fixed-order convergence to a simultaneous order range; essential quantitative error/conditioning source scope was missing. Assessment882 was reused rather than repeated.

The main gap remains actual-Xi all-degree algebraic-square positivity at
L030-L032/C032a. A quantitative boundary region valid for a growing
range of orders could initialize an order-tracked contact-propagation
argument. Propagation, simultaneous-contact control and transfer to
L030 remain independent unresolved requirements. The proposed statement
would not give a common interval for all orders, global PF, or RH.

The bounded source question is whether known quantitative saddlepoint,
Edgeworth or Hermite-matrix estimates cover the trial threshold under
C466a's exact analytic and density hypotheses. Retrieve primary theorem
hypotheses and essential weighted-derivative/error cases before importing
any bound. Search local quantitative/growing-order boundary claims and
failures before proposing a calculation. Reuse assessment882 for
fixed-order coverage; its decision does not approve this changed target.
Do not infer novelty from unsuccessful searches or infer a determinant
sign merely from entrywise small error.

Continuation test: identify a theorem or adequately assessed bounded
specialization controlling the full Gaussian-normalized determinant
error for all the proposed orders. If the existing estimates cannot
control conditioning, record the precise missing bound and nominate
one discriminating test rather than invoke fixed-order dominated
convergence with m varying. Import a stronger inspected theorem instead
of reproving it. No growing-order bound, normalization estimate or new
lemma has been derived in nomination906.

The trial growth law is a bounded comparison threshold, not an optimized
rate or a novelty claim. C466f supplies no justified new creative
contact-sign mechanism. This is established-route preparation only;
creative routing requires a separate actual sign mechanism and source
coverage. Matching Mathlib coverage is unchecked.

## Completed comparison907, 14 November 2026

The preceding paragraphs preserve the nomination and its original
unproved status. Updated fields record source readiness for a later
mathematical attempt, not success of that attempt.

### Local overlap and failures

C466a was read in full, including the sector estimate, weighted
inversion, Gaussian determinant and exact tilt/scale transfer.
Assessment882 is reused for its fixed-order audit and external density
inputs. Assessment883 distinguishes the cited finite global PF range
from arbitrary order; assessment888 records why boundary signs do not
pay contact-weight variation. Their stops concern those inferences,
not this quantitative boundary test. C466f's audited global-relative
stop is a contrast only.

The hypotheses/conclusions and comparison passages of
`drafts/literature/2026-11-05-hybrid-saddle-determinant-stability-scope.md`
were inspected. That target concerns a hybrid coefficient Toeplitz
matrix and an unpaid reference sign. C466a instead supplies an explicit
nonzero Gaussian reference determinant for each size. The old warning
still applies: failure of a sufficient inverse-norm bound does not
certify singularity or the wrong sign of the actual structured matrix.
No sibling notebook was read or used.

### Search record and primary cases

Queries executed on 14 November 2026 included:

- `saddle point Hankel determinant derivatives growing order Gaussian Hermite asymptotic`
- `Jensen polynomials degree growing quantitative Hermite limit Griffin Ono Rolen Thorner Zagier`
- `Ipsen Rehman perturbation bounds determinants characteristic polynomials 2008 pdf`
- `"reciprocal" "Xi" "growing" "Sra"`
- `saddlepoint density derivatives uniform derivative order error Hermite Fourier`
- `"Sra" "Fixed-order positivity" boundary`
- `"reciprocal" "Xi" "saddle" "positivity"`
- `"density" "growing order" "Hankel" Gaussian`
- `"Pólya frequency" "saddle" boundary`

Snippets located sources; unrelated hits are not coverage. This bounded
search does not establish originality.

**Boundary source.** Suvrit Sra, *On some positivity properties of the
Riemann Xi function*, [arXiv:2611.02944v1](https://arxiv.org/html/2611.02944v1),
2 November 2026, Appendix C.17 Proposition C.25, (C.63)--(C.65)
and complete proof; C.18 boundary proof (C.67)--(C.68) through its
Schur-complement argument. The former is fixed-order, matching C466a's
recorded limit; the latter treats even derivatives through six and
determinants through four. Its incomplete-gamma monotonicity check
is restricted to those derivative orders. Neither case states the
proposed growth law. No numerical certificate was replayed or imported.
The author [version page](https://suvrit.github.io/papers/riem-xi/)
identifies site v3 with arXiv v1, not with the older Hub rendering.
Hub timed out twice and the direct author PDF failed; arXiv supplied
the relevant primary text, resolving access for this target. No Polson
or broad signed-decomposition theorem is needed.

**Determinant tool.** I. C. F. Ipsen and R. Rehman, *Perturbation Bounds
for Determinants and Characteristic Polynomials*, SIAM J. Matrix Anal.
Appl. 30(2) (2008), 762--776,
[author PDF](https://ipsen.math.ncsu.edu/ps/simax070477.pdf),
Corollary 2.14 and proof, p770; underlying Corollary 2.7 and proof,
p767, and Theorem 2.13, pp769--770. For complex square A,E, A
nonsingular, Corollary 2.14 gives

\[
 \frac{|\det(A+E)-\det A|}{|\det A|}
 \le (1+\|A^{-1}\|_2\|E\|_2)^m-1,
\]

where m is the matrix size. No Hermitian or positive-definite hypothesis
on E is imposed. A later application must specify the Gaussian matrix,
its invertible normalization and the actual error matrix. The theorem
does not estimate these norms here. Use the finite bound rather than
only its first-order expansion when m varies. No reproof of the general
perturbation theorem is justified.

**Gamma input.** [NIST DLMF5.11.1](https://dlmf.nist.gov/5.11#E1)
and [5.11(ii)](https://dlmf.nist.gov/5.11#ii) were inspected for
the fixed-sector log-gamma expansion and complex remainder bound.
The latter bounds the truncated log-gamma remainder by the first
neglected term times sec(arg(z)/2)^(2n). This supports C466a's sector
input, not an order-uniform density theorem. Reuse its analytic
remainder/Cauchy framework; do not silently replace O_j constants by
order-independent constants.

**Different objects.** Griffin--Ono--Rolen--Thorner--Tripp--Wagner,
*Jensen polynomials for the Riemann xi function*,
[author-hosted submitted PDF](https://uva.theopenscholar.com/files/ken-ono/files/jenseneffectivesubmitted.pdf),
Theorem1.1 and defining coefficients, pp1--2; Section3.2, Theorem3.2
and Hermite-coefficient condition (3.3), pp10--11, were read. These
concern coefficient Jensen hyperbolicity, not p's derivative Hankel
matrix at x_s. C466a supplies no identification allowing import here.
Jonathan Holland, [arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1),
Theorem1.1 and introduction/Section2 definitions were also read:
the stated wedge n^3 log^2(n+2)>=K d^5 again concerns coefficient
Jensen polynomials. Its proof was not audited or imported; the object
mismatch precludes direct use here. Search leads on iid saddlepoint
approximations, including Reid's review, were not inspected as
applicable theorems and supply no premise.

### Permitted bounded attempt and decision threshold

Retain the exact TARGET. The future attempt is a quantitative
specialization, not a reproof of C466a or a new central sign mechanism.
Essential input ID is C466a; L018 fixes completion conventions.
L030--L032/C032a remain the destination. Other routes above are
contrasts, not inputs.

One discriminating test is relative determinant error strictly below
one, uniformly for all the stated m and all s>=S with one S. Apply
the cited finite perturbation bound after controlling weighted Fourier
errors and Gaussian inverse norms. Conditioning in monomials must be
paid or an explicit invertible basis change justified. A uniform
Gaussian-normalized ratio error <=1/2 would be a sufficient stronger
success threshold. These are requested thresholds, not estimates
derived or asserted in this literature turn.

Keep C466a's s-dependent two-regime Fourier bound instead of treating
its final fixed integrable majorant as quantitative order-uniform
convergence. A later proof must choose a frequency split, control the
local Taylor error and both tails with weights through 2m-2, track all
order dependence, and compare it with determinant conditioning.
These are unproved obligations, not source conclusions.

Continue if the bounded specialization yields the uniform sign or an
informative obstruction. If the sufficient bound fails, record the
precise failing comparison; that is not a counterexample to the target.
Do not weaken to fixed m and report success. A materially changed
range or mechanism requires separate coverage. Contact signs,
simultaneous contacts, propagation and L030 transfer stay independent
even on success.

No new lemma, growing-order bound, mathematical script or RH claim was
produced. Matching Mathlib coverage is unchecked. Import cited tools
in the later canonical proof if used. New readiness receives separate
supervisor approval next turn.
