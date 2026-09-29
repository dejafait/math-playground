# First Laguerre sign: zero-density and spacing assessment

TARGET: Review whether unconditional zero-density and critical-line zero-spacing theorems can control the negative reciprocal-zero contribution to D_1(Ξ;a)/Ξ(a)^2 uniformly for real |a|>40 with Ξ(a)≠0.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searches on 2026-09-27 for first Laguerre inequalities, zero compensation, unconditional zero density, critical-line gap bounds, short-interval critical zeros and unconditional pair correlation; theorem statements and the closest reciprocal-zero formula were read. No full uniform compensation theorem was found in this bounded search.
SOURCE_EVIDENCE: Csordás, arXiv:1309.0055v2, Proposition 2.2 equation (2.3), Proposition 2.3 and Open Problem 4.7, https://arxiv.org/pdf/1309.0055v2; Guth–Maynard, arXiv:2405.20552v2, Theorem 1.2, https://arxiv.org/html/2405.20552v2; Ivić–Jutila, Monatshefte 105 (1988), Theorem 1 pp. 59–60, https://doi.org/10.1007/BF01471104; BGSTB, arXiv:2306.04799v1, Theorem 1/Lemma 5, https://arxiv.org/html/2306.04799v1; Lamzouri, arXiv:2609.02882v1, Theorem 1.1/Proposition 2.1/Lemma 3.1, https://arxiv.org/pdf/2609.02882v1; Wang, arXiv:2609.07918v1, Theorems 1.1/2.2, https://arxiv.org/pdf/2609.07918v1; spacing comparisons and access details below.
COMPARISON: The reciprocal-square identity and its local negative-pair mechanism are known. The inspected density bounds count zeros, gap bounds count long gaps or exhibit some gaps, and pair-correlation formulas average over pairs with restricted test functions. None states the displacement-sensitive lower bound at every real center required here; even the recent simple-critical-zero proportions leave exceptional configurations uncontrolled.
GAP: Control every negative conjugate block against the positive blocks at the same center, uniformly for arbitrarily small off-line displacement b and for every exterior a. No checked statement bounds that signed sum by zero from below. Higher Laguerre levels remain separate gaps even if this first sign is established.
REASON: Direct import of the proposed uniform compensation estimate is unsupported. Before attempting such an estimate, test whether the selected coarse counting and gap upper bounds alone can exclude the known local negative-pair mechanism in an order-one model. This is an unresolved applicability question, not a proved impossibility theorem or a novelty claim.

## Scope, relevance and existing evidence

This completes the literature-only review of the unchanged TARGET.
The shared rules, local goal, whole overview, DAG, checkpoint and
pre-existing changes were inspected. Relevant detailed comparisons
reuse L251, L255–L257 and the
[earlier sign-input screen](../../ATTEMPTS/2026-09-21-theta-moment-literature-screen.md).
That screen had read Csordás's open problem but had not compared the
zero-density and spacing inputs for this target. The gate scaffold is
replaced by this assessment; all mathematical work is preserved.

The immediate gap is D_1(Ξ;a)=Ξ'(a)^2−Ξ(a)Ξ''(a)≥0 at every real
|a|>40. The normalized expression is considered only where Ξ(a)≠0.
No simplicity or real-root assumption is added. Existing finite-height
results and the stopped endpoint implementations do not answer this
uniform question.

Plausible downstream use: the first sign is one member of the low-index
segment required by L320's logarithmic witness bound. Even success
would leave the other signs through that bound, effective coverage of
remaining heights and the endpoint margin unresolved. L251 and L257
already prevent identifying a finite collection of signs with RH.

The entry test was whether the sources supply compensation at every
center, or an applicable local input towards it. The sources below
supply no such estimate. This review does not calculate a new bound,
construct a counterexample, or show that the sources jointly imply no
such estimate by any argument.

## Search record

Representative queries actually used:

- `Riemann xi Laguerre inequality zero density negative contribution reciprocal zeros Csordas`
- `Riemann xi first Laguerre inequality zeros close critical line compensation`
- `Guth Maynard zero density estimate theorem 2026 N sigma T 30 13`
- `unconditional gaps consecutive zeros critical line zeta every interval T exponent 0.156`
- `"critical line" "gap" "upper bound" "Ivić"`
- `"Gaps between consecutive zeros" "Ivic" 1987 pdf`
- `"zeros" "critical line" "short intervals" "Theorem" arxiv`
- `"Baluyot" "Goldston" "Suriajaya" "Turnage-Butterbaugh" "unconditionally" pair correlation Lemma 5`
- `"Laguerre" "Riemann" "compensation" zeros`
- `"Laguerre" "Riemann" "zero density" inequality 2025 2026`

Search snippets were used for discovery. The statements below were
read in primary texts. This is not an exhaustive literature search.

## Inspected statements and applicability

### The exact sign interface is already known

George Csordás, *Fourier transforms of positive definite kernels and
the Riemann ξ-Function*, [arXiv v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2).
Read Propositions 2.2–2.3 and their proofs, pp. 3–4, and Open Problem
4.7/Remark 4.8, p. 12. Equation (2.3) gives the real-root terms
(a−r)^(-2) and conjugate-pair terms

\[
 2m\frac{(a-\gamma)^2-b^2}{((a-\gamma)^2+b^2)^2}
\]

in the normalized first Laguerre form, with multiplicity m. This is
also the block formula already used in L251 and L255. Proposition 2.3
isolates a pair against a fixed remaining factor; its sign conclusion
depends on that factor and a sufficiently small b. It is not a
zeta-uniform compensation theorem. Open Problem 4.7 asks for the first
sign everywhere in the paper's scaled xi normalization. Reuse these
statements by citation, rather than reprove the local identity.

### Zero density counts exceptional zeros without locating compensation

Larry Guth and James Maynard, *New large value estimates for Dirichlet
polynomials*, [arXiv v2, 7 April 2026, Theorem 1.2 and (1.2)–(1.4)](https://arxiv.org/html/2405.20552v2).
For fixed 1/2<σ<1, their zero count with Re ρ≥σ and |Im ρ|≤T satisfies

\[
 N(\sigma,T)\le T^{15(1-\sigma)/(3+5\sigma)+o(1)}.
\]

Combining with the stated Ingham bound gives the uniform-exponent
form T^(30(1−σ)/13+o(1)). These are counts over heights, not bounds
for the signed reciprocal-square sum at a specified height. They
provide neither a lower bound for a nonzero displacement from the
critical line nor a compensating real zero near each exception.
The earlier fourth-moment assessment is reused for the rest of this
paper; no large-value calculation is repeated.

### Critical-line gaps: upper counting bounds and lower existence bounds

Aleksandar Ivić and Matti Jutila, *Gaps between consecutive zeros of
the Riemann zeta-function on the critical line*, Monatshefte für
Mathematik **105** (1988), 59–73,
[publication record](https://doi.org/10.1007/BF01471104),
[author-uploaded full text](https://www.researchgate.net/publication/227252747_Gaps_between_consecutive_zeros_of_the_Riemann_zeta-function_on_the_critical_line).
Read the introduction and Theorem 1, pp. 59–60, equations (1.1)–(1.2).
For the number R of critical-line gaps of length at least V in [0,T],
the theorem gives R≪TV^(-2)log T and R≪TV^(-3)(log T)^5.
The text notes their triviality for V≪log T. Thus these bounds do not
guarantee a line zero inside each displacement-scale neighborhood.
The introduction also reports older individual gap bounds; no optimal
current maximum-gap exponent is claimed or imported here.

H. M. Bui and M. B. Milinovich, *Gaps between zeros of the Riemann
zeta-function*, Quarterly Journal of Mathematics **69** (2018),
403–423, [author manuscript, §1.1 and Theorem 1.1, pp. 1–2](https://home.olemiss.edu/~mbmilino/LargeGaps.pdf).
The limsup of critical-line gaps normalized by 2π/log t exceeds 3.18
unconditionally. This is an existence result for large gaps, not an
upper bound for every gap. Its extension to the sequence of all zero
ordinates assumes RH. No assertion about where possible off-line
zeros sit within those gaps is supplied.

Aleksander Simonič, Timothy S. Trudgian and Caroline L.
Turnage-Butterbaugh, *Some explicit and unconditional results on gaps
between zeroes of the Riemann zeta-function*,
[arXiv v1, 20 October 2020, definitions and Theorem 1, pp. 1–2](https://arxiv.org/pdf/2010.10675v1).
The theorem gives explicit positive proportions of normalized gaps
on either side of one. Its zero sequence includes all nontrivial zero
ordinates, with multiplicity; it is not a count of critical-line zeros
only. Neither a proportion of gaps nor a small gap somewhere ensures
the needed positive reciprocal sum at every center.

### Unconditional pair correlation retains an averaging limitation

Siegfred Alan C. Baluyot, Daniel Alan Goldston, Ade Irma Suriajaya
and Caroline L. Turnage-Butterbaugh, *An unconditional Montgomery
Theorem for Pair Correlation of Zeros of the Riemann Zeta Function*,
[arXiv v1, Theorem 1 and §3 Lemma 5](https://arxiv.org/html/2306.04799v1).
Read those statements and the proof of Lemma 5. For a fixed real even
integrable test function supported in [−1,1] and Lipschitz at zero,
Lemma 5 evaluates a sum over all pairs up to T, with the weight
4/(4−(ρ−ρ′)^2), up to a relative O((log T)^(-1/2)) error.
It does not evaluate a reciprocal-square sum about a prescribed center.
Its support restrictions and dependence on the test function cannot
be dropped when introducing displacement-dependent localization.
The conditional strip/density hypotheses in Theorems 2–3 were read
as qualifications, not adopted as unconditional inputs.

### Recent critical-zero counts do not remove the pointwise issue

Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the
Riemann zeta function are simple and on the critical line*,
[arXiv v1, submitted 2 September 2026](https://arxiv.org/pdf/2609.02882v1).
Read Theorem 1.1, p. 3, Proposition 2.1, p. 5, and Lemma 3.1 with the
following weight-removal discussion, p. 10. The theorem states a
liminf proportion at least 0.6725007… of simple critical zeros and
0.8362503… of distinct zeros. The finite-multiset inequality controls
counts by a pair sum. Its application uses the preceding pair-correlation
input, not a lower bound for each reciprocal-square sum. This recent
preprint was compared at statement level; its proof and announced
formal certificates were not independently verified or imported.

Biao Wang, *Simple critical zeros and distinct zeros of the Riemann
zeta-function in short intervals*,
[arXiv v1, submitted 7 September 2026](https://arxiv.org/pdf/2609.07918v1).
Read Theorem 1.1 and its range discussion, pp. 2–3, and Theorem 2.2,
p. 4. For H=T^θ the stated lower proportion of simple critical zeros is
c(θ)=2−θ/2−cot(θ/√2)/√2, positive only for θ>0.5501939647….
The pair formula assumes fixed 0<λ<θ<1 and a fixed smooth test function
supported in [−λ,λ], with error O_g(H+T^λ(log T)^2).
Neither conclusion covers arbitrary neighborhoods of width b<1/2.
The preprint's main proof was not independently checked; even its
stated conclusions do not meet this target.

## Comparison with the required threshold

The following is an applicability comparison using the already saved
block formula, not a new estimate. In Xi coordinates a nonreal pair
is γ±ib, where b=|Re ρ−1/2|. L251 and L255 give a contribution
−2m/b² at its center and a negative contribution for |a−γ|<b.
L256 already records that only finitely many blocks are negative at
each fixed nonzero a, while all block sums converge absolutely.
Finiteness does not bound their size uniformly in b.

The required threshold is that the sum of all positive block
contributions dominate the absolute sum of all negative ones at
every a. Critical-line terms are part of that positive mass; other
nonreal pairs can also help. No reviewed theorem estimates this
comparison. In particular:

- An upper density bound gives a number of exceptions, not a
  displacement-sensitive weight bound for each exception.
- A global proportion, or a proportion in every power-length interval,
  does not prescribe zeros within the negative block's own width.
- Gap statistics cannot be read as a universal upper gap bound, and
  all-zero ordinates cannot be substituted for critical-line zeros.
- Fixed-test pair averages do not authorize taking a singular,
  center-dependent test or discarding the resulting exceptional centers.

These are failures of direct applicability. No counterexample
satisfying the selected counting and gap data together has been proved
in this turn. No assertion that zero-distribution methods are incapable
of proving the first sign is made. The achieved sign range and the
actual bound for the target are unchanged.

## Bounded continuation and redundancy check

Keep one concrete diagnostic: test the known local negative-pair
mechanism in an even order-one canonical product whose positive-real-part
zero count has the Riemann–von Mangoldt main term and O(log T) error,
and whose eventual real-zero gaps are O(1/log T). Require only one
nonreal quartet above height 40 and a negative first sign at its center.
The exact target and its pending review live in the
[new assessment](2026-09-27-count-preserving-laguerre-model.md).

This would test whether those specific coarse data rule out the local
obstruction. L251 already handles strip geometry and scalar signs;
it does not claim this zero-counting law. L264 explicitly does not
match actual-theta zero density. Repeating those examples without the
new count and gap requirements would be redundant. Csordás already
covers the fixed-factor sign mechanism, so any later proof must cite
it and justify only the distribution-compatible specialization.

Continue this diagnostic only through a proof meeting the count,
order, gap and sign conditions, or an identified conflict among those
conditions. If the model exists, stop using these coarse inputs alone
as a proposed compensation certificate and require additional actual-zeta
information. It would not satisfy the theta identity, Euler product or
every pair-correlation/gap statistic reviewed above. It would not be
a counterexample to RH. No construction is attempted here.

Outcome: EXPLORATION, LITERATURE, NOVELTY_UNCHECKED. This is the first
of at most three consecutive unresolved exploration turns. The review
supplies a source comparison and an actionable test, but neither an
actual-theta estimate nor a new impossibility result. The representation
and local mechanism are known; no full target theorem is imported,
reproduced or claimed beyond the checked literature.

## Access boundaries

All essential statements for this comparison were accessed. The
Ivić–Jutila publisher PDF request returned its subscription landing
page; the author-uploaded article supplied Theorem 1 and its range
discussion, rather than relying on the abstract alone. Its proof and
the older individual-gap sources it cites were not read. The arXiv
2010.10675v2 request failed; the accessible text identifies itself as
v1, which is the version compared. Journal revisions of the cited
preprints were not compared. Search-result forums, repository surveys
and unrelated claimed RH arguments were not used as theorem evidence.

## Mathlib

Full-target coverage: **not checked**. Supporting coverage for the
zero-density, spacing and first-sign results: **not checked**.
The named primary results above are mathematical sources, not claimed
Mathlib matches. Lamzouri's reference to an external Lean certificate
is not a checked Mathlib theorem or a formal proof of this target.
