# Spectral-derivative HCIZ lift: completed source gate

TARGET: Test a Vandermonde-retaining spectral-derivative HCIZ lift of L629's c=(0,1) functional at actual N=2, requiring exact recovery of L631's full degree-eight cross polynomial before an all-N extension.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the inspected scalar HCIZ/HG/Andreief assessment; a bounded differential-insertion search found Miglioli's polynomial radial differentiation identity and Eynard's pair-correlator formula. Exact queries, inspected cases and local comparisons are below; no matching full-tail arithmetic identity or half-margin theorem was identified, without an exhaustive-absence or novelty claim.
SOURCE_EVIDENCE: Reused McSwiggen arXiv:1712.03995v3 (2), Theorem 1 and Section 3.4/(24), including its differentiated normalization; inspected Miglioli arXiv:2312.16816v3 Section 2's invariant-function definition, Theorem 3.2 and full Proposition 4.1/(3) proof; inspected Eynard arXiv:math-ph/0406063v1 (1.1)–(1.7), Section 2's derivation and PDF (2.12)–(2.13), pp. 3–4.
COMPARISON: Classical spectral differentiation retains the discriminant, but its invariant-polynomial hypotheses do not identify L629's pair-symmetric arithmetic amplitude with an admissible operator. The correlator identity has a different insertion and normalization and assumes regular spectra. Neither supplies the required confluent arithmetic lift or positivity after signed extraction.
GAP: Construct or obstruct an explicit differential operator and removable confluent expression matching the actual six-term N=2 germ with full C_2 and tails; reproduce the constant amplitude and all nine coefficients for arbitrary complex a. Uniform growing-N domination and Xi transfer remain independent unresolved steps.
REASON: The relevant differential toolkit is accessible and compared; the missing arithmetic identification is a mathematical bridge, not an essential unread theorem. Admit one bounded construction test outside L631's stopped multiplicative class, with no assumed lift, interchange or sign.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changes the insertion to spectral differentiation of the full Vandermonde identity; this review supplies the previously missing differential-insertion and confluence comparison while reusing adequate scalar coverage.
SCOPE: Actual fixed N=2, arbitrary complex a1,a2 held fixed in differentiation, full r=2^j tail and analytic C_2, L629's complete c=(0,1) extraction and L631's coefficients in tau=log(2)/L. The fixed-N test is necessary for the nominated universal identity, not an asymptotic growing-N positivity result. No other observer or pointwise Xi sign is covered.
COVERED_TARGET: Test a Vandermonde-retaining spectral-derivative HCIZ lift of L629's c=(0,1) functional at actual N=2, requiring exact recovery of L631's full degree-eight cross polynomial before an all-N extension.

## Gap, relevance and bounded decision

The main gap remains actual-Xi initial signs at unbounded heights and
all-degree mixed positivity. The intermediate problem is the exact
fixed-N differential representation stated in TARGET. Its plausible
use is a later joint arithmetic representation capable of proving
Q_{N,L}>=Gamma/2 at N=floor(exp(L/100)), leaving room for L629's
qualified O(Gamma/L) transfer error. No such representation or bound
is supplied by this review; averaged margins would still leave
pointwise signs and other observers open.

The invocation-start nomination and diagnostic are preserved unchanged.
A new lift must specify which spectrum is differentiated, the operator,
its coefficients and its normalization, before comparing its output
with the diagnostic. Merely fitting nine numbers to unspecified free
parameters would not establish the nominated germ identity or a useful
arithmetic mechanism. A known formula may be cited within its hypotheses;
no reproof of HCIZ or the radial differentiation theorem is needed.

## Primary source comparison

### Multiplied HCIZ and singular spectra: reused input

C. McSwiggen, *A new proof of Harish-Chandra's integral formula*,
[arXiv:1712.03995v3, (2), Theorem 1, Section 3.4/(24)](https://arxiv.org/html/1712.03995v3).
Reuse the prior real distinct-spectrum formula with probability Haar
measure and factor product_{j=1}^{m-1} j!. Section 3.4 extends the
multiplied identity to complex singular Cartan elements and differentiates
it to determine its constant. This covers the bare kernel, not an
arbitrary arithmetic insertion. The quotient at a repeated spectrum
requires its removable limit; its vanishing denominator cannot simply
be cancelled after substituting singular values. L631's rank-two
normalization remains a separate, unaudited local specialization.

### Differential insertion retaining the Vandermonde

M. Miglioli, *HCIZ integral formula as unitarity of a canonical map
between reproducing kernel spaces*,
[arXiv:2312.16816v3, Proposition 4.1/(3), Theorem 3.2](https://arxiv.org/html/2312.16816v3).
For conjugation-invariant polynomials F,G on complex m-by-m matrices,
D the diagonal subspace, and x in D with distinct entries, (3) states

    F(partial_Z)G(x)
      = Delta(x)^(-1) {F|_D(partial_x)(Delta G|_D)} evaluated at x.

Delta=product_{i<j}(x_j-x_i). Read the invariant-space definition and
the full proof, including the converse's alternating-polynomial division
and evaluation at zero. The forward proof uses multiplication/derivation
adjoints under the unitary map psi:G -> c Delta G|_D. This is a known
radial differentiation identity, not an arithmetic positivity theorem.
For the proposed application, full conjugation invariance of the
polynomial symbol and an admissible invariant function must be checked;
pair symmetry alone supplies neither. The full B_2 is analytic near
zero, not polynomial or already identified as a Segal–Bargmann vector.
Any finite-jet use and removable limit must therefore be justified in
the construction. No such specialization is performed here.

### Stronger weighted-integral lead: different insertion

B. Eynard, *A short note about Morozov's formula*,
[arXiv:math-ph/0406063v1, PDF (2.12)–(2.13), pp. 3–4](https://arxiv.org/pdf/math-ph/0406063v1#page=3).
Read the diagonal complex-matrix setup, assumptions det(E)Delta(X)Delta(Y)
nonzero, and the full resolvent/determinant derivation. E_ij=exp(x_i y_j);
resolvent expansions initially require |x|>max|x_i| and |y|>max|y_j|.
Its normalized pair correlator equals
1-det(I-(x-X)^(-1)E(y-Y)^(-1)E^(-1)). Its Haar convention absorbs the
usual factorial factor. The insertion is a trace of two resolvents,
not L629's arithmetic amplitude. Repeated spectra violate its stated
regularity assumptions; no confluent arithmetic specialization is
imported. HTML renumbers the PDF's (2.13) as (2.24).

The general-correlator references named by Eynard are unread leads,
not premises. They are unnecessary for the bounded direct differential
identity test; using such a theorem later would require its own exact
hypothesis comparison. No source-access blocker remains for this test.

## Local overlap and failures checked

Reused [the completed Gram/simplex assessment](2026-11-01-signed-functional-gram-simplex-review.md),
including its inspected HG, product/confluent divided-difference,
Andreief and amplified-moment scope. No repeat broad positivity search
is needed. Read L629's complete signed prescription, L623's full Gamma,
L624's full arithmetic identity and compact convergence argument, and
L631's exact N=2 rational form and diagnostic polynomial. Checked the
[scaled-insertion stop](../../ATTEMPTS/2026-11-01-scaled-multiplicative-grassmannian-insertion-stop.md)
and [its decision history](../../history/2026-11-01-grassmannian-n2-insertion-test-01.md).
No cross-notebook theorem is used. These local results retain their
independent-audit qualifications; this is not a proof audit of L631.

L631's -16/9 actual first coefficient versus -8/9 for the multiplicative
insertion, and its degree-eight versus degree-four class obstruction,
remain unchanged evidence. Spectral derivatives on the entire multiplied
identity are outside that class. This difference justifies a test;
it does not assert that missing factors or higher terms are recovered.
The freezing, prefix, absolute-Cauchy and termwise stops are preserved.
L630 controls only a scalar first jet and cannot settle this target.

## Search record, admission and stopping test

New queries actually submitted: `HCIZ integral polynomial insertions
derivatives eigenvalues Vandermonde differential operator confluent`;
`Harish Chandra integral radial part invariant differential operators
Vandermonde McSwiggen`; `Morozov HCIZ correlators derivatives spectral
parameters degenerate eigenvalues`; `"HCIZ" "insertions" differential`;
`"Morozov" "Itzykson" "correlation functions" Eynard`; and
`"HCIZ integral formula as unitarity" arxiv`.
The search also located McSwiggen arXiv:1806.11155v2 Section 3.2.4's
classical radial-part statement, consistent with Miglioli. Its general
Lie-theoretic extension is not needed or newly imported. Search hits
and abstracts alone were not treated as theorem coverage. No matching
Mathlib theorem was checked; availability remains unknown.

After separate supervisor approval of this newly ready assessment,
perform exactly the saved fixed-N test. Require a specified arithmetic
construction and normalization, justified operations on the combined
analytic expression, and exact recovery of the constant amplitude and
all nine L631 coefficients for arbitrary complex a1,a2. Retain analytic
C_2 and every tail coordinate; L624's fixed-N compact convergence is
available, but no uniform all-N interchange is assumed. If finite jets
are used, the relationship to the full germ must be justified rather
than assumed from the source's polynomial theorem.

A mismatch, a violated source hypothesis, or an unjustified interchange
abandons that candidate. Inability to construct it is inconclusive,
not an automatic obstruction. Passing permits only a later all-N
representation/defect test with a coefficient-independent bound and
room for L629's error. It supplies no positivity of differentiated
integrals, negative direction, half-margin or RH candidate. L629 and
other input audits, realization, other observers and pointwise Xi
transfer remain open. No new mathematics or mathematical script was
written in this literature-only step; PROOF.md and DAG.md are unchanged.
