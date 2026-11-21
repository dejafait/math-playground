# One fixed positive atomic-mixture diagnostic — source approval

TARGET: Test the positive-cosh-mixture residual-index premise for mu=(delta_1+delta_3)/2+2delta_2 at r=3,R=8, certifying the two-root grouping and complete J-Q inertia without parameter tuning.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step452 searched cosh/residual/inertia/positive mixture, cosh/two zeros/Loewner mixture, cosh/J-Q inertia mixture and Arb/Cauchy/Taylor rigorous integration; reused step451 and the approved reciprocal-quartic assessment. No exact-model index theorem identified; no novelty inferred.
SOURCE_EVIDENCE: DLMF v1.2.8 4.28.2, 4.33.2, 4.35.7/27/30, 4.2.3/5/6 and 1.10.6/7 inspected; Johansson arXiv:1802.07942v1 Section2/2.1 pp.2–4 inspected through algorithm, analytic-domain and tolerance/evaluation-limit cases; ready de Boor/Duits/Sylvester interfaces reused. Direct links and qualifications below.
COMPARISON: Known methods cover complex-root enumeration and complete nonrational Laurent-series certification, but do not supply this model's grouping, margins, residues or index. Its finite atomic definition adds a premise absent from L783. No positive-mixture index implication is imported.
GAP: Certify every model premise for G_*(8z), then determine full complete-series J-Q inertia including nullity. Source access no longer blocks this attempt; quantitative bounds and signs remain uncomputed.
REASON: This one independently testable added-moment-premise diagnostic can reject a generic shortcut without transferring L783 entries or repeating L773's exhausted Turan grid; citation alone does not evaluate the specified matrix.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerned essential root-exhaustion and nonrational complete-series coverage; this turn supplies that comparison without performing the calculation.
SCOPE: Separate step452 approval of exactly the displayed law, r=3,R=8,k=2 and proposed sigma=9/8 to verify, for one REPRODUCTION calculation. No model factorization, root count, coefficient, index, general theorem or mathematical script was produced. No tuning, actual-Xi sign or global class premise.

## Proposed experiment, not established mathematics

Define the candidate by its measure:

    G_*(w)=integral cosh(t sqrt(w)) dmu(t),
    mu=(delta_1+delta_3)/2+2delta_2,
    r=3, R=8, k=2.

The square-root notation denotes the even entire cosh series. Use the
definitions in L777/L782/L783 with G_*(8z), never their computed model
entries. Proposed sigma=9/8 is a bound to verify, not an input.

Before research, compare the primary elementary hyperbolic formulas,
zero-exhaustion/entire-function interfaces and rigorous complete-series
evaluation methods to this exact model. Reuse ready literature instead
of rediscovering the determinant or inertia machinery. The source review
must retain all factorials, R scaling, the one-based projection deleting
coordinates1–3, coincident divided differences and residue signs.

The later single diagnostic must first certify all model premises,
including exactly two distinct simple nonzero negative normalized
interior roots, contour nonvanishing, and a zero-free neighborhood for F.
If these fail, record that obstruction and stop; do not select a different
radius or measure. If they hold, evaluate the complete h_3 and K, with
proved tails or an exact analytic expression and rigorous error control.
Then certify both n_0(J-Q)=0 and the actual n_-(J-Q), comparing it with
n_-(J). A coefficient preview or determinant parity is insufficient.

A mismatch would refute sufficiency of the tested premise under all
verified qualifications; a match is evidence for this one model only.
Neither result supplies actual-Xi signs or the missing all-degree step.
Close this diagnostic after the single test. Repetition requires a
materially new structural input, not parameter tuning. The generic
positive-integral route retains the independent residual-sign gap.

This is expected to be a known-method specialization/calculation, not
a creative mechanism merely because its inputs differ. Creative work
remains blocked on an independently motivated signed-form identity with
a credible sign payment. Full matching Mathlib coverage is unchecked.

## Completed source comparison — step452, 2026-11-05

The nomination above is retained as an unperformed experiment. This
separate review approves its unchanged target for one known-method
specialization. The main gap remains actual-Xi all-degree mixed positivity;
the model can test a generic shortcut, while actual-Xi tail signs, other
mixed minors and global grouping remain independent unresolved steps.

### Root and entire-function coverage

NIST DLMF v1.2.8 (2026-09-15), [4.28.2](https://dlmf.nist.gov/4.28.E2),
gives the complex exponential definition of cosh;
[4.33.2](https://dlmf.nist.gov/4.33.E2) gives its even Maclaurin series
with denominators (2n)!. These cover the transform notation. The finite
atomic specialization, entire convergence, nonnegative coefficients,
normalization and growth bound must still be justified for this model.
Do not omit factorials or the scaling w=8z.

DLMF [4.35.7](https://dlmf.nist.gov/4.35.E7),
[4.35.27](https://dlmf.nist.gov/4.35.E27) and
[4.35.30](https://dlmf.nist.gov/4.35.E30) were inspected: exact complex
sum-of-coshes and double/triple-argument identities. They provide
algebraic reduction methods for the nominated mixture, not a theorem
about its roots. No reduced polynomial or factorization is derived here.
DLMF [4.2.3/5/6](https://dlmf.nist.gov/4.2.i) specifies modulus/argument,
negative-real-axis values and the integer translates of the general
logarithm. Together with the exponential definition, these cover full
preimage enumeration after algebraic reduction. Principal inverse values
or real-axis sign changes alone do not exhaust complex roots.

The attempt must enumerate all branches relevant to both disks, track
multiplicities and the even square-root identification, and prove strict
separation from |z|=1 and |z|=sigma. Removability at the two removed
zeros precedes an assertion that F is entire. Growth is a separate
specialization and supplies no real-zero conclusion. A genus-zero
product is unnecessary for the local diagnostic; if asserted later it
needs its own precise Hadamard applicability argument. No product fact
is established or silently imported here.

Hadamard search leads were not used as genus-zero coverage: Petrow's
Theorem7.7 was inspected as an order-at-most-one genus-one statement;
Debray's classroom notes were accessed; Kupers's PDF returned403.
These optional leads do not block this fixed local diagnostic. DLMF
TeX endpoints and shell network retrieval also failed; the readable
primary HTML equations above supplied the essential interfaces.

### Complete nonrational evaluation

DLMF [1.10(iii), equations1.10.6–7](https://dlmf.nist.gov/1.10.iii)
assumes analyticity on an annulus, places the positively oriented
coefficient contour strictly within it, and gives the Laurent integral
and absolute locally uniform convergence. Use it for b only after its
annulus and F's nonvanishing are certified. Its pole at zero does not
permit Taylor bounds across zero.

Reuse L777's remaining-factor/truncation argument and L782's convergence
before regrouping as methods. They require a quantitative m_sigma>0,
the full M_b bound, coefficient enclosures and a complete tail budget.
Their actual-G or fixed-actual-pair statements do not establish the
model case. Supply its own bounds for both divided differences and
diagonal derivatives, and justify every infinite-series interchange.
The rational closed form or numerical entries in L783 cannot transfer.
No finite coefficient preview is a complete-series certificate.

Fredrik Johansson, [*Numerical integration in arbitrary-precision ball
arithmetic*, arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942),
Section2/2.1, printed pp.2–4, supplies a primary rigorous-evaluation
method if coefficient integrals are used. Its complex-segment algorithm
uses analytic enclosing ellipses for Gaussian error bounds, otherwise
subdividing or using direct interval enclosures. The callback must
rigorously enclose its function and reject unverified analytic domains,
including branch-cut overlaps. Requested tolerance is not a guarantee:
inspect actual output radii and evaluation-limit cases. No successful
precision or convergence for this model is imported.

The model implementation must include the contour parameterization and
Jacobian, root uncertainty, removable values and all denominator bounds.
An elementary interval/Taylor implementation with proved remainders is
also within the known series method. No package availability was tested.
Current FLINT documentation was reached but its revised text is not a
load-bearing source; the fixed primary paper provides the algorithm and
failure cases. This source review neither derives a tail formula nor
performs a model calculation.

### Reused determinant/index interfaces and recorded failures

Reuse `2026-11-05-reciprocal-quartic-inertia-test.md` and its direct
primary links: de Boor, *Divided Differences* (2005), Example2/(10),
p.49, Proposition25/(26) and proof pp.53–54, including repeated-argument
continuity; Duits, DPP2, Lemmas66/69 pp.51–52, finite-rank determinant
restriction; Sylvester's law of inertia, with the invertible-congruence
step of Berkolaiko–Kuchment (2022), Theorem2.7/proof pp.88–91.
Their unchanged theorem/proof-case coverage is ready and is not
reproved. De Boor's polynomial interface does not pay the infinite-series
limit. Neither determinant transfer nor the Schur theorem supplies
an automatic residual-index bound or operator selfadjointness.

Retain one-based Q_3 deleting coordinates1–3, beta_(4+n), complete
residues and their ordering, positive diagonal E, Q=-EKE and all R
factors. Verify the model's projected pairing and similarity instead
of invoking L782's actual-pair conclusion verbatim. Determine full
inertia of the real symmetric two-by-two matrix by rigorous congruence,
pivots or equivalent strict trace/determinant checks, covering zero
cases. Intervals containing zero leave the index uncertified;
determinant parity alone does not determine negative index and nullity.

L783 and `ATTEMPTS/2026-11-05-reciprocal-local-premise-index-stop.md`
were compared narrowly: their quartic has no established positive
cosh-mixture representation. L773 and
`ATTEMPTS/2026-11-04-two-atom-grid-turan-stop.md` concern the exhausted
Turan grid and a different target. Step451's positive-transform,
raw-moment/PF and signed-Schur review retains its extra-hypothesis
failures. This diagnostic transfers no computed entries and does not
reopen those stopped generic mechanisms.

### Approval and discriminating test

DECISION is SPECIALIZE for one REPRODUCTION calculation. First certify
all nominated premises for the fixed law and R=8, including the proposed
sigma=9/8, or record failure. A failed required premise ends the test
without changing the law or radius. If premises pass, certify the
complete matrix and compare n_0(J-Q) with0 and n_-(J-Q) with n_-(J).
Insufficient strict bounds are inconclusive, not a matching index.
Stop after that one test; no grid, tuning or automatic repeat is approved.

A mismatch rejects only the conjunction of verified premises; a match
clears only this model. Neither proves actual-Xi signs. This review
establishes method coverage, not a new mathematical result or novelty.
No lemmas or mathematical scripts were changed. Full matching Mathlib
coverage remains unchecked; mathematical exploration usage is unchanged.
