# Uniform unproduced-block bound — proposed critical-audit coverage

TARGET: Critically audit L115's uniform n=43–128 block bound against its precise hypotheses and L101's original truncation contract, without evaluating kernels or assembling the derivative.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Recovery source check reopened https://arxiv.org/pdf/1608.06423v2 and https://dlmf.nist.gov/4.5.E4; inspected Section 3.1, Lemma 4 statement and complete geometric-remainder proof, and DLMF equation with its domain. Reused the exact cutoff source comparison in drafts/literature/2026-10-25-unproduced-kernel-block-bound.md and its recorded duplicate/failure searches; read L101's kernel, coefficient bound, full tail estimates and relevant audit cases. No new discovery search or claim of originality is made.
SOURCE_EVIDENCE: Christian Wuthrich, Numerical modular symbols for elliptic curves, arXiv:1608.06423v2, PDF dated 24 March 2017, Section 3.1, Lemma 4 and proof printed pp.6–7, https://arxiv.org/pdf/1608.06423v2#page=6 and https://arxiv.org/pdf/1608.06423v2#page=7; NIST DLMF 4.5.4, https://dlmf.nist.gov/4.5.E4, log(x)<=x-1 for real x>0, both reopened 2026-10-25. L101 supplies the local kernel and unchanged 128-output contract; L115 contains the unaudited cutoff specialization.
COMPARISON: All mathematical mechanisms are within the existing SPECIALIZE assessment: positive full-kernel majorization, a geometric tail and rational exponential comparisons. The new task checks the correctness and scope of the explicit specialization, without deriving a different estimate or changing the finite-arithmetic contract.
GAP: An independent critical review of L115's complete proof and its limitations remains undone; neither source readiness nor structural validation establishes mathematical correctness. A 42-kernel derivative contract and zero exclusion remain outside this task.
REASON: Review the load-bearing block estimate before relying on it to change the assembly plan; this continuation is proposed for separate supervisor approval, not invoked or critically approved in the producing turn.
LITERATURE_REASON: Supervisor recovery identified missing direct primary-source URLs in this ready assessment; repair source traceability for the unchanged audit target without repeating discovery or performing its critical audit.
SCOPE: Audit only L115's stated bound for the fixed newform and every real t in [3/10,1/2], using L101 as the sole direct mathematical input. No new kernel certificates, mathematical scripts, derivative evaluation or rank comparison.

## Exact source scope and audit test

The earlier ready assessment compared the n=43–128 inequality with
L101's n>128 bound and inspected the primary-source hypotheses.
Reuse that coverage: the normalized elliptic form and parameter
interval are unchanged. The Mellin identity and the analytic-rank
inputs encapsulated in L101 are not needed to prove the block estimate.
No new independent theorem or full matching Mathlib coverage is claimed.
This is readiness for a REPRODUCTION audit, not a second mathematical
advance or a report that the audit already passed.

Read the complete L115 proof and L101's exact kernel/majorant and
remainder contract. Check nonnegativity on [1,128], parameter
monotonicity including both closed endpoints, the elementary improper
integral, the finite coefficient inequality, convergence of the enlarged
geometric sum, retention of factor four, and every strict comparison:
q<10/13; exp(3)>131/8>16; 43*(3/10)>12; the prefactor 520/387;
and 130<387. Check that no signed-series interchange, coefficient
outside the actual finite block, midpoint enclosure or derivative
nonvanishing is assumed. Audit the direct mathematical input against
the DAG and verify that L101's original contract is not silently revised.

A pass must identify the achieved threshold and preserve the remaining
assembly, parameter, provenance and nonvanishing gaps. A failure must
name the exact erroneous inequality or missing hypothesis and preserve
the producing proof as evidence while making any correction explicit.
Do not select or prove a new partial-assembly contract in this audit.
The supervisor's separate approval of this newly written assessment
is required before the proposed audit is invoked.

## Recovery source verification, 2026-10-25

The missing direct URLs above are now recorded. Wuthrich Section 3 fixes
f as the newform associated to the elliptic curve's isogeny class. Lemma 4
requires Im(tau)=y>0, epsilon>0 and T>T(y,epsilon), where
T(y,epsilon)=-log(2*pi*y*epsilon)/(2*pi*y). Its conclusion is an
absolute truncation error below epsilon for the integrated Fourier
series. Its proof explicitly imports |a_n|<=n from reference [13],
Lemma 2.9, then bounds the absolute tail by a convergent geometric
series. The statement and full proof were reopened, not merely a
search preview. Reference [13] was not newly inspected; no additional
claim about that reference is needed beyond reusing L101's assessed
input. The precise coefficient normalization agrees with the elliptic
newform fixed in L101. DLMF 4.5.4 was reopened with its real positive
domain, including equality at x=1.

These sources supply supporting inequalities and the method; neither
asserts L115's n=43–128 constant or audits its proof. Lemma 4's
modular-symbol truncation theorem is not itself a derivative contract.
Only its already assessed coefficient input and majorant mechanism
are reused here. The original duplicate/failure comparison is reused
from the producing assessment; no production route is reopened.
Full matching Mathlib coverage remains unchecked. This is a process
repair with no new mathematical result or independent correctness
verdict on L115. The exact audit target, hypotheses and pass/failure
test above remain unchanged.
