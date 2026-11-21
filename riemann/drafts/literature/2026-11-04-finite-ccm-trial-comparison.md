# Finite source-defined trial comparison — completed source review

TARGET: Assess exact source coverage for a certified comparison between L760's ground vector and the orthogonal projection of CCM's trial function k_lambda=E(h_lambda) at lambda=sqrt(13), N=120, z=i/4.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step367 reused the determinant-scope/parity/L760 assessments and the two finite-row stops, searched their trial/prolate/normalization passages, and searched exact CCM trial-coefficient and certified PSWF/Legendre-error terminology on the web. No matching validated coefficient comparison was identified in the inspected sources; this is not a novelty claim. Queries and inspected/unread distinctions are below.
SOURCE_EVIDENCE: CCM 2511.22755v1 (7.2),(7.5)-(7.12), Lemmas7.2-7.3 proof cases and section8; Connes 2602.04022v1 sections6.3-6.4/(20) and footnote20; Connes--Consani 2106.01715v1 section3/(3.3)-(3.4); Osipov--Rokhlin 1301.1707v1 Theorems1,3,10, (53)-(67), Remark9 and section5.1 truncation/inverse-iteration cases; NIST DLMF30.2.1,30.3(i),30.4(i)-(ii),30.8(i),30.16(i)-(ii). Version-specific links and scope appear below.
COMPARISON: The exact compactly supported source trial is specified, but the older parity-restricted coefficient recipe is approximate and uses a different linear constraint. Known Legendre spectral machinery supplies a finite-certificate mechanism; displayed asymptotic or machine-precision recipes do not themselves certify this cell. L759/L760 provide the ground input only.
GAP: Effective infinite-prolate mode identification, residual/tail enclosures, transport to all 241 projected coefficients and nonzero b(P_N k_lambda) remain to be established. No coefficient, boundary denominator, discrepancy or Xi limit was evaluated.
REASON: Import the source definitions and specialize the established Legendre method with explicit a posteriori errors; do not reprove prolate asymptotics or assume approximate inversion parity. The effective certificate is a necessary bounded prerequisite before the saved observable test. Its newly nominated assessment requires separate next-turn approval.
SCOPE: Exact single-cell source trial and certification prerequisites; no parameter sweep, parity symmetrization, fitted ground vector, family estimate or claimed Xi convergence.
LITERATURE_REASON: The saved new trial target had REVIEW_REQUIRED coverage; exact compact extension and the effective finite coefficient method were essential unread inputs. Ready ground-state and commutator coverage was reused.

## Intermediate purpose and bounded discriminator

Main gap: actual-Xi mixed positivity and initial signs. The spectral-triple
route also lacks quantitative actual ground/trial comparison and both
limits. L760's finite row saving is now audited but leaves the trial
input entirely unmeasured. Testing the specified source trial is a
different target from further cancellation of the inverse row.

The proposed future finite test uses v=P_N k_lambda, where P_N is the
orthogonal projection onto the exact translated orthonormal basis of
L759. The original nomination required a source review of this definition,
its domain and its coefficients. The completed review below identifies
the exact function and remaining effective certification work; it supplies
no new mathematical derivation.
Use the existing b and ell from L760. If b(v) can be enclosed away from
zero, propose to certify

    |ell(v)/b(v)-ell(xi)| / max(1,|ell(xi)|) <= 1/10.

This is only a research discriminator for one observable at i/4. A
certified larger value is informative negative evidence for this trial
in this cell; an interval straddling 1/10 is inconclusive. Failure to
enclose b(v) away from zero forbids division and requires resolving that
normalization or recording failure of this test. Do not replace v by a
fitted eigenvector to manufacture agreement. No result is asserted here.

The review should retrieve the primary definition and relevant proof
cases before wider passages, distinguish the finite construction from
asymptotic claims, and check exact/stronger results and known failures.
External large-parameter asymptotics are not automatically essential to
a fixed finite computation: identify only sources genuinely needed to
certify that computation. Reuse source material already inspected while
recognizing that its old target excluded this comparison. A citation to
trial convergence alone cannot pay the ground/trial difference.

Continue to a separately gated mathematical attempt only if the exact
source trial and a rigorous coefficient/error specification are available.
If access or scope becomes persistently blocked, park this dependent
target instead of repeating access checks. Passing the one-cell test
would still leave full-vector errors, boundary/family uniformity,
simple-even hypotheses, N and lambda limits and Xi transfer unresolved.

Essential local inputs: audited L759 and audited L760. Unresolved
assumptions for the proposed continuation: finite trial domain and
normalization, coefficient-error control and nonzero b(P_N k_lambda).
Mathlib full and supporting coverage remain unchecked, not absent.

## Mechanism comparison and routing

Three options were compared without doing new mathematics: further
commutator cancellation still faces the retained rR and uniform c/boundary
cost; a Galerkin boundary-trace convergence argument requires new analytic
domain/trace coverage beyond lowest-energy convergence; the actual finite
trial projection directly tests an independent missing input with the
already audited ground enclosure. Select the third. The first two are
neither disproved nor preapproved. The scoped stop is recorded in
`ATTEMPTS/2026-11-04-finite-row-saving-unpaid-trial-gap.md`.

At nomination the requested task was literature_comparison, standard/high.
The completed review below neither certifies novelty nor derives a trial
estimate. Its new mathematical continuation is subject to separate
supervisor approval; current routing is recorded only in PROGRESS.md.

## Completed source extraction — step367

The preceding nomination records the question at entry, not the current
routing decision. No trial calculation was performed in this review.

**Exact function.** [CCM, v1](https://arxiv.org/html/2511.22755v1#S7),
(7.2),(7.5)-(7.6), specifies

    PW_lambda = -d/dx ((lambda^2-x^2)d/dx) + (2pi lambda x)^2,
    E(f)(u) = sqrt(u) sum_(r>=1) f(ru),
    k_lambda = E(h_lambda)|_[lambda^-1,lambda],

where h_lambda is the nonzero, zero-integral linear combination of
prolate modes 0 and 4, up to a common scalar. Lemma7.2's proof uses
compressed Fourier eigenfunctions, not exact full-line self-duality.
Its unspecified asymptotic constants do not give finite coefficient
intervals. Lemma7.3 and section8 concern, respectively, trial-transform
convergence and the unresolved ground/trial comparison; neither supplies
the requested finite error. Their external asymptotic inputs are unused.

[Connes, 2602.04022v1](https://arxiv.org/html/2602.04022v1#S6.SS3),
sections6.3-6.4, makes the compact extension explicit: angular prolate
functions live on [-lambda,lambda] and are extended by zero. Formula(20)
and footnote20 specify the same zero-integral trial and finite sum, with
integer indices at most lambda^2. The integral is the additive integral
of h_lambda, not an integral of k_lambda against du/u. Scaling conventions
for the two modes must be retained when forming the combination. No
source guarantees nonzero b(P_N k_lambda). The selected projected
observable requires only the L2 trial and its finite projection; no
claim that k_lambda belongs to the unbounded Weil operator domain is
needed or approved. Boundary evaluation is that of the projected vector.

**A relevant failed shortcut.** [Connes--Consani, 2106.01715v1](https://arxiv.org/html/2106.01715v1#S3),
section3, (3.3) and its domain paragraph, specifies the closed positive
prolate differential operator. The paragraph before(3.4) explicitly
treats inversion parity as approximate. Its phi construction vanishes
at zero, whereas the saved CCM trial imposes zero integral. Formula(3.4)
therefore cannot be imported as an exact coefficient formula for this
target. In particular, do not discard the other inversion-parity
components, replace the trial by its even part, or impose both linear
constraints. The numerical Gram--Schmidt comparison in that section
supplies neither an interval error nor the requested boundary ratio.

**A usable exact spectral representation.** [Osipov--Rokhlin,
1301.1707v1](https://arxiv.org/html/1301.1707v1#S3.SS2), Theorems1,3,10
and(53)-(67), gives normalized Legendre functions
Pbar_j=sqrt(j+1/2)P_j and the infinite symmetric matrix

    M_jj = j(j+1) + c^2 [2j(j+1)-1]/[(2j+3)(2j-1)],
    M_(j,j+2) = M_(j+2,j)
             = c^2 (j+1)(j+2)/[(2j+3)sqrt((2j+1)(2j+5))].

For c>0 the unit L2 prolate coefficients satisfy the stated infinite
eigenproblem; even degrees use the even block. Theorem3 characterizes
the increasing simple differential eigenvalues by continuous solutions
on [-1,1]. The relevant parameter here is c=2pi lambda^2, not 2pi lambda.
Remark9 and section5.1 give candidate-generation/truncation methods;
their empirical cutoff and machine-precision stopping rule are not a
tail or rounding certificate. A future effective residual/gap enclosure
must include the omitted block and mode identification. This is the
specific implementation difference, not a proposed new PSWF theorem.

[NIST DLMF30.2.1](https://dlmf.nist.gov/30.2.E1),
[30.3(i)](https://dlmf.nist.gov/30.3.i),
[30.4(i)-(ii)](https://dlmf.nist.gov/30.4),
[30.8(i)](https://dlmf.nist.gov/30.8.i) and
[30.16](https://dlmf.nist.gov/30.16) were read for equation, bounded-endpoint
characterization, normalization, parity, recurrence and computation.
DLMF's spectral parameter includes a constant shift relative to the
positive differential operator above; do not identify those eigenvalues
by name alone. Its asymptotic error(30.16.4) has no displayed effective
constant. Neither it nor recurrence recessiveness alone encloses a
selected finite truncation. The residual-and-tail continuation below
does not require these asymptotic estimates.

## Search record and decision

Queries included `"Zeta Spectral Triples" "trial" prolate coefficients`,
`"2511.22755" "h_" prolate comparison`,
`prolate spheroidal wave functions rigorous computation error bounds Legendre expansion eigenfunctions finite Fourier certified`,
`"prolate" "a posteriori" eigenfunction error Legendre`,
`"On the evaluation of prolate spheroidal wave functions" theorem 10 error`
and `"prolate" "certified" eigenfunctions computation error bounds`.
Exact local scope/parity/L760 assessments and the direct-frequency and
unpaid-trial stops were checked before the primary sources. Their
ground-state coverage is reused; no entry or row calculation was replayed.

Search hits for numerical reproductions are not source certificates.
The Yale tr1450 PDF lead failed after redirection and was not read;
uniform PSWF asymptotic papers, the source behind Osipov--Rokhlin's
Remark9, and a certified holonomic-function paper remain unread leads.
They are not essential to a residual-and-tail proof using the exact
spectral representation, and no conclusion here imports their estimates.
Primary HTML was accessible; shell DNS failure is not a source blocker.

SPECIALIZE means the exact function and established spectral mechanism
are covered, not that its coefficients or the 1/10 test have passed.
The necessary reworking is an effective certificate: infinite-mode
labels and errors, the zero-integral combination, and transport to all
projected coefficients. The planned specification and bounded failure
test are in
`drafts/literature/2026-11-04-ccm-trial-effective-certificate.md`.
This newly nominated mathematical prerequisite needs separate approval
next turn. No full matching finite comparison theorem was verified;
no originality conclusion follows. Mathlib full and supporting coverage
remain unchecked, not absent. PROOF.md and DAG.md are unchanged because
the mathematical argument is unchanged.
