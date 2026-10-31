# Signed side-gap flux: completed conditional-bound source review

TARGET: Review source coverage for the one-sided gap-flux bound Q_T<=C_R a M_T under L503's unchanged signed rectangle hypotheses, with C_R independent of T and f_T.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-class, positive-real-part rectangle, signed boundary and one-sided Paley--Wiener searches completed below; reuse 2026-10-30-signed-rectangle-absolute-cost-review.md for unconditional norm/extremal comparisons. No matching theorem was identified; search failure does not establish novelty.
SOURCE_EVIDENCE: Axler--Bourdon--Ramey, Harmonic Function Theory, second edition, author PDF 17 July 2020, https://axler.net/HFT.pdf#page=124, Theorem 6.13(a)/Corollary 6.15, printed pp. 119--120; Brevig--Chirre--Ortega-Cerda--Seip, https://arxiv.org/pdf/2210.13922v2, (3.3), Theorem 3.6, Corollary 3.9 and Theorem 3.10, printed pp. 12--15. Statements, essential proof cases and endpoint qualifications inspected; prior Kovrijkine v1 Theorem 1 and ABR Green identity coverage reused.
COMPARISON: Positive Poisson representation requires positivity throughout its domain and supplies no continuation through this signed gap. Point-evaluation duality and its approximate certificate do not incorporate the rectangle inequalities or weighted cost; at p=1 the residual is a potentially unbounded distributional functional. Neither gives the proposed uniform O_R(a M_T) bound. L503's unconditional exponential-gap estimate remains the available local bound.
GAP: Construct a positivity-supported dual functional for this exact rectangle whose real-axis residual has a genuine norm O_R(a), or refute the proposed estimate within the exact smooth Fourier class. Such a certificate, its uniform constants and continuum validity are not provided by the inspected sources.
REASON: The strengthened one-sided estimate changes the target beyond prior coverage. The completed review identifies an uncovered quantitative dual-certificate test and an essential L1 endpoint pitfall; it does not settle the flux bound, certify originality or repeat the stopped unconditional closure.
SCOPE: Completed literature comparison for exactly the conditional bound below. The separately nominated dual-functional attempt has its own assessment and needs separate supervisor approval before mathematics; other geometries, detector construction and arithmetic transfer are outside scope.

## Exact family and proposed estimate

Fix R>0 independently of T. Use L=log T, a=log L/pi, b=a/4,
B=L/(4pi), lambda=pi/(2a), sigma=2pi R and
K(x)=1-(sin(pi x)/(pi x))^2 with K(0)=0. Let f_T be even entire,
real on R, with inverse Fourier representation

    f_T(z)=integral phi_T(v) exp(2pi i v z) dv,
    phi_T in C_c^infinity(R), supp phi_T subset [-R,R],
    Re f_T(x+iy)>=1 for |x|<=a and b<|y|<B.

There is no sign restriction elsewhere or uniform Fourier-derivative
bound. Define

    M_T=integral_R |f_T(x)| K(x) dx,
    Q_T=-integral_0^b exp(-lambda y)
           [Re f_T(a+iy)+Re f_T(-a+iy)] dy.

The proposed estimate is Q_T<=C_R a M_T for all sufficiently large T
and all such f_T, with C_R finite and independent of both T and f_T.
It is one-sided: no corresponding estimate for |Q_T| is assumed.
The constants in L503's necessary lower bound are in its canonical file.
Together with that lower bound the proposed estimate would force a
positive cost lower bound for fixed R. This is a prospective use, not
an established theorem or a proof of this estimate.

## Required comparison and bounded continuation test

Compare primary results on band-limited analytic continuation with
positive real part on a finite rectangle and on signed boundary norm
estimates. Retrieve exact hypotheses and essential proof cases before
deciding applicability. The general signed Fourier estimate already
used in L503 and full-strip Harnack do not cover the new difference.
An unweighted theorem must still address the K zero and uniformity in
the moving geometry; the existing A_R conversion may be reused.

The first mathematical input, if a later attempt is approved, is L503
(currently unaudited). L502 is only contrast. No zero-free estimate,
actual-zero sign, simplicity, spacing or cross-notebook result is an
input. Full Mathlib coverage remains unchecked. The main unresolved
actual-Xi signs, negative zero contributions and moving-test/height
transfer are independent even if this geometric target is settled.

The original nomination required a separate assessment identifying
adequate theorem coverage or a specific uncovered mechanism. Seek the
displayed O_R(a M_T) threshold; merely recovering L503's exponential
gap norm is not new evidence. If a theorem or admissible counterexample
settles this estimate, record its exact scope. No such result, source
import, novelty or counterexample is claimed. The review completed below
identifies a mechanism for a later bounded attempt, not its success.

## Completed source review: 2026-10-30

LITERATURE_REASON: The new conditional O_R(a M_T) estimate was not covered
by the ready first-mode assessment; reviewing the changed sign-sensitive
hypothesis and the L1 dual endpoint was essential before further mathematics.

The local duplicate/failure check read L503 in full, the prior signed
rectangle source comparison, its first-mode assessment, the first-mode
absolute-norm stop, and its dated history. No prior gap-flux certificate
or comparison with Theorem 3.10 was found in those scoped files. L503
remains unaudited. L502's full-strip mechanism is contrast only; no
other local lemma or cross-notebook theorem is imported.

Search queries included `"entire functions" "positive real part"
rectangle exponential type`, `"bandlimited" "positivity" "analytic
continuation" inequalities`, `"harmonic" "negative part" "rectangle"
boundary estimates analytic functions`, `"entire functions" "positive
real part" "strip" inequality`, `"bandlimited" "one-sided" "complex"`,
`"positive real part" "rectangle" "inequality" entire functions`,
`"bandlimited" "positive" "harmonic" inequality`, `"one-sided"
"Paley-Wiener" "extremal"`, `"entire" "positive real part" "rectangle"
"norm"`, and `"harmonic functions" "signed" "boundary" "bandlimited"`.
The exact conjunction searches gave unrelated or no matching results.
Search snippets, aggregator records and the surfaced QRH catalogue were
not mathematical evidence and were not followed as dependencies.

### Positive-harmonic representation: domain restriction

ABR, [primary PDF](https://axler.net/HFT.pdf#page=124), second edition,
17 July 2020, Theorem 6.13(a) and Corollary 6.15, printed pp. 119--120:
positive harmonic functions on the unit ball are precisely Poisson
integrals of unique finite positive boundary measures. Read the measure
case's weak-star subsequence/Poisson-limit argument and the corollary's
mean-value mass bound and positivity passage. Its sign hypothesis holds
throughout the ball. Applying it inside the known-positive rectangle
does not cover the exterior side-gap where Q is evaluated; no positive
measure representation across that gap or rectangle norm estimate is
imported. The earlier disk Harnack and Green comparisons remain adequate.

### Paley--Wiener duality: the endpoint issue

Brevig, Chirre, Ortega-Cerda and Seip, *Point evaluation in Paley--Wiener
spaces*, [v2, 1 November 2022](https://arxiv.org/pdf/2210.13922v2#page=12),
(3.3), Theorem 3.6 and its variational/Hahn--Banach proofs, Corollary 3.9
and Theorem 3.10, printed pp. 12--15, were inspected. Theorem 3.6 is the
unweighted origin-evaluation extremizer characterization for 1<=p<infinity;
its formula uses Phi=|varphi|^(p-2)varphi/||varphi||_p^p. The alternate
proof specifically treats the p=1 zero set. Corollary 3.9 expresses the
Fourier matching in distributions. Theorem 3.10 bounds the evaluation
constant using a candidate normalized by varphi(0)=1 and the dual
residual norm. Its proof tests Schwartz band-limited functions, then uses
Holder and density. At p=1 the residual is explicitly a possibly
unbounded functional on Schwartz L1 tests, rather than an automatically
bounded convolution. Thus formal Fourier matching or sampled residuals
cannot certify a finite norm. This is comparison, not an application to
Q: the source has no rectangle constraint or uniform moving-geometry
bound. No source theorem is reproved.

The new comparison concerns the rigorous residual norm; it does not
infer a particular certificate, separation equivalence or counterexample.
The source uses angular Fourier support [-pi,pi]; a later application
must reconcile this with support [-R,R] in the notebook's 2pi convention.
L503's elementary N<=A_R M conversion may be reused with its qualification
or replayed; an unweighted certificate need not divide by K at its zero.

### Other leads and bounded decision

Clunie--Rahman--Walker, *On Entire Functions of Exponential Type Bounded
on the Real Axis*, JLMS 61 (2000), 163--176,
[publisher DOI](https://doi.org/10.1112/S0024610799008236), surfaced;
only its abstract was available in the retrieved publisher result. No
theorem from it is claimed read. Sign-uncertainty and real-axis
Beurling--Selberg leads remain outside the inspected rectangle class;
their abstracts are not evidence for this flux inequality. These are
unread leads, not missing essential premises of the nominated elementary
duality test. There is no persistent source blocker for that test.

Decision EXPLORE means a bounded search did not establish coverage of
the exact bound. The next proposed mathematical test seeks a genuine
bounded real-axis representation after using positivity only on the
stated rectangle. It must control the complete signed Q, constants
independent of T and f, the smooth Fourier class and the L1 endpoint.
Continue this mechanism only with a uniform O_R(a) norm certificate or
a sharper rigorously quantified obstruction. An admissible family with
Q/(a M) unbounded would refute the proposed bound; a failed certificate
ansatz would refute only that ansatz. Repeating q_R(L) or a formal or
numerically sampled certificate supplies neither outcome. Save any
residual and stop the ansatz after one bounded attempt without new evidence.

This is EXPLORATION in literature, not a mathematical advance or a
negative resolution of the estimate. No lemma, mathematical script,
candidate solution or Mathlib matching theorem was produced. Actual-Xi
signs, negative zero contributions and every arithmetic/height transfer
remain independent. The proposed continuation is recorded in
[its own assessment](2026-10-30-signed-gap-flux-dual-test.md); its new
ready coverage requires separate supervisor approval before invocation.
