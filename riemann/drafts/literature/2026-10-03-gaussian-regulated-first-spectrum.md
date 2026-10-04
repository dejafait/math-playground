# Gaussian-regulated first Laguerre spectrum — source assessment

TARGET: Test whether L357's Gaussian-regulated approximants satisfy F_ε′²−F_εF_ε″≥0 at every real frequency for all sufficiently small ε, using an exact Mellin representation and a large-frequency sign test.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Seventeen exact-target, terminology and stronger-result queries on 2026-10-03 found no matching global-sign statement in the sources inspected. Read Csordas's associated-kernel criterion, DLMF gamma/beta transforms and differentiated asymptotics, and Paris's smoothed Dirichlet-series expansion; reuse the adequate Poisson/weighted-convergence assessment. Queries and reading limits appear below.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), 5.9.1, 5.12.1/3, 5.11.1–3/9–11 and 5.15.8–9, https://dlmf.nist.gov/5.12#E3; Csordas, arXiv:1309.0055v2 (2014-02-21), Definition 1.2, Theorems 3.5/3.7 and 4.6, Open Problem 4.7 and (4.9), pp. 2, 6–8, 11–13, https://arxiv.org/pdf/1309.0055v2; Paris, arXiv:1503.07329v1 (2015-03-25), (1.1), §2 (2.1)–(2.6) and Theorem 1, pp. 1–5, 8, https://arxiv.org/pdf/1503.07329v1. Statements, domains and the cited transform/remainder arguments were read.
COMPARISON: The gamma/beta integrals and gamma-derivative asymptotics cover scalar tools for an exact fixed-regulator Mellin calculation. Csordas characterizes associated-spectrum positivity under additional admissibility hypotheses; Paris estimates a smoothed Dirichlet series for fixed real exponents as damping tends to zero. Neither supplies this differentiated, subtracted and reflected family's sign for all real frequencies and all sufficiently small regulators.
GAP: Specialize the covered Mellin tools to exactly F_ε, with justified boundary terms and two frequency derivatives, then test its large-frequency first Laguerre sign at fixed positive ε. A positive tail would still leave its complementary frequencies and the regulator quantifier; a negative value for arbitrarily small ε would stop this certificate.
REASON: The unchanged spectral target now has accessible supporting coverage for a later mathematical invocation. Import the named transform and asymptotic formulas; test only the family's application and sign, which the checked statements do not determine. This review derives no Mellin formula, asymptotic or sign and makes no originality claim.
SCOPE: Exactly k_ε and its real-axis Fourier transform F_ε from L357, 0<ε≤1; a sufficient certificate would give one ε_0>0 with F_ε′²−F_εF_ε″≥0 on R for every 0<ε≤ε_0. No complex entire extension, real-root preservation, or higher-level condition is assumed.
LITERATURE_REASON: The required review concerns a changed spectral target outside the prior assessment's explicit weighted-approximation scope; the missing coverage is the exact Mellin/sign comparison, not another search for Poisson summation.
COVERED_TARGET: Derive a justified gamma/beta Mellin representation of L357's F_ε and its first two real-frequency derivatives at fixed ε>0, retaining the exact zero-mode subtraction and even reflection.
COVERED_TARGET: Test the large-frequency sign of F_ε′²−F_εF_ε″ for L357's Gaussian-regulated family at fixed ε>0, tracking whether any negative values occur for arbitrarily small ε.

## Fixed target, relevance and redundancy

The preceding [Gaussian zero-mode assessment](2026-10-03-gaussian-regulated-modular-zero-mode.md)
already covers the scalar Poisson identity and polynomial-weighted
Gaussian tails. Reuse it and the completed
[L357](../../lemmas/L357-gaussian-zero-mode-subtraction-repairs-weighted-convergence.md),
without redoing that source search or its weighted limit. The exact
definitions of a_ε, z_ε, h_ε, k_ε and F_ε remain those in L357:
the theta parameter is e^(2u)+ε, subtraction precedes
P=2D_u²−1/2, and the final kernel is the even reflection average.

The main gap remains actual-theta positivity at unbounded real
frequencies and low Laguerre indices. A vanishing-regulator first-sign
certificate, together with L357, could supply that first sign in the
limit. It would leave the higher low-index and mixed-form conditions
required for RH unresolved. The achieved O(ε) uniform absolute error
is not the required global nonnegative sign margin.

L233's positive Gaussian-mixture counterexample excludes generic
kernel-positivity signing. L234's cusp tails concern finite reflected
sums; L235's mass failure concerns finite modular averages; L356's
negative tail concerns a separate parity block. None decides this
smooth, fully subtracted Gaussian-regulated spectrum. Retain all
three stopped constructions and do not transfer their tails to F_ε.
The changed test exploits L357's repaired whole-line approximation;
it does not reopen a failed finite-truncation calculation.

## Search and reading record — 2026-10-03

Read the shared and local goals, checkpoint, complete PROOF.md
overview and DAG before reviewing the saved target. The active
notebook had no working-tree changes; other notebooks' unfinished
changes were preserved. Inspected L357, L233–L234, the preceding
assessment, the first-associated arithmetic/parity source notes and
the approximation history. No local result already signs F_ε.

Queries actually used:

- `"Riemann" "theta" "Gaussian" "regularization" Laguerre`
- `"theta" "Mellin" "Laguerre inequalities"`
- `"Fourier transforms of positive definite kernels" Csordas Laguerre`
- `"Gaussian" "regularized zeta function" Mellin`
- `"Riemann xi" "e^{-epsilon"`
- `"theta" "heat" "Laguerre inequality"`
- `"theta" "Mellin transform" "exp" "n" zeta cutoff`
- `"Gaussian regulated" theta Fourier zeros`
- `"theta" "zero mode" "Laguerre"`
- `"Laguerre" "theta" "regularized"`
- `"Gaussian" "zeta" "cutoff" "Mellin"`
- `Paris "generalised Euler-Jacobi series"`
- `"sum" "exp(-a" "n^2" "zeta" "Paris"`
- `"Riemann" "Laguerre inequalities" "universal factors" Csordas`
- `"Paris" "Euler-Jacobi" "S_p(a;w)"`
- `"The asymptotic expansion of a generalisation of the Euler-Jacobi series" arxiv`
- `"Gaussian" "Laguerre" "Riemann" "regularization"`

Literal regulator/sign searches mostly returned unrelated Gaussian,
regularization or Laguerre-polynomial material. The associated-kernel
and smoothed-series terminology led to the primary sources below.
No matching full-family sign theorem was found in this bounded
search; a failed query establishes neither originality nor a sign.

## Inspected statements and applicability

**Gamma and beta transforms.** Read NIST DLMF version 1.2.8:
[5.9.1](https://dlmf.nist.gov/5.9#E1) gives the exponential Mellin
integral for Re ν>0, μ>0, Re z>0, with principal powers.
[5.12.1 and 5.12.3](https://dlmf.nist.gov/5.12#E3) identify Euler's
beta integral and its positive-half-line version for Re a, Re b>0.
These are supporting formulas for the regulated Gaussian terms and
the zero mode. They do not include P, reflection, an infinite-sum
interchange or a sign. Their application must check convergence and
both real-frequency derivatives; no application formula is asserted
by this review.

**Differentiated large-parameter tools.** Read
[DLMF 5.11.1–3](https://dlmf.nist.gov/5.11#E1),
[5.11.9–11 and §5.11(ii)](https://dlmf.nist.gov/5.11#ii), and
[5.15.8–9](https://dlmf.nist.gov/5.15#E8).
The logarithmic, digamma and polygamma expansions use sectors
|arg z|≤π−δ. The vertical gamma-modulus equivalent is uniform for
bounded real parts. Complex logarithmic/digamma errors have explicit
sector factors; the gamma remainder bound uses |arg z|≤π/2 and
has a stated K=1 exception. These support a fixed-regulator tail
analysis, including derivatives, rather than differentiation of an
uncontrolled big-O term. A modulus bound alone does not sign the real
projection or its Laguerre combination. No uniform ε→0 asymptotic
is imported.

**Associated-kernel criterion and a different heat family.** George
Csordas, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
21 February 2014. Read Definition 1.2 (p. 2), Theorems 3.5 and 3.7
with the transform argument (pp. 6–8), Theorem 4.6, Open Problem 4.7
and (4.9) (pp. 11–13). Admissibility includes positivity, decrease
and super-Gaussian decay of every derivative. Strict log-concavity
makes associated kernels admissible; it does not prove positive
definiteness. The all-level criterion requires every associated
spectrum's sign. L357 does not establish these admissibility
hypotheses for k_ε. The paper poses the first actual-theta sign as
a problem; this is its 2014 statement, not a claim about all 2026
literature. Its heat family multiplies Φ(u) by exp(tu²), unlike the
saved index regulator and subtracted parameter shift. No equality
with that family or zero-preserving theorem for k_ε is supplied.

**Closest smoothed Dirichlet series.** R. B. Paris,
*The asymptotic expansion of a generalisation of the Euler-Jacobi
series*, [arXiv:1503.07329v1](https://arxiv.org/pdf/1503.07329v1),
25 March 2015. Read (1.1), §2's Cahen–Mellin representation and
contour/remainder analysis (2.1)–(2.6), pp. 1–5, and Theorem 1,
p. 8. Its series S_p(a;w)=Σ n^(−w)exp(−a n^p) is the relevant
Gaussian-damped terminology at p=2. The paper takes w real and
positive, with a→0 in |arg a|<π/2. Theorem 1 requires even positive
integers p,w and gives algebraic plus exponential expansions.
These are not estimates for an exponent with unbounded imaginary
part; their constants are not asserted uniform there. No first
Laguerre sign is stated. Use the elementary covered transform tools
for the family-specific calculation, rather than substituting the
target into this small-a theorem outside its hypotheses.

**Access and reuse limits.** DLMF's HTML math and the two arXiv PDF
text extractions were readable. Lowercase `.tex` requests failed;
the formulas and conditions were read in the HTML instead. A Paris
PDF screenshot attempt supplied no inspectable image in this tool
interface; the cited textual statements were accessible. The older
Poisson/weighted-Gaussian sources remain adequately covered by the
preceding assessment. Original de Bruijn, Newman, Pólya and Ki–Kim–Lee
proofs cited by Csordas, the DLMF books, and Paris's cited monographs
were not separately inspected and are not imported here. Unrelated
search hits and broader cutoff analogues are unread leads, not
evidence. No essential source gap remains for the stated bounded
Mellin and sign test; no general zero-preservation route is approved.

## Specialization boundary and discriminating test

The later research turn should import the scalar gamma/beta formulas
by citation, retaining the exact subtraction, full P and reflection.
It must justify endpoint terms, series/integral interchanges and
two frequency derivatives before using its Mellin expression. At
fixed ε>0, control the real projected expression and its derivatives
at large frequency. A complex modulus square or an unreflected
transform would be a different object. An exact representation
without sign information is a partial test, not the certificate.

Continue only with a concrete sign estimate at its stated scale or
an informative obstruction. To approve the certificate, cover every
real frequency for every 0<ε≤ε_0 with one ε_0>0. A positive tail
alone needs complementary-frequency control and a justified onset
bound. An analytic negative value for arbitrarily small ε stops this
certificate; one bad regulator away from zero does not settle the
quantifier. Frequencies may escape as ε decreases, so neither
L357's absolute error nor a fixed-frequency limit rules out failure.
The review computes none of these alternatives.

The decision is SPECIALIZE, not IMPORT of the global sign. Known
transforms and derivative estimates supply the inputs; their exact
application and this family's sign remain to be tested. Such an
application is appropriately a reproduction of these tools unless
a later result establishes a substantive difference beyond the
sources checked. No certified originality is claimed. This completed
source review is EXPLORATION; LITERATURE; NOVELTY_UNCHECKED, not a
mathematical advance or an informative negative sign result. It
spends and resets no mathematical exploration turn. The unchanged
TARGET and the two explicit subtargets are ready for research under
this assessment; the sole current Next action remains in PROGRESS.md.
All actual-zeta sign/exclusion ranges and the main gap are unchanged.

## Mathlib

Full regulated spectral target, gamma/beta application and
target-specific Fourier/asymptotic support: **not checked**.
The saved scalar supporting reference
[Real.tsum_exp_neg_mul_int_sq](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.tsum_exp_neg_mul_int_sq)
was previously recorded as present and is reused without a new
version check. It is not a match for this sign requirement. No full
matching theorem or library absence is asserted; a library lookup
was unnecessary for this source comparison.
