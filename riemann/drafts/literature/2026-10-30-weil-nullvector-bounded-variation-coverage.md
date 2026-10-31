# Fixed-model nullvector variation: completed source comparison

TARGET: Assess literature coverage for bounded variation of the zero extension of L516's nullvector under L520's fixed-model hypotheses, and for using it to represent each prime contribution to S(u) by an absolutely convergent Stieltjes correlation with the full signed measure retained.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched logarithmic-Laplacian bounded variation/BV/W1,1 eigenfunctions, zero-order nonlocal bounded variation, geometric-stable gradient estimates, and BV correlation/difference-quotient convergence; scoped local searches found no matching global estimate or duplicate. Reused the prime-shift regularity exclusions; inspected the new primary sources listed below. No novelty is inferred.
SOURCE_EVIDENCE: Kulczycki–Ryznar arXiv:1307.7158v1 Theorem 1.1, assumptions (A), Definition 2.1, Corollary 1.8, Proposition 6.7 proof and Example 7.2; Galerne (2016), doi:10.1017/apr.2016.60, Section 2 Lemma 1/Theorem 1 and proofs pp.951–953; Jarohs–Kassmann–Weth arXiv:2311.15337v2 Theorem 1.5, A3_2, Theorem 5.1 and growth/oscillation proof cases; paper 67 v1 Sections 3.2–3.3 and 7, with L513/L515/L516/L520.
COMPARISON: The geometric-stable gradient theorem requires nonnegative harmonic data; the signed translated equation is not covered. The weakly singular theorem assumes BV of its kernel and concludes continuity of its solution, not BV of that solution. Galerne supplies a precise global L1 difference-quotient criterion and weak-* derivative measures; its finite-variation premise remains missing here. Conditional correlation specialization is accessible once that premise is proved.
GAP: Establish finite global translation variation of f=Eu for the complete fixed model, including endpoints and all generated images; then check the moving continuous tests and shift/dilation normalization in each prime correlation. No global BV bound, individual Stieltjes formula, arithmetic sign or eigenvalue-relative saving is established.
REASON: Essential theorem comparison is complete; park automatic harmonic-gradient and kernel-BV-to-solution-BV imports. A direct L1 translation-difference closure is a concrete mathematical test beyond the inspected sources, subject to separate approval of its new continuation. This turn is source review only.

LITERATURE_REASON: The proposed target changes from a local two-sided
asymptotic to global variation and individual correlation limits. The
earlier regularity comparison did not inspect the hypotheses needed for
this use; the ready cusp target itself needs no further literature.

Keep exactly L520's fixed conditional setup: 0<a<A, ell=2a>log(2),
the real normalized nullvector of L516's complete model, nonzero left
trace, and exclusion of the direct reflected-endpoint collision at
log(2). Retain c=log(2pi), nu_rho, all prime-power atoms including
cutoff equality, and the full signed pole. Do not assume smoothness or
separation of other generated images, a quantitative trace-error rate,
H1 regularity, a spectral gap or trace vanishing. L513/L515/L516/L520
are the essential local inputs; L520's conclusion is local evidence,
not a theorem about total variation. No cross-notebook input is planned.

The main gap remains actual-Xi all-degree positivity and the signed
bound in L516. Finite variation, if available with adequate control of
the dilation limit, could expose the individual signed prime terms to
estimation instead of using only their combined limit. Even this would
not establish the sign or eigenvalue-relative bound, nullvector
existence, source realization, branch rates, collars or Xi transfer.

## Primary hypotheses and actual readings

1. [Kulczycki–Ryznar, *Gradient estimates of harmonic functions and
   transition densities for Levy processes*, arXiv:1307.7158v1,
   26 July 2013](https://arxiv.org/pdf/1307.7158v1), pp.1–2, 6,
   30–32. Theorem 1.1 assumes a pure-jump isotropic process with
   infinite radial Levy density, the monotonicity/absolute-continuity
   and comparison conditions (H1), and scale-invariant Harnack (H2).
   Its function is nonnegative on the whole space and harmonic in D
   in Definition 2.1's exit-expectation sense. It bounds its gradient
   by c f(x)/(dist(x, boundary D) wedge 1). Example 7.2 includes
   log(1+lambda^(beta/2)), 0<beta<=2, through (A3), including
   one dimension. Slowing the process leaves harmonicity unchanged.
   Proposition 6.7's proof obtains its forcing from exterior harmonic
   data and uses the local linear increment estimate (42) before
   differentiating the Green integral. L516 has an interior signed
   forcing, not that representation. Corollary 1.8 is off diagonal;
   it supplies no global integrable gradient for this forcing. Thus
   neither dimension nor transience is the present mismatch; it is
   the harmonic-data hypothesis and missing global estimate.

2. [Galerne, *Random fields of bounded variation and computation of
   their variation intensity*, Adv. Appl. Probab. **48** (2016),
   947–971](https://doi.org/10.1017/apr.2016.60), Section 2,
   Lemma 1 and Theorem 1, pp.951–953, including their complete proofs.
   This section is deterministic. For an open U, direction e and
   f in L1(U), finite directional variation is equivalent to finite
   liminf of the L1 norms of translation difference quotients on
   U eroded by [0,he]. When finite, those signed measures converge
   weak-* to D_e f, and their total variations tend to |D_e f|(U).
   Lemma 1 bounds every quotient norm by this variation. Taking
   U=R and e=1 gives exactly the needed global criterion; L515's
   bounded compact support supplies L1, not the finite liminf.
   The proof uses smooth approximation, distributional testing and
   measure compactness. No random-field, stationarity or positivity
   assumption is needed for this theorem. This is a standard input
   to cite, not a theorem to reprove as new mathematics.

3. [Jarohs–Kassmann–Weth, *Continuity of solutions to equations with
   weakly singular nonlocal operators*, arXiv:2311.15337v2,
   2 March 2025](https://arxiv.org/html/2311.15337v2), Theorem 1.5,
   conditions K/K_as/A1_gamma/A2/A3_1–A3_2, and Theorem 5.1.
   The operator kernel is nonnegative, comparable to j, with controlled
   antisymmetric part. Its density satisfies the gamma-moment condition,
   0<gamma<1, infinite mass, and annular comparability or the stated
   annular BV estimate. Data f,W are locally bounded and the weak
   solution is globally bounded (or has the stated bounded tail).
   The conclusion is continuity with an interior modulus. The BV
   condition A3_2 concerns j, not the solution. The growth proof's
   Case 2 uses variation to control translated annular kernels;
   Theorem 5.1 concludes via oscillation decay (80)–(86). These proof
   cases contain no global L1 difference-quotient estimate for u.
   No specialization of this theorem is needed to duplicate L515's
   existing continuity conclusion.

The full primary PDF for Galerne is linked from the publisher DOI;
the exact accessed URL is retained in the working source notes.
The inaccessible author-hosted gradient PDF was replaced by arXiv v1;
there is no persistent source blocker. The served v2 HTML for the
weakly singular paper has a later displayed manuscript date; the
version identifier and inspected theorem numbers above fix the text
used. No claim of auditing the eventual journal version is made.

## Correlation applicability, without performing the specialization

Galerne's weak-* statement tests fixed C0 functions, with a uniform
total-variation bound conditional on BV. L516 instead pairs a shift
difference with u_r. A later application must rewrite each term as
a translation-difference measure paired with the correctly shifted
continuous factor, and check its uniform convergence as r decreases
to one. L515's compact continuous representative is relevant to this
check; L2 convergence alone does not justify testing a singular
derivative measure. It must also track shift/(r-1), signs, both
translations and every cutoff/equality atom. Under BV these are
finite-measure/continuous-test operations rather than an H1 argument.
No individual prime formula is asserted or derived here. In particular
a conditional absolutely convergent Stieltjes integral would not give
the sign, branch uniformity or eigenvalue-relative bound in L516 (6).

## Comparison, duplicates and bounded next test

Reuse the inspected theorem comparisons in
[prime-shift-cusp coverage](2026-10-30-weil-prime-shift-cusp-coverage.md)
and its direct-regularity stop. Smooth-forcing assumptions and the
transient whole-space Green restriction remain in force. L520 proves
a local profile and logarithmic remainder, not variation of the
remainder. The local inverse kernel and commutator formulas in L520
(4)–(14), and L513's half-line potential, are available inputs; no
global estimate for their combination has been recorded.

Among direct harmonic-gradient import, smooth-forcing bootstrap and
global L1 finite differences, only the last presently has a concrete
test without an unavailable theorem hypothesis. Seek a bound on
Q_h=||f(.+h)-f||_1/h uniform for small positive h. A potential closure
Q_h<=theta Q_h+C must have theta<1 and C independent of h, with
endpoint terms controlled and all atomic translates retained. This
is a proposed threshold, not an established inequality. An interior
estimate with constants diverging as the cutoff approaches the
endpoints does not suffice. Nor may one differentiate a trace
little-o or replace the signed model by a positive convolution.

Continue only if such global closure or another finite-variation
estimate is obtained. Otherwise preserve the exact uncontrolled
boundary/translate term and park that implementation; this would
not disprove global BV, the nullvector hypothesis, L520 or RH.
The next test has a separate assessment and requires separate
approval before mathematical work. Mathlib matching is not checked;
unknown coverage is not absence. No cross-notebook input is used.
