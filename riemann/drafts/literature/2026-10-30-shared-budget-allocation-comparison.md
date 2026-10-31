# Shared-budget allocation: completed source comparison

TARGET: Review source coverage for aggregate signed positivity versus conserved pairwise allocations in a symmetric two-pair/two-real-zero block.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Targeted local shared-budget/aggregate-allocation searches and external allocation, fractional-residue, sextic, two-pair and logarithmic-concavity searches found no exact comparison; queries, primary passages and limitations are recorded below. This is not a novelty claim.
SOURCE_EVIDENCE: Retrieved Csordas arXiv:1309.0055v2 Definition 1.1, Proposition 2.2 (2.3) and Proposition 2.3; Tyaglov arXiv:0902.0413v3 Theorem 4.1 and its proof cases; Katkova–Tyaglov–Vishnyakova arXiv:2406.00686v1 Theorem 2.2 and Section 6 (6.55)–(6.69). Reused Cardon and Tyaglov–Atia comparisons from 2026-10-30-signed-real-zero-allocation-coverage.md.
COMPARISON: The signed identity covers the aggregate polynomial but supplies no conserved decomposition; zero-count results do not supply allocation constants, and the exact-count theorem requires real simple derivative zeros. L509 and L251/L257 cover isolated compensation or center masking, not joint budget competition.
GAP: No inspected result decides aggregate nonnegativity versus simultaneous constant allocations for the defined h,r>0 family. Neither equivalence nor a strict separating example has been established.
REASON: The changed joint-budget scope now has a bounded theorem-level comparison and no essential source blocker; a finite certificate search is justified, subject to separate approval of its newly written continuation assessment.
SCOPE: h>0 and r>0, unit displacement and unit real-zero budgets, two simple conjugate pairs at centers +/-h; all inequalities on real x other than +/-r. No actual-Xi geometry or infinite assembly.
LITERATURE_REASON: The joint conserved-budget target was REVIEW_REQUIRED and lies outside the ready single-pair audit; this step supplies its missing source comparison.

## Exact proposed comparison

For c in {h,-h} define the signed pair term

    K_c(x)=2((x-c)^2-1)/((x-c)^2+1)^2.

The aggregate expression to compare is

    H(x)=K_h(x)+K_{-h}(x)+1/(x+r)^2+1/(x-r)^2.

The proposed allocation condition asks for four nonnegative constants
alpha_h, beta_h, alpha_{-h}, beta_{-h}, with

    alpha_h+alpha_{-h}<=1,   beta_h+beta_{-h}<=1,

such that for each c in {h,-h} the individual expression

    K_c(x)+alpha_c/(x+r)^2+beta_c/(x-r)^2

is nonnegative at every real x!=+/-r. These are definitions for
the next source review, not conclusions. The question is whether
known results decide equivalence with aggregate nonnegativity,
or give a rigorously certifiable strict separation, in this family.
Any next calculation needs its own approved exact target.

## Relevance and discriminator

The main gap remains actual-Xi all-degree positivity. A pairwise
allocation strategy must conserve each real zero's multiplicity;
the isolated L509 criterion does not test budget competition or
cancellation between distinct pairs. A strict separation would
identify a specific loss of the decomposition; an exact equivalence
under stated hypotheses could justify this finite assembly. Neither
would supply actual-Xi geometry, infinite convergence, unmatched
mass or higher signs.

First reuse the existing inspected theorem comparisons and search
the precise joint statement, stronger allocation/decomposition
results and positive-residue obstructions. Compare L251/L257 masking
and the recorded L354 count/gap and L471 ordinary-moment stops only
where relevant; do not reopen their unchanged claims. Continue to
a separately gated finite test only if the comparison identifies
an uncovered, independently decidable statement or a precise import.
If the new block merely restates an existing result or stopped
mechanism, record that evidence and select a materially different
target. No creative actual-Xi claim is yet justified by this finite
nomination. Mathlib coverage is unchecked.

## Completed source review, 30 October 2026

The pending language above records the nominated question, not a result.
This section completes its review without doing the finite mathematics.

### Primary evidence and applicability

George Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-Function*, [arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/html/1309.0055v2),
Definition 1.1, Proposition 2.2, equation (2.3), and Proposition 2.3,
were retrieved. The class in Definition 1.1 has Gaussian coefficient
a>=0, real exponential coefficient, strip-contained zeros and summable
reciprocal squares; finite products are expressly allowed. Proposition
2.2 assumes strip half-width one, f(0)!=0 and absence of nonreal centers
from an interval of length greater than two for its interval-sign claim.
Its proof gives the signed zero-sum identity. For source comparison take

    P(z)=(z^2-r^2)(((z-h)^2+1)((z+h)^2+1)).

For h,r>0 this finite real polynomial has the stipulated simple zeros,
lies in the source strip class, and P(0)!=0. Equation (2.3) identifies
the supplied H with (P'^2-PP'')/P^2 away from +/-r. This is applicability
of the cited identity, not a new sign result. The interval exclusion
does not decide the whole real axis. Proposition 2.3 fixes the remaining
factor while varying a pair's displacement; it does not give a moving
joint-budget criterion. Neither proposition asserts fractional
multiplicity allocations to prescribed individual factors.

Mikhail Tyaglov, *On the number of real critical points of logarithmic
derivatives and the Hawaii conjecture*, [arXiv:0902.0413v3, 23 January 2011](https://arxiv.org/html/0902.0413v3),
Theorem 4.1 (4.1), was retrieved with its proof. For a non-exponential
LP* function phi having 2m nonreal zeros, counting multiplicities, it
states 2m-2m_1 <= Z_R(Q) <= 2m, where Q=(phi'/phi)' and 2m_1 counts
nonreal derivative zeros. LP* is a real polynomial factor times an LP
function, so the finite P qualifies. Read the zero-Q-count case, the
finite property-A reduction and the telescoping upper-bound argument;
the reused assessment covers the class definition and notation. This
counts zeros of the aggregate logarithmic derivative. It neither
characterizes its sign from h,r nor constructs the four allocations.
No sign is inferred from an upper zero-count bound, and a fractional
block is not treated as the logarithmic derivative of an entire
function with noninteger zero multiplicities.

Olga Katkova, Mikhail Tyaglov and Anna Vishnyakova, *On the number of real
zeroes of a homogeneous differential polynomial and a generalization of
the Hawaii conjecture*, [arXiv:2406.00686v1](https://arxiv.org/html/2406.00686v1),
Theorem 2.2 (2.4), assumes a real degree-n polynomial with simple real
zeros and only real simple derivative zeros. For kappa>=(n-1)/n it
gives Z_R(kappa(p')^2-pp'')=Z_C(p), counting multiplicities. Retrieved
Section 6, Lemma 6.1 and (6.55)–(6.69): its kappa=1 case uses monotonicity
of p/p' on the intervals separated by the real derivative roots and
counts one zero on each interval of the second type. These hypotheses
are additional to our zero configuration; none has been verified for
P here. The result gives no individual real-zero budgets. A future
configuration satisfying its derivative hypotheses must be compared
with it before making a novelty claim. The versioned page identifies
v1 as 2 June 2024 and displays an internal date of 24 August 2026;
the cited identifier and equation numbers specify the inspected text.
No independent audit of this source's supporting proofs is claimed.

Reuse the inspected Cardon arXiv:0911.1122v1 Theorems 1.1/2.1,
Corollary 2.2 and proof comparison, and Tyaglov–Atia arXiv:1912.04951v2
Section 2/Theorem 2.2 comparison, in
[the signed-allocation assessment](2026-10-30-signed-real-zero-allocation-coverage.md).
Cardon needs all orders for its real-zero characterization, whereas this
question concerns only the first sign. Tyaglov–Atia assumes a real-rooted
input polynomial and excludes P. Their kappa parameters and auxiliary
polynomials do not implement a split of each prescribed real-zero unit
between the two signed pairs. No new retrieval of those unchanged
comparisons or import of their conclusions is needed.

### Duplicates, failures and bounded search record

Read L509's statement and single-pair optimization, and L251/L257's
statements and relevant masking proofs. None asserts a conserved
two-pair equivalence or separation. Targeted local searches for
shared budget, conserved allocation, aggregate allocation, two-pair
real-zero blocks and pairwise allocation found the nominated assessment
and L509's application caveat, not an exact duplicate. This is a scoped
comparison, not a search of every notebook proof.

Read the L354 failure record
`ATTEMPTS/2026-09-27-count-and-gap-first-sign-test.md` and the L471
failure record `ATTEMPTS/2026-10-27-displacement-weighted-negative-mass-test.md`.
They stop coarse count/gap sufficiency and the ordinary-moment summation
implementation, respectively. Retaining signed pair contributions and
conserving real-zero charges is a distinct finite question, not a repair
of either failed implication. L508 remains the positive-measure detector
contrast already recorded; it is not an input to this finite test.

External queries actually issued included:

- `"Laguerre inequality" "allocation" real zeros complex pairs`
- `"logarithmic derivative" "positive residues" nonreal zeros Laguerre inequality`
- `"Laguerre inequality" "nonnegative" "decomposition" polynomial`
- `"Laguerre inequality" "two conjugate" pairs`
- `"Laguerre inequality" "sextic"` and `"Laguerre inequality" "sextic polynomial"`
- `"Laguerre inequality" "two real roots"`
- `"nonnegative rational functions" "decomposition" "prescribed poles"`
- `"logarithmic derivative" "fractional" "Laguerre"`
- `"Laguerre inequality" "two pairs" zeros`
- `polynomial "logarithmic concavity" "nonreal" zeros factorization`
- `"Laguerre inequality" "factors" "nonreal"`

These returned the count/identity literature, unrelated orthogonal
polynomial material and other leads, but no inspected exact match.
Shapiro's *Problems Around Polynomials* Section 9 appeared as a lead
back to Tyaglov, whose primary theorem was inspected directly. Optional
Muranaka material remains unread/nonessential as recorded in the reused
assessment. Search snippets, repositories and claimed RH results were
not used as theorem evidence. No essential source is blocked, and the
bounded unsuccessful search does not establish originality.

### Decision and continuation test

Outcome is EXPLORATION: new source comparison, no mathematical theorem,
separating example, equivalence or improved Xi bound. EXPLORE permits a
bounded attempt at the exact finite comparison. The separate newly
written [finite-test assessment](2026-10-30-shared-budget-finite-test.md)
nominates a rational grid and exact certificate requirements; it needs
separate approval before calculation. No calculation was run here.

A strict certified separation would identify a concrete loss in the
pairwise sufficient condition and motivate collective cancellation.
An exact equivalence would instead support this finite assembly, but
is not claimed or needed to justify the bounded test. A grid search
without a certified separation proves neither equivalence nor failure
of collective cancellation. Stop that grid after one bounded attempt;
any continuation must supply a specific new discriminating idea rather
than repeat the search at a finer mesh. Actual-Xi geometry, summability,
unmatched mass and higher signs are independent unproved requirements.
No justified creative actual-Xi mechanism is ready from these sources.
Mathlib coverage of the full comparison remains unchecked.
