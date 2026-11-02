# Screw-function signed remainder: completed bounded source comparison

TARGET: Compare Suzuki's screw-function criterion with the local sign gap and determine whether it supplies an unconditional finite-interval remainder bound after subtracting verified real zeros.
CHECKED: 2026-11-01
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Searched Suzuki screw functions/RH/finite intervals/remainders, exact-title and verified-zero tail terminology; checked specific local canonical-system, post-C499e, Weil-support, nodal and pole-resolvent comparisons. Retrieved the primary Suzuki sources below. A directly relevant recent scalar-tail preprint was located, but its theorem text could not be retrieved.
SOURCE_EVIDENCE: Suzuki 2206.03682v4 PDF (internal date 31 May 2023), Theorems 1.1–1.3, 1.5–1.7, (1.9)–(1.11), Sections 2.2, 3.1–3.5, 4.3 including the full small-window/finite-codimension proof cases, and 7.2; Suzuki 2606.09096v3 (23 September 2026), Theorems 1.1–1.5, (1.3)–(1.9), (2.2)–(2.5), Section 5.1 and Sections 8.1–8.5. Mittermeier Zenodo 23544568 v2 landing page only; exact tail theorem and certificate remain unread.
COMPARISON: Suzuki's zero expansion is unconditional, but its positive spectral-square interpretation requires real zeros. Small-window positivity, positivity on a restricted finite-codimension space, and lower boundedness on each fixed window are genuine weaker statements; none is the requested estimate after removing a specified verified-zero set. A scalar-tail bound would still need comparison with the full quadratic form.
GAP: No inspected theorem gives the desired signed subtracted-form bound with specified test space, explicit window dependence and sufficient positivity threshold. The newer scalar-tail report cannot be evaluated from landing-page claims; its exact theorem/proof cases are essential missing coverage for that particular mechanism. No dependent mathematical target is ready.
REASON: Close the criterion-only positivity/realization implementation on source-scope evidence; park the inaccessible quantitative scalar-tail lead without claiming it false or absent. Repeated access attempts are not a continuation. Move to a separate signed arithmetic correlation screen; no progress beyond the checked literature or RH resolution is asserted.
SCOPE: Literature comparison only. No new mathematical result, application, lemma, script, zero-free improvement, certificate replay or source-proof correctness audit is approved.

## Completed comparison and source evidence

The original nomination is preserved below. Its main gap and discriminating
test have not changed: an unconditional signed estimate for the actual
subtracted form could support a later arithmetic sign test, leaving global
control and transfer to the mixed signs open. An RH-equivalent global
inequality, real-zero-only measure or finite positive matrix does not
meet that test. The inspected Suzuki sources do not supply that estimate;
the directly relevant quantitative report remains inaccessible at theorem
level. This is not a general impossibility result for screw functions.

Masatoshi Suzuki, *Aspects of the screw function corresponding to the
Riemann zeta-function*, J. London Math. Soc. 108 (2023), 1448–1487,
[DOI 10.1112/jlms.12785](https://doi.org/10.1112/jlms.12785),
controlling version [2206.03682v4 PDF](https://arxiv.org/pdf/2206.03682v4).
The arXiv wrapper fixes v4 to May 30, 2023 and the PDF internal date is
May 31, 2023. The [HTML rendering](https://arxiv.org/html/2206.03682v4)
instead displays an inconsistent August 2026 date. Numbering here refers
to the PDF; HTML supplied readable proof formulas, with normalization,
zero series and the small-window statement checked against PDF text.
No inference of a new version is made from that date anomaly.

- Theorem 1.1, printed pp.1–2, uses the standard completion with factor
  1/2. Psi is real, continuous, zero at zero and extended evenly.
  For Im(z)>1/2 its one-sided transform is
  -z^(-2)(xi'/xi)(1/2-iz). Its zero representation is
  Psi(t)=sum_gamma (1-cos(gamma t))/gamma^2 for t>=0, with **all**
  zeros of xi(1/2-iz) counted with multiplicity, including complex gamma.
  Section 2.2's complete proof uses Hadamard factorization, the vanishing
  central logarithmic derivative, absolute convergence, |Im(gamma)|<=1/2,
  the gamma to -gamma symmetry and uniqueness of the transform. It
  assumes no RH. Theorem 1.1(3) is an absolute growth estimate, not a
  favorable signed remainder bound.
- Equations (1.4), (1.8)–(1.11), printed pp.2–3, define g=-Psi and
  G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0). Equation (1.9) is the zero series
  sum_gamma (exp(i gamma t)-1)(exp(-i gamma u)-1)/gamma^2.
  The Hermitian form integrates G_g(t,u) phi(u) conjugate(phi(t))
  on [-a,a]^2. The criterion's space mathfrak C_0(a) consists of smooth
  compactly supported functions in that interval with integral zero,
  not just finitely many nodes. These statements remove no zeros.
- Theorems 1.2–1.3 require positivity for **every** finite a to obtain
  RH. Section 3.1, printed pp.9–10, first writes the general bilinear
  spectral formula (3.1), then assumes gamma real for the modulus-square
  expression (3.2). Using that expression for unknown complex zeros
  would change its hypotheses. Proposition 3.1, (3.8), identifies the
  form on derivatives of smooth supported functions with Weil's form
  by integration by parts; it supplies no new sign.
- Theorem 1.7 is Psi(t)>=0 for every real t iff RH. Section 7.2's
  converse uses the Laplace-transform theorem for nonnegative functions
  and absence of real zeta zeros on the relevant half-line. It does
  not prove an independent global sign. Finite ranges have different
  quantifiers. No scalar-to-full-form inference is made here.
- Theorem 4.2, printed pp.12–15, gives unconditional positivity on
  L2(-a,a) for sufficiently small a, without a numerical a_0. Read the
  complete proof: pole/prime/archimedean splitting (4.5)–(4.8), shifted
  Fourier estimates, low-frequency loss (4.11) and small-a absorption.
  This is not a verified-zero subtraction. Theorem 4.1's reported
  numerical minimum is not imported as a certified computation.
- Theorem 4.3, printed pp.15–16: for a_0>0 and mu>0, there exists N
  with form >= mu integral_R |Phi_1(phi,z)|^2 dz for 0<a<=a_0,
  restricted to mathfrak K_(N,0)(a). Here
  Phi_1=(hat(phi)(z)-hat(phi)(0))/z, hat(phi)(0)=0 and its primitive
  belongs to K_N(a), whose periodic Fourier coefficients |n|<=N
  vanish. Read (4.1), (4.12)–(4.13) and the complete Fourier-tail proof.
  Fourier-mode restrictions on test functions differ from subtracting
  verified zeros. N is existential; the low modes and their coupling
  are not certified positive by this result.

These are precisely cited source statements, not an independent audit of
every printed constant or estimate. In particular, later use of the
coercivity proofs must justify quadratic-form domination rather than
infer it from pointwise kernel inequalities. No reproof or quantitative
specialization was carried out.

Suzuki, *Weil's quadratic form via the screw function*,
[2606.09096v3](https://arxiv.org/html/2606.09096v3), 23 September 2026,
Sections 1.2, 2.2–2.3, 5.1 and 8, omits the factor 1/2 in xi; its
logarithmic derivative and explicit g normalization are unaffected.
G_a is mean-zero compressed convolution by g. Theorem 1.1 identifies
the Friedrichs extension of D*G_a D with the localized Weil operator
A_a, where D=i d/dx has Dirichlet domain H_0^1(-a,a). Theorems 1.3
and 1.4 give continuity of the bottom lambda_a and a positive, simple,
even ground state for sufficiently small a, with a logarithmic small-a
asymptotic. Section 5.1 uses the prime-free small-a regime and a bounded
smooth remainder, not arbitrary-window signed control.

Lower boundedness does not assert lambda_a>=0. Theorem 1.5 constructs
real-zero characteristic functions in the shifted norm
Q_W-lambda||.||_2^2 with lambda<lambda_a. That shift does not prove
lambda_a>=0. Sections 8.1–8.5 distinguish A_a, compact G_a and the
inverse Neumann Laplacian; the zero generalized eigenvalue is exceptional.
The formal Fredholm step (8.4)–(8.5) explicitly leaves domain issues
aside. None is a verified-zero signed remainder theorem. These source
results have not been independently audited or applied locally.

## Quantitative report and exact access blocker

Rainer Andreas Mittermeier, *A Zero-Side Positivity Certificate for
Suzuki's Screw Function through X=2·10^29: Window Means and One-Sided
Criteria*, [Zenodo 23544568 v2](https://zenodo.org/records/23544568),
22 October 2026. The v1 search hit led to this newer record. Its landing
page claims scalar zero-tail estimates using finite verified height,
explicit counts/density and 3000 certified zeros. It reports finite
scalar/window/Cesaro ranges and explicitly leaves the infinite tail
open. These are **landing-page claims only** here: no constants,
ranges, certificate or theorem are accepted as inputs.

The file `261021_Mittermeier_RH_Zero_Side_Certificate_Companion_v2.pdf`
failed web retrieval with a Unicode decoding error at the download
link; direct file and record/file-content API paths were inaccessible.
The v1 PDF also failed. Terminal arXiv downloads failed DNS resolution;
web arXiv access succeeded. No credentials or keys were used. Stop
repeating those access paths. Exact tail hypotheses and any full-form
conclusion remain unknown; newly accessible primary text could reopen
this lead. This is a source blocker, not evidence of a mathematical
impossibility or of novelty.

## Duplicate check and disposition

The post-C499e and direct canonical-system screens explicitly left screw
functions unread, so this is new source coverage. L618 is a closed
contrast. The specific Weil-support-enlargement assessment already
checks Zhu 2608.24827v2 and its full-complement/parity/retraction scope;
a search hit was checked against the primary abstract but no new
support theorem was imported. Nodal/modulus and rank-two pole-resolvent
comparisons retain their missing full-form sign/arithmetic numerator.
Renaming those mechanisms would add no input.

L018/L466 were nominal possible inputs only: no local applicability
argument or new verified-height conclusion is made, and no local lemma
proof is used. No simplicity, removed endpoint, cross-notebook input,
canonical lemma, script, DAG edge or proof assembly change occurs.

Close the criterion-only implementation and park the inaccessible
scalar-tail mechanism. The separate next nomination screens a signed
arithmetic correlation input against the L575 fixed-square little-o
stop; it is not approved mathematics. No ready creative target has
emerged because an independent actual-Xi signed estimate is missing.

## Original unread nomination (historical; superseded above)

## Intended comparison and discriminating test

The main gap remains actual-Xi all-degree mixed signs at unbounded
heights, including the initial degrees below the logarithmic tails.
A possible intermediate input is an unconditional lower bound for the
remainder of the screw-function quadratic form on a specified finite
interval, after subtracting contributions of finitely many verified
real zeros. This is a question for source assessment, not a proposed
proved theorem or a statement that such a lower bound is available.

First locate primary Suzuki screw-function statements and identify the
exact object, test-function hypotheses and zero representation. Read
the relevant theorem hypotheses and essential proof cases before larger
extracts. Determine precisely what positivity is equivalent to RH and
whether any independent remainder estimate is actually proved. Keep
finite verified zeros, multiplicities, endpoints and off-line zero
contributions distinct; neither a finite numerical matrix nor an
all-positive spectral representation premised on RH is the needed input.

Reuse the earlier canonical-system comparison and its stops. Search
specific notebook paths for screw-function terminology and the resulting
exact theorem names before loading detailed proofs. Nominal local inputs
for a later applicability comparison are L018 (completion), L466
(qualified verified-height signs and its source), and L618 (the closed
compact-norm diagnostic, as a contrast, not a mathematical premise).
Their full hypotheses must be read if used. No cross-notebook input is
proposed. No source result has been imported by this nomination.

Continue toward a separate research target only if the sources identify
an independently justified signed estimate with explicit hypotheses,
interval dependence and an actual-Xi use beyond finite verified signs.
Record its precise threshold and the remaining transfer gap. If only
RH-conditional/global-equivalent positivity or already screened
realization assumptions are available, close this lead with that exact
source evidence; do not repackage the criterion as a new lemma. A
quantitative estimate may leave other independent gaps unresolved.

This source comparison has not earned proof_attempt/creative routing.
If it identifies a materially different mechanism and a bounded central
sign test, nominate that later target with its own coverage and precise
escalation. Otherwise retain the source obstruction and choose a different
independently testable mechanism. No exploration counter is reset here.

## Mathlib

Matching Mathlib coverage has not been checked and remains unknown.
Supporting zeta APIs and L618's informal audit do not establish the
screw criterion or the proposed subtracted-remainder estimate. The
primary-source comparison above is complete to its stated access limit,
but no formalization or source-proof correctness audit is claimed.
