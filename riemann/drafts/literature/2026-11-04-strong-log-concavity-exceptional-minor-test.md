# Strong log-concavity versus an exceptional minor — specialization gate

TARGET: Construct an explicit positive entire coefficient sequence b with b_n^2>=(11/4)b_(n-1)b_(n+1) for n>=1 and det[b_(4+j-i)]_(i,j=0)^4<0, specializing Katkova–Vishnyakova Theorem 4(i), and certify all-iterate log-concavity via McNamara–Sagan Lemma 2.1.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step407 compared condensation, coefficient multipliers, infinite log-concavity and the sharp adjacent-ratio determinant threshold; narrow local searches found no matching entire countermodel certificate. Reuse the completed exceptional-coefficient assessment for queries, duplicates and exact limits; no novelty claim.
SOURCE_EVIDENCE: Katkova–Vishnyakova math/0504183v1 Theorem4(i) p.3 and Section3 p.12 complete Toeplitz sharpness proof; McNamara–Sagan 0808.1065v2 Section2 pp.3–4 Lemma2.1 with its full preceding proof. Both primary statements and relevant proof cases were inspected in step407; precise URLs and obligations below.
COMPARISON: The first source supplies a finite positive Toeplitz counterexample below c_5=3; the second supplies all-iterate log-concavity from the global factor r_0=(3+sqrt(5))/2. The requested 11/4 lies between these constants. The global positive entire extension and explicit certificate are not supplied by either inspected statement and must be justified.
GAP: Produce an explicit finite prefix b_0,...,b_8 with exact ratio checks and a negative D_(5,4), then a positive tail satisfying the junction and every later ratio bound, entire convergence and strict all-iterate positivity. No such sequence has been constructed here.
REASON: One bounded known-result specialization tests whether a generic all-iterate Turán condition could close the exceptional edge before a creative actual-Xi bridge is pursued. It imports known mathematics and proves only the stated extension/certificate obligations; it does not reprove the source sharpness or preservation theorems.
SCOPE: Positive one-sided coefficient sequences with b_(-1)=0, an entire ordinary generating function and the stated global 11/4 bound; one exceptional order-five minor. No actual-K moment representation, Xi realization, full LP property or consequence for actual-Xi signs is assumed or approved.

## Primary inputs and exact difference

Use [Katkova–Vishnyakova, arXiv:math/0504183v1](https://arxiv.org/pdf/math/0504183v1),
Theorem4(i), printed p.3, with k=5 and Section3's Toeplitz
construction on printed p.12. The source defines TP_2(c) using
strictly positive entries and nonstrict adjacent multiplicative
inequalities. Its complete relevant proof uses a symmetric
tridiagonal limiting matrix, its sine determinant and successively
small positive Toeplitz diagonals. It supplies negative determinants
for c<c_5. The theorem's sharpness is known; import it precisely.
Do not mistake the Hankel proof for the required Toeplitz case.

Use [McNamara–Sagan, arXiv:0808.1065v2](https://arxiv.org/pdf/0808.1065v2),
Section2 pp.3–4, Lemma2.1 and its preceding proof. For nonnegative
sequences extended by zero outside the index set, r_0-factor
log-concavity is preserved by L(b)_n=b_n^2-b_(n-1)b_(n+1).
It implies nonnegative iterates at all orders. Strictness, when
claimed for a positive sequence, must be justified with its actual
bound and the n=0 boundary; the theorem must not be upgraded silently.

This is a finite-to-entire specialization, not a proposed new
sharpness theorem. A finite matrix alone does not provide an entire
sequence. Identify its nine Toeplitz diagonal values with b_0,...,b_8
using the stated shifted determinant, certify their local inequalities,
and prove the infinite extension and junction inequalities. Give
a convergence proof for the resulting power series. An explicit
rational prefix and exact arithmetic certificate are preferable
to a decimal example, but any rigorous explicit certificate suffices.

## Relevance and bounded discriminator

The main gap is actual-Xi exceptional signs; local L021's factorial
conventions and L771's smoothing explain the motivation only.
No lemma input is needed for the abstract countermodel itself.
L766 remains unaudited and is not a mathematical premise.
The new Liu–Mao preprint is also not a premise: the test concerns
the proposed generic inference even if its conclusion were accepted.

Seek det[b_(4+j-i)]<0 with *all* coefficient and all-iterate conditions
proved, not a finite preview of L-iterates. That success would stop
a generic infinite-log-concavity-to-exceptional-sign bridge while
leaving actual-Xi-specific information and other routes available.
If the chosen explicit specialization fails, retain that failure
and distinguish an inadequate parameter choice from a theorem about
all such sequences. Limit the next turn to this single order-five
construction and its complete certificate; do not start a parameter
survey across orders or attempt actual-Xi signs.

The missing actual-theta moment constraints must remain explicit.
A countermodel in this larger coefficient class refutes only that
generic implication, not a claim incorporating additional actual-Xi
structure and not RH. No complete RH candidate is proposed.

Mathlib coverage for the full source statements and extended
countermodel is not checked; availability remains unknown.
No new mathematics or script was written while preparing this gate.
The assessment was newly written in step407 and awaits the
supervisor's separate next-turn approval before invocation.

