# A supplied negative Li margin versus a mixed witness — bounded source comparison

TARGET: Assess whether a supplied certified Li coefficient lambda_n<=-epsilon yields a negative L030 form with explicit degree D(n,epsilon,A), using A>=sum_j|beta_j| and L026's actual-node geometry but no node separations.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step159 searched Li/Chebyshev pairings, Li coefficients with quadratic forms/Hankel matrices, Li-criterion polynomial approximation, and weighted square-root approximation on complex sectors. Inspected the primary sources below and scoped local detector/failed-import records. No exact D(n,epsilon,A) theorem was located; this is bounded search coverage, not a novelty or nonexistence claim.
SOURCE_EVIDENCE: Lagarias, AIF57(5)(2007), pp.1690,1701-1706, Lemmas2.2-2.3 and Theorem3.1/proof; Mazhouda-Smajlovic arXiv:1511.04603v1, Theorem2/proof pp.9-10 and off-line pairing in Theorem3 proof pp.10-11; Suzuki arXiv:2206.03682v4, (1.13), Theorem8.1/(8.1)-(8.3), proof setup (8.4)-(8.5) and closing discussion pp.25-28; NIST DLMF1.9.30-31,1.10.1,1.10.4,4.6.7,18.5.1-4, version1.2.8. Reuse step158's finite-Li assessment and local L018/L024-L026/L030-L032/C032a/L895.
COMPARISON: Lagarias supplies an exact rational Weil-form observable for Li coefficients without RH. Suzuki's finite moment conversion uses a different moment sequence and does not supply an L030 degree. The ordinate-only Chebyshev replacement is RH-equivalent, not an unconditional input. Standard complex Taylor/binomial tools cover approximation after a justified regularization, but supply no ready complete-sum or degree certificate for this weight.
GAP: Prove or obstruct the conditional conversion using only n,epsilon,A and L026: exact actual-node pairing, real algebraic-square representation/regularization, an explicit degree, and an upper error below epsilon/2 for the whole node sum including beta->0 and multiplicities. No such estimate or factorization is proved here.
REASON: Essential source comparison is now sufficient for one bounded attempt at the unchanged conditional target. Start from the cited rational Weil identity rather than a possibly RH-assuming ordinate formula or an unspecified head. Investigate the remaining quantitative bridge; do not reprove the cited identity or reopen finite-window constants.
SCOPE: Actual Xi and paired beta_j=alpha_j^(-2); integer n>=1, epsilon>0 and finite A>0 are supplied, with lambda_n<=-epsilon and sum_j|beta_j|<=A. No negative actual coefficient is asserted. No individual zero locations, separations, simplicity, RH or effective Li window is an unstated premise.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
A quantitative conversion would make a certified negative Li coefficient
usable in the same hierarchy. It would not establish such a coefficient,
prove any mixed sign, close RH or by itself supply D(T,delta).

## Primary inputs and applicability

J. C. Lagarias, *Li coefficients for automorphic L-functions*,
Ann. Inst. Fourier 57(5) (2007), 1689-1740,
[Theorem 3.1, equations (3.1)-(3.6), pp.1704-1706](https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf#page=17),
defines G_n(s)=1-(1-1/s)^n and states

    <G_n,G_m>_W = lambda_n + lambda_{-m} - lambda_{n-m},
    <G_n,G_n>_W = 2 Re(lambda_n).

Here <F,G>_W sums F(rho) conjugate(G(1-conjugate(rho))) over
all zeros with multiplicity. The class consists of functions holomorphic
in the open critical strip with uniform O(1/|s|) decay outside |Im s|<=1;
the quadratic sum is absolute. The proof uses G_m(1-s)=G_{-m}(s)
and (3.6), rather than RH. [Introduction (1.1)-(1.3), p.1690,
and Lemmas 2.2-2.3, pp.1701-1702](https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf#page=14)
specify Li normalization, star convergence and reflection. Its zeta case
uses the same nontrivial zeros as L018; G_n's poles are only 0,1,
excluded by L018, and its stated decay applies for fixed n. The
indefinite notation <G_n,G_n> is not an assumption of positivity.
This is a rational test in s, not beta*q(beta). No L030 conversion
or effective polynomial degree is stated.

K. Mazhouda and L. Smajlovic, *On relations equivalent to the generalized
Riemann hypothesis for the Selberg class*,
[arXiv:1511.04603v1, Theorem 2 and proof, pp.9-10](https://arxiv.org/pdf/1511.04603v1#page=9),
identifies the ordinate-only Chebyshev formula (7), for all positive n,
with GRH under its class hypotheses. Its forward proof explicitly
sets rho=1/2+i*gamma. In the proof of Theorem 3, pp.10-11, an
unconditional expression retains sigma and the modulus of
(rho-1)/rho before imposing any critical-line condition. Thus the
ordinate formula cannot replace the actual complex alpha_j in this
target. The present review uses only this scope warning, not an
unverified specialization of the paper's Selberg-class criteria.

M. Suzuki, *Aspects of the screw function corresponding to the Riemann
zeta-function*, [arXiv:2206.03682v4](https://arxiv.org/pdf/2206.03682v4#page=25),
version header 30 May 2023, internal date 31 May 2023,
Theorem 8.1, (8.1)-(8.3), pp.25-26, gives mutually inverse finite
linear relations between Li coefficients and the moments (1.13).
Those moments integrate t^k against e^(-t/2)*Psi(t)/4 on [0,infinity);
they are not L025's reciprocal-square power sums. The proof setup
(8.4)-(8.5) and closing discussion through (8.8), pp.26-28, identify
the generating-function conversion. The author explicitly notes that
positivity does not transfer directly through these relations.
This is relevant overlap, but neither its moment-Hankel criterion
nor its finite linear conversion is the requested negative L030 form.
No coefficient formula from this theorem is used in an argument here.

The [NIST DLMF, version 1.2.8 (15 September 2026)](https://dlmf.nist.gov/),
inspected at the following exact statements, supplies the elementary
analytic tools for a bounded attempt:

- [18.5.1-4](https://dlmf.nist.gov/18.5.i): Chebyshev trigonometric/Laurent
  representations. Their displayed real-variable notation must not be
  read as a claim that the actual nodes are real. A future use at complex
  arguments needs the polynomial identity justification and exact pairing.
- [4.6.7](https://dlmf.nist.gov/4.6.E7) and
  [1.10.4](https://dlmf.nist.gov/1.10.E4): binomial expansions on |z|<1,
  with principal values. They do not cover the singular origin by fiat.
- [1.10.1](https://dlmf.nist.gov/1.10.E1): Taylor expansion on an analytic
  disk; [1.9.30-31](https://dlmf.nist.gov/1.9.E31): Cauchy formulas for
  a positively oriented simple contour and an interior evaluation point,
  assuming continuity on the closed interior and analyticity inside.
  A later explicit remainder needs a specified contour, supremum and
  strict interior radius; none is certified in this source turn.

These standard statements are cited, not reproved. In particular,
neither convergence on a fixed compact nor a real-interval approximation
theorem supplies uniform weighted error over unknown complex nodes.

## Local duplicates and recorded failures

Read the full statements/proofs of L018/L024-L026/L030-L032/C032a and
L895's relevant head/tail construction. L030 requires beta^2 times an
algebraic square; a modulus square is a different expression. L032's
degree depends on its entire finite head and interpolation constants.
L895's simultaneous certificate still takes every head location and
tail mass as inputs. No such data are supplied by n,epsilon,A.
Its min-max/precision extensions are irrelevant to the present conversion.

Reuse [step158's completed assessment](2026-11-10-height-deviation-witness-degree-review-157.md)
and [the direct-import stop](../../ATTEMPTS/2026-11-10-finite-li-index-mixed-degree-import-limit-158.md).
Do not identify a finite Li index with a polynomial degree, and do not
repeat inaccessible publisher retrieval. Scoped searches found no local
completed Li-to-L030 conversion. An unrelated joint-grid assessment
uses different symbols and supplies no result for this target.

## Bounded next mathematical test, not a result

Use Lagarias's exact rational quadratic observable as the starting point.
Test reflection into even/odd parts and regularization of the resulting
square amplitudes, followed by a complex polynomial truncation with
explicit degree. This is a proposed mechanism, not an asserted
factorization. The finite poles are known, but their treatment and the
behavior at beta=0 still need proof from L026's actual geometry.

The decisive success certificate is one real polynomial, or finitely many
real polynomials whose summed L030 value is negative, with degree bounded
explicitly using only n,epsilon,A and the fixed L026 constants. An
intermediate summed certificate must identify why one member is negative.
Require a proved upper comparison error below epsilon/2 after normalizing
the rational observable to lambda_n, including every node and multiplicity.
A one-sided comparison may suffice; no two-sided weighted approximation
near zero is assumed. Account for regularization and truncation separately.

Abandon this proposed construction if its bound needs an unknown node
clearance/separation, an additional mass-tail modulus, an uncontrolled
function norm, or an already RH-equivalent sign. A failed ansatz is not
a disproof of existence of D(n,epsilon,A). Preserve the exact failed
inequality before choosing a materially different mechanism.

The supplied negative Li margin, total mass bound and actual-node
identification remain hypotheses. Obtaining n,epsilon,A from T,delta,
proving actual mixed signs, and covering all heights/degrees remain
independent gaps. No off-line zero or negative actual Li coefficient is
asserted. No new mathematical result, canonical lemma, program, or
argument change was produced during this literature-only review.
Mathlib full matching conversion: not checked; unknown, not absent.
No cross-notebook input is used. Uninspected abstract/search leads about
model-space norms, Faber computation or other moment criteria are not
imported and are not essential to this elementary bounded test.

## Search record and decision

Queries included `Li criterion Chebyshev polynomials sum zeros formula`,
`Li coefficients quadratic forms Lagarias`, `Li coefficients Hankel
matrices`, `Li criterion polynomial approximation`, `weighted polynomial
approximation sector square root`, and `polynomial approximation zero
of order weighted complex origin`. Followed the exact Lagarias,
Mazhouda-Smajlovic and Suzuki papers above and their relevant statements;
search snippets and model memory are not source evidence. The finite-Li
assessment is reused without reopening its irrelevant constants.

EXPLORE covers the unchanged target and this elementary rational/regularized
approximation attempt, not a promise that it works. It does not approve
unrelated new theorems. The completed review may support a separate
proof_attempt/creative after supervisor approval: the unresolved central
obstruction is quantitative passage from a known rational negative
observable to beta^2 polynomial squares at the zero accumulation.
