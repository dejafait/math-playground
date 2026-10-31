# Finite-interval multiplicative Hardy-space review

TARGET: Assess whether finite-interval multiplicative Hardy-space L1 inequalities can give a positive T(log T)^3 lower bound for L477's exact residual R_T while controlling cancellation between its two phase sums.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact/stronger-result searches for Helson coefficient inequalities, finite-interval Dirichlet norms and nonharmonic L1 lower bounds; inspected the primary Helson, Bondarenko--Heap--Seip and Jaming--Kellay--Saba statements and relevant proof cases listed below. Reused local L318/L319 and the stationary-involution failure; no matching complete-residual theorem was established, and no novelty is inferred.
SOURCE_EVIDENCE: Helson, Studia Math. 176 (2006), (2.10), pp. 89--90, https://scispace.com/pdf/hankel-forms-and-sums-of-random-variables-17nxezaacy.pdf ; Bondarenko--Heap--Seip arXiv:1405.6516v3, Theorem 2/(6)/(11), https://arxiv.org/pdf/1405.6516v3 ; Jaming--Kellay--Saba arXiv:2303.10919v2, Theorem 1.1(iii), Proposition 2.4, Lemma 2.9, Remark 2.13 and Corollary 2.14, https://arxiv.org/html/2303.10919v2 ; Jaming--Kellay--Saba--Wang arXiv:2409.07093v1, Theorem 1.5 and proof opening, https://arxiv.org/pdf/2409.07093v1 . Read L477 in full; its first critical audit remains pending.
COMPARISON: Helson/Bondarenko--Heap--Seip supply Haar or infinite-time analytic-polynomial norms; Jaming--Kellay--Saba supplies a dimension-uniform finite-interval inequality for separated fixed linear frequencies. Neither inspected statement controls L477's complete real residual with its actual chirped product sum. This is a documented scope mismatch, not a lower or upper bound for E(T).
GAP: A quantitative growing-length finite-height transfer, suitable coefficient weights after grouping/analytic lifting, and control of cancellation with the chirped product sum are unproved. No inspected theorem or specified finite-sum extension establishes the required positive c T(log T)^3 scale for the complete residual.
REASON: The source-comparison target is completed with an informative negative applicability decision. Park automatic Hardy-norm transfer; do not approve a dependent full-scale lower-bound attempt from these citations alone. EXPLORE records that the bounded search found no adequate match, not permission to omit the remaining obligations. Nominate the independently testable first audit of L477 separately.
LITERATURE_REASON: A new multiplicative Hardy-space norm mechanism may address the residual that survived the elementary cutoff calculation; its finite-interval hypotheses and treatment of cancellation are essential unread coverage.
SCOPE: Actual real heights t in [T,2T], exact L477 R_T and theta, all ordered pairs n,m<=M, no RH, simplicity, spacing, external half-plane premise or substitution of independent random phases.

## Original nomination, preserved before the completed review below

The following nomination records the state before this literature turn;
its unread-source descriptions are superseded by the completed review.

### Exact input and decision sought

Use the definitions and full proof in L477. It gives

    |E(T)-integral_T^(2T)|R_T(t)|dt| <= C T(log T)^(5/2),

where R_T is the sum of the ratio and chirped product cosine
expressions in its (2). Its signed integral O(sqrt(T)) and its
absolute upper bound O(T(log T)^3) decide neither defect threshold.
The full-scale lower bound sought would rule out this particular
positive square as a little-o approximation, not refute RH or
the mean negative-mass target.

The new lead is coefficient lower bounds for multiplicative
Dirichlet Hardy spaces, including results described as Helson-type
inequalities. These are uninspected leads, not theorem inputs.
Retrieve a primary theorem's complete hypotheses, the relevant
finite/infinite averaging distinction, and proof cases essential
to its claimed applicability before reading larger passages.

Specifically compare the growing polynomial length with the
averaging interval; determine whether any constants are uniform
in that regime. Track real parts and both phase sums. A bound on
one complex analytic polynomial does not by itself lower-bound
the real sum after cancellation. Do not assert a finite-height
transfer, equidistribution rate, frequency projection bound or
chirped-phase separation without source coverage.

Continue only if the inspected result or a precisely identified
finite-sum extension gives an independently testable route to a
positive full-scale lower bound for the complete residual. If the
theorems cover only infinite-time norms or an isolated component,
record that scope mismatch and leave the proposed transfer
unapproved. A failed source match is not proof that E is small,
large or impossible to estimate. Any later new derivation receives
a separate ready assessment and mathematical turn.

### Recorded failures and limits

The local L318/L319 comparison is historical, not an input to
L477. The stationary-involution stop is preserved in
`ATTEMPTS/2026-09-24-actual-phase-poisson-ratio-test.md`.
This nomination does not repeat that signing mechanism or assert
that generic multiplicative phases model actual heights.

The earlier L317 fourth-order dominance failure, L472/L473
moment-law limitation and L475 band-cost failure remain in force.
L477 resolves the dyadic endpoint cost for this square but leaves
the absolute residual. Its proof is canonical, its critical audit
is pending, and no full matching Mathlib theorem has been checked.
No cross-notebook theorem is used.

## Completed source comparison, 29 October 2026

The main RH gap is still unproved all-degree actual-Xi positivity.
The intermediate target reviewed here is a full-scale lower bound for
the exact L477 residual, retaining both phases. Its downstream use is
to reject this particular fixed square as a little-o approximation;
neither that rejection nor success of the square would prove RH.

### Inspected primary statements and essential proof cases

1. **Helson, _Hankel forms and sums of random variables_, Studia
   Math. 176(1) (2006), 85--92, (2.10), pp. 89--90.**
   [Primary article, PDF mirror](https://scispace.com/pdf/hankel-forms-and-sums-of-random-variables-17nxezaacy.pdf).
   For analytic H1 functions on the infinite torus, the square root
   of the sum of squared coefficients divided by d(n) is at most
   the H1 norm; measures are normalized Haar measures. Read Lemma 1,
   pp. 87--88, its H2 factorization proof, and the finite-variable
   iteration (3.1)--(3.6), pp. 89--90. The proof alternates
   one-variable contraction and Minkowski over product measure.
   It gives no rate for sampling a growing polynomial on a finite
   height interval. The DOI endpoint was inaccessible; the complete
   relevant primary proof was readable in the mirror, so this is
   not an essential source blocker.

2. **Bondarenko--Heap--Seip, _An inequality of Hardy--Littlewood
   type for Dirichlet polynomials_, arXiv:1405.6516v3, 9 January
   2015, Theorem 2, pp. 4--8.**
   [Primary preprint](https://arxiv.org/pdf/1405.6516v3).
   For arbitrary complex coefficients of F(s)=sum_(n<=N) a_n n^(-s)
   and 0<q<=2, the coefficient bound is

       (sum |mu(n)| |a_n|^2 d(n)^(log(q)/log(2)-1))^(1/2)
           <= ||F||_q.

   The norm is the limit of height means with F fixed. The paper
   also records Helson's stronger all-integer q=1 bound as (6).
   Read the zero-free and Blaschke cases of Lemma 1, the Bohr/Haar
   identity (11), and the tensor iteration completing Theorem 2.
   These establish a uniform coefficient inequality on the torus,
   without a quantitative finite-height approximation in N.

3. **Jaming--Kellay--Saba, _The Littlewood problem and non-harmonic
   Fourier series_, arXiv:2303.10919v2, 24 July 2023; Math. Ann.
   389 (2024), 1939--1961, Theorem 1.1(iii).**
   [Primary preprint](https://arxiv.org/html/2303.10919v2).
   For ordered real frequencies with |lambda_k-lambda_l|>=|k-l|,
   arbitrary complex a_k, and H>=72,

       H^(-1) integral_(-H/2)^(H/2)
           |sum a_k exp(2pi i lambda_k t)| dt
           >= (1/122) sum |a_k|/(k+1).

   Read Proposition 2.4, Lemmas 2.6/2.8/2.9, Remark 2.13,
   Corollary 2.14 and the finite-interval conclusion in Section 2.3.
   In particular Remark 2.13 repairs the N-dependent preliminary
   correction for the fixed-interval case; it cannot be skipped
   when claiming a uniform constant. The result concerns a single
   fixed linear-frequency exponential polynomial, with no chirp.
   The infinite-time assertions (i)--(ii) have different hypotheses.

4. **Jaming--Kellay--Saba--Wang, _On L1-norms for non-harmonic
   trigonometric polynomials with sparse frequencies_,
   arXiv:2409.07093v1, 11 September 2024, Theorem 1.5, p. 3.**
   [Primary preprint](https://arxiv.org/pdf/2409.07093v1).
   The any-positive-interval extension assumes a fixed increasing
   sequence whose gaps tend to infinity; its constant depends on
   that sequence and the interval. Read the proof opening, where
   the tail-gap threshold is selected from that fixed sequence,
   and the stated compactness limitation. This is no uniform theorem
   for changing clustered ratio-frequency sets or chirped sums.
   No dependent use of its later proof is proposed.

The inspected sections of Bondarenko--Brevig--Saksman--Seip,
[arXiv:1801.06515v2](https://arxiv.org/pdf/1801.06515v2), were
secondary corroboration of the Hardy-space setting: Theorem 2.1
and the coefficient/partial-sum discussion. No theorem from that
paper is imported or asserted to improve the bounds above.

### Applicability decision for the exact residual

L477 (2) contains a real ratio-frequency cosine sum and a product
sum with phase 2theta(t)-t log(nm). Its cutoff grows with the same
T that controls the interval. Helson's analytic function hypotheses
do not directly cover the whole expression. A Laurent-polynomial
lift of the ratio part would still need tracked coefficient weights
and a quantitative height transfer; merely clearing negative powers
does not provide these estimates. This is a scope comparison, not
a newly proved impossibility theorem for such a lift.

The real ratio sum can be written using both signs of fixed
frequencies. A correct application of a finite-interval theorem
would have to group equal frequencies, order the entire retained
set, check its separation after normalization, and evaluate the
weighted coefficient lower bound. No such application or full-scale
bound is carried out in this literature-only turn. More basically,
the product sum has the actual non-linear theta phase, outside the
inspected theorem. A lower bound for the ratio part, or for a complex
polynomial before taking a real part, cannot be cited as a bound for
their complete sum without a cancellation estimate. Multiplying by
a unimodular chirp does not make both phases linear in these source
statements. Freezing theta and using independent prime phases are
not authorized substitutions.

The discriminating continuation test was source coverage for a
concrete full-residual lower bound at scale T(log T)^3. The inspected
results do not pass it. Park their direct application and leave
E(T)=o(T(log T)^3) and the opposite positive-limsup test both open.
This is new evidence about this literature lead, not mathematical
progress beyond the inspected sources. It does not exhaust other
finite-height mechanisms and does not reopen L319's involution.

### Search record and remaining leads

Queries included `Helson inequality Hardy space Dirichlet polynomials
L1 finite interval lower bound Bondarenko Seip`, `Dirichlet polynomial
finite interval L1 lower bounds multiplicative Hardy space Saksman
Seip`, `"Helson" "inequality" "Dirichlet polynomials"`,
`"Dirichlet polynomials" "finite intervals" "norm"`,
`"L1" "non-harmonic" "Jaming" lower bounds`, and
`Helson "Hankel forms and sums of random variables" pdf`.
Several broad Hardy searches returned unrelated PDE inequalities;
those were not treated as evidence. A guessed publisher download
endpoint and the Helson DOI failed, but the primary mirror resolved
the essential Helson statement/proof. No persistent access blocker
is claimed. The local searches and L318/L319 comparison from the
nomination were reused; L477 was read completely this turn.

The sparse-frequency paper's reference to Jaming--Saba's survey
for constants nearer the separation threshold is an unread lead.
The recent local-embedding search hit was not inspected and is not
an input. Neither is evidence of complete-residual cancellation
control. Do not infer current open-problem status from older papers.
Full matching Mathlib coverage was not checked. No source theorem
is added as a canonical mathematical input and no reproof is made.

The separate L477 audit nomination is in
`drafts/literature/2026-10-29-l477-first-critical-audit-coverage.md`.
It uses the existing analytic input scope and does not continue the
uncovered Hardy-space transfer. The newly written nomination needs
separate approval before its mathematical audit.
